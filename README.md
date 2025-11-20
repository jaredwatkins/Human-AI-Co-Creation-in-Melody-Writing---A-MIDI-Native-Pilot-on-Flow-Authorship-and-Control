# AI-Human-Co-Creation-Project-Planned-Pilot

# Human–AI Co-Creation in Melody Writing
Pilot for my Human-AI Co-Creation Project

This project explores **human–AI melodic collaboration** using symbolic sequence models such as the Music Transformer and RNN-based anticipation networks.  
It includes experiments for real-time melody co-writing and analysis of creative agency between human and machine.

## Features
- Symbolic melody generation and continuation using Transformer and RNN models  
- Real-time co-creation pipeline (`run_anticipation.py`)  
- Model comparison and evaluation tools  
- Ready for ISMIR reproducibility (Python 3.8+)

### Model
- [`stanford-crfm/music-small-800k`](https://huggingface.co/stanford-crfm/music-small-800k)
- Autoregressive transformer trained on 800k MIDI sequences
- Hosted via HuggingFace Transformers

### Data and artifacts
- Project materials and study artifacts: https://doi.org/10.17605/OSF.IO/P3HQG

## Quick Start

1. **Clone the repository**
   ```bash
   git clone https://github.com/your-username/your-repo-name.git
   cd your-repo-name

2. **Create and activate a Python 3.8 environment**
   python3.8 -m venv venv
source venv/bin/activate   # macOS/Linux
venv\Scripts\activate      # Windows
  
3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
  
4. **Run generation:**

   python run_anticipation.py --input my_melody.mid --output output.mid

**Folder overview**
    anticipation/         # Core model files
    utils/                # Helper functions
    generate.py           # Model inference script
    run_anticipation.py   # Main experiment runner
    requirements.txt      # Dependencies
    README.md             # Project documentation
    LICENSE               # License information


