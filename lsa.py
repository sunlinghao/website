# -*- coding: utf-8 -*-
"""
Created on Wed Jun 11 17:02:39 2014
@author: modified by zhouxu,add plot
"""
import numpy as np
from collections import Counter
import string

mydoclist = ['Julie loves me more than Linda loves me',
             'Jane likes me more than Julie loves me',
             'He likes basketball more than baseball']
# split()  分割字符串  默认分割 分隔符
def build_lexicon(corpus):  # 做一个全部单词字典
    lexicon = set()
    for doc in corpus:
        lexicon.update([word for word in doc.split()])
    return lexicon

def tf(term,document):
    return freq(term,document)

def freq(term,document):   #返回该单词次数
    return document.split().count(term)

vocabulary = build_lexicon(mydoclist)  # beg of word
# print list(vocabulary)
doc_term_matrix = []
print 'Our vocabulary vector is['+','.join(list(vocabulary))+']'  #
for doc in mydoclist:
    print 'The doc is"'+doc+'"'
    tf_vector = [tf(word,doc) for word in vocabulary]
    # tf_vector=[]
    # for word in vocabulary:   #一句顶三句   计算每个单词的出现频率
    #     tf_vector.append(tf(word,doc))
    tf_vector_string = ','.join(format(freq,'d')for freq in tf_vector)  #十进制输出
    print 'The tf vector for Document %d is [%s]'% ((mydoclist.index(doc)+1), tf_vector_string)
    doc_term_matrix.append(tf_vector)
print 'All combined,here is our master document term matrix:'
print doc_term_matrix
    # print list(tf.elements())



import math
def l2_normalizer(vec):   #标准化
    denom = np.sum([el**2 for el in vec])
    return [(el / math.sqrt(denom)) for el in vec]

def numDocsContaining(word,doclist):  #计算每个单词出现频率
    doccount = 0
    for doc in doclist:
        if freq(word,doc) > 0:
            doccount+=1
    return doccount

def idf(word,doclist):  #单词在文本频率
    n_samples = len(doclist)
    df = numDocsContaining(word,doclist)
    return np.log(n_samples / 1+df)


doc_term_matrix_l2 = []
for vec in doc_term_matrix:
    doc_term_matrix_l2.append(l2_normalizer(vec))
# print np.matrix(doc_term_matrix)
print np.matrix(doc_term_matrix_l2)

my_idf_vector = [idf(word,mydoclist) for word in vocabulary]
# print 'The inverse document frequency vector is ['+','.join(format(freq,'f')for freq in my_idf_vector)+']'
print my_idf_vector
def build_idf_matrix(idf_vector):
    """
    IDF向量转化为BxB的矩阵 
    """
    idf_mat = np.zeros((len(idf_vector), len(idf_vector)))
    np.fill_diagonal(idf_mat, idf_vector)  #填满对角线
    return idf_mat

my_idf_matrix = build_idf_matrix(my_idf_vector)
# print my_idf_matrix

doc_term_matrix_tfidf = []

# performing tf-idf matrix multiplication
for tf_vector in doc_term_matrix:
    doc_term_matrix_tfidf.append(np.dot(tf_vector, my_idf_matrix))

# normalizing
doc_term_matrix_tfidf_l2 = []
for tf_vector in doc_term_matrix_tfidf:
    doc_term_matrix_tfidf_l2.append(l2_normalizer(tf_vector))

print vocabulary
print np.matrix(doc_term_matrix_tfidf_l2)  # np.matrix() just to make it easier to look at

