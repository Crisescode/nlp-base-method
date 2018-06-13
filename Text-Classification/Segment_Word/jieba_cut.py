import jieba

jieba.suggest_freq("沙瑞金", True)
jieba.suggest_freq("易学习", True)
jieba.suggest_freq("王大路", True)
jieba.suggest_freq("欧阳菁", True)
jieba.suggest_freq("京州", True)


#第一个文档分词#
with open("nlp_test0.txt", "r+") as f:
    document = f.read()

    document_cut = jieba.cut(document)
    result = " ".join(document_cut)

    with open("nlp_test1.txt", "w+") as f2:
        f2.write(result)
f.close()
f2.close()

#第二个文档分词#
with open("nlp_test2.txt", "r+") as f:
    document2 = f.read()

    document_cut2 = jieba.cut(document2)
    result2 = " ".join(document_cut2)

    with open("nlp_test3.txt", "w+") as f2:
        f2.write(result2)

f.close()
f2.close()

#第三个文档分词#
with open("nlp_test4.txt", "r+") as f:
    document3 = f.read()

    document_cut2 = jieba.cut(document3)
    result3 = " ".join(document_cut2)
    
    print(result3)

    with open("nlp_test5.txt", "w+") as f2:
        f2.write(result3)

f.close()
f2.close()
