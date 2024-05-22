#!/usr/bin/env python
# coding: utf-8

# In[3]:


import io 
import os
import collections

file = io.open("C:\\Users\\lenovo\\OneDrive\\Desktop\\word_cloud\\98-0.txt" , "r" , encoding="utf-8")

wordcount = {}

for word in file.read().lower().split() :
    word = word.replace(",","")
    word = word.replace(".","")
    word = word.replace('"',"")
    word = word.replace('“',"")
    if word not in file1 :
        if word not in wordcount :
            wordcount[word] =1
        else :
            wordcount[word] +=1

d = collections.Counter(wordcount)

for word , count in d.most_common(10) :
    print(word,":",count)


# In[4]:


import io 
import os 
import collections

file = io.open("C:\\Users\\lenovo\\OneDrive\\Desktop\\word_cloud\\98-0.txt" , "r" , encoding="utf-8")

stopwords = set(line.strip() for line in open('C:\\Users\\lenovo\\OneDrive\\Desktop\\word_cloud\\stopwords.txt'))

wordcount = {}

for word in file.read().lower().split() :
    word = word.replace(".","")
    word = word.replace(",","")
    word = word.replace('"',"")
    word = word.replace('“',"")
    if word not in stopwords :
        if word not in wordcount :
            wordcount[word] = 1
        else :
            wordcount[word] += 1

d = collections.Counter(wordcount)

for word , count in d.most_common(10) :
    print(word , ":" , count)


# In[ ]:




