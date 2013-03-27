#!/sw/bin/python

import math
import numpy as np
import scipy.sparse as sp
import re

def range_f(begin, end, step):
    # like range, but works on non-integer too
    seq = []
    while True:
        if step > 0 and begin > end: break
        if step < 0 and begin < end: break
        seq.append(begin)
        begin = begin + step
    return seq

def permute_sequence(seq):
    n = len(seq)
    if n <= 1: return seq

    mid = int(n / 2)
    left = permute_sequence(seq[:mid])
    right = permute_sequence(seq[mid + 1:])

    ret = [seq[mid]]
    while left or right:
        if left: ret.append(left.pop(0))
        if right: ret.append(right.pop(0))

    return ret

def pow_sequence(seq, base):
	ret = []
	for v in seq:
		ret.append(math.pow(base, v))
	
	return ret
	
def range_log2based(begin, end, step):
	return pow_sequence(permute_sequence(range_f(begin, end, step)), 2)
	
	
def load_svmlight_file(file_path):
	
	datas = []
	labels = []

	pattern = re.compile(r'\s+')

	for line in open(file_path):
		line = line.strip()

		if line.startswith("#"):
			continue

		
		data = []
        # Remove inline comments.
		line = line.split("#")
		line = line[0].strip()

		line = re.sub(pattern, ' ', line)
		y, features = line.split(" ", 1)

		labels.append(float(y))
		
		for feat in features.split(" "):
			idx, value = feat.split(":")

			if value == 'NA':
				value = 0

			data.append(float(value))

		datas.append(data)
    
	return np.array(datas, dtype=np.double), np.array(labels, dtype=np.double)
	
def accuracy(y, y_pred):
    return float(sum(x == True for x in np.equal(y, y_pred))) / float(len(y))


def check_kfold_cv(k, y):
    """Creates a valid and usable cv generator
    """
    if k is None:
        k = 3
        
    y = np.asanyarray(y)
    n = y.shape[0]
    
    _, y_sorted = np.unique(y, return_inverse=True)
    
    max_k = min(np.min(np.bincount(y_sorted)), n)
    
    if k > max_k: #if a big k, then let it do leave-one-out at max
        k = max_k
    
    return k  
            
        

