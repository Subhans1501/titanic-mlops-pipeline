
import os
import urllib.request
import sys
DATA_URL="https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
OUTPUT_DIR=os.path.join("data","raw")
OUTPUT_FILE=os.path.join(OUTPUT_DIR,"titanic.csv")
def download_data():
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)
        print(f"Created directory: {OUTPUT_DIR}")
    print(f"Downloading data from {DATA_URL}...")
    try:
        urllib.request.urlretrieve(DATA_URL, OUTPUT_FILE)
        print(f"Data downloaded successfully to {OUTPUT_FILE}")
    except Exception as e:
        print(f"Error downloading data: {e}")
        sys.exit(1)
if __name__ == "__main__":
    download_data()
