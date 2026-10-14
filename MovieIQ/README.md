# 🎬 MovieIQ — Film Success Intelligence

> **An interactive Data Analytics, Business Intelligence, and Machine Learning dashboard for analysing movie financial performance, audience behaviour, genre trends, and historical success patterns.**

MovieIQ is a professional **Streamlit-based analytics platform** that transforms movie-level data into meaningful business insights through:

- 📊 Exploratory Data Analysis (EDA)
- 💰 Financial Performance Analysis
- 🎭 Genre Intelligence
- 👥 Audience Intelligence
- 📈 Success Driver Analysis
- 🧪 Statistical Analysis
- 🤖 Random Forest Classification
- 🎯 Predictive Screening
- 💡 Business Intelligence Insights
- 📋 Data Quality Analysis

---

## 📌 Project Overview

MovieIQ analyses historical movie data to understand the factors associated with financial success and audience performance.

The project focuses on the following analytical areas:

- Movie financial performance
- Budget and revenue relationships
- Genre-level performance
- Audience popularity and ratings
- Success-related characteristics
- Statistical relationships
- Historical success classification
- Business-oriented interpretation

### 🎯 Success Definition

For this project, a movie is classified as **financially successful** when:

```text
Revenue > Budget
```

The analytical target is defined as:

| Success | Definition | Meaning |
|---:|---|---|
| `1` | Revenue > Budget | Financial Success |
| `0` | Revenue ≤ Budget | Financial Failure |

> **Note:** This is an analytical definition used for this project. It does not represent complete accounting profit because real-world movie profitability also depends on marketing, distribution, taxes, revenue sharing, financing, and other commercial costs.

---

# 🎯 Project Objectives

MovieIQ aims to:

1. Analyse historical movie financial performance.
2. Understand the relationship between budget and revenue.
3. Identify genre-level performance patterns.
4. Analyse popularity, ratings, and audience engagement.
5. Identify variables associated with movie success.
6. Perform statistical hypothesis testing.
7. Build a Random Forest classification model.
8. Evaluate machine-learning performance using multiple metrics.
9. Provide an interactive movie exploration experience.
10. Translate analytical findings into business-oriented insights.

---

# 📊 Dashboard Modules

MovieIQ contains multiple analytical modules designed to provide an end-to-end movie intelligence experience.

---

## 🏠 1. Executive Overview

Provides a high-level summary of the movie dataset.

### Key KPIs

- Total Movies
- Total Revenue
- Average Budget
- Average Revenue
- Success Rate

### Analysis

- Budget vs Revenue
- Genre Performance
- Financial Performance
- Executive Signals

---

## 🎬 2. Movie Explorer

An interactive movie catalogue for detailed exploration.

### Features

- 🔎 Movie search
- 🎭 Genre filtering
- 🎯 Success / Failure filtering
- ⭐ Rating filtering
- 📈 Popularity filtering
- 📅 Release-year filtering
- ↕️ Sorting and ranking

### Sorting Options

Users can sort movies by:

- Revenue
- Profit
- ROI
- Rating
- Popularity
- Budget

### Movie Profile

Individual movie analysis includes:

- Movie title
- Budget
- Revenue
- Profit
- ROI
- Genre
- Rating
- Popularity
- Runtime
- Financial outcome

---

# 💰 3. Financial Performance

Analyses the financial characteristics of movies.

### Key Metrics

- Total Revenue
- Total Budget
- Total Profit
- Average ROI

### Analysis

- Budget vs Revenue
- ROI Distribution
- Revenue by Success Status
- Financial Performance Comparison

---

# 🎭 4. Genre Intelligence

Examines movie performance across genres.

### Metrics

- Movie Count
- Average Revenue
- Average Budget
- Average ROI
- Success Rate

This module helps identify historically stronger and weaker genre-level financial patterns.

---

# 👥 5. Audience Intelligence

Explores audience-related indicators and their relationship with financial performance.

