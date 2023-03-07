# This Source Code Form is subject to the terms of the Creative
# Commons V1 License. If a copy of the same was not distributed with this
# file, You can obtain one at
# https://github.com/reproducibilityproject/ACMREP22/blob/main/LICENSE

import numpy as np
import pandas as pd

# helper function to load data
def load_data():
    # read the dataframe with badged articles
    badged_data = pd.read_csv('acm_results_reproduced.csv')

    # change funding source column
    badged_data = badged_data.assign(fund_avail = list(map(lambda x: 1 if type(x) == str \
                                                           else 0, \
                                                           badged_data.funding_sources)))
    # change acceptance rate column
    badged_data = badged_data.assign(accept_avail = list(map(lambda x: 1 if type(x) == str \
                                                           else 0, \
                                                           badged_data.acceptance_rate)))

    # add link to code column
    badged_data = badged_data.assign(link_to_code = list(map(is_hyp_pres, \
                                                             badged_data.paper_full_text)))

    # set the target variable
    badged_data = badged_data.assign(target = list(map(lambda x: 1, badged_data.doi)))

    # read the dataframe with unbadged articles
    unbadged_data = pd.read_csv('acm_unbadged_articles.csv')

    # change funding source column
    unbadged_data = unbadged_data.assign(fund_avail = list(map(lambda x: 1 if type(x) == str \
                                                           else 0, \
                                                           unbadged_data.funding_sources)))
    # change acceptance rate column
    unbadged_data = unbadged_data.assign(accept_avail = list(map(lambda x: 1 if type(x) == str \
                                                           else 0, \
                                                           unbadged_data.acceptance_rate)))

    # add link to code column
    unbadged_data = unbadged_data.assign(link_to_code = list(map(is_hyp_pres, \
                                                             unbadged_data.paper_full_text)))

    # set the target variable
    unbadged_data = unbadged_data.assign(target = list(map(lambda x: 0, unbadged_data.doi)))
    
    # read the data frame
    acm_full_data = pd.read_csv('acm_full_Wed_Feb_16_00_26_14_2022.csv')

    # binary feature for funding source availability
    acm_full_data = acm_full_data.assign(fund_avail = list(map(lambda x: 1 if type(x) == str \
                                                  else 0, acm_full_data.funding_sources)))

    # binary feature for acceptance rate availability
    acm_full_data = acm_full_data.assign(accept_avail = list(map(lambda x: 1 if type(x) == int \
                                                  else 0, acm_full_data.acceptance_rate)))

    # add link to code column
    acm_full_data = acm_full_data.assign(link_to_code = list(map(is_hyp_pres, \
                                                             acm_full_data.full_text)))

    # artifacts available
    acm_art_avail =  acm_full_data.loc[acm_full_data['badges'].apply(lambda x: 'Artifacts Available' in x and \
                                             'Artifacts Evaluated & Reusable' not in x and \
                                             'Results Reproduced' not in x)].reset_index(drop=True)

    # rename citations to gs_citations
    acm_art_avail = acm_art_avail.rename(columns={'citations': 'gs_citations'})

    # add target
    acm_art_avail = acm_art_avail.assign(target = list(map(lambda x: 2, range(len(acm_art_avail)))))

    # gather the list of linguistic features
    # linguistic_features = ['yules_i', 'word_count', 'average_word_length', 
    #                        'fwgawl','syllables_count', 'complex_words']

    # gather the list of scholarly features
    scholarly_features = ['gs_citations']

    # gather the list of structural features
    structural_features = ['is_intro_pres', 'is_meth_pres','is_res_pres',
                           'no_images', 'no_tables', 'no_alg',
                           'no_equations']

    # gather misc features
    misc_features = ['fund_avail', 'accept_avail', 'suppl_info', 'link_to_code']

    # gather the target value
    target_val = ['target']

    # form a list of comprising of all the features
    X_y =  scholarly_features + \
            structural_features + \
            misc_features + \
            target_val

    # concat the datasets
    raw_data = pd.concat([badged_data[X_y + ['index_terms']], \
                          unbadged_data[X_y + ['index_terms']], \
                          acm_art_avail[X_y + ['index_terms']]])

    # reset the index
    raw_data = raw_data.reset_index(drop=True)

    # return raw pandas dataframe
    return raw_data, X_y
