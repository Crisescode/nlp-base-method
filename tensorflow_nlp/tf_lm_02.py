import codecs
import collections
from operator import itemgetter


raw_data = "/home/ros/PycharmProjects/data/simple-examples/data/ptb.train.txt"
vocab_output = "/home/ros/PycharmProjects/nlp-base-method/tensorflow_nlp/ptb.vocab"

counter = collections.Counter()
with codecs.open(raw_data,"r","utf-8") as f:
    for line in f:
        for word in line.strip().split():
            counter[word] += 1

sorted_word_to_cnt = sorted(counter.items(),
                            key=itemgetter(1),
                            reverse=True)
print(sorted_word_to_cnt)
sort_words = [x[0] for x in sorted_word_to_cnt]
print(sort_words)

sort_words = ["<eos>"] + sort_words
print(sort_words)

sort_words = ["<unk>", "<sos>", "<eos>"] + sort_words
if len(sort_words) > 10000:
    sort_words = sort_words[:10000]

with codecs.open(vocab_output,"w","utf-8") as file_output:
    for word in sort_words:
        file_output.write(word + '\n')
    