### Key Variables

- Popularity
- Vote Average
- Vote Count
- Revenue
- Success Status

### Analysis

- Popularity vs Revenue
- Rating vs Revenue
- Audience Signals by Outcome

---

# 📈 6. Success Drivers

Examines relationships between important numerical variables.

### Analysis Includes

- Correlation Matrix
- Numerical Feature Relationships
- Successful vs Unsuccessful Movie Comparison

### Variables

- Budget
- Revenue
- Profit
- ROI
- Popularity
- Runtime
- Vote Average
- Vote Count

> **Important:** Correlation indicates association and does not prove causation.

---

# 🧪 7. Statistical Testing

MovieIQ uses statistical methods to evaluate selected relationships.

## Independent T-Test

Used to compare popularity between successful and unsuccessful movies.

### Hypotheses

**Null Hypothesis (H₀)**

```text
Mean popularity is equal between successful and unsuccessful movies.
```

**Alternative Hypothesis (H₁)**

```text
Mean popularity differs between successful and unsuccessful movies.
```

### Significance Level

```text
α = 0.05
```

---

## Chi-Square Test

Used to examine the relationship between genre and movie success.

### Hypotheses

**Null Hypothesis (H₀)**

```text
Genre and movie success are independent.
```

**Alternative Hypothesis (H₁)**

```text
Genre and movie success are associated.
```

### Significance Level

```text
α = 0.05
```

---

## Pearson Correlation

Used to measure the linear relationship between:

```text
Budget ↔ Revenue
```

The analysis reports:

- Pearson correlation coefficient
- P-value

> A statistically significant correlation does not necessarily imply a causal relationship.

---

# 🤖 8. Predictive Analytics

MovieIQ includes a **Random Forest Classifier** for historical movie-success screening.

The model predicts:

```text
Success
   vs
Failure
```

### Target Variable

```text
success
```

### Model Features

The current model uses:

```text
budget
popularity
runtime
vote_average
primary_genre
```

### Random Forest Configuration

| Parameter | Value |
|---|---:|
| Number of Estimators | 300 |
| Maximum Depth | 10 |
| Minimum Samples Split | 5 |
| Minimum Samples Leaf | 2 |
| Class Weight | Balanced |
| Random State | 42 |
| Parallel Processing | Enabled |

The model is trained **dynamically inside the Streamlit application**.

> No separate `random_forest.pkl` file is required in the current MovieIQ implementation.

---

# 🎯 9. Model Evaluation

The Random Forest model is evaluated using a held-out test dataset.

### Evaluation Metrics

- Accuracy
- Precision
- Recall
- F1 Score
- ROC-AUC

### Additional Outputs

- Confusion Matrix
- ROC Curve
- Classification Report
- Feature Importance

Using multiple evaluation metrics provides a more complete understanding of model performance than relying only on accuracy.

---

# 🔄 Analytical Workflow

```text
Raw Movie Dataset
        ↓
Data Loading
        ↓
Data Cleaning & Preparation
        ↓
Feature Engineering
        ↓
Exploratory Data Analysis
        ↓
Financial Analysis
        ↓
Genre Analysis
        ↓
Audience Analysis
        ↓
Correlation Analysis
        ↓
Statistical Testing
        ↓
Random Forest Classification
        ↓
Model Evaluation
        ↓
Business Insights
```

---

# 🧮 Key Calculations

## Profit

```text
Profit = Revenue − Budget
```

## ROI

```text
ROI = (Revenue − Budget) / Budget
```

## Success Target

```text
Success = 1  if Revenue > Budget
Success = 0  if Revenue ≤ Budget
```

---

# ⚙️ Data Preparation

MovieIQ performs several preparation and feature-engineering operations automatically.

### Data Preparation

- Numeric data conversion
- Missing-value handling
- Duplicate analysis
- Financial validation
- Zero-budget detection
- Negative-budget detection
- Zero-revenue analysis

### Feature Engineering

