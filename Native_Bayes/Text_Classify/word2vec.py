import bayes

listOPosts,listClasses = bayes.loadDataSet()
myVocabList = bayes.createVocabList(listOPosts)

print(myVocabList)

vecList1 = bayes.setOfWords2Vec(myVocabList,listOPosts[0])
vecList4 = bayes.setOfWords2Vec(myVocabList,listOPosts[3])
print(vecList1)
print(vecList4)

trainMat = []
for postinDoc in listOPosts:
    trainMat.append(bayes.setOfWords2Vec(myVocabList,postinDoc))

print(trainMat)
print(len(trainMat))
print(listClasses)

p0V,p1V,pAb = bayes.trainNB0(trainMat,listClasses)
# print(pAb)
print(p0V)
# print(p1V)