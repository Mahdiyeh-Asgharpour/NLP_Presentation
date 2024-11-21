import  nltk
# nltk.download()
sample_text="I love this course and I think I can finish it. The professor said :We have an exam next weekend."
sentences=nltk.sent_tokenize(sample_text)
words=nltk.word_tokenize(sample_text)
print(sentences)
print(len(sentences))
print(words)
print(len(words))