- Success target creation
- Profit calculation
- ROI calculation
- Genre extraction
- Primary genre creation
- Release-year extraction

### Analytical Segmentation

MovieIQ also supports segmentation of:

- Budget
- Rating
- Popularity
- Revenue

---

# 🛠️ Technology Stack

| Category | Technologies |
|---|---|
| Programming | Python |
| Data Analysis | Pandas, NumPy |
| Visualization | Plotly |
| Statistics | SciPy |
| Machine Learning | Scikit-learn |
| Dashboard | Streamlit |
| Development | VS Code, Jupyter Notebook, Google Colab |

---

# 📂 Project Structure

```text
MovieIQ/
│
├── MovieIQ.py
├── movies.csv
├── requirements.txt
├── README.md
│
├── data/
│   └── movies.csv
│
└── assets/
    ├── movieiq_logo.png
    └── favicon.png
```

### Project Files

| File / Folder | Description |
|---|---|
| `MovieIQ.py` | Main Streamlit application |
| `movies.csv` | Movie dataset |
| `requirements.txt` | Required Python dependencies |
| `README.md` | Project documentation |
| `data/` | Dataset directory |
| `assets/` | Logo and favicon resources |

> The Random Forest model is trained dynamically inside `MovieIQ.py`. The current project does not require a separate `model/`, `train_model.py`, or `random_forest.pkl` file.

---

# 📦 Installation & Setup

## 1. Clone or Download the Project

Download the repository and open the project directory.

```bash
cd MovieIQ
```

---

## 2. Create a Virtual Environment

### Windows

```bash
python -m venv venv
```

Activate the environment:

```bash
venv\Scripts\activate
```

### macOS / Linux

```bash
python3 -m venv venv
```

Activate:

```bash
source venv/bin/activate
```

---

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 4. Run the Application

```bash
streamlit run MovieIQ.py
```

The MovieIQ dashboard will open automatically in your browser.

---

# 📄 Dataset Requirements

The application is designed to work with movie-level data containing fields such as:

```text
title
budget
revenue
popularity
runtime
vote_average
vote_count
genres
release_date
```

MovieIQ prepares the available data dynamically before performing analysis.

---

# 💡 Business Value

MovieIQ demonstrates how raw movie data can be transformed into an interactive Business Intelligence solution.

### 🎥 Producers

Benchmark proposed movie projects against historical movie characteristics.

### 🏢 Studios

Use historical financial and genre patterns as an early-stage screening tool.

### 💼 Investors

Use financial metrics and model outputs as supporting evidence for further analysis.

### 📣 Marketing Teams

Analyse historical popularity and audience signals to understand engagement patterns.

---

# 📌 Key Analytical Questions

MovieIQ is designed to answer practical business questions.

## 💰 Financial

- Does budget relate to revenue?
- Which movies generate the highest ROI?
- Which movies achieve financial success?
- How does financial performance vary across movies?

## 🎭 Genre

- Which genres generate the highest average revenue?
- Which genres have higher historical success rates?
- Which genres provide stronger ROI?

## 👥 Audience

- Is popularity associated with revenue?
- Does rating relate to financial performance?
- Do successful movies show stronger audience engagement?

## 🧪 Statistical

- Is popularity significantly different between successful and unsuccessful movies?
- Is genre associated with movie success?
- How strong is the budget-revenue relationship?

## 🤖 Predictive

- Can historical movie characteristics classify financial success?
- Which features are most important to the model?
- How well does the Random Forest classify success?

---

# 💡 Business Insights

MovieIQ converts analytical findings into business-oriented recommendations for:

- 🎥 Studios
- 🎬 Producers
- 💼 Investors
- 📣 Marketing Teams

The dashboard is designed to support **data-informed decision-making** rather than replace business judgment.

---

# ⚠️ Model & Business Limitations

MovieIQ should be considered a **historical analytical screening system**, not a guaranteed box-office forecasting platform.

