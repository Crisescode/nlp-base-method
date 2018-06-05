import codecs
import keras

raw_data = "/home/ros/PycharmProjects/data/simple-examples/data/ptb.train.txt"
input_vocab_file = "/home/ros/PycharmProjects/nlp-base-method/tensorflow_nlp/ptb.vocab"
output_data = "/home/ros/PycharmProjects/nlp-base-method/tensorflow_nlp/ptb.train"

with codecs.open(input_vocab_file, "r", "utf-8") as f_vocab:
    vocab = [w.strip() for w in f_vocab.readlines()]
print(vocab)

word_to_id = {k: v for (k, v) in zip(vocab, range(len(vocab)))}
print(word_to_id)

def get_id(word):
    return word_to_id[word] if word in word_to_id else word_to_id["<unk>"]

fin = codecs.open(raw_data, "r", "utf-8")
fout = codecs.open(output_data, "w", "utf-8")

for line in fin:
    words = line.strip().split() + ["<eos>"]
    out_line = " ".join([str(get_id(w)) for w in words]) + "\n"
    fout.write(out_line)
fin.close()
fout.close()


