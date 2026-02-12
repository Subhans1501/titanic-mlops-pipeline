
import os
import pandas as pd
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
PREDICTIONS_PATH = os.path.join("results", "predictions.csv")
Y_TEST_PATH = os.path.join("data", "processed", "y_test.csv")
METRICS_PATH = os.path.join("results", "metrics.txt")
def evaluate():
    if not os.path.exists(PREDICTIONS_PATH):
        print(f"Error: {PREDICTIONS_PATH} not found. Run 'make predict' first.")
        return
    if not os.path.exists(Y_TEST_PATH):
        print(f"Error: {Y_TEST_PATH} not found. Run 'make train' first.")
        return

    print("Loading predictions and ground truth...")
    y_pred = pd.read_csv(PREDICTIONS_PATH)['Survived']
    y_true = pd.read_csv(Y_TEST_PATH)['Survived']

    # Calculate Metrics
    print("Calculating metrics...")
    accuracy = accuracy_score(y_true, y_pred)
    precision = precision_score(y_true, y_pred)
    recall = recall_score(y_true, y_pred)
    f1 = f1_score(y_true, y_pred)

    metrics_text = (
        f"Accuracy: {accuracy:.4f}\n"
        f"Precision: {precision:.4f}\n"
        f"Recall: {recall:.4f}\n"
        f"F1 Score: {f1:.4f}\n"
    )

    print("----------------Metrics----------------")
    print(metrics_text)
    print("---------------------------------------")

    # Save Metrics
    os.makedirs(os.path.dirname(METRICS_PATH), exist_ok=True)
    with open(METRICS_PATH, 'w') as f:
        f.write(metrics_text)
    print(f"Metrics saved to {METRICS_PATH}")
if __name__ == "__main__":
    evaluate()
