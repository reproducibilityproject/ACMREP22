## Leveraging human-in-the-loop ML models to learn representations of reproducible articles

## Abstract
Reproducibility crisis in science unequivocally influenced the approach to conduct research across various disciplines, consequently encouraging researchers to produce preemptively reproducible works. The expectations of preemptively reproducible research include accessible data, hyperlink to code repository, and availability of supplemental artifacts. Additionally, having limited data on signals for reproducible science makes it challenging to hold a nuanced perspective on what it means to be reproducible for the respective discipline. Human-in-the-loop machine learning techniques are capable on operating on limited data to helps us learn representations of potential signals for reproducibility across topics, journals, and conferences. In this paper, we built a dataset of ACM articles that are a.) Badged as "Results Reproduced``, b.) Badged as "Artifacts Available," and c.) Unbadged. We then trained an active learning model to distinguish reproducible articles from other badged categories. Our active learning model utilized only 10% of training data and performed similar to best performing supervised learning model. The results make a strong case for human-in-the-loop machine learning techniques as a strategy for learning representations about reproducible works.

## Install necessary libraries
```bash
# install numpy
!pip install -q numpy

# install pandas
!pip install -q pandas

# install tqdm
!pip install -q tqdm

# install scikit-learn
!pip install -q scikit-learn

# install active learning library modAL
!pip install -q modAL

# install skorch
!pip install -q skorch
```

## Repository structure
The repository consists of information associated with the research on **Reproducibility Badges** for the paper *Leveraging human-in-the-loop ML models to learn representations of reproducible articles*. This work is a smaller part of a larger project on understanding Reproducibility in Sciences. The repository has 4 directories:
- `data/` - The directory that consists of three datasets used for the statistical tests.
- `src/` - Code, documentation, and essential information about the models built for the project.
- `scripts/` - Essential scripts necessary for setting up the project.
- `notebooks/` - Jupyter notebook(s) with sample code showcasing how to utilize the resources of the project.

## License
[Creative Commons v1](https://github.com/reproducibilityproject/ACMREP22/blob/main/LICENSE)

## Authors
[Akhil Pandey](https://github.com/akhilpandey95), [Hamed Alhoori](https://github.com/alhoori), [David Koop](https://github.com/dakoop)

## Acknowledgement
This work is supported in part by NSF Grant No. [2022443](https://www.nsf.gov/awardsearch/showAward?AWD_ID=2022443&HistoricalAwards=false).



