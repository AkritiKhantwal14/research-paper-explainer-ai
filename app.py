import streamlit as st 
from pdf_reader import extract_pdf_text

from prompts import(simple_summary_prompt,
    technical_prompt,
    literature_review_prompt,
    research_gap_prompt,
    recommendation_prompt,chat_with_paper_prompt)

import urllib.request
import json

from export import save_docx
from retriever import create_vector_store, retrieve_chunks
from chunker import chunk_text

import streamlit as st

st.set_page_config(
    page_title="Research Paper Explainer",
    page_icon="📚",
    layout="wide"
)

st.markdown("""
<style>
div[data-baseweb="select"] {
    cursor: pointer !important;
}

div[data-baseweb="select"] * {
    cursor: pointer !important;
}
</style>
""", unsafe_allow_html=True)

st.title("Research Paper Explainer")

uploaded_files=st.file_uploader(
    "Upload PDF",
    type=["pdf"],
    accept_multiple_files=True
)

analysis_type=st.segmented_control(
    "Select Analysis Type",
    [ 
        "Simple Summary",
        "Technical Explanation",
        "Literature Review",
        "Research Gap Analysis",
        "Recommendations",
        "Paper Comparison",
        "Multi-Paper Literature Review",
        "Chat With Paper"
    ]
)

question = ""

if analysis_type == "Chat With Paper":
    question = st.text_input(
        "Ask a question about the paper"
    )

papers = []

if uploaded_files:

    for uploaded_file in uploaded_files:

        with open(uploaded_file.name, "wb") as f:
            f.write(uploaded_file.getbuffer())

        article = extract_pdf_text(uploaded_file.name)
        chunks = chunk_text(article)

        if "index" not in st.session_state:
            index, chunks = create_vector_store(chunks)

            st.session_state.index = index
            st.session_state.chunks = chunks
        else:
            index = st.session_state.index
            chunks = st.session_state.chunks
        papers.append(article)

    st.success(f"{len(papers)} paper(s) uploaded successfully!")

def generate_response(prompt):

    data = json.dumps({
        "model": "llama3:latest",
        "prompt": prompt,
        "stream": False
    }).encode("utf-8")

    req = urllib.request.Request(
        "http://localhost:11434/api/generate",
        data=data,
        headers={"Content-Type": "application/json"}
    )

    response = urllib.request.urlopen(req)

    result = json.loads(response.read())

    return result["response"]

if uploaded_files and analysis_type != "Select":
    
    if st.button("Generate"):

        if analysis_type=="Simple Summary":
            prompt=simple_summary_prompt(article)

        elif analysis_type == "Technical Explanation":
            prompt = technical_prompt(article)

        elif analysis_type == "Literature Review":
            prompt = literature_review_prompt(article)

        elif analysis_type == "Research Gap Analysis":
            prompt = research_gap_prompt(article)

        elif analysis_type == "Recommendations":
            prompt = recommendation_prompt(article)

        elif analysis_type == "Paper Comparison":

            if len(papers) < 2:
                st.error("Please upload at least 2 papers.")
                st.stop()

            paper_summaries = []

            for i, paper in enumerate(papers):

                st.write(f"Summarizing Paper {i+1}...")

                summary_prompt = f"""
                Summarize this research paper.

                Include:
                1. Research Objective
                2. Methodology
                3. Key Findings
                4. Limitations

                Paper:
                {paper}
                """

                summary = generate_response(summary_prompt)

                paper_summaries.append(
                    f"\n\nPAPER {i+1}\n{summary}"
                )

            combined_summaries = "\n".join(paper_summaries)

            prompt = f"""
            Compare the following research papers.

            For EACH paper discuss:

            - Research Objective
            - Methodology
            - Key Findings
            - Strengths
            - Weaknesses

            Then provide:

            1. Similarities
            2. Differences
            3. Research Gaps
            4. Future Research Directions
            5. Which Paper Has the Stronger Contribution and Why

            IMPORTANT:
            - Mention every paper separately.
            - Create comparison tables when appropriate.
            - Base conclusions only on the provided paper summaries.

            Papers:

            {combined_summaries}
            """

        elif analysis_type == "Multi-Paper Literature Review":

            paper_summaries = []

            for i, paper in enumerate(papers):

                st.write(f"Summarizing Paper {i+1}...")

                summary_prompt = f"""
                Summarize this research paper.

                Include:
                - Objective
                - Methodology
                - Key Findings
                - Limitations

                Paper:
                {paper}
                """

                summary = generate_response(summary_prompt)

                paper_summaries.append(
                    f"\nPAPER {i+1}\n{summary}"
                )

            all_papers = "\n\n".join(paper_summaries)

            prompt = f"""
            Generate a comparative literature review from these research papers.

            Include:

            1. Introduction
            2. Summary of Each Paper
            3. Methodologies Used
            4. Comparative Analysis
            5. Similarities
            6. Differences
            7. Research Gaps
            8. Future Scope
            9. Conclusion

            Papers:

            {all_papers}
            """
        
            

        elif analysis_type == "Chat With Paper":
            context = retrieve_chunks(
                question,
                index,
                chunks
            )
            prompt = chat_with_paper_prompt(
                context,
                question
            )

        with st.spinner("Analyzing Research Paper..."):

            try:

                result = generate_response(prompt)

                st.subheader("Result")

                st.write(result)
        
                filename=analysis_type.lower().replace(" ","_") + ".docx"
                save_docx(result,filename)

                with open(filename,"rb") as file:
                    st.download_button(
                        label="Download Result",
                        data=file,
                        file_name=filename,
                        mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document"
                    )
            except Exception as e:
                st.error(f"Error: {e}")
        
