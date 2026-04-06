def preprocess_data(df):
    df = df.copy()

    # Normalize values (simple scaling)
    df["clicks"] = df["clicks"] / 100
    df["time_spent"] = df["time_spent"] / 300
    df["activity"] = df["activity"] / 50

    return df