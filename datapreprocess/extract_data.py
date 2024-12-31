import pandas as pd
import os

def extractColumns(source_file, source_folder, destination_file, destination_folder, required_columns):
    source_path = os.path.join("dataset", source_folder, source_file)
    df = pd.read_csv(source_path)
    extracted_df = df[required_columns]
    
    destination_path = os.path.join("dataset", destination_folder, destination_file)
    extracted_df.to_csv(destination_path, index=False)

def main():
    train_columns = ['Name', 'Taste', 'Canonical SMILES']
    test_columns = ['Name', 'Canonical SMILES', 'Label']
    extractColumns("training_data_bitter.csv", "train_set", "bitter_data_extracted.csv", "extracted_train_set", train_columns)
    extractColumns("training_data_sweet.csv", "train_set", "sweet_data_extracted.csv", "extracted_train_set", train_columns)
    extractColumns("testing_data_bitter.csv", "test_set", "bitter_data_extracted.csv", "extracted_test_set", test_columns)
    extractColumns("testing_data_sweet.csv", "test_set", "sweet_data_extracted.csv", "extracted_test_set", test_columns)

main()