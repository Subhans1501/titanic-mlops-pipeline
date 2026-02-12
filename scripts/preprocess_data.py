
import os
import pandas as pd
import numpy as np

RAW_DATA_PATH = os.path.join("data", "raw", "titanic.csv")
PROCESSED_DATA_PATH = os.path.join("data", "processed", "titanic_processed.csv")

def preprocess_data():
    if not os.path.exists(RAW_DATA_PATH):
        print(f"Error: {RAW_DATA_PATH} not found. Run 'make download-data' first.")
        return

    print("Loading raw data...")
    df = pd.read_csv(RAW_DATA_PATH)
    print("Handling missing values...")
    df['Age'] = df['Age'].fillna(df['Age'].median())
    df['Embarked'] = df['Embarked'].fillna(df['Embarked'].mode()[0])
    df['Fare'] = df['Fare'].fillna(df['Fare'].median())
    if 'Cabin' in df.columns:
        df.drop(columns=['Cabin'], inplace=True)
    df = df.dropna(subset=['Survived'])
    print("Encoding categorical variables...")
    df['Sex'] = df['Sex'].map({'male': 0, 'female': 1})
    df = pd.get_dummies(df, columns=['Embarked'], prefix='Embarked', drop_first=True)
    
    for col in df.columns:
        if df[col].dtype == 'bool':
            df[col] = df[col].astype(int)

    os.makedirs(os.path.dirname(PROCESSED_DATA_PATH), exist_ok=True)
    
    print(f"Saving processed data to {PROCESSED_DATA_PATH}...")
    df.to_csv(PROCESSED_DATA_PATH, index=False)
    print("Preprocessing complete.")

if __name__ == "__main__":
    preprocess_data()
