import pandas as pd
from weighted_edit_distance import WeightedEditDistance

ins_weight = 0.00661448  
del_weight = 0.09521592
subs_weight = 0.92466402

def evaluate(test_smiles):
    df_b = pd.read_csv('dataset/separated_train_set/bitter_train_data.csv')
    df_s = pd.read_csv('dataset/separated_train_set/sweet_train_data.csv')
    df_t = pd.read_csv('dataset/separated_train_set/tasteless_train_data.csv')

    bitter_smiles = df_b['Canonical SMILES'].to_list()
    sweet_smiles = df_s['Canonical SMILES'].to_list()
    tasteless_smiles = df_t['Canonical SMILES'].to_list()

    bitter_score = WeightedEditDistance(test_smiles, bitter_smiles, ins_weight, del_weight, subs_weight, mode = 1).getScore()
    sweet__score = WeightedEditDistance(test_smiles, sweet_smiles, ins_weight, del_weight, subs_weight, mode = 1).getScore()
    tasteless_score = WeightedEditDistance(test_smiles, tasteless_smiles, ins_weight, del_weight, subs_weight, mode = 1).getScore()

    return (bitter_score, sweet__score, tasteless_score)
