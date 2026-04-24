def detect_signals(row):
    signals = []
    trace = []

    if row['heart_rate'] > 100:
        signals.append("tachycardia")
        trace.append(f"HR={row['heart_rate']} > 100")

    if row['respiratory_rate'] > 20:
        signals.append("tachypnea")
        trace.append(f"RR={row['respiratory_rate']} > 20")

    if row['spo2'] < 92:
        signals.append("hypoxia")
        trace.append(f"SpO2={row['spo2']} < 92")

    if row['temperature'] > 38:
        signals.append("fever")
        trace.append(f"Temp={row['temperature']} > 38")

    return signals, trace


def compute_risk(signals):
    if len(signals) == 0:
        return "LOW"
    elif len(signals) <= 2:
        return "MEDIUM"
    else:
        return "HIGH"


def ai_layer(signals, risk):
    if not signals:
        return "Patient vitals are stable."

    explanation = f"Patient shows {', '.join(signals)}."

    if risk == "MEDIUM":
        explanation += " Mild physiological stress detected."
    elif risk == "HIGH":
        explanation += " Critical condition detected."

    return explanation
