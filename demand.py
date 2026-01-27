import pandas as pd
import matplotlib.pyplot as plt

TAX_RATE = 0.08


def base_growth(start_year, end_year):
    df = pd.read_csv(
        "t2data.csv",
        comment="#",
        skiprows=7,
        header=None
    )

    df.columns = [
        "Year",
        "Tourist count (million)",
        "Winter tourists",
        "Winter share"
    ]

    df["Year"] = pd.to_numeric(df["Year"], errors="coerce")
    df["Tourist count (million)"] = pd.to_numeric(
        df["Tourist count (million)"], errors="coerce"
    )
    df = df.dropna(subset=["Year", "Tourist count (million)"])

    T_start = df.loc[df["Year"] == start_year, "Tourist count (million)"].iloc[0]
    T_end   = df.loc[df["Year"] == end_year,   "Tourist count (million)"].iloc[0]

    n = end_year - start_year
    return (T_end / T_start) ** (1 / n) - 1


def simulate_tourism_demand(
    start_year,
    end_year,
    T0,
    g_base,
    gamma,
    tax_rate=TAX_RATE
):
    """
    Implements:
    T(t) = T(t-1) * (1 + g - gamma * tau)
    """

    years = [start_year]
    T_vals = [T0]

    for _ in range(start_year + 1, end_year + 1):
        T_next = T_vals[-1] * (1 + g_base - gamma * tax_rate)
        T_vals.append(T_next)
        years.append(years[-1] + 1)

    return pd.DataFrame({
        "Year": years,
        "T": T_vals
    })


def apply_seasonal_adjustment(df, S_peak=1.2, S_off=0.8):
    """
    Implements Eq. (2)
    """

    df = df.copy()
    df["T_peak"] = S_peak * df["T"]
    df["T_off"]  = S_off  * df["T"]
    return df
def plot_tourism_demand_model():
    # initial condition from data
    df_init = pd.read_csv("t2data.csv", comment="#", nrows=5)
    df_init["Year"] = df_init["Year"].astype(int)

    T_2019 = df_init.loc[df_init["Year"] == 2019,
                         "Tourist count (million)"].iloc[0]

    g_base = base_growth(2006, 2023)
    gamma = 0.1

    demand_df = simulate_tourism_demand(
        start_year=2019,
        end_year=2023,
        T0=T_2019,
        g_base=g_base,
        gamma=gamma
    )

    demand_df = apply_seasonal_adjustment(demand_df)

    plt.figure()
    plt.plot(demand_df["Year"], demand_df["T"], label="Total Tourism Demand")
    plt.plot(demand_df["Year"], demand_df["T_peak"], linestyle="--", label="Peak Season")
    plt.plot(demand_df["Year"], demand_df["T_off"], linestyle="--", label="Off-Peak Season")

    plt.xlabel("Year")
    plt.ylabel("Tourists (million)")
    plt.title("Modeled Tourism Demand (2019–2023)")
    plt.legend()
    plt.tight_layout()
    plt.show()
if __name__ == "__main__":
    plot_tourism_demand_model()

