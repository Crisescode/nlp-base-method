import pynlpir

pynlpir.open()
str = "聊天机器人到底该怎么做？"
segs = pynlpir.segment(str)
segments = pynlpir.segment(str, pos_tagging=True, pos_names="all", pos_english=False)
for seg in segs:
    pass
    #print(seg[0],'\t',seg[1])

key_words = pynlpir.get_key_words(str, weighted=True)
for key_word in key_words:
    pass
    #print(key_word[0],'\t',key_word[1])

for segment in segments:
    print(segment[0],"\t",segment[1])

k_ws = pynlpir.get_key_words(str, weighted=True)
for k_w in k_ws:
    print(k_w[0], '\t', k_w[1])