#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys, os
import codecs
import numpy as np

from sklearn.feature_extraction.text import TfidfVectorizer #テキストから特徴量を抽出
from sklearn.cluster import KMeans, MiniBatchKMeans#K平均法。非階層型クラスタリングアルゴリズム
from sklearn.decomposition import TruncatedSVD#特徴量の次元圧縮
from sklearn.preprocessing import Normalizer#スケーリングーバランスをとるため、平均を引いて標準偏差で割る

class Analyzer:
    def __init__(self, args):#クラスタリングの設定
        self.infile = args[1]
        self.outfile = args[2]
        self.num_clusters = 10 #分類するクラスタの数ー変更するとまた結果がかわるかも
        self.lsa_dim = 500
        self.max_df = 0.8
        self.max_features = 10000
        self.minibatch = True

    def _read_from_file(self):#ファイル読み込み
        list = []
        file = open(self.infile, 'r')
        for line in file:
            line2,line2=line.strip().split('\t')
            list.append(line2)
        file.close
        return list

    def make_cluster(self):#クラスタを生成して返す
        texts = self._read_from_file()#処理対象の文字列によるリストを生成する
#        print("texts are %(texts)s" %locals() )
        #ベクトルを生成する
        vectorizer = TfidfVectorizer(
            max_df=self.max_df,
            max_features=self.max_features,
            stop_words='english'
            )
        X = vectorizer.fit_transform(texts)
#        print("X values are %(X)s" %locals() )
        #KMeans K平均法ーインスタンスを生成しクラスタリングする
        #パラメータはデータ量や特性に応じて適切なものを与えるようにする
        if self.minibatch:
            km = MiniBatchKMeans(
                n_clusters=self.num_clusters,
                init='k-means++', batch_size=1000,
                n_init=10, max_no_improvement=10,
                verbose=True
                )
        else:
            km = KMeans(
                n_clusters=self.num_clusters,
                init='k-means++',
                n_init=1,
                verbose=True
                )
        km.fit(X)
        labels = km.labels_
        #属するクラスタとその距離を計算する
        transformed = km.transform(X)
        dists = np.zeros(labels.shape)
        for i in range(len(labels)):
            dists[i] = transformed[i, labels[i]]

        clusters = []
        for i in range(self.num_clusters):
            cluster = []
            ii = np.where(labels==i)[0]
            dd = dists[ii]
            di = np.vstack([dd,ii]).transpose().tolist()
            di.sort()
            for d, j in di:
                cluster.append(texts[int(j)])
            clusters.append(cluster)

        return clusters #生成したクラスタを返す

    def write_cluster(self, clusters):
        f = codecs.open('result.txt', 'w', 'utf-8')#ファイル名は固定！上書きされてしまいます。
        for i, texts in enumerate(clusters):
            for text in texts:
                f.write('%d: %s\n' % (i, text.replace('/n', '')))

if __name__ == '__main__':
    if sys.version_info > (3,0):
        if len(sys.argv) > 2:
            analyzer = Analyzer(sys.argv)
            clusters = analyzer.make_cluster()
            #print("Result clusters are %(clusters)s" %locals() )
            analyzer.write_cluster(clusters)

        else:
            print("Invalid arguments")
    else:
        print("This program require python > 3.0")
