'''
Created on Aug 31, 2011

@author: h0cked
'''

import numpy as np

#cross_validation.Bootstrap(n_samples, n_bootstraps=100, n_train=0.4, random_state=0 )

class Scaler(object):
    """Scaler does the same as svm-scale
    """
    
    def __init__(self, lower=-1.0, upper=1.0):
        """Scale each feature independently to [min, max]
        Parameters
        ----------
       
        """

        self.lower = lower
        self.upper = upper
        self.features_min = None
        self.features_max = None
        
        
          
    def fit(self, X_train):
        
        n_samples, n_features = X_train.shape
        
        X_train = np.array(X_train)
        
        features_min = np.zeros(n_features)
        features_max = np.zeros(n_features)
        
        for f_idx in range(n_features):
            features_min[f_idx] = min(X_train[:,f_idx])        
            features_max[f_idx] = max(X_train[:,f_idx])
            
        self.features_min = features_min
        self.features_max = features_max
        
        return self
    
    def transform(self, X_test): #not just test, you need to transform the train as well
        
        features_min = self.features_min
        features_max = self.features_max
        
        assert features_min != None, ValueError('Probably you have not run fit on training data set yet!') 
        assert features_max != None, ValueError('Probably you have not run fit on training data set yet!') 
        
        n_samples, n_features = X_test.shape
        
        assert n_features == len(features_min), ValueError('The number of featuers in your input data is not the same when you ran fit!')
        
        lower = self.lower
        upper = self.upper
        
        X = np.zeros((n_samples, n_features), float)
        
        for f_idx in range(n_features):
            for i in range(n_samples):
                v = X_test[i,f_idx]
                if v == features_min[f_idx]:
                    v = lower
                if v == features_max[f_idx]:
                    v = upper
                    
                X[i,f_idx] = lower + (upper-lower) * (v-features_min[f_idx])/(features_max[f_idx]-features_min[f_idx])
        
        
        return X
        
    
    def __repr__(self):
        return '%s.%s(lower=%0.1f, upper=%0.1f)' % (
                                self.__class__.__module__,
                                self.__class__.__name__,
                                self.lower,
                                self.upper,
                                )
