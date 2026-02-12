
import os
import pandas as pd
import pickle

MODEL_PATH = os.path.join("models", "model.pkl")
X_TEST_PATH = os.path.join("data", "processed", "X_test.csv")
PREDICTIONS_PATH = os.path.join("results", "predictions.csv")
def predict():
    if not os.path.exists(MODEL_PATH):
        print(f"Error: {MODEL_PATH} not found. Run 'make train' first.")
        return
    if not os.path.exists(X_TEST_PATH):
        print(f"Error: {X_TEST_PATH} not found. Run 'make train' first.")
        return

    print("Loading model and test data...")
    with open(MODEL_PATH, 'rb') as f:
        model = pickle.load(f)
    
    X_test = pd.read_csv(X_TEST_PATH)

    print("Generating predictions...")
    predictions = model.predict(X_test)

    os.makedirs(os.path.dirname(PREDICTIONS_PATH), exist_ok=True)
    pd.DataFrame(predictions, columns=['Survived']).to_csv(PREDICTIONS_PATH, index=False)
    print(f"Predictions saved to {PREDICTIONS_PATH}")

if __name__ == "__main__":
    predict()
