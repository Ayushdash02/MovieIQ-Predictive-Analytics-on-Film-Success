
<div align="center">

  <img src="assets/movieiq_logo.png" alt="MovieIQ Logo" width="180"/>

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

## Table of Contents

- [Project Overview](#-project-overview)
- [Business Problem](#-business-problem)
- [Project Objectives](#-project-objectives)
- [Key Features](#-key-features)
- [Analytical Workflow](#-analytical-workflow)
- [Machine Learning Methodology](#-machine-learning-methodology)
- [Dashboard Modules](#-dashboard-modules)
- [Technology Stack](#-technology-stack)
- [Project Structure](#-project-structure)
- [Installation and Setup](#-installation-and-setup)
- [How Success Is Defined](#-how-success-is-defined)
- [Key Business Questions](#-key-business-questions)
- [Business Value](#-business-value)
- [Limitations](#-limitations)
- [Future Enhancements](#-future-enhancements)
- [Author](#-author)

---

## 🎬 Project Overview

**MovieIQ — Predictive Analytics on Film Success** is a data analytics and machine learning project designed to investigate the financial performance, audience reception, and potential success of movies.

The project combines exploratory data analysis (EDA), statistical hypothesis testing, interactive data visualization, feature engineering, and Random Forest classification to identify patterns associated with movie success.

An interactive Streamlit dashboard brings the analytical findings together in a unified interface, allowing users to explore movie performance, investigate success drivers, and understand model predictions.

### Project Highlights

- Exploratory analysis of movie financial and audience data.
- Budget, revenue, profit, and return on investment (ROI) analysis.
- Genre-wise and audience-rating comparisons.
- Statistical hypothesis testing.
- Random Forest classification for movie success prediction.
- Model evaluation using classification metrics.
- Interactive visualizations and business recommendations.

---

## 🎯 Business Problem

Movie production involves substantial financial investment, uncertain audience demand, and unpredictable commercial outcomes.

Production budgets, genres, audience ratings, popularity, and runtime may be associated with a movie's financial performance. However, these relationships do not guarantee commercial success.

MovieIQ investigates these factors to identify meaningful patterns in historical movie data and develop a classification model that estimates whether a movie may achieve financial success under a defined target criterion.

The objective is to support data-informed analysis rather than replace creative judgment, market research, or professional investment decisions.

---

## 🎯 Project Objectives

1. Evaluate the financial performance of movies using budget, revenue, profit, and ROI.
2. Identify differences in performance across movie genres and budget segments.
3. Investigate relationships between audience ratings, popularity, runtime, and revenue.
4. Apply statistical tests to evaluate selected analytical hypotheses.
5. Build a Random Forest classification model for movie success prediction.
6. Evaluate model performance using appropriate classification metrics.
7. Develop an interactive Streamlit dashboard for data exploration and reporting.
8. Translate analytical findings into practical business recommendations.

---

## 🚀 Key Features

| Feature | Description |
|---|---|
| Executive Overview | Summarizes major portfolio performance indicators. |
| Movie Explorer | Supports detailed exploration and filtering of movie records. |
| Financial Performance | Analyzes revenue, profit, budget, and ROI. |
| Genre Intelligence | Compares performance across movie genres. |
| Audience Intelligence | Examines ratings, popularity, and audience engagement. |
| Success Drivers | Investigates variables associated with movie success. |
| Statistical Testing | Evaluates selected hypotheses using statistical methods. |
| Predictive Analytics | Applies a trained Random Forest classifier. |
| Model Performance | Presents classification evaluation results. |
| Business Insights | Converts findings into actionable recommendations. |
| Data Quality | Examines missing values, duplicates, and data consistency. |

---

## 🔄 Analytical Workflow

<div align="center">

**Data Collection → Data Cleaning → Feature Engineering → Exploratory Data Analysis → Statistical Testing → Model Training → Model Evaluation → Dashboard Development → Business Recommendations**

</div>

### Workflow Details

**1. Data Preparation**
- Load the movie dataset.
- Inspect column names, data types, and dataset dimensions.
- Identify missing values, duplicate records, and invalid financial values.
- Validate the fields required for financial analysis.

**2. Feature Engineering**
- Calculate profit and return on investment.
- Extract release year from release dates.
- Standardize genre information.
- Create budget, rating, popularity, and revenue segments.
- Define the binary movie success target.

**3. Exploratory Data Analysis**
- Analyze financial performance distributions.
- Investigate budget–revenue relationships.
- Compare genre performance.
- Explore audience ratings and popularity patterns.
- Examine correlations among numerical variables.

**4. Statistical Analysis**
- Apply suitable hypothesis tests.
- Interpret statistical significance using p-values.
- Assess relationships and differences within the analyzed dataset.

**5. Predictive Modeling**
- Prepare model features and target labels.
- Split data into training and testing sets.
- Train a Random Forest classifier.
- Evaluate predictions on held-out data.

**6. Dashboard Development**
- Build interactive Streamlit pages.
- Present key metrics, charts, filters, and model results.
- Communicate findings through business-oriented insights.

---

## 🤖 Machine Learning Methodology

### Algorithm: Random Forest Classifier

MovieIQ uses a Random Forest classification approach to estimate the probability or class of movie success from selected input features.

Random Forest combines multiple decision trees to produce a classification result. It can model nonlinear relationships and interactions between input variables.

### Target Variable

The binary target is defined as:

- **Successful (1):** Revenue is greater than budget.
- **Not Successful (0):** Revenue is less than or equal to budget.

This is a simplified financial definition of success. It does not account for marketing costs, distribution fees, taxes, or other production-related expenses unless those costs are included in the dataset.

### Model Evaluation Metrics

| Metric | Purpose |
|---|---|
| Accuracy | Measures the proportion of correct predictions. |
| Precision | Measures how many predicted successes are actually successful. |
| Recall | Measures how many actual successes the model identifies. |
| F1-score | Balances precision and recall. |
| Confusion Matrix | Shows correct and incorrect predictions by class. |
| Feature Importance | Indicates which included features contribute to the fitted model's decisions. |

Actual model performance values should be taken from the final trained model and test results rather than assumed in advance.

---

## 📊 Dashboard Modules

The MovieIQ Streamlit dashboard is organized into analytical modules:

| Module | Analytical Focus |
|---|---|
| Executive Overview | Overall movie portfolio performance |
| Movie Explorer | Individual records and filtering |
| Financial Performance | Budgets, revenues, profits, and ROI |
| Genre Intelligence | Genre-level financial and audience trends |
| Audience Intelligence | Ratings, popularity, and engagement |
| Success Drivers | Factors associated with success |
| Statistical Testing | Hypothesis testing and interpretation |
| Predictive Analytics | Movie success classification |
| Model Performance | Classification metrics and diagnostics |
| Business Insights | Findings and recommendations |
| Data Quality | Dataset validation and quality checks |

### 📸 Dashboard Previews

Add your actual Streamlit screenshots to the `previews/` directory and use the corresponding filenames below.

<div align="center">

### Executive Overview

<img src="previews/executive-overview.png" alt="MovieIQ Executive Overview Dashboard" width="100%"/>

### Financial Performance

<img src="previews/financial-performance.png" alt="MovieIQ Financial Performance Dashboard" width="100%"/>

### Genre Intelligence

<img src="previews/genre-intelligence.png" alt="MovieIQ Genre Intelligence Dashboard" width="100%"/>

### Predictive Analytics

<img src="previews/predictive-analytics.png" alt="MovieIQ Predictive Analytics Dashboard" width="100%"/>

</div>

> **Note:** These are the expected screenshot paths. Upload your images using these exact filenames or update the paths to match your actual files. GitHub will not display images that have not been uploaded.

---

## 🛠️ Technology Stack

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| Pandas | Data manipulation and analysis |
| NumPy | Numerical computation |
| Matplotlib | Statistical plotting |
| Seaborn | Exploratory data visualization |
| Plotly | Interactive visualizations |
| Scikit-learn | Machine learning and model evaluation |
| Streamlit | Interactive analytics dashboard |
| Joblib / Pickle | Model serialization, depending on implementation |
| Git and GitHub | Version control and project hosting |

Only retain libraries that are actually used by your implementation.

---

## 📁 Project Structure

```text
MovieIQ-Predictive-Analytics-on-Film-Success/
│
├── MovieIQ.py
├── requirements.txt
├── README.md
│
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
└── previews/
    ├── executive-overview.png
    ├── financial-performance.png
    ├── genre-intelligence.png
    └── predictive-analytics.png
```

> Adjust this structure to match your actual repository. Avoid uploading duplicate datasets or model files unless both are required by the application.

---

## ⚙️ Installation and Setup

### Prerequisites

- Python 3.10 or another version supported by your dependencies.
- Git.
- A code editor such as Visual Studio Code.

### Step 1: Clone the Repository

```bash
git clone https://github.com/YOUR-USERNAME/MovieIQ-Predictive-Analytics-on-Film-Success.git
```

Replace `YOUR-USERNAME` with your GitHub username.

### Step 2: Navigate to the Project Directory

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

### Step 5: Verify the Required Files

Confirm that the application can access the movie dataset, trained model, and assets at the paths expected by the code.

### Step 6: Run the Streamlit Dashboard

```bash
python -m streamlit run MovieIQ.py
```

Streamlit will provide a local URL, typically:

```text
http://localhost:8501
```

Open that URL in your browser to explore the dashboard.

---

## 💰 How Success Is Defined

MovieIQ uses a simple revenue-versus-budget rule to create the classification target:

\[
\text{Success} =
\begin{cases}
1, & \text{if Revenue} > \text{Budget} \\
0, & \text{if Revenue} \leq \text{Budget}
\end{cases}
\]

Profit is calculated as:

\[
\text{Profit} = \text{Revenue} - \text{Budget}
\]

Return on investment is calculated as:

\[
\text{ROI (\%)} =
\frac{\text{Revenue} - \text{Budget}}{\text{Budget}}
\times 100
\]

These metrics represent simplified financial indicators. Revenue exceeding production budget does not necessarily mean a movie generated a net profit after all associated expenses.

---

## 🔍 Key Business Questions

MovieIQ explores questions such as:

- Is a higher production budget associated with higher revenue?
- Which genres demonstrate stronger financial performance?
- How do audience ratings and popularity relate to revenue?
- Which budget segments exhibit different success patterns?
- Are there statistically significant differences between selected movie groups?
- How effectively can a Random Forest classifier identify movie success?
- Which features contribute most to the trained model's predictions?
- How can historical movie data support more informed investment analysis?

---

## 💡 Business Value

The project demonstrates how data analytics and machine learning can support film industry research.

Potential applications include:

- **Production planning:** Explore historical relationships between budgets and revenue.
- **Genre strategy:** Compare genre-level financial performance.
- **Audience research:** Investigate rating and popularity patterns.
- **Risk assessment:** Examine historical success rates across budget segments.
- **Decision support:** Use classification outputs as one input to preliminary analysis.
- **Reporting:** Communicate trends through interactive visualizations.

Model predictions are exploratory estimates, not guarantees of future box-office performance.

---

## ⚠️ Limitations

- Historical movie data may contain missing, inconsistent, or incomplete financial records.
- Reported revenue and budget may not represent complete financial outcomes.
- The success definition does not account for all production and distribution costs.
- Genre, rating, and popularity fields may be incomplete or measured inconsistently.
- Predictive performance depends on feature selection, data quality, and the train-test methodology.
- Feature importance does not establish causation.
- A model trained on historical records may not generalize to future releases or changing audience preferences.

---

## 🔮 Future Enhancements

- Incorporate inflation-adjusted financial metrics.
- Add marketing, distribution, and release-strategy variables where available.
- Apply cross-validation and systematic hyperparameter tuning.
- Evaluate additional classification algorithms.
- Add probability calibration and explainability methods.
- Improve deployment, testing, and model version management.
- Integrate updated datasets and monitor model performance over time.

---

## 👨‍💻 Author

<div align="center">

**Ayush Dash**

Data Analytics • Business Intelligence • Machine Learning

[GitHub](https://github.com/YOUR-USERNAME)

</div>

---

<div align="center">

**MovieIQ — Turning Movie Data into Predictive Intelligence**

*Built for analytical exploration, predictive modeling, and data-driven decision support.*

</div>
