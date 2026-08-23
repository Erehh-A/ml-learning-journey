# Telco Customer Churn Predictor

A beginner-friendly Streamlit web app that uses a previously trained scikit-learn Logistic Regression pipeline to estimate whether a Telco customer is likely to churn.

The app does **not** retrain the model. It loads the saved pipeline, sends it one raw customer row, gets a churn probability, and applies the project decision threshold of **0.40**.

## Live Demo

[Try the Customer Churn Predictor](https://customer-churn-predictor-5cewbvfxsmjufenjrvdwxl.streamlit.app/)

## App Preview

![Customer Churn Predictor](images/first.png)
![Customer Churn Predictor](images/second.png)

## Project layout

```text
.
├── app.py
├── requirements.txt
├── README.md
├── models/
│   ├── churn_model.pkl       # required: saved best_model pipeline
│   └── threshold.pkl         # optional: saved threshold (0.40 is the fallback)
└── notebooks/                # keep your training / EDA notebooks here
```

## First-time setup

1. Create the `models` folder.
2. Copy the artifacts saved from the training notebook into it:

   ```python
   joblib.dump(best_model, "models/churn_model.pkl")
   joblib.dump(0.4, "models/threshold.pkl")
   ```

   `best_model` must be the whole pipeline: preprocessing plus Logistic Regression. Do not save only the classifier.

3. Install the packages:

   ```bash
   pip install -r requirements.txt
   ```

4. Start the app:

   ```bash
   streamlit run app.py
   ```

## How a prediction works

```text
Form inputs → one-row pandas DataFrame → saved preprocessing pipeline
            → Logistic Regression probability → threshold (0.40) → result
```

The app collects the standard raw Telco fields and then uses the column names stored by the loaded pipeline. This protects the app from mismatched feature order and lets it work with a saved model variant that expects fewer fields.

## Concepts to understand

- **Inference:** using a trained model on a new customer. There is no `.fit()` in the app.
- **Pipeline:** the saved object contains the original preprocessing (scaling and one-hot encoding) and the classifier, so the app supplies raw values such as `"Fiber optic"`.
- **DataFrame:** the `[value]` wrapping used in a notebook becomes one DataFrame row here; models expect a table-shaped input even for one customer.
- **Probability vs. decision:** the model returns a number from 0 to 1. The project rule converts it to churn/not-churn using `probability >= 0.40`.

## Note on input fields

The common IBM Telco dataset has 19 usable raw input columns after removing `customerID` and `Churn`. If your final pipeline was trained with a reduced set (for example, 17 columns), the app automatically sends only the exact columns stored in that pipeline.
