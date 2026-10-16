# Solar Micro-Grid Dispatch Planner

## Agaba Steven. 
### Registration Number: S26M19/002. 
### Access Number: B38624

## Project Description

This project develops a Solar Micro-Grid Dispatch Planner for a rural health centre in Kasese, Uganda. The system determines how much energy should be supplied by solar panels and batteries to satisfy daily electricity demand constraints. Using Object-Oriented Programming (OOP), the project analyzes system stability, solves energy dispatch problems, evaluates computational performance, estimates operating costs, and performs sensitivity analysis under changing demand conditions.

## Objectives

The project aims to:

- Model a micro-grid using linear algebra.
- Solve daily energy dispatch requirements.
- Evaluate determinant and condition number of the coefficient matrix.
- Compare loop-based and vectorized numerical solutions.
- Detect physically infeasible solutions.
- Apply a non-negative least squares approach where necessary.
- Analyze solar and battery energy usage statistics.
- Calculate daily and monthly operating costs.
- Visualize energy consumption and cost trends.
- Perform Monte Carlo sensitivity analysis.
- Extend the model through a Hybrid Micro-Grid subclass.

## Project Structure

```text
mini_project2_microgrid/
│
├── src/
│   ├── __init__.py
│   └── microgrid.py
│
├── tests/
│   └── test_microgrid.py
│
├── demands.csv
│
├── project2_microgrid.ipynb
│
├── README.md
├── requirements.txt
└── environment.yml
```

## Installation

Install the required packages:

```bash
pip install -r requirements.txt
```

## Running the Project

Launch Jupyter Notebook:

```bash
jupyter notebook
```

Open:

```text
project2_microgrid.ipynb
```

Run all cells using:

```text
Kernel → Restart & Run All
```

The notebook should execute successfully from start to finish without errors.

## Testing

Run the unit tests using:

```bash
pytest
```

The tests verify:

- Correct matrix structure
- Correct solution dimensions
- Non-zero determinant of the system

## Mathematical Model

The micro-grid is represented by:

```text
3x + 2y = D1
4x + y  = D2
```

where:

- x = solar energy contribution (kWh)
- y = battery energy contribution (kWh)
- D1 = daytime load demand
- D2 = critical-equipment load demand

The model uses NumPy linear algebra functions to solve the system of equations.

## Cost Assumptions

Energy costs are assumed to be:

```text
Solar Energy   = UGX 150 per kWh
Battery Energy = UGX 450 per kWh
```

These values are illustrative and used for planning purposes only.

## Findings Summary

The coefficient matrix was found to be invertible, meaning that a unique dispatch solution exists for each day. Vectorized matrix operations performed faster than loop-based implementations due to NumPy's optimized numerical routines. The cost analysis showed that battery usage contributes most of the operational cost because of its higher unit price. Sensitivity analysis demonstrated that small demand variations produce manageable changes in dispatch levels, confirming the stability of the system.

## Limitations

- Demand values are synthetically generated.
- Weather conditions affecting solar generation are not included.
- Battery degradation is not modeled.
- Energy prices are assumed constant.
- The model does not consider equipment failures or maintenance schedules.

## AI Usage Declaration

Microsoft Copilot was used to assist with:

- Understanding assignment requirements
- Code design and debugging
- Documentation writing
- Statistical interpretation
- OOP structure development

All generated code was reviewed, tested, modified where necessary, and fully understood before submission.

## Author

Steven AGABA

Mini-Project 2: Solar Micro-Grid Dispatch Planner