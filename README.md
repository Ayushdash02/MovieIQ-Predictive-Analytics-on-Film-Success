
<div align="center">

  <img src="preview/movieiq-logo.png" alt="MovieIQ Logo" width="180"/>

  # MovieIQ — Predictive Analytics on Film Success

  ### Machine Learning Project Brief

  **Predicting Whether a Movie Will Succeed**

  <p>
    <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python"/>
    <img src="https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white" alt="Pandas"/>
    <img src="https://img.shields.io/badge/Scikit--learn-F7931E?style=for-the-badge&logo=scikitlearn&logoColor=white" alt="Scikit-learn"/>
    <img src="https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white" alt="Streamlit"/>
    <img src="https://img.shields.io/badge/Plotly-3F4F75?style=for-the-badge&logo=plotly&logoColor=white" alt="Plotly"/>
  </p>

  <p>
    An end-to-end movie analytics and machine learning project
    that transforms film industry data into financial insights,
    audience intelligence, and predictive success indicators.
  </p>

</div>

---

## 📑 Table of Contents

- [Project Overview](#-project-overview)
- [Business Problem](#-business-problem)
- [Project Objectives](#-project-objectives)
- [Key Features](#-key-features)
- [Analytical Workflow](#-analytical-workflow)
- [Machine Learning Methodology](#-machine-learning-methodology)
- [Dashboard Previews](#-dashboard-previews)
- [Analytical Visualizations](#-analytical-visualizations)
- [Technology Stack](#-technology-stack)
- [Project Structure](#-project-structure)
- [Installation and Setup](#-installation-and-setup)
- [Financial Metrics](#-financial-metrics)
- [Business Value](#-business-value)
- [Limitations](#-limitations)
- [Future Enhancements](#-future-enhancements)
- [Author](#-author)

---

## 🎬 Project Overview

**MovieIQ — Predictive Analytics on Film Success** is an end-to-end data analytics and machine learning project focused on understanding movie financial performance, audience reception, and potential commercial success.

The project combines exploratory data analysis (EDA), feature engineering, statistical hypothesis testing, interactive visualization, and Random Forest classification to investigate factors associated with movie success.

An interactive Streamlit dashboard presents the results through financial analysis, genre comparisons, audience intelligence, model evaluation, data quality assessment, and business recommendations.

### Project Highlights

- Comprehensive exploratory data analysis.
- Movie budget, revenue, profit, and ROI analysis.
- Genre-wise financial performance comparisons.
- Audience rating and popularity analysis.
- Statistical hypothesis testing.
- Random Forest classification for movie success prediction.
- Model evaluation using classification metrics and a confusion matrix.
- ROC curve analysis.
- Interactive Streamlit dashboard with Plotly visualizations.
- Business insights and data-driven recommendations.

---

## 🎯 Business Problem

The film industry involves substantial financial investments, uncertain audience demand, and unpredictable commercial outcomes. Understanding which factors are associated with financial success can help stakeholders investigate historical performance and potential risks.

Movie budgets, genres, audience ratings, popularity, and runtime may be associated with financial outcomes. However, these relationships do not necessarily imply causation or guarantee future success.

MovieIQ analyzes historical movie data and develops a classification model to estimate whether a movie meets a defined financial success criterion.

The objective is to support data-informed analysis rather than replace professional judgment, market research, or comprehensive film investment decisions.

---

## 🎯 Project Objectives

1. Analyze movie financial performance using budget, revenue, profit, and ROI.
2. Examine performance differences across genres and budget segments.
3. Investigate relationships between audience ratings, popularity, runtime, and revenue.
4. Apply statistical tests to evaluate selected hypotheses.
5. Develop a Random Forest classifier to predict movie success.
6. Evaluate predictive performance using classification metrics.
7. Build an interactive Streamlit dashboard.
8. Translate findings into practical business recommendations.

---

## 🚀 Key Features

| Feature | Description |
|---|---|
| Executive Overview | Summarizes portfolio-level performance indicators. |
| Movie Explorer | Enables movie-level exploration and filtering. |
| Financial Performance | Analyzes budget, revenue, profit, and ROI. |
| Genre Intelligence | Compares financial and audience trends by genre. |
| Audience Intelligence | Examines ratings, popularity, and engagement indicators. |
| Success Drivers | Investigates factors associated with movie success. |
| Statistical Testing | Presents hypothesis tests and statistical findings. |
| Predictive Analytics | Applies the trained Random Forest classifier. |
| Model Performance | Evaluates model predictions and classification metrics. |
| Business Insights | Communicates analytical findings and recommendations. |
| Data Quality | Examines missing values, duplicates, and data consistency. |

---

## 🔄 Analytical Workflow

<div align="center">

**Data Collection → Data Cleaning → Feature Engineering → Exploratory Data Analysis → Statistical Testing → Model Training → Model Evaluation → Dashboard Development → Business Recommendations**

</div>

### 1. Data Preparation

- Load and inspect the movie dataset.
- Review data types, dimensions, and column distributions.
- Identify missing values and duplicate records.
- Validate financial records and analytical variables.

### 2. Feature Engineering

- Calculate profit and return on investment.
- Extract release year from release dates.
- Standardize and process genre information.
- Create budget, rating, popularity, and revenue segments.
- Define the binary movie success target.

### 3. Exploratory Data Analysis

- Analyze financial performance distributions.
- Investigate the relationship between budget and revenue.
- Compare performance across genres.
- Examine audience ratings and popularity.
- Investigate correlations among numerical variables.

### 4. Statistical Analysis

- Apply suitable statistical hypothesis tests.
- Interpret p-values and statistical significance.
- Examine selected differences and relationships in the dataset.

### 5. Predictive Modeling

- Prepare model features and target labels.
- Separate training and testing data.
- Train a Random Forest classifier.
- Evaluate predictions on held-out data.

### 6. Dashboard Development

- Develop interactive Streamlit dashboard pages.
- Present key performance indicators and visualizations.
- Communicate findings through business-oriented insights.

---

## 🤖 Machine Learning Methodology

### Algorithm: Random Forest Classifier

MovieIQ uses a Random Forest classification model to estimate whether a movie meets the project's financial success criterion.

Random Forest combines multiple decision trees to generate predictions and can capture nonlinear relationships and interactions between input variables.

### Target Variable

| Class | Definition |
|---|---|
| Successful (1) | Revenue is greater than budget. |
| Not Successful (0) | Revenue is less than or equal to budget. |

This represents a simplified financial success definition. It does not account for marketing expenditure, distribution fees, taxes, or other costs unless those expenses are included in the dataset.

### Model Evaluation Metrics

| Metric | Analytical Purpose |
|---|---|
| Accuracy | Measures the proportion of correct predictions. |
| Precision | Measures the proportion of predicted successes that are actual successes. |
| Recall | Measures the proportion of actual successes correctly identified. |
| F1-score | Balances precision and recall. |
| Confusion Matrix | Summarizes correct and incorrect predictions by class. |
| ROC Curve | Evaluates class discrimination across decision thresholds. |
| Feature Importance | Shows the relative importance assigned to features by the fitted model. |

Actual evaluation values should be taken from the final trained model and test results.

---

## 📸 Dashboard Previews

Explore the MovieIQ Streamlit dashboard through its 11 analytical modules.

### 1. Executive Overview

A consolidated view of movie portfolio performance and key financial indicators.

<p align="center">
  <img src="dashboard-preview/executive-overview.png" alt="MovieIQ Executive Overview Dashboard" width="100%">
</p>

### 2. Movie Explorer

Explore individual movie records and investigate relevant movie attributes.

<p align="center">
  <img src="dashboard-preview/movie-explorer.png" alt="MovieIQ Movie Explorer Dashboard" width="100%">
</p>

### 3. Financial Performance

Analyze budgets, revenue, profitability, and return on investment.

<p align="center">
  <img src="dashboard-preview/financial-performance.png" alt="MovieIQ Financial Performance Dashboard" width="100%">
</p>

### 4. Genre Intelligence

Compare genre-level performance and differences in financial outcomes.

<p align="center">
  <img src="dashboard-preview/genre-intelligence.png" alt="MovieIQ Genre Intelligence Dashboard" width="100%">
</p>

### 5. Audience Intelligence

Investigate audience ratings, movie popularity, and engagement indicators.

<p align="center">
  <img src="dashboard-preview/audience-intelligence.png" alt="MovieIQ Audience Intelligence Dashboard" width="100%">
</p>

### 6. Success Drivers

Explore variables associated with movie success and compare performance patterns.

<p align="center">
  <img src="dashboard-preview/success-drivers.png" alt="MovieIQ Success Drivers Dashboard" width="100%">
</p>

### 7. Statistical Testing

Review hypothesis-testing results and selected statistical relationships.

<p align="center">
  <img src="dashboard-preview/statistical-testing.png" alt="MovieIQ Statistical Testing Dashboard" width="100%">
</p>

### 8. Predictive Analytics

Explore the machine learning module for estimating movie success.

<p align="center">
  <img src="dashboard-preview/predictive-analytics.png" alt="MovieIQ Predictive Analytics Dashboard" width="100%">
</p>

### 9. Model Performance

Review classification metrics and model diagnostics.

<p align="center">
  <img src="dashboard-preview/model-performance.png" alt="MovieIQ Model Performance Dashboard" width="100%">
</p>

### 10. Business Insights

Review analytical findings and potential business recommendations.

<p align="center">
  <img src="dashboard-preview/business-insights.png" alt="MovieIQ Business Insights Dashboard" width="100%">
</p>

### 11. Data Quality

Inspect data quality indicators and potential dataset issues.

<p align="center">
  <img src="dashboard-preview/data-quality.png" alt="MovieIQ Data Quality Dashboard" width="100%">
</p>

---

## 📊 Analytical Visualizations

This section presents the supporting analytical outputs, statistical tests, financial charts, and model evaluation images stored in `preview/`.

### 1. Budget vs. Revenue

Examines the relationship between movie production budgets and revenue.

<p align="center">
  <img src="preview/budget-vs-revenue.jpg" alt="Budget vs Revenue Analysis" width="100%">
</p>

### 2. Budget vs. Revenue — Log Scale

Visualizes financial relationships across a wider range of budget and revenue values.

<p align="center">
  <img src="preview/budget-vs-revenue-log-scale.jpg" alt="Budget vs Revenue Log Scale" width="100%">
</p>

### 3. Top Genres by Average Revenue

Compares average revenue across genres.

<p align="center">
  <img src="preview/top-genres-by-avg-revenue.jpg" alt="Top Genres by Average Revenue" width="100%">
</p>

### 4. Top Genres by Success Rate

Compares genre-level success rates using the project's financial success definition.

<p align="center">
  <img src="preview/top-genres-by-success-rate.jpg" alt="Top Genres by Success Rate" width="100%">
</p>

### 5. Chi-Square Test — Genre vs. Success

Examines whether genre and the defined success category are statistically associated.

<p align="center">
  <img src="preview/chi-square-test-genre-vs-success.jpg" alt="Chi Square Test Genre vs Success" width="100%">
</p>

### 6. Independent T-Test — Popularity

Presents the independent-samples t-test comparing popularity between the selected groups.

<p align="center">
  <img src="preview/independent-T-test-popularity.jpg" alt="Independent T Test Popularity" width="100%">
</p>

### 7. Confusion Matrix

Summarizes the classification model's correct and incorrect predictions.

<p align="center">
  <img src="preview/matrix.jpg" alt="MovieIQ Confusion Matrix" width="100%">
</p>

### 8. ROC Curve

Illustrates the classification model's ability to distinguish between target classes across decision thresholds.

<p align="center">
  <img src="preview/roc-curve.jpg" alt="MovieIQ ROC Curve" width="100%">
</p>

### 9. Selected Movie Profile

Displays a selected movie's analytical profile and available attributes.

<p align="center">
  <img src="preview/selected-movie-profile.jpg" alt="Selected Movie Profile" width="100%">
</p>

### 10. Data Quality Assessment

Highlights data quality checks and potential data issues.

<p align="center">
  <img src="preview/data-quality.jpg" alt="MovieIQ Data Quality Analysis" width="100%">
</p>

### 11. Prepared Dataset Preview

Shows a sample of the prepared movie dataset.

<p align="center">
  <img src="preview/prepared-data-preview.jpg" alt="Prepared Dataset Preview" width="100%">
</p>

### 12. Dashboard KPI Cards

Presents key performance indicators used to summarize movie portfolio performance.

<p align="center">
  <img src="preview/KPI_cards.jpg" alt="MovieIQ KPI Cards" width="100%">
</p>

### 13. MovieIQ Project Logo

<p align="center">
  <img src="preview/movieiq-logo.png" alt="MovieIQ Project Logo" width="220">
</p>

---

## 🛠️ Technology Stack

| Technology | Application |
|---|---|
| Python | Core programming and analytical workflow |
| Pandas | Data manipulation and analysis |
| NumPy | Numerical computation |
| Matplotlib | Statistical visualization |
| Seaborn | Exploratory data visualization |
| Plotly | Interactive charts |
| Scikit-learn | Machine learning and model evaluation |
| Streamlit | Interactive dashboard development |
| Git | Version control |
| GitHub | Source code hosting and documentation |

Keep the dependency list aligned with the libraries actually used by the application.

---

## 📁 Project Structure

```text
MovieIQ-Predictive-Analytics-on-Film-Success/
│
├── MovieIQ.py
├── requirements.txt
├── README.md
├── movies.csv
│
├── data/
│   └── movies.csv
│
├── models/
│   └── random_forest.pkl
│
├── assets/
│   ├── movieiq_logo.png
│   └── favicon.png
│
├── dashboard-preview/
│   ├── audience-intelligence.png
│   ├── business-insights.png
│   ├── data-quality.png
│   ├── executive-overview.png
│   ├── financial-performance.png
│   ├── genre-intelligence.png
│   ├── model-performance.png
│   ├── movie-explorer.png
│   ├── predictive-analytics.png
│   ├── statistical-testing.png
│   └── success-drivers.png
│
└── preview/
    ├── budget-vs-revenue.jpg
    ├── budget-vs-revenue-log-scale.jpg
    ├── chi-square-test-genre-vs-success.jpg
    ├── data-quality.jpg
    ├── independent-T-test-popularity.jpg
    ├── KPI_cards.jpg
    ├── matrix.jpg
    ├── movieiq-logo.png
    ├── prepared-data-preview.jpg
    ├── roc-curve.jpg
    ├── selected-movie-profile.jpg
    ├── top-genres-by-avg-revenue.jpg
    └── top-genres-by-success-rate.jpg
```

Adjust this structure to match your actual repository. Keep only files and folders required by your implementation.

---

## ⚙️ Installation and Setup

### Prerequisites

- Python installed on your system.
- Git installed on your system.
- A code editor such as Visual Studio Code.

### Step 1: Clone the Repository

```bash
git clone https://github.com/YOUR-USERNAME/MovieIQ-Predictive-Analytics-on-Film-Success.git
```

Replace `YOUR-USERNAME` with your GitHub username.

### Step 2: Navigate to the Project

```bash
cd MovieIQ-Predictive-Analytics-on-Film-Success
```

### Step 3: Create a Virtual Environment

```bash
python -m venv .venv
```

Activate it on Windows:

```bash
.venv\Scripts\activate
```

### Step 4: Install Dependencies

```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```

### Step 5: Verify Required Files

Confirm that the dataset, trained model, logo, and other required assets are available at the paths expected by `MovieIQ.py`.

### Step 6: Launch the Dashboard

```bash
python -m streamlit run MovieIQ.py
```

Open the local URL displayed in the terminal, typically:

```text
http://localhost:8501
```

---

## 💰 Financial Metrics

### Profit

\[
\text{Profit} = \text{Revenue} - \text{Budget}
\]

### Return on Investment

\[
\text{ROI (\%)} =
\frac{\text{Revenue} - \text{Budget}}{\text{Budget}}
\times 100
\]

### Financial Success Classification

\[
\text{Success} =
\begin{cases}
1, & \text{if Revenue} > \text{Budget} \\
0, & \text{if Revenue} \leq \text{Budget}
\end{cases}
\]

These are simplified financial indicators. Revenue exceeding production budget does not necessarily establish net profitability after all associated expenses.

---

## 🔍 Key Business Questions

- Is production budget associated with movie revenue?
- Which genres demonstrate stronger financial performance?
- How are audience ratings and popularity related to revenue?
- How does financial success vary across budget segments?
- Are selected differences between movie groups statistically significant?
- How effectively does the Random Forest classifier identify movie success?
- Which features contribute most to the model's predictions?
- How can historical movie data inform preliminary investment analysis?

---

## 💡 Business Value

MovieIQ demonstrates how data analytics and machine learning can support film industry research.

- **Production planning:** Explore historical budget and revenue patterns.
- **Genre strategy:** Compare genre-level performance.
- **Audience research:** Investigate rating and popularity relationships.
- **Risk assessment:** Examine historical success rates across budget segments.
- **Decision support:** Use model outputs as one input to preliminary analysis.
- **Reporting:** Communicate findings through interactive visualizations.

Predictions are estimates based on the available data and model assumptions, not guarantees of future box-office performance.

---

## ⚠️ Limitations

- Historical movie data may contain missing, inconsistent, or incomplete financial records.
- Budget and revenue figures may not represent complete financial outcomes.
- The target definition does not account for every production and distribution cost.
- Genre, rating, and popularity information may be incomplete or inconsistent.
- Predictive performance depends on data quality, feature selection, and evaluation methodology.
- Feature importance does not establish causation.
- A model trained on historical movies may not generalize to future releases.

---

## 🔮 Future Enhancements

- Incorporate inflation-adjusted financial metrics.
- Add marketing, distribution, and release-strategy variables.
- Apply cross-validation and systematic hyperparameter tuning.
- Compare Random Forest with other classification algorithms.
- Add model explainability and probability calibration.
- Improve deployment, automated testing, and model versioning.
- Integrate updated datasets and monitor model performance over time.

---

## 👨‍💻 Author

<div align="center">

**Ayush Dash**

Data Analytics | Business Intelligence | Machine Learning

[GitHub Profile](https://github.com/YOUR-USERNAME)

</div>

---

<div align="center">

**MovieIQ — Turning Movie Data into Predictive Intelligence**

*An analytical project combining financial performance analysis, statistical methods, and machine learning.*

</div>
