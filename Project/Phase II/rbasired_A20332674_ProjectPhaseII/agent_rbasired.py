import sys
import numpy as np

from sklearn import cross_validation
from sklearn import linear_model
from sklearn.preprocessing import StandardScaler

from sklearn import svm
from sklearn.naive_bayes import BernoulliNB
from sklearn.svm import SVC
from sklearn.neighbors import NearestNeighbors
from sklearn.ensemble import RandomForestClassifier
from sklearn import tree
from agents import Agent
from sklearn.ensemble import AdaBoostClassifier
from sklearn.cross_validation import cross_val_score
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import ExtraTreesClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import GradientBoostingClassifier

class rbasired(Agent):
    
    def fit_a_classifier(self, X_train, y_train, X_validation, y_validation):

	treeClf = tree.DecisionTreeClassifier()
	treeClf.fit(X_train, y_train);
	treeScore = cross_val_score(treeClf, X_validation, y_validation).mean()
	"print treeScore"
	
	svmClf = svm.SVC(probability = True)
	svmClf.fit(X_train, y_train)
	svmScore = cross_val_score(svmClf, X_validation, y_validation).mean()
	"print svmScore"

	randomClf = RandomForestClassifier()
	randomClf.fit(X_train, y_train)
	randomScore = cross_val_score(randomClf, X_validation, y_validation).mean()
	"print randomScore"

	bernoulliClf = BernoulliNB()
	bernoulliClf.fit(X_train, y_train)
	bernoulliScore = cross_val_score(bernoulliClf, X_validation, y_validation).mean()
	"print bernoulliScore"

	extraTreeClf = ExtraTreesClassifier()
	extraTreeClf.fit(X_train, y_train)
	extraTreeScore = cross_val_score(extraTreeClf, X_validation, y_validation).mean()
	"print extraTreeScore"

	adaBoostClf = AdaBoostClassifier()
	adaBoostClf.fit(X_train, y_train)
	adaBoostScore = cross_val_score(adaBoostClf, X_validation, y_validation).mean()
	"print adaBoostScore"

	graBoostClf = GradientBoostingClassifier()
	graBoostClf.fit(X_train, y_train)
	graBoostScore = cross_val_score(graBoostClf, X_validation, y_validation).mean()
	"print graBoostScore"
	
	"Default classifier as Bernoulli"
        self.classifier = bernoulliClf	
	if (treeScore > graBoostScore and treeScore > adaBoostScore and treeScore > extraTreeScore and treeScore > bernoulliScore and treeScore > randomScore and treeScore > svmScore):
	        self.classifier = treeClf
		print "Tree Classifier"
	if (svmScore > graBoostScore and svmScore > adaBoostScore and svmScore > extraTreeScore and svmScore > bernoulliScore and svmScore > randomScore and svmScore > treeScore):
	        self.classifier = svmClf
		print "SVM Classifier"
	if (randomScore > graBoostScore and randomScore > adaBoostScore and randomScore > extraTreeScore and randomScore > bernoulliScore and randomScore > svmScore and randomScore > treeScore):
	        self.classifier = randomClf
		print "Random Classifier"
        if (bernoulliScore > graBoostScore and bernoulliScore > adaBoostScore and bernoulliScore > extraTreeScore and bernoulliScore > svmScore and bernoulliScore > randomScore and bernoulliScore > treeScore):
	        self.classifier = bernoulliClf
		print "Bernoulli Classifier"
        if (extraTreeScore > graBoostScore and extraTreeScore > adaBoostScore and extraTreeScore > bernoulliScore and extraTreeScore > svmScore and extraTreeScore > randomScore and extraTreeScore > treeScore):
	        self.classifier = extraTreeClf
		print "Extra Tree Classifier"
        if (adaBoostScore > graBoostScore and adaBoostScore > extraTreeScore and adaBoostScore > bernoulliScore and adaBoostScore > svmScore and adaBoostScore > randomScore and adaBoostScore > treeScore):
	        self.classifier = adaBoostClf
		print "Ada Boost Classifier"
	if (graBoostScore > adaBoostScore and graBoostScore > extraTreeScore and graBoostScore > bernoulliScore and graBoostScore > svmScore and graBoostScore > randomScore and graBoostScore > treeScore):
	        self.classifier = graBoostClf
		print "GRA Boost Classifier"
"	self.classifier = treeClf	"
