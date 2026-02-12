
PYTHON = python
PIP = pip

.PHONY: all setup download-data preprocess features train predict evaluate clean

all: evaluate

setup:
	$(PIP) install -r requirements.txt

download-data:
	$(PYTHON) scripts/download_data.py

preprocess: download-data
	$(PYTHON) scripts/preprocess_data.py

features: preprocess
	$(PYTHON) scripts/feature_engineering.py

train: features
	$(PYTHON) scripts/train_model.py

predict: train
	$(PYTHON) scripts/predict.py

evaluate: predict
	$(PYTHON) scripts/evaluate.py

clean:
	$(PYTHON) scripts/clean.py
