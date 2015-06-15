# -*- coding: utf-8 -*-

import MeCab
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

words={}
def getNoun(text):
    tagger=MeCab.Tagger('-Owakati')
    tagger.parse('')
    node=tagger.parseToNode(text.encode('utf-8'))
    while node:
        noun=node.feature.split(',')[0]
        if noun==r'名詞':
            words.setdefault(node.surface,0)
            words[node.surface]+=1
        node=node.next
    return words
    
f=open('sub.txt')
#f1=open('collocation.txt','w')
for line in f:
    line1,line2=line.strip().split('\t')
    d=getNoun(line2)
    for k,v in words.items():
        print k.decode('utf-8'), v
    
f.close()    
#f1.close()
