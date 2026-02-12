
import os
import pandas as pd
import pickle
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

INPUT_PATH = os.path.join("features", "titanic_features.csv")
MODEL_PATH = os.path.join("models", "model.pkl")
X_TEST_PATH = os.path.join("data", "processed", "X_test.csv")
Y_TEST_PATH = os.path.join("data", "processed", "y_test.csv")

def train_model():
    if not os.path.exists(INPUT_PATH):
        print(f"Error: {INPUT_PATH} not found. Run 'make features' first.")
        return

    print("Loading features...")
    df = pd.read_csv(INPUT_PATH)

    X = df.drop(columns=['Survived'])
    y = df['Survived']

    print("Splitting data into train and test sets...")
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    print("Training Random Forest Classifier...")
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)
    os.makedirs(os.path.dirname(MODEL_PATH), exist_ok=True)
    print(f"Saving model to {MODEL_PATH}...")
    with open(MODEL_PATH, 'wb') as f:
        pickle.dump(model, f)

    print(f"Saving test data to {X_TEST_PATH} and {Y_TEST_PATH}...")
    X_test.to_csv(X_TEST_PATH, index=False)
    y_test.to_csv(Y_TEST_PATH, index=False)
    
    print("Model training complete.")

if __name__ == "__main__":
    train_model()
