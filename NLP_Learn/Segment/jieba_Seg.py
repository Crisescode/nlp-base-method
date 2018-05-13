import jieba

#结巴分词--全模式
sent = "在包含问题的所有姐的解空间树中，按照深度优先搜索的策略，从根节点出发深度搜索解空间树"
wordlist = jieba.cut(sent, cut_all=True)

print(" | ".join(wordlist))

#结巴分词--精确切分
wordlist = jieba.cut(sent)
print(" | ".join(wordlist))

#结巴分词--搜索引擎模式
wordlist = jieba.cut_for_search(sent)
print(" | ".join(wordlist))