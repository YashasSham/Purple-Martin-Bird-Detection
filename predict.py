
# -*- coding: utf-8 -*-
"""
Created on Mon Oct  1 05:15:17 2018

@author: Yasha
"""

import tensorflow as tf
import numpy as np
import os

def init():
    global sess, saver, graph
    ##restore the saved model 
    sess = tf.Session()
    # Recreate the network graph
    saver = tf.train.import_meta_graph('output/bird.meta')
    # load the weights saved using the restore method.
    saver.restore(sess, tf.train.latest_checkpoint('output/'))
    graph = tf.get_default_graph()

def predict_video(images,image_size,num_channels):
    images = np.array(images, dtype=np.uint8)
    images = images.astype('float32')
    images = np.multiply(images, 1.0/255.0) 
    
    x_batch = images.reshape(len(images), image_size,image_size,num_channels) 
    y_pred = graph.get_tensor_by_name("y_pred:0")

    ##feed the images to the input placeholders
    x= graph.get_tensor_by_name("x:0") 
    y_true = graph.get_tensor_by_name("y_true:0") 
    y_test_images = np.zeros((1, len(os.listdir('train/')))) 
    
    
    feed_dict_testing = {x: x_batch, y_true: y_test_images}
    result=sess.run(y_pred, feed_dict=feed_dict_testing)
    # result [probabiliy_of_female probability_of_male probability_of_not ]
    
    result[result >= 0.5] = 1.0
    result[result < 0.5] = 0.0
    prediction = []
    for i in range(len(result)):
        if (result[i,0] == 1):
            prediction.append('incubating')
        if result[i,1] == 1:
            prediction.append('not-incubating')
    return result, prediction 
