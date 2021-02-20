import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt
import seaborn as sns

from src.riski_const import FeaturesNames


class ExploreCTG:
    def __init__(self, df, ctg, out_dir: str):
        self.__df = df
        self.__ctg = ctg
        self.__riski_mat = None
        self.__out = out_dir

    def run(self):
        self.__plot_network()

    def __plot_network(self):
        """
        function goal is to display matrix as a
                network graph
        """

        # add nodes labels
        labeldict = {}
        idx = 0
        for tmp_nm in self.__df[FeaturesNames.ORDER_ID]:
            labeldict[idx] = tmp_nm
            idx += 1

        # plot the graph
        plt.figure()
        plt.title('Costumer Transactions Graph')
        nx.draw_networkx(self.__ctg,
                         font_size=6,
                         node_size=30,
                         labels=labeldict,
                         with_labels=True,
                         # pos=nx.spring_layout(self.__riski_mat)
                         )
        plt.savefig(self.__out + '\CostumerTransactionGraph.png')  # save as png
        # plt.show()


    def find_communities(self):
        pass

    def __find_clusters(self):
        pass

    def __find_hubs(self):
        # Analyze alignment matrix
        pr = nx.pagerank(self.__ctg, alpha=0.9)
        pr = list(pr.values())

        # # keep the features we want to explore
        # d = {'seq_sz_lst': seq_sz_lst, 'pageRank': pr, 'gc_lst': gc_lst}
        # df = pd.DataFrame(data=d, index=list(range(0, lst_sz)))


#TODO:
# set scoring method
# write simple tests
# explore the data
# https://www.kaggle.com/pmarcelino/comprehensive-data-exploration-with-python
# analyze the graphs - hubs - clusters - outliers - PageRank
# write the report
