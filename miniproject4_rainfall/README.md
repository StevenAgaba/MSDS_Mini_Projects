# Rainfall Pattern & Crop Suitability Analyser

## Agaba Steven. 
### Registration Number: S26M19/002. 
### Access Number: B38624

## Project Description

This project analyzes rainfall patterns across selected regions of Uganda and evaluates crop suitability based on monthly rainfall conditions. The analysis helps agricultural extension officers identify suitable planting periods, compare regional rainfall characteristics, detect rainfall seasons, and provide evidence-based recommendations to farmers.

The project uses NumPy, SciPy, Pandas, Matplotlib, and Object-Oriented Programming (OOP) to perform statistical analysis, similarity measurement, peak detection, and visualization.

---

## Objectives

The project aims to:

- Analyze monthly rainfall distributions across regions.
- Calculate annual rainfall totals and descriptive statistics.
- Identify wettest and driest months.
- Compute coefficients of variation for rainfall stability assessment.
- Evaluate crop suitability using predefined rainfall thresholds.
- Compare regions using multiple similarity and distance measures.
- Detect rainfall seasons automatically using signal processing methods.
- Visualize rainfall patterns and crop suitability.
- Generate farmer advisory recommendations.
- Demonstrate year-to-year rainfall variability.

---

## Project Structure

```text
mini_project4_rainfall/
│
├── src/
│   ├── __init__.py
│   ├── region.py
│   └── croprules.py
│
├── tests/
│   └── test_rainfall.py
│
├── project4_rainfall.ipynb
│
├── README.md
├── requirements.txt
└── environment.yml
```

---

## Installation

Install required packages:

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
project4_rainfall.ipynb
```

Run all notebook cells:

```text
Kernel → Restart & Run All
```

The notebook is designed to execute successfully from beginning to end without modification.

---

## Dataset

Illustrative monthly rainfall data (mm) were provided for:

- Kampala
- Gulu
- Mbarara

The data represent monthly rainfall totals from January to December.

---

## Object-Oriented Design

### Region Class

The `Region` class stores rainfall data and provides methods for:

- Annual rainfall total
- Mean rainfall
- Wettest month detection
- Driest month detection
- Coefficient of variation calculation

### CropRule Class

The `CropRule` class evaluates rainfall suitability for crops including:

- Maize
- Beans
- Coffee

Monthly rainfall values are classified into categories such as:

- Suitable
- Marginal
- Drought Risk
- Waterlogging Risk

---

## Similarity Analysis

Three similarity/distance measures are implemented:

### Cosine Similarity

Measures similarity of rainfall patterns regardless of scale.

### Pearson Correlation

Measures strength and direction of linear relationships between regions.

### Euclidean Distance

Measures absolute differences between rainfall values.

### Important Observation

Regions can have very high cosine similarity even when one region receives substantially more rainfall overall. This occurs because cosine similarity evaluates pattern shape rather than total magnitude.

---

## Rainfall Season Detection

The project uses:

```python
scipy.signal.find_peaks()
```

to identify rainfall peaks and classify rainfall regimes as:

- Unimodal
- Bimodal

Results can be compared against known rainfall patterns in Uganda.

---

## Visualizations

The notebook produces:

### Line Chart

Comparison of monthly rainfall for all regions.

### Crop Suitability Heatmap

Visualization of monthly crop suitability across regions.

### Monthly Variability Boxplots

Extension analysis showing year-to-year variability of rainfall.

---

## Farmer Advisory

A short advisory note is generated for farmers in Mbarara, identifying:

- Suitable crops
- Optimal planting periods
- Potential drought-risk periods

---

## Key Findings

The analysis demonstrates that rainfall distribution differs considerably across regions, affecting crop suitability and planting decisions. Similarity metrics provide different perspectives on regional rainfall behaviour, while peak detection helps identify rainfall seasons. These insights support agricultural planning and climate-informed farming decisions.

---

## Limitations

- The rainfall dataset is illustrative rather than observed meteorological data.
- Crop suitability is based only on rainfall thresholds.
- Soil type, temperature, elevation, and agronomic practices are not included.
- Pest and disease pressures are not considered.
- Recommendations should be viewed as educational examples rather than operational agricultural advice.

---

## Testing

Run automated tests using:

```bash
pytest
```

The tests verify:

- Annual rainfall calculations
- Mean rainfall calculations
- Coefficient of variation computations

---

## AI Usage Declaration

Microsoft Copilot was used to assist with:

- Project planning
- OOP design
- Statistical analysis
- Similarity-measure implementation
- Documentation writing
- Debugging and code review

All code was reviewed, tested, and understood before submission.

---

## Author

Steven AGABA

Mini-Project 4: Rainfall Pattern & Crop Suitability Analyser