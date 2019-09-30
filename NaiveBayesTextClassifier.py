import json
import numpy as np

# opens file creates file objects
train_ldoc = open('trainlabels.txt')
train_ddoc = open('traindata.txt')

# reads the file and splits the lines output is a list
train_dlist = train_ddoc.read().splitlines()
train_llist = train_ldoc.read().splitlines()
# creates two dictionaries for storing word counts...
# class_dicts are dictionaries of all the differents word there length = num of words in that class
# list dict is a list of dictnaries for each document it's length is the number of documents of that class
class_dict1 = dict()
class_dict0 = dict()
listdict0 = []
listdict1 = []


def check_dict1(a_word):
    global class_dict1
    if a_word not in class_dict1:
        class_dict1[a_word] = 1
    else:
        wordcount = class_dict1.get(a_word)
        wordcount += 1
        class_dict1[a_word] = wordcount


def check_dict0(a_word):
    global class_dict0
    if a_word not in class_dict0:
        class_dict0[a_word] = 1
    else:
        wordcount = class_dict0.get(a_word)
        wordcount += 1
        class_dict0[a_word] = wordcount



def word_count():
    global train_dlist
    global train_llist
    global listdict0
    global listdict1
    doc1count = 0
    doc0count = 0
    stop_words = ['and', 'as', 'the', 'is', 'a' ]
    for i, phrase in enumerate(train_dlist):
        word_list = phrase.split()
        if train_llist[i] == '1':
            listdict1.append({})
            doc1count += 1
            for w in word_list:
                check_dict1(w)
                if w not in listdict1[doc1count - 1]:
                    listdict1[doc1count - 1][w] = 1
                else:
                    listdict1[doc1count - 1][w] += 1
        else:
            listdict0.append({})
            doc0count += 1
            for w in word_list:
                check_dict0(w)
                if w not in listdict0[doc0count - 1]:
                    listdict0[doc0count - 1][w] = 1
                else:
                    listdict0[doc0count - 1][w] += 1
    for i in stop_words:
        class_dict1.pop(i, 0)
        class_dict0.pop(i, 0)


def calc_prior_prob():
    global train_llist
    prior_probs = [0.0, 0.0]
    denom = len(listdict0) + len(listdict1)
    prior_probs[0] = np.log((float(len(listdict0)) / float(denom)))
    prior_probs[1] = np.log((float(len(listdict1)) / float(denom)))
    return prior_probs


def vocab_size():
    vocab1_size = len(class_dict1)
    vocab0_size = len(class_dict0)
    vocabsize = len(class_dict0)

    for key in class_dict1:
        if key not in class_dict0:
            vocabsize += 1
    return vocab0_size, vocab1_size, vocabsize


# should vocabulary be the vocabulary of both classes or the respective class
def calc_cond_probs():
    global class_dict1
    global class_dict0
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










word_count()
calc_prior_prob()



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


