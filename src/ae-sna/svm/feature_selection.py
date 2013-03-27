'''
Created on Aug 31, 2011

@author: h0cked
'''

import math
import numpy as np
import itertools as it
import scipy.stats

from sklearn import cross_validation
from .util import *

from sklearn.grid_search import GridSearchCV
from sklearn import svm
from sklearn.metrics import classification_report
from sklearn.metrics import precision_score
from sklearn.metrics import recall_score
from sklearn.metrics import roc_curve, auc
from sklearn.metrics import confusion_matrix



################################################################################
# Univariate feature selection
from sklearn.feature_selection import SelectKBest, f_classif
# As a scoring function, we use a F test for classification


#Feature Selector
class FeatureSelector:
    
    def __init__(self, mode='fscore', params=None):
        self.mode = mode
        self.params = params
        
        self.best_features = []
        self.cv_score = 0.0
        self._scores = 0.0
        
    def select(self, X_train, y_train, params = None):
        if params != None:
            self.params = params
            
        if self.params != None and 'tuned_parameters' in self.params:
            self.tuned_parameters = self.params['tuned_parameters']
        else:
            self.tuned_parameters = {
                                     #'kernel':('linear', 'rbf'),
                kernel:'rbf',
                       'C': range_log2based(-2,9,2), #[1, 5, 10, 50, 100],-log2c -2,9,2 -log2g 1,-11,-2
                                     'gamma': range_log2based(1,-11,-2)#[0.0001, 0.0005, 0.001, 0.005, 0.01, 0.1],
                                     } 
        
        n_samples, n_features = X_train.shape
        
        if self.mode == 'fscore':
            score_func = f_classif
            min_num_of_features = 2
            if self.params != None and 'score_func' in self.params and self.params['score_func'] != None:
                score_func = self.params['score_func']
            if self.params != None and 'min_num_of_features' in self.params and self.params['min_num_of_features'] != None:
                min_num_of_features = self.params['min_num_of_features']

            return self.fscore_select(X_train, y_train, min_num_of_features, score_func)
        
        if self.mode == 'corrcoef':
            threshold = 0.15
            if self.params != None and 'threshold' in self.params:
                threshold = self.params['threshold']
            
            return self.pearson_corrcoef_select(X_train, y_train, threshold)
        
        if self.mode == 'combinatorial':
            
            features = None
            r_max = None
            
            if self.params != None and 'features' in self.params and self.params['features'] != None:
                features = self.params['features']
            else:
                features = range(n_features)
                
            if self.params != None and 'r_max' in self.params and self.params['r_max'] != None:
                r_max = self.params['r_max']
            else:
                r_max = 11
                
                
            return self.combinatorial_select(X_train, y_train, features, r_max)
        
        return self
    
    def combinatorial_select(self, X_train, y_train, features=None, r_max = 11):
        
        n_features = len(features)
        
        if n_features > r_max:
            n_features = r_max
        
        print 'n_features: %i; features: %s'%(n_features, features)   
        
        #only considering CV scores... may need to extend it to consider ROC_AUC
        b_mean_cv_score = 0.0
        b_features = []     
        for r in range(n_features):
            print 'test combination of %i features'%r
            
            if r == 0: # no reason to do 0 feature
                continue
            for c_iter in it.combinations(features, r):
                X_train_fs = X_train[:,c_iter]
                #print X_train_fs.shape
        
                kf = check_kfold_cv(10, y_train)
                
                #print kf
                    
                #grid search for best params
                grid_search = GridSearchCV(svm.SVC(probability=True), self.tuned_parameters, fit_params={'class_weight': 'auto'}, cv=kf, n_jobs=1)
                grid_search  = grid_search.fit(X_train_fs, y_train)
                
                clf = grid_search.best_estimator
                
                this_scores = cross_validation.cross_val_score(clf, X_train_fs, y_train, cv=kf, n_jobs=1)
                
                mean_cv_score = np.mean(this_scores)
                
                if mean_cv_score > b_mean_cv_score:
                    b_mean_cv_score = mean_cv_score
                    b_features = c_iter
                    
                
        self.cv_score = b_mean_cv_score
        self.best_features = np.array(b_features)
        self._scores = None
        
        return self
    
    def pearson_corrcoef_select(self, X_train, y_train, threshold):
        
        n_samples, n_features = X_train.shape
        
        pearson_ranks = np.zeros(n_features)

        for i in range(n_features):
            pearson_ranks[i], _ = scipy.stats.pearsonr(X_train[:,i], y_train)
        
        pearson_ranks = np.abs(pearson_ranks)
        
        self._scores = pearson_ranks.copy()
        
        #indices = np.argsort(pearson_ranks)
        
        #indices = indices[::-1] #reverse order
        
        self.best_features = np.flatnonzero(pearson_ranks >= threshold)

        X_train_fs = X_train[:,self.best_features]
        
        kf = check_kfold_cv(5, y_train)
            
        #grid search for best params
        grid_search = GridSearchCV(svm.SVC(probability=True), self.tuned_parameters, fit_params={'class_weight': 'auto'}, cv=kf, n_jobs=1)
        grid_search  = grid_search.fit(X_train_fs, y_train)
        
        clf = grid_search.best_estimator
        
        this_scores = cross_validation.cross_validation_score(clf, X_train_fs, y_train, cv=kf, n_jobs=1)
        
        mean_cv_score = np.mean(this_scores)
        
        self.cv_score = mean_cv_score
        
        
        return self
        
        
        
    #use cross-validation to determine the best features
    def fscore_select(self, X_train, y_train, min_num_of_features=2, score_func=f_classif):
        
        n_samples, n_features = X_train.shape
        
        ################################################################################
        # Set the parameters by cross-validation
        tuned_parameters = {
            #'kernel':('linear', 'rbf'),
            'C': range_log2based(-2,9,2), #[1, 5, 10, 50, 100],-log2c -2,9,2 -log2g 1,-11,-2
            'gamma': range_log2based(1,-11,-2)#[0.0001, 0.0005, 0.001, 0.005, 0.01, 0.1],
        }
        
        k = n_features
       
        b_mean_cv_score = 0.0
        b_features = []
        
        
        
        while k > 2:
            
            #print k
            #feature selection
            selector = SelectKBest(score_func, k=k)
            selector.fit(X_train, y_train)      
            
            X_train_fs = selector.transform(X_train)      
            
            kf = check_kfold_cv(10, y_train)
            
            #grid search for best params
            grid_search = GridSearchCV(svm.SVC(probability=False, class_weight='auto'), self.tuned_parameters, cv=kf, n_jobs=1)
            grid_search  = grid_search.fit(X_train_fs, y_train)
            
            clf = grid_search.best_estimator_
            
            this_scores = cross_validation.cross_val_score(clf, X_train_fs, y_train, cv=kf, n_jobs=-1)
            
            mean_cv_score = np.mean(this_scores)
                   
            if mean_cv_score >= b_mean_cv_score:
                b_mean_cv_score = mean_cv_score
                b_features = selector.get_support(indices=True)
    
            
            k = k - k/3
            
        self._scores = score_func(X_train, y_train)
        self.best_features = np.array(b_features)
        self.cv_score = b_mean_cv_score
        
        return self


    def __repr__(self):
        return '%s.%s(mode=%s, params=%s, cv_score=%s, best_features=%s)' % (
                                self.__class__.__module__,
                                self.__class__.__name__,
                                self.mode,
                                self.params,
                                self.cv_score,
                                self.best_features,
                                )

        