import matplotlib.pyplot as plt

def plot_dashboard(df):
    plt.figure(figsize=(12, 8))

    # Risk distribution
    plt.subplot(2,2,1)
    df['risk'].value_counts().plot(kind='bar')
    plt.title("Risk Distribution")

    # Top signals
    plt.subplot(2,2,2)
    df['signals'].explode().value_counts().head(5).plot(kind='bar')
    plt.title("Top Signals")

    # Heart rate trend
    plt.subplot(2,2,3)
    df['heart_rate'].rolling(50).mean().plot()
    plt.title("Heart Rate Trend")

    plt.tight_layout()
    plt.savefig("dashboard.png")
    plt.show()
