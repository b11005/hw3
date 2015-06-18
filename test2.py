#_*_ coding:utf-8 _*_

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
from sklearn.decomposition import TruncatedSVD
from sklearn.preprocessing import Normalizer


def main():

    _items = [
        'わたし まけ まし た わ',
        'わたし まけ まし た わ',
        'わたし まけ まし た わ',
        'わたし まけ まし た わ',
        'となり の きゃく は よく かき くう きゃく だ',
        'にわ には にわ なかにわ には にわ にわとり が いる',
        'バカ と テスト と 召喚獣',
        '俺 の 妹 が こんな に 可愛い わけ が ない'
    ]


    vectorizer = TfidfVectorizer(
        use_idf=True
    )
    X = vectorizer.fit_transform(_items)

    lsa = TruncatedSVD(10)
    X = lsa.fit_transform(X)
    X = Normalizer(copy=False).fit_transform(X)

    km = KMeans(
        init='k-means++',
    )
    km.fit(X)

    print(km.labels_)


if __name__ == '__main__':
    main()
