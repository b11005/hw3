from sklearn.datasets import load_digits
from sklearn.cross_validation import train_test_split
from sklearn import svm
from sklearn.metrics import accuracy_score,classification_report

digits = load_digits()
print(digits.data.shape)
data_train, data_test, label_train, label_test = train_test_split(digits.data, digits.target)

lin_svc = svm.LinearSVC()
lin_svc.fit(data_train, label_train)
predict = lin_svc.predict(data_test)
print (accuracy_score(label_test, predict))
print (classification_report(label_test, predict))
