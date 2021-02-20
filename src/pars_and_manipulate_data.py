import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from src.riski_const import FeaturesNames, SELECTED_FEATURES


class ParsAndManipulate:
    def __init__(self, file_path: str):
        self.__file_path = file_path

    def run(self):
        self.__import_data()
        # self.__initial_data_exploration()

    def get_df(self) -> pd.DataFrame:
        return self.__df

    def __import_data(self) -> None:
        self.__df = pd.read_csv(self.__file_path)
        self.__df.info()
        # self.__df = self.__df[0:4] # for testing
        self.__modify_input_data()

    def __initial_data_exploration(self):

        # check feature distribution is not normal/unified
        self.__df[SELECTED_FEATURES].hist(bins=100)
        self.__df[[FeaturesNames.SHIPPING_ZIP]].hist(bins=100)
        g = sns.jointplot(x=FeaturesNames.ORDER_STATUS_INT, y=FeaturesNames.SHIPPING_ZIP, kind="reg", data=self.__df)
        g.fig.suptitle('Correlation between ' + FeaturesNames.ORDER_STATUS_INT + ' & ' + FeaturesNames.SHIPPING_ZIP)

        pd.plotting.scatter_matrix(self.__df[SELECTED_FEATURES])
        plt.show()

        self.__print_pair_plots()

    def __print_pair_plots(self):
        sns.set()
        sns.pairplot(self.__df[SELECTED_FEATURES], size=2.5)
        plt.show()

    def __modify_input_data(self):
        self.__df = self.__df.drop(['Unnamed: 0'], axis=1)

        self.__df[FeaturesNames.ORDER_STATUS_INT], mapping = self.__ctgr2int(FeaturesNames.ORDER_STATUS_STR)
        self.__df[FeaturesNames.NORM_NAME_INT], mapping = self.__ctgr2int(FeaturesNames.NORM_NAME_STR)
        self.__df[FeaturesNames.BROWSER_IP_INT], mapping = self.__ctgr2int(FeaturesNames.BROWSER_IP_STR)
        self.__df[FeaturesNames.EMAIL_INT], mapping = self.__ctgr2int(FeaturesNames.EMAIL_STR)
        self.__df[FeaturesNames.ORDER_CAPTURED_AT_STR] = self.__df[FeaturesNames.ORDER_CAPTURED_AT_STR].str.strip()
        self.__df[FeaturesNames.ORDER_CAPTURED_AT_INT], mapping = self.__ctgr2int(FeaturesNames.ORDER_CAPTURED_AT_STR)
        self.__df[FeaturesNames.SHIPPING_ADDRESS1_INT], mapping = self.__ctgr2int(FeaturesNames.SHIPPING_ADDRESS1_STR)

        self.__combine_relevant_features()

    def __ctgr2int(self, tmp_title):
        s = self.__df[tmp_title]
        res = pd.factorize(s)
        return res[0], res[1]

    def __combine_relevant_features(self):

        tmp_df = self.__df[SELECTED_FEATURES]

        self.__df[FeaturesNames.COMBINED] = tmp_df.values.tolist()
