# This Source Code Form is subject to the terms of the Creative
# Commons V1 License. If a copy of the same was not distributed with this
# file, You can obtain one at
# https://github.com/reproducibilityproject/ACMREP22/blob/main/LICENSE

import numpy as np
import pandas as pd
from tqdm import tqdm
import seaborn as sns
import matplotlib as mpl
import matplotlib.pyplot as plt
from collections import Counter
from sklearn.manifold import TSNE
from sklearn.decomposition import PCA

#@title Evaluating the performance of the AL model
# Plot our performance over time.
fig, ax = plt.subplots(figsize=(8.5, 6), dpi=130)

ax.plot(performance_history, label='AL test accuracy')
ax.plot(performance_history_val, label='AL val accuracy')
# specifying horizontal line type
# ax.axhline(y = max(performance_history), color = 'r', linestyle = '--')
# ax.axvline(x = performance_history.index(max(performance_history)), color = 'r', linestyle = '--')
ax.scatter(range(len(performance_history)), performance_history, s=13)
ax.scatter(range(len(performance_history_val)), performance_history_val, s=13)
# ax.scatter(performance_history.index(max(performance_history)), max(performance_history), label='Max test Acc: ' + str(np.round(max(performance_history), 4) * 100), s=100)

ax.xaxis.set_major_locator(mpl.ticker.MaxNLocator(nbins=5, integer=True))
ax.yaxis.set_major_locator(mpl.ticker.MaxNLocator(nbins=10))
ax.yaxis.set_major_formatter(mpl.ticker.PercentFormatter(xmax=1))

ax.set_ylim(bottom=0, top=1)
ax.grid(True)

# ax.set_title('Incremental classification accuracy')
ax.set_xlabel('Query iteration')
ax.set_ylabel('Classification Accuracy')
ax.legend()

plt.show()


#@title Evaluating the performance of the Pytorch AL model
# Plot our performance over time.
fig, ax = plt.subplots(figsize=(8.5, 6), dpi=130)

ax.plot(torch_pf_history)
ax.scatter(range(len(torch_pf_history)), torch_pf_history, s=13)

ax.xaxis.set_major_locator(mpl.ticker.MaxNLocator(nbins=5, integer=True))
ax.yaxis.set_major_locator(mpl.ticker.MaxNLocator(nbins=10))
ax.yaxis.set_major_formatter(mpl.ticker.PercentFormatter(xmax=1))

ax.set_ylim(bottom=0, top=1)
ax.grid(True)

ax.set_title('Incremental classification accuracy of the Pytorch AL model')
ax.set_xlabel('Query iteration')
ax.set_ylabel('Classification Accuracy')

plt.show()

