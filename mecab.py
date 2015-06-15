# -*- coding: utf-8 -*-
# coding: utf-8
import MeCab

words={}
def getNoun(text):
    tagger=MeCab.Tagger('Ochasen')
    node=tagger.parseToNode(text.encode('utf-8'))
    while node:
        noun=node.feature.split(',')[0]
        if noun==u'です':
            words.setdefault(node.surface,0)
            words[node.serface]+=1
        node=node.next
    return words
    
f=open('sub.txt')
f1=open('collocation.txt','w')
for line in f:
    line1,line2=line.strip().split('\t')
    d=getNoun(line2)
    for k,v in sorted(words.items(), key=lambda x:x[1]):
        f1.write(k, v)
    
f.close()    
f1.close()
