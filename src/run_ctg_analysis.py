import numpy as np

from src.pars_and_manipulate_data import ParsAndManipulate
from src.gen_costumer_transaction_graph import GenCTG
from src.explore_ctg import ExploreCTG

if __name__ == "__main__":

    file_nm = r'C:\Desktop\FindingTransactionsHubs\data\customer_trust_interview_dataset.csv'

    parser = ParsAndManipulate(file_path=file_nm)
    parser.run()

    ctg_gen = GenCTG(df=parser.get_df())
    ctg_gen.run()

    out = r'C:\Desktop\FindingTransactionsHubs\out'
    np.savetxt(out+'\score_mat.csv', ctg_gen.get_ctg_base_mat())
    my_data = np.genfromtxt(out+'\score_mat.csv', delimiter=',')

    explorer = ExploreCTG(df=parser.get_df(), ctg=ctg_gen.get_ctg(), out_dir=out)
    explorer.run()