The current dataset does not include several potentially important commercial variables, including:

- Marketing expenditure
- Release timing
- Cast popularity
- Director influence
- Distributor
- Production company
- Competition
- Advertising strategy
- Market conditions

Therefore, model predictions should be interpreted as:

> **Decision-support signals rather than guaranteed outcomes.**

---

# 🔍 Analytical Principle

## Association ≠ Causation

A strong relationship between two variables does not necessarily mean that one variable causes the other.

For example:

```text
Higher Budget
      ↓
Higher Revenue
```

may represent a strong historical association, but it does not prove that increasing a movie's budget alone will cause higher revenue.

MovieIQ findings should therefore be combined with domain knowledge and additional commercial information.

---

# 🚀 Future Enhancements

Potential future improvements include:

## 🤖 Machine Learning

- Logistic Regression
- Gradient Boosting
- XGBoost
- Hyperparameter tuning
- Cross-validation
- Model comparison
- Threshold optimization
- SHAP-based model explainability

## 🎬 Additional Features

- Cast information
- Director information
- Production company
- Marketing budget
- Distributor
- Franchise information
- Release month
- Competition indicators

## 📊 Dashboard Improvements

- Advanced executive scorecards
- Movie comparison mode
- Portfolio benchmarking
- Automated insight generation
- Downloadable analytical reports
- Advanced filtering
- Interactive benchmarking

---

# 🏆 Project Highlights

## 📊 Data Analytics

- Data cleaning
- Feature engineering
- Exploratory Data Analysis
- KPI development
- Segmentation
- Data quality analysis

## 💼 Business Intelligence

- Executive dashboard
- Financial analysis
- Genre intelligence
- Audience intelligence
- Business recommendations

## 🧪 Statistics

- Independent T-Test
- Chi-Square Test
- Pearson Correlation

## 🤖 Machine Learning

- Random Forest Classification
- Train/Test Split
- Classification Metrics
- ROC-AUC
- Confusion Matrix
- ROC Curve
- Feature Importance

## 💻 Application Development

- Streamlit
- Interactive filters
- Interactive visualizations
- Movie exploration
- Predictive screening

---

# 👨‍💻 Author

## Ayush Dash

**Data Analyst / BI Analyst Portfolio Project**

### Core Skills Demonstrated

```text
Python
Pandas
NumPy
SQL
Power BI
Streamlit
Plotly
Data Visualization
Exploratory Data Analysis
Statistics
Machine Learning
Business Intelligence
```

---

# 🎓 Project Purpose

MovieIQ was developed as a professional portfolio project to demonstrate an end-to-end analytical workflow:

```text
Raw Data
   ↓
Data Cleaning
   ↓
EDA
   ↓
Statistics
   ↓
Machine Learning
   ↓
Visualization
   ↓
Business Intelligence
```

The project demonstrates the ability to transform a raw dataset into an interactive analytical application and communicate technical findings through business-oriented insights.

---

# ⚖️ Disclaimer

MovieIQ is an **educational and portfolio analytics project**.

The project defines financial success as:

```text
Revenue > Budget
```

This definition does not represent complete accounting profit because real-world movie profitability may also involve:

- Marketing costs
- Distribution costs
- Taxes
- Revenue sharing
- Financing costs
- Other commercial expenses

Machine-learning predictions are historical analytical outputs and should **not** be interpreted as guaranteed box-office forecasts or investment advice.

---

# ⭐ Project Summary

> **MovieIQ — From Movie Data to Measurable Business Intelligence.**

MovieIQ combines:

```text
Data Analytics
      +
Statistical Analysis
      +
Machine Learning
      +
Interactive Visualization
      +
Business Intelligence
```

to create a complete **Film Success Intelligence** platform.

---

## ⭐ If you find this project interesting

Feel free to explore the project, review the analytical workflow, and use it as a reference for building data-driven applications with **Python, Streamlit, Statistics, and Machine Learning**.