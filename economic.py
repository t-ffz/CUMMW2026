# economic_model.py
import pandas as pd
import matplotlib.pyplot as plt
from demand import base_growth, simulate_tourism_demand

# model parameters
TAX_RATE = 0.08
ALPHA = 0.4        # variable cost fraction of revenue
CFIXED = 50        # fixed costs in million $
R_INITIAL = 100     # average revenue per tourist ($ million / million tourists)
GAMMA = 0.1         # sensitivity to tax rate


# economic Functions
def tourism_revenue(T, r=R_INITIAL):
    return r * T

def government_revenue(R, tau=TAX_RATE):
    return tau * R

def tourism_cost(T, c_fixed=CFIXED, alpha=ALPHA, r=R_INITIAL):
    return c_fixed + alpha * r * T

def tourism_profit(R, C):
    return R - C


# simulation Using Demand Model
def simulate_economics_2019_2026():
    # 1. Get base growth from demand.py
    g_base = base_growth(2006, 2023)

    # 2. Get initial tourists (2019)
    df_init = pd.read_csv("t2data.csv", comment="#", nrows=5)
    T0 = df_init.loc[df_init["Year"] == 2019, "Tourist count (million)"].iloc[0]

    # 3. Simulate tourism demand (2019–2026)
    demand_df = simulate_tourism_demand(
        start_year=2019,
        end_year=2026,
        T0=T0,
        g_base=g_base,
        gamma=GAMMA,
        tax_rate=TAX_RATE
    )

    # 4. Compute economic outputs
    R_vals, G_vals, C_vals, P_vals = [], [], [], []
    for T in demand_df["T"]:
        R = tourism_revenue(T)
        G = government_revenue(R)
        C = tourism_cost(T)
        P = tourism_profit(R, C)

        R_vals.append(R)
        G_vals.append(G)
        C_vals.append(C)
        P_vals.append(P)

    demand_df["Tourism Revenue"] = R_vals
    demand_df["Government Revenue"] = G_vals
    demand_df["Tourism Cost"] = C_vals
    demand_df["Tourism Profit"] = P_vals

    return demand_df


# Plotting Function
def plot_economics(df):
    plt.figure(figsize=(10, 6))
    plt.plot(df["Year"], df["Tourism Revenue"], marker="o", label="Tourism Revenue")
    plt.plot(df["Year"], df["Government Revenue"], marker="o", label="Government Revenue")
    plt.plot(df["Year"], df["Tourism Cost"], marker="o", label="Tourism Cost")
    plt.plot(df["Year"], df["Tourism Profit"], marker="o", label="Tourism Profit")
    plt.xlabel("Year")
    plt.ylabel("Million $")
    plt.title("Projected Tourism Economics (2019–2026)")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()


# main
if __name__ == "__main__":
    df_econ = simulate_economics_2019_2026()
    print(df_econ)
    plot_economics(df_econ)

