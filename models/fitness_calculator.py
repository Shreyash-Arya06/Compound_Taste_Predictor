import pandas as pd
from weighted_edit_distance import WeightedEditDistance

def calculateFitness(bitter_smiles, sweet_smiles, tasteless_smiles, ins_weight = 1, del_weight = 1, subs_weight = 1):
    bitter_bitter = WeightedEditDistance(bitter_smiles, bitter_smiles, ins_weight, del_weight, subs_weight)
    sweet_sweet = WeightedEditDistance(sweet_smiles, sweet_smiles, ins_weight, del_weight, subs_weight)
    tasteless_tasteless = WeightedEditDistance(tasteless_smiles, tasteless_smiles, ins_weight, del_weight, subs_weight)

    cost_bb = bitter_bitter.getScore()
    print('bitter_bitter done!')
    cost_ss = sweet_sweet.getScore()
    print('sweet_sweet done!')
    cost_tt = tasteless_tasteless.getScore()
    print('tasteless_tasteless done!')

    total = (cost_bb+cost_ss+cost_tt)
    final_score = total / 3

    return final_score

def main(ins_weight = 1, del_weight = 1, subs_weight = 1):
    df_b = pd.read_csv("dataset/separated_train_set/bitter_train_data.csv")
    df_s = pd.read_csv("dataset/separated_train_set/sweet_train_data.csv")
    df_t = pd.read_csv("dataset/separated_train_set/tasteless_train_data.csv")
    bitter_smiles = df_b['Canonical SMILES'].to_list()
    sweet_smiles = df_s['Canonical SMILES'].to_list()
    tasteless_smiles = df_t['Canonical SMILES'].to_list()
    final_score = calculateFitness(bitter_smiles, sweet_smiles, tasteless_smiles, ins_weight, del_weight, subs_weight)

    return final_score
