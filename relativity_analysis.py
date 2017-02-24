#!/usr/bin/env python
# -*- coding:utf8 -*-
import sys
import numpy as np
import cPickle as pickle
import jieba
import datetime

def load_model(model_path):
	with open(model_path,'rb') as f:
		clfs = pickle.load(f)
	return clfs

def read_stopdict(stopword_file):
	stopword_dict = set([])
	f = open(stopword_file, 'rb')
	for line in f:
		line = line.strip('\r\n').decode('utf-8')
		stopword_dict.add(line)
	f.close()
	return stopword_dict


def load_vec_fit(path):
    with open(path, 'rb') as f:
        d = pickle.load(f)
    return d

def vectorize_test(test_x,data_path):
    vect_fit = load_vec_fit(data_path)
    test_vec = vect_fit.transform(test_x)

    return test_vec

def relativity_predict(test_x, clfs):

    result = None
    label = 0
    for key in clfs:
        model = clfs[key]
        if model == None:
            continue
        pre = model.predict(test_x)
        if result is None:
            result =pre
        else:
            result += pre
    if result >=1 :
        label = 1
    return label

def seg_text(str):
    stopword_file = './data/all_stopword.txt'
    stopword_dict = read_stopdict(stopword_file)
    str_seg = jieba.cut(str.strip('\n'))
    str_words = []
    for word in str_seg:
        if word == ' ' or word in stopword_dict:
            continue
        str_words.append(word)

    seg_words = ' '.join(str_words)
    str_words = []
    str_words.append(seg_words)
    test_x = np.asarray(str_words)

    return test_x


if __name__ == '__main__':

    sys.stderr.write('load model...\n')


    data_path = './data/relative_train_fit'

    model_path = './data/relative_model'
    clfs = load_model(model_path)

    if clfs == None:
        sys.std.write('Error:load model error!')
        sys.exit(1)
    sys.stderr.write('Info: load model successfully!\n')

    while True:

        str = raw_input('please input some str:\n')
        if str == 'quit':
            sys.exit(1)
        start = datetime.datetime.now()
        sentence_x = seg_text(str)
        test_vec = vectorize_test(sentence_x, data_path)
        label = relativity_predict(test_vec,clfs)
        end = datetime.datetime.now()
        print 'predict label:%d,time:%ss' %(label,(end-start).seconds)
