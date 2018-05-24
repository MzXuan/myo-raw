#!/usr/bin/env python
#title           :classify.py
#description     :This is for classifing the recorded gesture data
#author          :ZHAO Xuan
#date            :2018-05-24
#=============================================================================

from __future__ import print_function
from sklearn import svm
import pickle
import sys


if __name__ == '__main__':
    if len(sys.argv) >=2:
        file_name = sys.argv[1]
    else:
        file_name = './data_set/data.pkl'

    print (file_name)
    # with open('./data_set/') as f:


