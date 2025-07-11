import matplotlib.pyplot as plt

def plot_regimes(data, states):
    plt.figure(figsize=(15, 5))
    for i in range(max(states) + 1):
        plt.plot(data[states == i], '.', label=f"Regime {i}")
    plt.legend()
    plt.title("Regime Detection")
    plt.xlabel("Time")
    plt.ylabel("Returns")
    plt.show()