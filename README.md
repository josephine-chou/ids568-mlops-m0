# IDS 568 Milestone 0: Environment & CI Setup

![CI](https://github.com/josephine-chou/ids568-mlops-m0/actions/workflows/ci.yml/badge.svg)

## Setup
```bash
git clone https://github.com/josephine-chou/ids568-mlops-m0.git
cd ids568-mlops-m0
python3.12 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
pytest tests/ -v
```

## Reproducibility Documentation

Environment reproducibility is fundamental to reliable ML lifecycle operations. This project implements three key principles: first, dependency pinning uses exact version specifications (numpy==1.26.4) to prevent version drift that causes inconsistent model behavior across environments; second, virtual environment isolation ensures each project maintains independent package installations, avoiding conflicts; third, continuous integration through GitHub Actions validates that environments can be recreated in clean states, catching hidden dependencies before deployment. These practices directly support deployment success by ensuring data preprocessing, model training, and inference all use identical package versions. In production systems, environment inconsistencies frequently cause deployment failures where models trained with one library version produce different predictions or fail entirely when deployed with another version. Establishing reproducibility from the start prevents these costly issues.

## Structure
```
├── .github/workflows/ci.yml
├── src/__init__.py
├── tests/test_smoke.py
└── requirements.txt
```