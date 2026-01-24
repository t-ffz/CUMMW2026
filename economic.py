import pandas as pd

# Model parameters
TAX_RATE = 0.08     # τ
ALPHA = 0.4         # α ∈ (0,1)
RAW_ROWS = slice(0, 5)   # Raw (non-normalized) table only


def compute_avg_revenue_per_tourist(calibration_year=2023):
    """
    Computes average revenue per tourist:
    r = (Tourism revenue) / (Tourist count)

    Uses raw Juneau data only.
    """

    df = pd.read_csv("t2data.csv", comment="#")
    df = df.iloc[RAW_ROWS].copy()

    df["Year"] = pd.to_numeric(df["Year"], errors="coerce")
    df["Tourist count (million)"] = pd.to_numeric(
        df["Tourist count (million)"], errors="coerce"
    )
    df["Tourism revenue (million $)"] = pd.to_numeric(
        df["Tourism revenue (million $)"], errors="coerce"
    )

    row = df.loc[df["Year"] == calibration_year].iloc[0]

    r = row["Tourism revenue (million $)"] / row["Tourist count (million)"]
    return r

def tourism_revenue(T, r):
    """
    R(t) = r * T(t)
    """
    return r * T


def tourism_cost(T, r, alpha=ALPHA):
    """
    C(t) = c_var * T(t)
    c_var = α * r
    """
    return alpha * r * T


def government_revenue(R, tax_rate=TAX_RATE):
    """
    G(t) = τ * R(t)
    """
    return tax_rate * R


def tourism_profit(T, r, alpha=ALPHA):
    """
    P(t) = R(t) - C(t)
    Simplified: (1 - α) * r * T
    """
    return (1 - alpha) * r * T

def economic_outputs(T, r=None):
    """
    Returns R(t), C(t), G(t), P(t)
    """

    if r is None:
        r = compute_avg_revenue_per_tourist()

    R = tourism_revenue(T, r)
    C = tourism_cost(T, r)
    G = government_revenue(R)
    P = tourism_profit(T, r)

    return R, C, G, P

# debugging 
def main():
    # 2023 data as checking
    df = pd.read_csv("t2data.csv", comment="#").iloc[RAW_ROWS]
    T_2023 = pd.to_numeric(
    df.loc[df["Year"] == 2023, "Tourist count (million)"].iloc[0],
    errors="coerce")

    r = compute_avg_revenue_per_tourist()
    R, C, G, P = economic_outputs(T_2023, r)

    print(f"r = {r:.2f}")
    print(f"T = {T_2023:.3f} million")
    print(f"R = ${R:.2f} million")
    print(f"C = ${C:.2f} million")
    print(f"G = ${G:.2f} million")
    print(f"P = ${P:.2f} million")


if __name__ == "__main__":
    main()

