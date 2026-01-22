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
│   ├── environment.py              # 3.3 Environmental Evolution Model
│   └── satisfaction.py             # 3.4 Resident Satisfaction Model
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

---

### `data/`

Contains raw historical datasets (2019–2023) collected from government reports,
climate monitoring agencies, and resident surveys. These data are used **only during
initialization** to estimate parameters, construct composite indices, and set initial
conditions. They are not used directly in the forward simulation.

---

### `config.py`

Centralized configuration file containing all model assumptions and parameters
(e.g., growth rates, cost coefficients, environmental recovery rates, and weighting
factors). This makes assumptions explicit and enables easy sensitivity analysis.

---

### `utils/`

Utility functions that support data preprocessing, including CSV loading,
min–max normalization, and entropy-based weight calculations. These utilities are
model-agnostic and reusable.

---

### `indices/`

Implements the construction of composite indices, most notably the environmental
index derived from normalized climate variables using the entropy weight method.
Each index outputs a scalar value used by the analytical models.

---

### `models/`

Contains the core analytical models corresponding directly to the paper sections:

* Tourist demand model
* Economic benefit model
* Environmental evolution model
* Resident satisfaction model

Each model is implemented as a deterministic function and does not directly read
from raw data files.

---

### `simulation/`

Implements the dynamic programming logic that optimizes policy decisions (e.g.,
tax rates and government spending) over a multi-year horizon by evaluating tradeoffs
between economic profit, environmental sustainability, and resident satisfaction.

---

### `results/`

Stores generated output tables and figures produced by the simulation and used
for analysis, validation, and reporting.

---

### `main.py`

The project entry point. Runs the full pipeline from data loading and index
construction to model simulation, optimization, and result generation.

---

### Design Philosophy

Historical data are used to calibrate parameters and initialize the system.
After initialization, the system evolves analytically according to model equations,
with policy decisions optimized using dynamic programming. This separation ensures
clarity, reproducibility, and alignment with the modeling methodology.


