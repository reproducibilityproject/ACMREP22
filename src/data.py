# This Source Code Form is subject to the terms of the Creative
# Commons V1 License. If a copy of the same was not distributed with this
# file, You can obtain one at
# https://github.com/reproducibilityproject/ACMREP22/blob/main/LICENSE

import numpy as np
import pandas as pd
from tqdm import tqdm
from dataloader import load_data
from collections import Counter
from sklearn.model_selection import train_test_split

# use data loader to obtain raw data
raw_data, X_y = load_data()

# show the columns
print("Columns of the final data: \n", raw_data[X_y].columns)

# assing the features and labels to a numpy array
X_raw = raw_data[X_y[:-1]].values
y_raw = raw_data[X_y[-1]].values

# obtain unlabeled samples
X_unlab = raw_data.loc[raw_data.target.apply(lambda x: x==0)].reset_index(drop=True)[X_y[:-1]].values
y_unlab = raw_data.loc[raw_data.target.apply(lambda x: x==0)].reset_index(drop=True)[X_y[-1]].values

#@title Prepare data for training and testing, and querying
X_train, X_test, y_train, y_test = train_test_split(raw_data[X_y[:-1]].values, raw_data[X_y[-1]].values, test_size=0.2, random_state=123)
X_train, X_val, y_train, y_val = train_test_split(X_train, y_train, test_size=0.25, random_state=123)

# set seed for numpy
np.random.seed(2022)

# obtain 10 percent of the training data
no_train_samples = np.random.randint(low=0, high=X_train.shape[0], size=int(np.floor(X_train.shape[0]/10)))
X_train_10 = X_train[no_train_samples]
y_train_10 = y_train[no_train_samples]

# Isolate our examples for our labeled dataset.
n_labeled_examples = X_train_10.shape[0]
training_indices = np.random.randint(low=0, high=n_labeled_examples + 1, size=3)

X_train_al = X_train_10[training_indices]
y_train_al = y_train_10[training_indices]

# Isolate the non-training examples we'll be querying.
X_pool = np.delete(X_train_10, training_indices, axis=0)
y_pool = np.delete(y_train_10, training_indices, axis=0)


