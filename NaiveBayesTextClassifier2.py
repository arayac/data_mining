import json
import numpy as np

# opens file creates file objects
train_ldoc = open('trainlabels.txt')
train_ddoc = open('traindata.txt')
train_dlist = train_ddoc.read().splitlines()
train_llist = train_ldoc.read().splitlines()


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
# extract label is the label you want to break off from the data i.e. '1' or '0' in this case
def isolate_data(data, labels, extract_label):
    isolated_data = []
    for index, doc in enumerate(data):
        if labels[index] == extract_label:
            isolated_data.append(doc)
    return isolated_data


def create_vocab_dict(data):
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
    vocab_sizes = vocab_size(class_dict0, class_dict1)
    for key in class_dict1:
        class1_prob[key] = np.log((class_dict1[key] + 1) / (totalwords1 + vocab_sizes[2]))
    for key in class_dict0:
        class0_prob[key] = np.log((class_dict0[key] + 1) / (totalwords0 + vocab_sizes[2]))

    return class0_prob, class1_prob, vocab_sizes[2]


def train_mnb(data, labels):
    doc_list0 = isolate_data(data, labels, '0')
    doc_list1 = isolate_data(data, labels, '1')
    dict0, doc0count = create_vocab_dict(doc_list0)
    dict1, doc1count = create_vocab_dict(doc_list1)
    priori_probs = calc_prior_prob(doc0count, doc1count)
    class0_probs, class1_probs, vocabsize, = calc_cond_probs(dict0, dict1)
    return class0_probs, class1_probs, priori_probs, vocabsize













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


