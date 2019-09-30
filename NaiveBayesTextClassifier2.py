import json
import numpy as np

# opens file creates file objects
train_ldoc = open('trainlabels.txt')
train_ddoc = open('traindata.txt')

# reads the file and splits the lines of text into a list
train_dlist = train_ddoc.read().splitlines()
train_llist = train_ldoc.read().splitlines()
# creates two dictionaries for storing word counts...
# class_dicts are dictionaries of all the differents word there length = num of words in that class
# list dict is a list of dictnaries for each document it's length is the number of documents of that class


def check_dict(a_word, a_dict):
    stop_words = ['and', 'as', 'the', 'is', 'a' ]
    if a_word in stop_words:
        return a_dict
    elif a_word not in a_dict:
        a_dict[a_word] = 1
    else:
        wordcount = a_dict.get(a_word)
        wordcount += 1
        a_dict[a_word] = wordcount
    return a_dict


# assumes a 1:1 relationship between the data and labels i.e. label[i] corresponds to data[i] for all i, i >= 0
def create_vocab_dict(data, labels):
    vocab_dict = dict()
    doccount = 0
    for phrase in data:
        word_list = phrase.split()
        doccount += 1
        for w in word_list:
            vocab_dict = check_dict(w, vocab_dict)
    return vocab_dict, doccount


def calc_prior_prob(num_class0, num_class1):
    prior_probs = [0.0, 0.0]
    denom = num_class0 + num_class1
    prior_probs[0] = np.log((float(num_class0) / float(denom)))
    prior_probs[1] = np.log((float(num_class1) / float(denom)))
    return prior_probs


def vocab_size(class_dict0, class_dict1):
    vocab1_size = len(class_dict1)
    vocab0_size = len(class_dict0)
    vocabsize = len(class_dict0)
    for key in class_dict1:
        if key not in class_dict0:
            vocabsize += 1
    return vocab0_size, vocab1_size, vocabsize


# should vocabulary be the vocabulary of both classes or the respective class
def calc_cond_probs(class_dict0, class_dict1):
    class0_prob = dict()
    class1_prob = dict()
    countlist0 = class_dict0.values()
    countlist1 = class_dict1.values()
    totalwords0 = sum(countlist0)
    totalwords1 = sum(countlist1)
    for key in class_dict1:
        class1_prob[key] = np.log((class_dict1[key] + 1) / (totalwords1 + vocab_size()[2]))
    for key in class_dict0:
        class0_prob[key] = np.log((class_dict0[key] + 1) / (totalwords0 + vocab_size()[2]))

    return class0_prob, class1_prob












'''

with open('outputf.txt', 'w+') as outputf:
    outputf.write(json.dumps(class_dict0))
    outputf.write('\n \n')
    outputf.write((json.dumps(class_dict1)))
    outputf.write('\n \n')
    outputf.write(json.dumps(listdict1))
    outputf.write('\n \n')
    outputf.write((json.dumps(listdict0)))
    outputf.write('\n \n')
    outputf.write('unique words in class 0: ' + str(numwords0))
    outputf.write('\n \n')
    outputf.write('unique words in class 1: ' + str(numwords1))
    outputf.write('\n \n')
    outputf.write('total words in class 0: ' + str(totalword0))
    outputf.write('\n \n')
    outputf.write('total word in class 1: ' + str(totalword1))

'''
# print(train_dlist)
# print(train_llist)


