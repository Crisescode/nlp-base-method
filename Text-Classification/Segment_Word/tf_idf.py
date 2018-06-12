from sklearn.feature_extraction.text import TfidfTransformer, TfidfVectorizer
from sklearn.feature_extraction.text import CountVectorizer

corpus=["I come to China to travel",
    "This is a car polupar in China",
    "I love tea and Apple ",
    "The work is to write some papers in science"]

# vectorizer=CountVectorizer()
#
# transformer = TfidfTransformer()
# tfidf = transformer.fit_transform(vectorizer.fit_transform(corpus))
# print(tfidf)

tfidef2 = TfidfVectorizer()
re = tfidef2.fit_transform(corpus)
print(re)

