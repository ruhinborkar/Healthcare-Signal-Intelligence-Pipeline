from ingestion import load_data, validate_data
from engine import detect_signals, compute_risk, ai_layer
from output import build_output, to_json, log
from visualization import plot_dashboard

def run_pipeline():

    df = load_data("patient_vitals.csv")
    df = validate_data(df)

    # SIGNAL DETECTION
    df['signals'], df['trace'] = zip(*df.apply(detect_signals, axis=1))

    # RISK ENGINE
    df['risk'] = df['signals'].apply(compute_risk)

    # AI LAYER
    df['ai_explanation'] = df.apply(
        lambda r: ai_layer(r['signals'], r['risk']), axis=1
    )

    # OUTPUT + LOGGING
    outputs = []
    for _, row in df.iterrows():
        record = build_output(row)
        outputs.append(record)
        log(record)

    # VISUALIZATION
    plot_dashboard(df)

    return outputs


if __name__ == "__main__":
    results = run_pipeline()

    print("\nSample JSON Output:\n")
    print(to_json(results[0]))
