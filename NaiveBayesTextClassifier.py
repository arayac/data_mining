import json
import numpy as np

# opens file creates file objects
train_ldoc = open('trainlabels.txt')
train_ddoc = open('traindata.txt')

# reads the file and splits the lines output is a list
train_dlist = train_ddoc.read().splitlines()
train_llist = train_ldoc.read().splitlines()
# creates two dictionaries for storing word counts
class_dict1 = dict()
class_dict0 = dict()
listdict0 = []
listdict1 = []
numwords0 = 0
numwords1 = 0



def check_dict1(a_word):
    global numwords1
    global class_dict1
    if a_word not in class_dict1:
        class_dict1[a_word] = 1
        numwords1 += 1
    else:
        wordcount = class_dict1.get(a_word)
        wordcount += 1
        class_dict1[a_word] = wordcount


def check_dict0(a_word):
    global numwords0
    global class_dict0
    if a_word not in class_dict0:
        class_dict0[a_word] = 1
        numwords0 += 1
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



word_count()
countlist0 = class_dict0.values()
countlist1 = class_dict1.values()
totalword0 = sum(countlist0)
totalword1 = sum(countlist1)


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


# print(train_dlist)
# print(train_llist)


