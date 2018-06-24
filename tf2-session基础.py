# -*- coding: utf-8 -*-
"""
Created on Sat Jun 16 22:59:37 2018

@author: LU
"""
## 4-1

import tensorflow as tf
config = tf.ConfigProto(log_device_placement=True, allow_soft_placement=True)
config.gpu_options.allow_growth = True

a = tf.constant('Hello Tensorflow')
sess = tf.Session(config = config)
print(sess.run(a))
sess.close()
## 4-2
b = tf.constant(2)
c = tf.constant(9)
with tf.Session(config = config) as sess:
    print(sess.run(b+c))
    print(sess.run(c**b))
## 4-3
a = tf.placeholder(tf.int16)
b = tf.placeholder(tf.int16)
c = tf.add(a,b)
d = tf.multiply(a,b)

with tf.Session(config = config) as sess:
    print('plus:%i'%sess.run(c, feed_dict={a:4, b:5}))
    print('multiply:%i'%sess.run(d, feed_dict={a:4, b:5}))
    print('combination:%s'%eval(
            'sess.run([c,d], feed_dict={a:4,b:5})'))# eval转化字符串