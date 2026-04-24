import pandas as pd

def load_data(path):
    df = pd.read_csv(path)
    df['timestamp'] = pd.to_datetime(df['timestamp'])
    return df

def validate_data(df):
    required = [
        'patient_id', 'timestamp',
        'heart_rate', 'spo2',
        'temperature', 'respiratory_rate'
    ]

    for col in required:
        assert col in df.columns, f"Missing column: {col}"

    return df
