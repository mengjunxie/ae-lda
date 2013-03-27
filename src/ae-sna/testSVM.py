"""
=====================================================================
test SVM
=====================================================================
"""
print __doc__

import logging
import numpy as np

from scipy import interp
import pylab as pl

from sklearn.metrics import roc_curve, auc

from sklearn.cross_validation import train_test_split
from sklearn.grid_search import GridSearchCV
from sklearn.metrics import precision_score
from sklearn.metrics import recall_score
from svm.util import *
from svm import feature_selection
from svm import sampling

from sklearn.svm import SVC


# Display progress logs on stdout
logging.basicConfig(level=logging.INFO,
    format='[%(asctime)s] [%(levelname)s]: %(message)s')

logger = logging.getLogger(__name__)

def mergeTextualFeaturesWithSemanticFeatures(textualfeatureMatrixFile,semanticfeatureMatrixFile):
    textualfeatureMatrix = np.load(textualfeatureMatrixFile)
    semanticfeatureMatrix = np.load(semanticfeatureMatrixFile)

    subjectFeatureMatrix = []
    for tr in textualfeatureMatrix:
        for sr in semanticfeatureMatrix:
            if tr[0] == sr[0]:
                subjectFV = np.append(np.copy(tr), sr[1:])
                subjectFeatureMatrix.append(subjectFV)

    return np.array(subjectFeatureMatrix)

def main():
    textualfeatureMatrixFile = "../../result/classification-features/textural-features-ae.npy"
    semanticfeatureMatrixFile = "../../result/classification-features/ae-tweets-semGroups-semTypes.npy"


    subjectFeatureMatrix = mergeTextualFeaturesWithSemanticFeatures(textualfeatureMatrixFile,semanticfeatureMatrixFile)

    X_o = np.array(subjectFeatureMatrix[:, 3:], dtype=np.uint)
    y_o = np.array(subjectFeatureMatrix[:, 2], dtype=np.uint)

    random_state = None

    n_bootstraps = 10

    # Set the parameters by cross-validation
    tuned_parameters = [{'kernel': ['linear'], 'C': [1, 10, 100, 1000, 10000]}]

    scores = [
        ('precision', precision_score),
        ('recall', recall_score),
    ]

    score_name = 'recall'
    score_func = recall_score

    fselector = feature_selection.FeatureSelector(mode='fscore',
        params={'tuned_parameters': tuned_parameters, 'min_num_of_features': 2})


    downSampling = sampling.BalancedDownSampling(y_o, n_bootstraps=n_bootstraps, random_state=random_state)

    mean_tpr = 0.0
    mean_fpr = np.linspace(0, 1, 100)
    all_tpr = []
    all_acc = []


    best_sample_indices = None

    best_roc_auc = 0



    for i, sample_indices in enumerate(downSampling):
        X = X_o[sample_indices, :]
        y = y_o[sample_indices]

        fselector = fselector.select(X, y)
        #fselector.best_features

        print fselector

        X = X[:, fselector.best_features]

        X_train, X_test, y_train, y_test = train_test_split(X, y, test_fraction=0.33, random_state=0)

        logger.info("# Tuning hyper-parameters for %s" % score_name)

        clf = GridSearchCV(SVC(C=1, probability=True), tuned_parameters, score_func=score_func)
        clf.fit(X_train, y_train, cv=5)

        logger.info("Best parameters set found on development set: %s" % clf.best_estimator)
        logger.info("==========")

        clf = clf.best_estimator

        y_true, y_pred = y_test, clf.predict(X_test)
        #print classification_report(y_true, y_pred)

        probas_ = clf.predict_proba(X_test)

        acc = accuracy(y_test, y_pred)
        logger.info("Accuracy: %s", acc)
        all_acc.append(acc)

        fpr, tpr, thresholds = roc_curve(y_test, probas_[:, 1])
        mean_tpr += interp(mean_fpr, fpr, tpr)
        mean_tpr[0] = 0.0
        roc_auc = auc(fpr, tpr)
        logger.info("ROC_AUC: %s", roc_auc)

        if roc_auc > best_roc_auc:
            best_roc_auc = roc_auc
            best_sample_indices = sample_indices

    pl.plot([0, 1], [0, 1], '--', color=(0.6, 0.6, 0.6), label='Luck')

    mean_acc = np.sum(all_acc) / n_bootstraps

    logger.info('(Mean ACC: %0.2f)' % mean_acc)
    mean_tpr /= n_bootstraps
    mean_tpr[-1] = 1.0
    mean_auc = auc(mean_fpr, mean_tpr)
    pl.plot(mean_fpr, mean_tpr, 'k--', color='red',
        label='Mean ROC (area = %0.2f)' % mean_auc, lw=2)

    pl.xlim([-0.05, 1.05])
    pl.ylim([-0.05, 1.05])
    pl.xlabel('False Positive Rate (FTR)')
    pl.ylabel('True Positive Rate (TPR)')
    pl.title('(Mean ACC: %0.2f)' % (mean_acc))
    pl.legend(loc="lower right")

    pl.show()
    pl.close()

    print best_roc_auc, best_sample_indices

    return


if __name__ == '__main__':
    main()