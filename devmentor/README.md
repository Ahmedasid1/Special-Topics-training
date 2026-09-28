# Special Topics Training

A Python environment for hands-on training in modern data science and large language model workflows. The included dependencies support exploratory notebooks, Hugging Face models and datasets, embeddings, fine-tuning, retrieval-augmented generation (RAG), and Modal-based cloud execution.

## Topics

- Data science with NumPy, pandas, matplotlib, and scikit-learn
- Interactive notebook development with Jupyter and IPython kernels
- Model and dataset workflows with PyTorch and Hugging Face
- Sentence embeddings with Sentence Transformers
- Parameter-efficient fine-tuning with PEFT and TRL
- RAG applications with LangChain, ChromaDB, and PDF ingestion
- Cloud execution with Modal

## Setup

Prerequisites: Python 3.10 or later and `pip`.

```powershell
git clone https://github.com/Ahmedasid1/Special-Topics-training.git
Set-Location "Special-Topics-training"
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

On macOS or Linux, activate the virtual environment with:

```bash
source .venv/bin/activate
```

## Use Jupyter

After activating the environment, launch Jupyter Lab:

```powershell
jupyter lab
```

When creating a notebook, select the Python kernel associated with this project's `.venv` environment.

## Dependencies

The full dependency list is maintained in [requirements.txt](requirements.txt). Install or update the environment whenever that file changes:

```powershell
python -m pip install -r requirements.txt
```

## Optional Services

Some workflows require their own authentication before use:

- Hugging Face: authenticate with `huggingface-cli login` when accessing gated models or publishing assets.
- Modal: authenticate with `modal setup` before running cloud functions.
