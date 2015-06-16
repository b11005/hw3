# -*- coding: utf-8 -*-

import MeCab
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

words={}
def getNoun(text):#単語に区切り、単語が何回でてくるか数える
    tagger=MeCab.Tagger('-Owakati')#MeCabの設定
    tagger.parse('')#parseToNodeのバグ回避
    node=tagger.parseToNode(text.encode('utf-8'))
#    node=tagger.parse(text)
    while node:#ハッシュに入れて数える
        noun=node.feature.split(",")[0]
        if noun==u'名詞':
            words.setdefault(node.surface,0)
            words[node.surface]+=1
        node=node.next
    return words
    
f=open('sub.txt')
#f1=open('collocation.txt','w')
for line in f:
    line1,line2=line.strip().split('\t')
    d=getNoun(line2)
    for k,v in sorted(words.items(), key=lambda x:x[1], reverse=True):
        print k.decode('utf-8'), v,
    print
    
f.close()    
#f1.close()
