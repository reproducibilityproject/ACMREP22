# This Source Code Form is subject to the terms of the Creative
# Commons V1 License. If a copy of the same was not distributed with this
# file, You can obtain one at
# https://github.com/reproducibilityproject/ACMREP22/blob/main/LICENSE

import numpy as np
import pandas as pd
from tqdm import tqdm
from sklearn import metrics
from collections import Counter
from sklearn.ensemble import RandomForestClassifier

#@title Regular Supervised Learning model [RandomForestClassifier]
# define the model class
model = RandomForestClassifier(random_state=1234)

# fit the model
model.fit(X_train, y_train)

# print model params
print(model)

# make the predictions
y_predict = model.predict(X_test)
y_predict_val = model.predict(X_val)

# print evaluation metrics
print('Classification results:')
rec = metrics.accuracy_score(y_test, y_predict)
print("Test accuracy: %.2f%%" % (rec * 100.0))
rec_val = metrics.accuracy_score(y_val, y_predict_val)
print("Val accuracy: %.2f%%" % (rec_val * 100.0))
f1 = metrics.f1_score(y_test, y_predict, average='micro')
f1_val = metrics.f1_score(y_val, y_predict_val, average='micro')
print("Test micro f1: %.2f%%" % (f1 * 100.0))
print("Val micro f1: %.2f%%" % (f1_val * 100.0))
test_roc_score = metrics.roc_auc_score(y_test, model.predict_proba(X_test), multi_class="ovr", average='weighted')
val_roc_score = metrics.roc_auc_score(y_val, model.predict_proba(X_val), multi_class="ovr", average='weighted')
print("Test micro avg ROC AUC score: %.2f%%" % (test_roc_score * 100.0))
print("Val micro avg ROC AUC score: %.2f%%" % (val_roc_score * 100.0))

