from sklearn.decomposition import LatentDirichletAllocation
from sklearn.feature_extraction.text import CountVectorizer


with open("nlp_test1.txt", "r") as f1:
    res1 = f1.read()
with open("nlp_test3.txt", "r") as f2:
    res2 = f2.read()
with open("nlp_test5.txt", "r") as f3:
    res3 = f3.read()

#从文件导入停用词表#
stpwrdpath = "stop_words.txt"

stpwrd_dic = open(stpwrdpath, "rb")
stpwrd_content = stpwrd_dic.read().decode("gbk")

#将停用词表转换成list
stpwrdlist = stpwrd_content.splitlines()
#print(stpwrdlist)
stpwrd_dic.close()

corpus = [res1, res2, res3]
cntVector = CountVectorizer(stop_words=stpwrdlist)
cntTf = cntVector.fit_transform(corpus)
#print(cntTf)

lda = LatentDirichletAllocation(n_topics=2, learning_offset=50, random_state=0)

docres = lda.fit_transform(cntTf)

print(docres)
print(lda.components_)



