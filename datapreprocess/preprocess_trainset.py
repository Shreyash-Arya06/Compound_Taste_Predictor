import pandas as pd
import os

def main():
    df_b_train = pd.read_csv("dataset/extracted_train_set/bitter_data_extracted.csv")
    df_s_train = pd.read_csv("dataset/extracted_train_set/sweet_data_extracted.csv")
    df_b_test = pd.read_csv("dataset/extracted_test_set/bitter_data_extracted.csv")
    df_s_test = pd.read_csv("dataset/extracted_test_set/sweet_data_extracted.csv")

    col = 'Canonical SMILES'
    df_b1 = df_b_train[~df_b_train[col].isin(df_b_test[col])]
    df_b = df_b1[~df_b1[col].isin(df_s_test[col])]
    df_s1 = df_s_train[~df_s_train[col].isin(df_b_test[col])]
    df_s = df_s1[~df_s1[col].isin(df_s_test[col])]
    
    group_column = "Taste"

    group_b = df_b.groupby(group_column)
    group_s = df_s.groupby(group_column)

    all_groups = set(df_b[group_column].unique()).union(df_s[group_column].unique())

    for group_value in all_groups:
        group_b_df = group_b.get_group(group_value) if group_value in group_b.groups else pd.DataFrame()
        group_s_df = group_s.get_group(group_value) if group_value in group_s.groups else pd.DataFrame()

        combined_group = pd.concat([group_b_df, group_s_df], ignore_index=True)
        combined_group.drop_duplicates(inplace=True)

        directory = "dataset/separated_train_set"
        file_name = f"{group_value.lower()}_train_data.csv"
        file_path = os.path.join(directory, file_name)
        
        combined_group.to_csv(file_path, index=False)

main()