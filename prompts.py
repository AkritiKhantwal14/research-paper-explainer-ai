def simple_summary_prompt(article):
    return f"""
    Summarize this research paper in simple language.

    Article:
    {article}
    """

def fun_explanation(article):
    return f""" 
    Give fun explanation of the article.
    Article:
    {article}
    """

def quiz(article):
    return f""" 
    Generate a quiz with 5 questions from the article.
    Article:
    {article}
    """

def key_takeaways(article):
    return f""" 
    Generate 5 important key takeaways from the article.
    Article:
    {article}
    """

def beginner(article):
    return f""" 
    Explain the article like i am a beginner student.
    Article:
    {article}
    """

def technical_prompt(article):
    return f"""
    Generate a technical explanation of the methodology,
    architecture, and implementation discussed in this paper.

    Paper:
    {article}
    """

def literature_review_prompt(article):
    return f"""
    Generate a structured literature review from this research paper.

    Include:
    1. Research Objective
    2. Existing Problem
    3. Methodology Used
    4. Key Findings
    5. Limitations
    6. Research Gaps
    7. Future Scope

    IMPORTANT:
    Do not invent references, citations, journals, websites, authors, or papers.
    Use only information explicitly present in the uploaded paper.
    If references are not available, write "Not specified in the paper".

    Paper:
    {article}
    """
def research_gap_prompt(article):
    return f"""
    Analyze this research paper and identify:

    1. Current Problem Being Solved
    2. Limitations of the Proposed Approach
    3. Missing Experiments
    4. Unexplored Areas
    5. Open Research Questions
    6. Potential Future Research Directions
    7. Suggested Improvements

    Paper:
    {article}
    """

def recommendation_prompt(article):
    return f"""
    Analyze this research paper.

    Identify:

    1. Main Research Domain
    2. Key Technologies
    3. Important Concepts
    4. Research Keywords

    Then recommend:

    - 10 important research papers that should be read next
    - Why each paper is relevant
    - Suggested reading order

    Paper:
    {article}
    """

def citation_prompt(article):
    return f"""
    Extract citation information from this research paper.

    Generate citations in:

    1. IEEE
    2. APA
    3. MLA
    4. Chicago

    Also identify:
    - Title
    - Authors
    - Publication Year
    - Conference/Journal

    Paper:
    {article}
    """

def metadata_prompt(article):
    return f"""
    Extract:

    - Paper Title
    - Authors
    - Affiliations
    - Abstract
    - Keywords
    - Publication Year
    - Conference or Journal

    Paper:
    {article}
    """

def chat_with_paper_prompt(context, question):
    return f"""
    You are an expert research assistant.

    Answer ONLY from the provided context.

    Context:
    {context}

    Question:
    {question}

    Answer:
    """