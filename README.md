# CUMMW2026
```text
sustainable-tourism-model/
│
├── README.md                       # Project overview & methodology
│
├── data/
│   ├── tourism.csv                 # Tourist count & revenue (2019–2023)
│   ├── environment.csv             # Climate data (temp, snowfall, ocean)
│   ├── social.csv                  # Resident survey / sentiment data
│
├── config.py                       # All parameters & assumptions
│
├── utils/
│   ├── __init__.py
│   ├── data_loader.py              # Load CSVs into DataFrames
│   ├── normalization.py            # Min–max scaling
│   ├── entropy_weights.py          # Entropy weight method (env index)
│
├── indices/
│   ├── __init__.py
│   └── environment_index.py        # Builds composite environmental index
│
├── models/
│   ├── __init__.py
│   ├── demand.py                   # 3.1 Tourist Demand Model
│   ├── economic.py                 # 3.2 Economic Benefit Model
│   └── environment.py              # 3.3 Environmental Evolution Model
│
├── simulation/
│   ├── __init__.py
│   └── dp_solver.py                # Dynamic programming optimization
│
├── results/
│   ├── tables/                     # Output CSVs (projections)
│   └── figures/                    # Generated plots
│
├── main.py                         # End-to-end pipeline runner
└── requirements.txt
```

## Repository Structure & Workflow Explanation

This repository implements a sustainable tourism management model that integrates
economic, environmental, and social components and optimizes policy decisions using
dynamic programming.

The project is organized to reflect the modeling pipeline used in the paper:

**historical data → parameter calibration → analytical models → optimization → results**

### Design Philosophy

Historical data are used to calibrate parameters and initialize the system.
After initialization, the system evolves analytically according to model equations,
with policy decisions optimized using dynamic programming. This separation ensures
clarity, reproducibility, and alignment with the modeling methodology.


