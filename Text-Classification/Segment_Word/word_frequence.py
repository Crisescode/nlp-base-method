from sklearn.feature_extraction.text import CountVectorizer, HashingVectorizer

vectorizer = CountVectorizer()
corpus = ["I come to China to travel",
    "This is a car polupar in China",
    "I love tea and Apple ",
    "The work is to write some papers in science"]

print(vectorizer.fit_transform(corpus))

print(vectorizer.fit_transform(corpus).toarray())

print(vectorizer.get_feature_names())

'''
输出结果:
(0, 16)	1
  (0, 3)	1
  (0, 15)	2
  (0, 4)	1
  (1, 5)	1
  (1, 9)	1
  (1, 2)	1
  (1, 6)	1
  (1, 14)	1
  (1, 3)	1
  (2, 1)	1
  (2, 0)	1
  (2, 12)	1
  (2, 7)	1
  (3, 10)	1
  (3, 8)	1
  (3, 11)	1
  (3, 18)	1
  (3, 17)	1
  (3, 13)	1
  (3, 5)	1
  (3, 6)	1
  (3, 15)	1
  
  左边的括号中第一个数字是文本的序号，第二个数字是词的序号，注意词的序号是基于所有的文档的，
  第三个数字就是我们的词频。
'''

#利用hash trick 进行降维
vectorizer2 = HashingVectorizer(n_features=6, norm= None)
print(vectorizer2.fit_transform(corpus))