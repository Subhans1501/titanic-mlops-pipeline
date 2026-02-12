
import os
import pandas as pd
import numpy as np

INPUT_PATH = os.path.join("data", "processed", "titanic_processed.csv")
OUTPUT_PATH = os.path.join("features", "titanic_features.csv")

def feature_engineering():
    if not os.path.exists(INPUT_PATH):
        print(f"Error: {INPUT_PATH} not found. Run 'make preprocess' first.")
        return

    print("Loading processed data...")
    df = pd.read_csv(INPUT_PATH)
    print("Creating FamilySize feature...")
    df['FamilySize'] = df['SibSp'] + df['Parch'] + 1
    print("Extracting Title from Name...")
    df['Title'] = df['Name'].apply(lambda x: x.split(',')[1].split('.')[0].strip())
    common_titles = ['Mr', 'Miss', 'Mrs', 'Master']
    df['Title'] = df['Title'].apply(lambda x: x if x in common_titles else 'Rare')
    df = pd.get_dummies(df, columns=['Title'], prefix='Title')
    cols_to_drop = ['Name', 'Ticket', 'PassengerId'] 
    df.drop(columns=[c for c in cols_to_drop if c in df.columns], inplace=True)
    object_cols = df.select_dtypes(include=['object']).columns
    if len(object_cols) > 0:
        print(f"Warning: Dropping remaining non-numeric columns: {list(object_cols)}")
        df.drop(columns=object_cols, inplace=True)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    print(f"Saving features to {OUTPUT_PATH}...")
    df.to_csv(OUTPUT_PATH, index=False)
    print("Feature engineering complete.")
if __name__ == "__main__":
    feature_engineering()
