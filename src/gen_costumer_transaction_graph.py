import pandas as pd
import numpy as np
import networkx as nx

from src.riski_const import FeaturesNames


class GenCTG:
    def __init__(self, df: pd.DataFrame):
        self.__df = df
        self.__riski_graph = None
        self.__score_mat = None

    def run(self):
        self.__create_scoring_matrix()
        self.__create_connectivity_mat()

    def get_ctg(self):
        return self.__riski_graph

    def get_ctg_base_mat(self):
        return self.__score_mat

    def __create_scoring_matrix(self):
        print('Please wait while I am calculating the CTG...')

        # init vars
        trans_sz = len(self.__df)
        trans_mat = np.zeros((trans_sz, trans_sz))

        # calculate connectivity matrix
        # TODO: optimize this part
        for i in range(0, trans_sz - 1):
            for j in range(i + 1, trans_sz):
                trans_mat[i, j] = self.__set_score_2_trans(self.__df.iloc[i], self.__df.iloc[j])

        # add the matrix conjugate transpose for Symmetry
        trans_mat = trans_mat.conj().T + trans_mat
        trans_mat = trans_mat / trans_mat.max()
        self.__score_mat = trans_mat

    @staticmethod
    def __set_score_2_trans(trans1, trans2) -> float:
        # create new feature - the 2 trans have same email/time/etc.
        # each common feature will add 1 to the score.
        return sum(np.array(trans1[FeaturesNames.COMBINED]) == np.array(trans2[FeaturesNames.COMBINED]))

    def __create_connectivity_mat(self):
        top_001 = np.percentile(self.__score_mat, 99.9)
        top_001_mat = (self.__score_mat >= top_001) * self.__score_mat
        top_001_graph = nx.from_numpy_matrix(top_001_mat)
        self.__riski_graph = top_001_graph
        self.__riski_mat = top_001_mat
