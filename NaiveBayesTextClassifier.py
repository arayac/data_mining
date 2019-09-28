import pandas as pd
train_ldoc = open('trainlabels.txt')
train_ddoc = open('traindata.txt')
train_dlist = train_ddoc.readlines()
train_llist = train_ldoc.readlines()

print(train_dlist)
print(train_llist)


'''  def word_count():
    wordfreq = dict()
'''