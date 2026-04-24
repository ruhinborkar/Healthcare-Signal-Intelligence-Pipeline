import json

def build_output(row, source="patient_vitals.csv"):
    return {
        "patient_id": row['patient_id'],
        "timestamp": str(row['timestamp']),
        "signals": row['signals'],
        "risk": row['risk'],
        "trace": row['trace'],
        "ai_explanation": row['ai_explanation'],
        "trace_id": str(row.name),
        "source": source
    }

def to_json(record):
    return json.dumps(record)

def log(record):
    print(
        f"[INFO] ID={record['trace_id']} | "
        f"Patient={record['patient_id']} | "
        f"Risk={record['risk']} | "
        f"Signals={record['signals']}"
    )
