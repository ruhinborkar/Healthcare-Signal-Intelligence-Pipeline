# Healthcare-Signal-Intelligence-Pipeline
This project implements a deterministic clinical signal intelligence system for monitoring patient vitals. It analyzes physiological data such as heart rate, oxygen saturation, temperature, and respiratory rate to detect abnormalities, classify risk levels, and generate structured, explainable outputs. The system is modular, traceable, and produces standardized JSON outputs suitable for real-world healthcare pipelines.

# Features
- Deterministic rule-based decision system  
- Multi-signal anomaly detection (tachycardia, hypoxia, etc.)  
- Risk classification (LOW / MEDIUM / HIGH)  
- Explainable AI layer (human-readable output)  
- Structured JSON output (API-ready)  
- Traceability with trace_id and rule logs  
- Visualization dashboard for insights
  
# System Architecture
ingestion.py      → data loading & validation  
engine.py         → signal detection + risk engine  
output.py         → JSON output + traceability  
visualization.py  → dashboard generation  
main.py           → pipeline execution  

# How to Run
python main.py
pip install pandas matplotlib

# Dataset
Due to size limitations, a sample dataset is included:
- `patient_vitals_sample.csv`
The system works on full-scale datasets in the same format.

# Sample Output
   json
{
  "patient_id": "P0001",
  "timestamp": "2025-01-02 14:00:00",
  "signals": [],
  "risk": "LOW",
  "trace": [],
  "ai_explanation": "Patient vitals are stable.",
  "trace_id": "0",
  "source": "patient_vitals.csv"
}

# Visualization
The system generates a dashboard (`dashboard.png`) showing:
- Risk distribution  
- Signal frequency  
- Vital trends  

# Deterministic Guarantee
This system is fully deterministic:
- Same input → same output  
- No randomness  
- Rule-based logic ensures reproducibility

# Traceability
Each output includes:
- `trace_id` → unique identifier  
- `trace` → rule-level explanation  
- `source` → data origin  
This enables debugging, auditing, and replay.

# Dataset
Due to GitHub file size limitations, a sample dataset is provided.  
The system works identically on the full dataset with the same structure.

## 🎯 Conclusion
This project demonstrates a structured, explainable, and deterministic pipeline for patient monitoring, aligned with real-world system design principles and integration requirements.
