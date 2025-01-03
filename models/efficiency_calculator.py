import pandas as pd
from evaluate import evaluate

def main():
    df_btest = pd.read_csv('dataset/extracted_test_set/bitter_data_extracted.csv')
    df_stest = pd.read_csv('dataset/extracted_test_set/sweet_data_extracted.csv')
    
    total_bitter = 171
    total_sweet = 161
    correct_bitter_guess = 0
    correct_sweet_guess = 0

    for row in df_btest.itertuples(index=True, name='Row'):
        bitter_score, sweet_score, tasteless_score = evaluate(row[2])
        predicted_label = 0
        if (bitter_score >= sweet_score and bitter_score >= tasteless_score):
            predicted_label = 1
        
        if (predicted_label == row[3]):
            correct_bitter_guess += 1

    for row in df_stest.itertuples(index=True, name='Row'):
        bitter_score, sweet_score, tasteless_score = evaluate(row[2])
        predicted_label = 0
        if (sweet_score >= bitter_score and sweet_score >= tasteless_score):
            predicted_label = 1
        
        if (predicted_label == row[3]):
            correct_sweet_guess += 1
        
    print(f'Efficiency in bitter guess\t->\t{round((correct_bitter_guess/total_bitter)*100, 4)}%')
    print(f'Efficiency in sweet guess\t->\t{round((correct_sweet_guess/total_sweet)*100, 4)}%')
    print(f'Total efficiency\t->\t{round(((correct_bitter_guess+correct_sweet_guess)/(total_bitter+total_sweet))*100, 4)}%')

main()