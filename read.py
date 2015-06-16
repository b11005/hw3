#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding("utf-8")

f = open('links.txt')
wiki_name = {}
new_file = open('subgraph_links.txt','w')

for line in f:
    link1,link2 = line.strip().split('\t')
    if int(link1) < 10000 and int(link2) < 10000:
        print >> new_file, line.strip()

f.close()
new_file.close()

f1 = open('pages.txt')
topic={}
file=open('sub.txt','w')

for page in f1:
    page1,page2 = page.strip().split('\t')
    page2=page2.decode('utf-8')
    if int(page1)<10000 and len(page2)<10000:
        print >> file, page.strip()
f1.close()
file.close()
