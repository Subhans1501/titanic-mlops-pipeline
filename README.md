# MLOps Pipeline Automation: Automated Machine Learning Workflow with Makefile

## Project Overview
This project implements a fully automated MLOps pipeline designed for **reproducibility**. By utilizing a central `Makefile`, the entire workflow—from environment setup and data ingestion to model training and evaluation—is managed through a single command-point, ensuring a consistent dependency chain.

## Project Structure

```

├── scripts/          # Python scripts for each pipeline stage
│   ├── download_data.py   # Data ingestion
│   ├── preprocess.py      # Data cleaning and preparation
│   ├── train.py           # Model training logic
│   └── evaluate.py        # Performance metrics generation
├── data/             # Raw and processed datasets (git-ignored)
├── models/           # Saved model artifacts (.pkl)
├── Makefile          # Main automation script
└── README.md         # Project documentation

````

## Getting Started

### Prerequisites
- Python 3.x
- `make` utility (standard on Linux/macOS)

### Installation & Setup
To set up the virtual environment and install dependencies:

```bash
make setup
````

## Pipeline Execution

The pipeline follows a strict dependency chain. You can run individual stages or the entire workflow at once.

| Target               | Description                                          |
| -------------------- | ---------------------------------------------------- |
| `make download-data` | Fetches the raw dataset from the source.             |
| `make preprocess`    | Cleans data and handles missing values.              |
| `make features`      | Performs feature engineering and scaling.            |
| `make train`         | Trains the model and saves the weights to `models/`. |
| `make evaluate`      | Generates final metrics and evaluation logs.         |
| `make all`           | Runs the entire pipeline from start to finish.       |

### Cleanup

To remove generated artifacts, logs, and temporary files:

```bash
make clean
```

## Performance Metrics

After running `make evaluate`, the system generates a summary of the model's performance. Metrics include:

* Accuracy / F1-Score
* Inference Latency
* Confusion Matrix

## Author

**Subhan Shahid**
BSAI Student @ FAST-NUCES
Aspiring AI & Full-Stack Engineer
