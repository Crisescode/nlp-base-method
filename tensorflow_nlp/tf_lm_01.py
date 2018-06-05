import tensorflow as tf

word_labels = tf.constant([2, 0])

predict_logits = tf.constant([[2.0, -1.0, 3.0], [1.0, 0.0, -0.5]])
loss = tf.nn.sparse_softmax_cross_entropy_with_logits(
    labels=word_labels, logits=predict_logits
)


sess = tf.Session()
print(sess.run(loss))

