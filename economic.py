import pandas as pd
import matplotlib.pyplot as plt

# Model parameters
TAX_RATE = 0.08
ALPHA = 0.4
RAW_ROWS = slice(0, 5)   # ONLY 2019–2023 block


def compute_avg_revenue_per_tourist(calibration_year=2023):
    df = pd.read_csv("t2data.csv", comment="#").iloc[RAW_ROWS].copy()

    df["Year"] = pd.to_numeric(df["Year"], errors="coerce")
    df["Tourist count (million)"] = pd.to_numeric(
        df["Tourist count (million)"], errors="coerce"
    )
    df["Tourism revenue (million $)"] = pd.to_numeric(
        df["Tourism revenue (million $)"], errors="coerce"
    )

    row = df.loc[df["Year"] == calibration_year].iloc[0]

    return row["Tourism revenue (million $)"] / row["Tourist count (million)"]


def tourism_revenue(T, r):
    return r * T


def tourism_cost(T, r, alpha=ALPHA):
    return alpha * r * T


def government_revenue(R, tax_rate=TAX_RATE):
    return tax_rate * R


def tourism_profit(T, r, alpha=ALPHA):
    return (1 - alpha) * r * T


def economic_outputs(T, r):
    R = tourism_revenue(T, r)
    C = tourism_cost(T, r)
    G = government_revenue(R)
    P = tourism_profit(T, r)
    return R, C, G, P


def plot_modeled_tourism_revenue():
    df = pd.read_csv("t2data.csv", comment="#").iloc[RAW_ROWS].copy()

    df["Year"] = pd.to_numeric(df["Year"], errors="coerce")
    df["Tourist count (million)"] = pd.to_numeric(
        df["Tourist count (million)"], errors="coerce"
    )

    # drop bad rows explicitly
    df = df.dropna(subset=["Year", "Tourist count (million)"])
    df = df.sort_values("Year")

    r = compute_avg_revenue_per_tourist()

    years = []
    revenues = []

    for _, row in df.iterrows():
        T = row["Tourist count (million)"]
        year = int(row["Year"])

        R, _, _, _ = economic_outputs(T, r)

        years.append(year)
        revenues.append(R)

    plt.figure()
    plt.bar(years, revenues)
    plt.xlabel("Year")
    plt.ylabel("Modeled Tourism Revenue (million $)")
    plt.title("Modeled Tourism Revenue vs. Year")
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    plot_modeled_tourism_revenue()

