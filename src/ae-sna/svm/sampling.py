'''
Created on Aug 31, 2011

@author: h0cked
'''

import numpy as np

from sklearn.utils import check_random_state

#cross_validation.Bootstrap(n_samples, n_bootstraps=100, n_train=0.4, random_state=0 )

class BootstrapStartified(object):
    """Bootstrap through stratified sampling
    """
    
    def __init__(self, y, n_test=2, n_bootstraps=10, half_and_half=False, random_state=None):
        """Bootstrap through stratified sampling
        Parameters
        ----------
        y: array, [n_samples]
            Samples to pick out 
        n_test: int
            number of test samples
        """
        self.y = y
        self.n_test = n_test
        self.n_bootstraps = n_bootstraps
        self.random_state = random_state
        self.half_and_half = half_and_half
    
    def __iter__(self):
        rng = self.random_state = check_random_state(self.random_state)
        y = self.y.copy()
        n_test = self.n_test
        n = y.size
        
        idx = range(n)
        
        labels = np.unique(y)    
        assert labels.size == 2, ValueError('We can only deal with 2-class; labels.size = %d' % labels.size)
        
        p_y = np.flatnonzero(y == labels[0])
        n_y = np.flatnonzero(y == labels[1])
        
        if self.half_and_half:
            n_p_y_test = int(n_test * 0.5)
            n_n_y_test = int(n_test * 0.5)
        else:
            n_p_y_test = int(n_test * (float(p_y.size) / float(y.size)))
            n_n_y_test = int(n_test * (float(n_y.size) / float(y.size)))
        
        for i in range(self.n_bootstraps):
         
            p_y_c = p_y.copy()
            n_y_c = n_y.copy()
            rng.shuffle(p_y_c)
            rng.shuffle(n_y_c)           
      
            test_index = np.union1d(p_y_c[0:n_p_y_test], n_y_c[0:n_n_y_test])
            train_index = np.setdiff1d(idx, test_index, assume_unique=True)
                        
            yield train_index, test_index
            
    
    def __repr__(self):
        return '%s.%s(labels=%s, n_test=%i, n_bootstraps=%i, half_and_half=%s, random_state=%s)' % (
                                self.__class__.__module__,
                                self.__class__.__name__,
                                self.y,
                                self.n_test,
                                self.n_bootstraps,
                                self.half_and_half,
                                self.random_state
                                )

    def __len__(self):
        return self.n_test
    
    
class BalancedDownSampling(object):
    """In a unbalanced dataset, downsampling the larger class
    """
    
    def __init__(self, y, n_bootstraps=10, random_state=None):
        """In a unbalanced dataset, downsampling the larger class
        Parameters
        ----------
        y: array, [n_samples]
            Samples to pick out
        """
        self.y = y
        self.n_bootstraps = n_bootstraps
        self.random_state = random_state
        
    def __iter__(self):        
        rng = self.random_state = check_random_state(self.random_state)
        y = self.y.copy()
        n = y.size
        
        idx = range(n)
        
        labels = np.unique(y)    
        assert labels.size == 2, ValueError('We can only deal with 2-class; labels.size = %d' % labels.size)
        
        p_y = np.flatnonzero(y == labels[0])
        n_y = np.flatnonzero(y == labels[1])
        
        s = np.minimum(p_y.size, n_y.size) 

        for i in range(self.n_bootstraps):
         
            p_y_c = p_y.copy()
            n_y_c = n_y.copy()
            rng.shuffle(p_y_c)
            rng.shuffle(n_y_c)           
      
            sample_indices = np.union1d(p_y_c[0:s], n_y_c[0:s])
            
            rng.shuffle(sample_indices)            
            
            yield sample_indices
        
            
    
    def __repr__(self):
        return '%s.%s(labels=%s, n_bootstraps=%i, random_state=%s)' % (
                                self.__class__.__module__,
                                self.__class__.__name__,
                                self.y,
                                self.n_bootstraps,
                                self.random_state
                                )

    def __len__(self):
        return self.n_bootstraps