# 🚀 ML Learning Journey

> My journey of learning Machine Learning from fundamentals to building and deploying real-world ML projects.

## 👋 About

Hi! I'm a B.Tech student from India currently entering my 3rd year.

This repository documents my journey of learning **Machine Learning, Data Science, and ML Engineering** by building things rather than only completing courses.

I'm using this repository to keep track of the concepts I learn, the experiments I run, the problems I encounter, and the projects I build.

## 📚 What I've Learned

### 🐍 Python & Development Tools

* [x] Python fundamentals & revision
* [x] Git & GitHub basics
* [x] Git workflow — repositories, commits, branches, push/pull, etc.

### 📊 Data Science

* [x] NumPy
* [x] Pandas
* [x] Matplotlib
* [x] Seaborn
* [x] Exploratory Data Analysis (EDA)
* [x] Univariate Analysis
* [x] Bivariate Analysis
* [x] Data cleaning
* [x] Feature Engineering fundamentals
* [x] Handling missing values
* [x] Standardization & Normalization
* [x] Categorical data encoding

### 🤖 Machine Learning

* [x] Train/Test Split
* [x] Logistic Regression
* [x] Decision Trees
* [x] Random Forest
* [x] Gradient Boosting / XGBoost
* [x] Classification
* [x] Confusion Matrix
* [x] Accuracy
* [x] Precision
* [x] Recall
* [x] F1 Score
* [x] ROC-AUC
* [x] Classification threshold tuning and precision–recall trade-offs
* [x] Model comparison
* [x] Hyperparameter tuning with GridSearchCV
* [x] Logistic Regression coefficient interpretation
* [x] Scikit-learn Pipelines
* [x] ColumnTransformer
* [x] One-Hot Encoding
* [x] StandardScaler

### 🛠️ ML Applications & Workflow

* [x] Saving and loading trained models with Joblib
* [x] Building a Streamlit ML application
* [x] Deploying a Streamlit application

### 🚧 Currently Working On

* [x] Improving model performance
* [x] Comparing multiple ML models
* [x] Model interpretation & feature importance
* [x] Streamlit application
* [x] Model deployment
* [x] Project documentation & presentation

---

# 🧠 Current Project

## 📞 Customer Churn Prediction

My first end-to-end Machine Learning project.

### Problem

Telecommunication companies lose customers when they cancel their services. The goal of this project is to use customer information to predict whether a customer is likely to churn.

### Dataset

The project uses a Telco Customer Churn dataset containing **7,043 customer records and 21 columns**.

### 🔎 EDA Findings

Some interesting patterns discovered during EDA:

* The dataset contains approximately **73.5% non-churned and 26.5% churned customers**.
* Month-to-month customers have a significantly higher churn rate (~42.7%) compared with one-year (~11.3%) and two-year (~2.8%) contracts.
* Customers using electronic checks have a substantially higher churn rate (~45%).
* Fiber-optic customers have a much higher churn rate (~42%) compared with DSL (~19%).
* Customers who churn generally have shorter tenure.
* Customers who churn tend to have higher monthly charges.
* `TotalCharges` was stored as a string and required conversion to a numerical datatype.
* 11 missing `TotalCharges` values were identified and investigated; all corresponded to customers with zero tenure.

### ⚙️ ML Pipeline

```text
Raw Dataset
     ↓
Exploratory Data Analysis
     ↓
Data Cleaning
     ↓
Feature Engineering
     ↓
Train/Test Split
     ↓
Categorical Encoding + Feature Scaling
     ↓
Model Comparison and Hyperparameter Tuning
     ↓
Logistic Regression Pipeline
     ↓
Model Evaluation and Threshold Tuning (0.40)
     ↓
Coefficient Interpretation
     ↓
Save Model with Joblib
     ↓
Streamlit App and Deployment
```

### 🛠️ Technologies Used

* Python
* Pandas
* NumPy
* Matplotlib
* Seaborn
* Scikit-learn
* Joblib
* Streamlit
* Git & GitHub

### ✅ Project Status

**Completed and deployed**

The project includes preprocessing, model comparison, hyperparameter tuning, threshold tuning, Logistic Regression coefficient interpretation, and a saved Logistic Regression pipeline. The Streamlit app loads the saved model, predicts churn from raw customer inputs, and uses a decision threshold of **0.40**.

🚀 [Try the deployed Customer Churn Predictor](https://customer-churn-predictor-5cewbvfxsmjufenjrvdwxl.streamlit.app/)

---

# 📂 Repository Structure

```text
ml-learning-journey/
│
├── 01_Python/
│
├── 02_NumPy/
│
├── 03_Pandas/
│
├── 04_Matplotlib/
│
├── 05_Seaborn/
│
├── 06_EDA/
│
├── 07_Feature Engineering/
│
├── 08_Evaluation/
│
└── 09_Projects/
    │
    └── customer-churn-prediction/
        │
        ├── data/
        ├── models/
        │   ├── churn_model.pkl
        │   └── threshold.pkl
        ├── notebooks/
        │   ├── 01_eda.ipynb
        │   └── 02_preprocessing.ipynb
        ├── app.py
        ├── requirements.txt
        └── README.md
```

---

# 📈 Progress

| Area | Status |
| --- | :---: |
| Python | ✅ |
| Git & GitHub | ✅ |
| NumPy | ✅ |
| Pandas | ✅ |
| Matplotlib | ✅ |
| Seaborn | ✅ |
| EDA | ✅ |
| Feature Engineering | ✅ |
| Data Preprocessing | ✅ |
| Logistic Regression | ✅ |
| Model Evaluation | ✅ |
| Model Comparison | ✅ |
| Hyperparameter Tuning | ✅ |
| Streamlit | ✅ |
| Deployment | ✅ |
| ML Projects | ✅ |

---

# 🎯 What's Next?

My next focus is building more end-to-end projects and strengthening my understanding of the **complete ML development workflow**.

```text
Learn
  ↓
Experiment
  ↓
Build
  ↓
Evaluate
  ↓
Improve
  ↓
Deploy
  ↓
Repeat
```

The goal isn't to memorize every library or algorithm.

The goal is to become capable of taking a problem, working with real data, building an ML solution, evaluating it properly, and deploying it as a usable application.

---

## 💡 Why This Repository Exists

This repository is more than a collection of notebooks.

It is a public record of my progress toward becoming an ML Engineer.

I use it to document:

* Concepts I learn
* Experiments I perform
* Projects I build
* Mistakes and problems I encounter
* Solutions I discover
* Progress over time

Every meaningful commit represents another step forward.

---

## 🤝 Feedback

I'm still learning, so feedback on my code, projects, ML approach, and repository structure is always welcome.

If you find something that could be improved, feel free to open an issue or reach out.

⭐ If you find this journey interesting, consider giving the repository a star!
