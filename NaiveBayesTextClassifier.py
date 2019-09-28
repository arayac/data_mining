import pandas as pd
import numpy as np

# opens file creates file objects
train_ldoc = open('trainlabels.txt')
train_ddoc = open('traindata.txt')


# reads the file and splits the lines output is a list
train_dlist = train_ddoc.read().splitlines()
train_llist = train_ldoc.read().splitlines()
# creates two dictionaries for storing word counts
class1_dict = dict()
class0_dict = dict()

def word_count():
    for i in train_dlist:
        if train_llist[i] == 1:
            word_list = train_dlist[i].split()
            for w in word_list:
                if word_list[w] not in class1_dict:


        else:




# print(train_dlist)
# print(train_llist)


