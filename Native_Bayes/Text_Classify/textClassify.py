import bayes

listOPosts,listClasses = bayes.loadDataSet()
myVocabList = bayes.createVocabList(listOPosts)

print(myVocabList)

vecList1 = bayes.setOfWords2Vec(myVocabList,listOPosts[0])
vecList4 = bayes.setOfWords2Vec(myVocabList,listOPosts[3])
print(vecList1)
print(vecList4)