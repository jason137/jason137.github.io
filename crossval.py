#!/usr/bin/env python3
import numpy as np
import pandas as pd
pd.set_option('display.width', None)

import sklearn.cross_validation as cv
from sklearn.linear_model import LogisticRegression as LR
from sklearn.tree import DecisionTreeClassifier as Tree

from ggplot import *

INPUT_FILE = 'data/heart_disease.tsv'

# cf Wasserman c22

# TODO create un-regzd logistic regression?

def get_extended_data(input_file=INPUT_FILE):

    raw_data = pd.read_csv(input_file, sep='\t')
    features, target = raw_data.ix[:, :-1], raw_data.ix[:, -1]

    N = len(features.columns)   # 9
    for i in range(N):

        # initialize extended feature set
        if i == 0:
            ext_features = features

        squared_dim = features.ix[:, i] ** 2
        ext_features = pd.concat([ext_features, squared_dim], axis=1)
        new_col = features.columns[i] + '_2'
        ext_features.columns = ext_features.columns.tolist()[:-1] + [new_col]

    return ext_features, target

def run_models(features, target):

    errors = list()

    N = len(features.columns)   # 18
    for i in range(N):

        # clf = LR()
        clf = Tree()
        model_features = pd.DataFrame(features.ix[:, :i + 1])    # make sure 1d df is not interpreted as Series

        results = cv.cross_val_score(clf, model_features, target, cv=10)
        err = round(100 * (1 - np.mean(results)), 0)
        errors.append(err)

    k = pd.DataFrame({'num_features': range(1, N+1), 'error_rate': errors})
    k = k[['num_features', 'error_rate']]
    print(k)

    plot = ggplot(k, aes('num_features', 'error_rate'))
    plot = plot + geom_point() + geom_line()

    print(plot)

def main():

    xs, y = get_extended_data()
    run_models(xs, y)

if __name__ == '__main__':
    main()
