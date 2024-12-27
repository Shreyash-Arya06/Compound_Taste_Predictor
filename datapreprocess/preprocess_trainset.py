import pandas as pd
import os

def main():
    df_b = pd.read_csv("dataset/extracted_train_set/bitter_data_extracted.csv")
    df_s = pd.read_csv("dataset/extracted_train_set/sweet_data_extracted.csv")
    
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
        file_name = f"{group_value}_train_data.csv"
        file_path = os.path.join(directory, file_name)
        
        combined_group.to_csv(file_path, index=False)

main()