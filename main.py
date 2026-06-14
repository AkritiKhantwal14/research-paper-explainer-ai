filename = input(" Enter Filename:")
file = open(filename , "r") # File name and read mode
text = file.read() #converts entire file to string
print(text)
wordcount=len(text)
print("word count="+str(wordcount) )
file.close()
