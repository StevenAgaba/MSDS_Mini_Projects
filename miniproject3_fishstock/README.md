# Lake Victoria Fish Stock & Export Risk Model

## Agaba Steven. 
### Registration Number: S26M19/002. 
### Access Number: B38624

## Project Description

This project develops a fish-stock sustainability and export-risk assessment model for a fish-export cooperative in Jinja, Uganda. The project replaces an unrealistic Fibonacci growth approach with a logistic population growth model that incorporates harvesting. Revenue uncertainty is evaluated using a stochastic fish-price model, Monte Carlo simulation, coefficient of variation (CV), and Value-at-Risk (VaR).

The model helps assess whether harvesting practices are sustainable and quantifies the financial risks associated with fish export revenues.

---

## Objectives

The project aims to:

- Demonstrate why unbounded Fibonacci growth is biologically unrealistic.
- Model fish-stock dynamics using logistic population growth.
- Incorporate harvesting into the stock model.
- Simulate fish prices using a random walk process.
- Compute weekly and annual export revenues.
- Measure revenue risk using statistical methods.
- Classify risk using the coefficient of variation (CV).
- Estimate downside risk using Monte Carlo simulation and Value-at-Risk (VaR).
- Compare different harvesting scenarios.
- Evaluate sustainability against Maximum Sustainable Yield (MSY).
- Analyze the impact of a closed harvesting season.

---

## Project Structure

```text
mini_project3_fishstock/
│
├── src/
│   ├── __init__.py
│   ├── fishstock.py
│   └── riskmodel.py
│
├── tests/
│   └── test_fishstock.py
│
├── project3_fishstock.ipynb
│
├── README.md
├── requirements.txt
└── environment.yml
```

---

## Installation

Install the required packages:

```bash
pip install -r requirements.txt
```

---

## Running the Project

Start Jupyter Notebook:

```bash
jupyter notebook
```

Open:

```text
project3_fishstock.ipynb
```

Execute:

```text
Kernel → Restart & Run All
```

The notebook is designed to run from top to bottom without errors.

---

## Testing

Run unit tests using:

```bash
pytest
```

The test suite verifies:

- Positive fish-stock levels
- Correct simulation lengths
- Correct harvest-output lengths

---

## Logistic Growth Model

Fish stock evolves according to:

```text
N(t+1) = N(t)
       + rN(t)(1 - N(t)/K)
       - hN(t)
```

where:

- N(t) = fish stock at time t
- r = intrinsic growth rate
- K = carrying capacity
- h = harvest rate

Project parameters:

```text
r = 0.4
K = 10,000 tonnes
N(0) = 4,000 tonnes
```

---

## Price Simulation

Weekly fish prices are simulated using a bounded random-walk model:

```text
Initial price = UGX 12,000/kg
Minimum price = UGX 9,000/kg
Maximum price = UGX 16,000/kg
```

A fixed random seed is used to ensure reproducibility.

---

## Revenue Model

Weekly revenue is calculated as:

```text
Revenue = Harvest (kg) × Price
```

Annual revenue is obtained by summing all weekly revenues.

---

## Risk Assessment

The project evaluates risk using:

### Coefficient of Variation (CV)

```text
CV = Standard Deviation / Mean
```

Risk categories:

```text
CV < 0.15          → Low Risk
0.15 ≤ CV < 0.30  → Moderate Risk
CV ≥ 0.30          → High Risk
```

### Value-at-Risk (VaR)

A Monte Carlo simulation with at least 1,000 price paths is performed to estimate:

```text
5% Value-at-Risk (VaR)
```

This metric measures potential downside revenue risk.

---

## Scenario Analysis

The following harvest rates are evaluated:

```text
h = 0.05
h = 0.10
h = 0.20
h = 0.30
```

For each scenario, the project reports:

- Final fish stock
- Total annual revenue
- Coefficient of variation
- Risk classification

Results are compared against the theoretical Maximum Sustainable Yield (MSY):

```text
MSY = rK / 4
```

---

## Visualizations

The notebook produces:

1. Fish-stock trajectories for all harvest rates.
2. Histogram of simulated annual revenues.
3. Value-at-Risk marker on the revenue distribution.

---

## Extension: Closed Season

A closed fishing season of eight weeks per year is introduced to assess its impact on long-term fish-stock sustainability and revenue generation over a five-year period.

This extension demonstrates how conservation policies may improve long-run ecological and economic outcomes.

---

## Key Findings

The logistic growth model generated more realistic fish-stock behaviour than the Fibonacci approach because it incorporates carrying-capacity constraints. Harvesting intensity significantly affected both sustainability and profitability. Monte Carlo simulation provided a practical method for quantifying revenue uncertainty, while Value-at-Risk offered a meaningful measure of downside financial risk.

The analysis demonstrated that sustainable harvesting strategies can balance revenue generation with long-term fish-stock preservation.

---

## Limitations

- Fish prices are simulated rather than obtained from real market data.
- Environmental factors affecting fish populations are not included.
- Fish mortality, migration, and species interactions are simplified.
- Illegal fishing and regulatory effects are not considered.
- Market demand fluctuations are represented only through price variability.

---

## AI Usage Declaration

Microsoft Copilot was used to assist with:

- Understanding assignment requirements
- OOP design and implementation
- Statistical analysis guidance
- Monte Carlo simulation development
- Documentation preparation
- Debugging and code review

All code was reviewed, tested, and understood before submission.

---

## Author

Steven AGABA

Mini-Project 3: Lake Victoria Fish Stock & Export Risk Model