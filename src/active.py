# This Source Code Form is subject to the terms of the Creative
# Commons V1 License. If a copy of the same was not distributed with this
# file, You can obtain one at
# https://github.com/reproducibilityproject/ACMREP22/blob/main/LICENSE

import numpy as np
import pandas as pd
from tqdm import tqdm
from sklearn import metrics
from collections import Counter
from modAL.models import ActiveLearner
from modAL.uncertainty import uncertainty_sampling

#@title Build and train the active learning model
# Specify our core estimator along with it's active learning model.
rf = RandomForestClassifier(n_estimators=100, random_state=123)

# build the active learning model
learner = ActiveLearner(estimator=rf, \
                        X_training=X_train_al, \
                        y_training=y_train_al)

# Isolate the data we'll need for plotting.
predictions = learner.predict(X_test)
is_correct = (predictions == y_test)

# Record our learner's score on the raw data.
unqueried_score = learner.score(X_test, y_test)
unqueried_score_val = learner.score(X_val, y_val)

# print the unqueried score
print('Unqueried score for the AL model on test data', unqueried_score)
print('Unqueried score for the AL model on validation data', unqueried_score_val)

#@title Query, teach and record the active learning model
N_QUERIES = 75
performance_history = [unqueried_score]
performance_history_val = [unqueried_score_val]

# Allow our model to query our unlabeled dataset for the most
# informative points according to our query strategy (uncertainty sampling).
for index in range(N_QUERIES):
  query_index, query_instance = learner.query(X_pool)

  # Teach our ActiveLearner model the record it has requested.
  X, y = X_pool[query_index].reshape(1, -1), y_pool[query_index].reshape(1, )
  learner.teach(X=X, y=y)

  # Remove the queried instance from the unlabeled pool.
  X_pool, y_pool = np.delete(X_pool, query_index, axis=0), np.delete(y_pool, query_index)

  # Calculate and report our model's accuracy.
  model_accuracy = learner.score(X_test, y_test)
  model_accuracy_val = learner.score(X_val, y_val)
  print('Accuracy after query {n}: {acc:0.4f}'.format(n=index + 1, acc=model_accuracy))

  # Save our model's performance for plotting.
  performance_history.append(model_accuracy)
  performance_history_val.append(model_accuracy_val)



