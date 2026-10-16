# Taxi Route Revenue, Pricing & Fleet Planner

## Agaba Steven. 
### Registration Number: S26M19/002. 
### Access Number: B38624

## Project Description

This project develops a demand forecasting, pricing, revenue analysis, and fleet-planning system for a taxi (matatu) association operating 14-seater vehicles on selected routes originating from Kampala. The analysis uses historical passenger counts, fare information, forecasting models, and supply-demand equilibrium concepts to support operational and planning decisions.

The project applies Object-Oriented Programming (OOP), linear algebra, forecasting techniques, statistical analysis, backtesting, and fleet-capacity planning.

---

## Objectives

The project aims to:

- Analyze passenger demand on different taxi routes.
- Calculate daily and total route revenues.
- Generate descriptive statistics for passenger volumes.
- Determine the supply-demand equilibrium fare and passenger level.
- Compare forecasting methods using backtesting.
- Select the best forecasting model for each route.
- Forecast future passenger demand and revenue.
- Estimate vehicle deployment requirements.
- Evaluate seasonal demand patterns.
- Support data-driven operational decision-making.

---

## Project Structure

```text
mini_project5_taxi/
│
├── src/
│   ├── __init__.py
│   ├── route.py
│   └── forecasting.py
│
├── tests/
│   └── test_taxi.py
│
├── project5_taxi.ipynb
│
├── README.md
├── requirements.txt
└── environment.yml
```

---

## Installation

Install project dependencies:

```bash
pip install -r requirements.txt
```

---

## Running the Project

Launch Jupyter Notebook:

```bash
jupyter notebook
```

Open:

```text
project5_taxi.ipynb
```

Run the notebook:

```text
Kernel → Restart & Run All
```

The notebook is designed to run from top to bottom without modification.

---

## Dataset

Three taxi routes are analyzed:

### Kampala – Ntinda

```text
[35, 40, 42, 50, 55, 60, 48, 52, 47, 45]
```

Fare:

```text
UGX 2,000
```

### Kampala – Entebbe

```text
[60, 58, 65, 70, 72, 80, 75, 68, 66, 64]
```

Fare:

```text
UGX 5,000
```

### Kampala – Mukono

```text
[45, 47, 50, 49, 55, 62, 58, 53, 51, 50]
```

Fare:

```text
UGX 3,000
```

---

## Object-Oriented Design

### Route Class

The `Route` class stores:

- Route name
- Passenger counts
- Fare per passenger

Methods include:

- Daily revenue calculation
- Total revenue calculation
- Mean passenger count
- Variance
- Standard deviation

### Forecaster Base Class

The forecasting system is implemented using inheritance.

Derived forecasting classes include:

1. Moving Average Forecast
2. Exponential Smoothing Forecast
3. Linear Trend Forecast

This design allows forecasting methods to be added or modified easily.

---

## Supply-Demand Equilibrium Analysis

The Ntinda route uses the following demand and supply equations:

### Demand

```text
Qd = 120 − 0.02P
```

### Supply

```text
Qs = 10 + 0.03P
```

The equations are expressed as a 2×2 linear system and solved using:

```python
scipy.linalg.solve()
```

The resulting equilibrium fare and passenger volume are compared with the current fare of UGX 2,000.

---

## Forecasting Models

Three forecasting approaches are compared:

### 1. Moving Average

Uses the average of the previous three days.

### 2. Exponential Smoothing

Applies weighted averaging with tunable parameter α.

### 3. Linear Trend

Fits a linear trend line using polynomial regression.

---

## Forecast Evaluation

Forecast performance is evaluated using:

```text
MAE (Mean Absolute Error)
```

A rolling-origin (walk-forward) backtesting approach is used on Days 4–10.

The forecasting model with the lowest MAE is selected as the best-performing model for each route.

---

## Day 11 Revenue Forecasting

Using the selected forecasting model:

- Day 11 passenger demand is predicted.
- Expected revenue is calculated using route-specific fares.
- Forecast revenue is compared with historical observations.

---

## Fleet Planning

Vehicle requirements are calculated using:

```text
14 passengers per vehicle
8 one-way trips per vehicle per day
```

Daily vehicle capacity:

```text
14 × 8 = 112 passengers
```

A 15% operational buffer is added before determining final deployment numbers.

The resulting fleet estimates help route managers allocate vehicles efficiently.

---

## Extension: Seasonal Demand Analysis

A synthetic 60-day dataset is generated that includes:

- Higher demand on Fridays
- Lower demand on Sundays

The project demonstrates that:

```text
Seasonal Naive Forecasting
```

can outperform a simple moving average when recurring weekly demand patterns exist.

---

## Visualizations

The notebook produces:

### Revenue Trends

Shows route revenue over time.

### Forecast Comparisons

Compares actual and predicted demand.

### Seasonal Analysis Outputs

Demonstrates recurring weekly demand patterns.

---

## Key Findings

The analysis reveals differences in passenger demand, revenue, and forecasting performance across the three routes. Forecasting models produce varying levels of accuracy depending on demand patterns. Fleet-planning calculations translate passenger forecasts into practical deployment decisions, while equilibrium analysis provides insight into route pricing and market efficiency.

The extension analysis highlights the importance of capturing seasonality in transportation demand forecasting.

---

## Limitations

- Only ten days of observed data are available.
- Passenger demand may be influenced by fuel prices, weather, holidays, and economic conditions.
- Traffic congestion and competitor activity are not modeled.
- Revenue calculations assume all forecasted passengers travel and pay the stated fare.
- Vehicle operating costs are not included in the analysis.

---

## Testing

Run automated tests:

```bash
pytest
```

Tests verify:

- Revenue calculations
- Mean passenger calculations
- Standard deviation calculations

---

## AI Usage Declaration

Microsoft Copilot was used to assist with:

- Interpreting assignment requirements
- Designing OOP classes
- Implementing forecasting methods
- Developing backtesting logic
- Preparing documentation
- Debugging and code review

All code was reviewed, tested, and understood before submission.

---

## Author

Steven AGABA

Mini-Project 5: Taxi Route Revenue, Pricing & Fleet Planner