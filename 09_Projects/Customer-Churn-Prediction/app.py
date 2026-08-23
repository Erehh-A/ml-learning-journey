"""Streamlit interface for the Telco Customer Churn prediction pipeline."""

from pathlib import Path

import joblib
import pandas as pd
import streamlit as st


# -------------------------------------------------
# Page setup
# -------------------------------------------------
st.set_page_config(
    page_title="Customer Churn Predictor",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="collapsed",
)

st.markdown("""
<style>
    .block-container {
        max-width: 1100px;
        padding-top: 2.5rem;
        padding-bottom: 3rem;
    }

    h1 {
        font-size: 2.4rem !important;
        margin-bottom: 0.2rem;
    }

    div[data-testid="stForm"] {
        border: 1px solid #334155;
        border-radius: 14px;
        padding: 22px;
    }

    div[data-testid="stMetric"] {
        background-color: #1e293b;
        border: 1px solid #334155;
        border-radius: 12px;
        padding: 16px;
    }

    .stButton > button {
        width: 100%;
        border-radius: 9px;
        font-weight: 600;
        padding: 0.55rem;
    }
</style>
""", unsafe_allow_html=True)


# -------------------------------------------------
# Project settings
# -------------------------------------------------
APP_DIR = Path(__file__).resolve().parent
DEFAULT_THRESHOLD = 0.40

# These are the raw fields from the Telco Customer Churn dataset.
FIELD_ORDER = [
    "gender",
    "SeniorCitizen",
    "Partner",
    "Dependents",
    "tenure",
    "PhoneService",
    "MultipleLines",
    "InternetService",
    "OnlineSecurity",
    "OnlineBackup",
    "DeviceProtection",
    "TechSupport",
    "StreamingTV",
    "StreamingMovies",
    "Contract",
    "PaperlessBilling",
    "PaymentMethod",
    "MonthlyCharges",
    "TotalCharges",
]


def find_artifact(filename: str) -> Path | None:
    """Find a model artifact in common project locations."""
    for folder in (APP_DIR / "models", APP_DIR / "model", APP_DIR):
        candidate = folder / filename

        if candidate.exists():
            return candidate

    return None


@st.cache_resource
def load_artifacts():
    """Load the trained model pipeline and decision threshold."""
    model_path = find_artifact("churn_model.pkl")

    if model_path is None:
        raise FileNotFoundError(
            "Could not find churn_model.pkl. "
            "Place it inside the models folder."
        )

    model = joblib.load(model_path)

    threshold_path = find_artifact("threshold.pkl")

    if threshold_path is not None:
        threshold = float(joblib.load(threshold_path))
    else:
        threshold = DEFAULT_THRESHOLD

    return model, threshold, model_path, threshold_path


def prediction_features(model) -> list[str]:
    """Get the feature names expected by the trained pipeline."""
    learned_features = getattr(model, "feature_names_in_", None)

    if learned_features is None:
        return FIELD_ORDER

    return list(learned_features)


def positive_class_index(model) -> int:
    """Find which predict_proba column represents churn."""
    classes = list(getattr(model, "classes_", []))

    for positive_label in (1, "Yes", "yes", True):
        if positive_label in classes:
            return classes.index(positive_label)

    # Standard fallback for a binary 0 / 1 classification model.
    return 1


def make_customer_row(values: dict, expected_features: list[str]) -> pd.DataFrame:
    """Create one customer row in exactly the order expected by the model."""
    missing = [
        column for column in expected_features
        if column not in values
    ]

    if missing:
        raise ValueError(
            "The app has no input configured for: "
            + ", ".join(missing)
        )

    return pd.DataFrame([
        {column: values[column] for column in expected_features}
    ])


# -------------------------------------------------
# App header
# -------------------------------------------------
st.title("📊 Customer Churn Predictor")
st.caption(
    "Enter customer details to estimate the likelihood of churn."
)
st.divider()


# -------------------------------------------------
# Load saved model
# -------------------------------------------------
try:
    best_model, final_threshold, model_path, threshold_path = load_artifacts()

except Exception as error:
    st.error("The trained model could not be loaded.")
    st.code(str(error))
    st.info(
        "Check that `churn_model.pkl` and `threshold.pkl` "
        "are inside the `models` folder."
    )
    st.stop()


expected_features = prediction_features(best_model)

unknown_features = [
    feature for feature in expected_features
    if feature not in FIELD_ORDER
]

if unknown_features:
    st.error(
        "This model expects fields the app does not know how to collect: "
        + ", ".join(unknown_features)
    )
    st.stop()


# -------------------------------------------------
# Customer input form
# -------------------------------------------------
with st.form("customer_form"):
    st.subheader("Customer information")
    st.caption("Complete the fields below, then select Predict churn.")

    left, middle, right = st.columns(3)

    with left:
        gender = st.selectbox("Gender", ["Female", "Male"])

        senior_citizen = st.selectbox(
            "Senior citizen",
            [0, 1],
            format_func=lambda value: "Yes" if value else "No",
        )

        partner = st.selectbox("Partner", ["No", "Yes"])
        dependents = st.selectbox("Dependents", ["No", "Yes"])

        tenure = st.number_input(
            "Tenure (months)",
            min_value=0,
            max_value=120,
            value=12,
            step=1,
        )

        phone_service = st.selectbox(
            "Phone service",
            ["Yes", "No"],
        )

        multiple_lines = st.selectbox(
            "Multiple lines",
            ["No", "Yes", "No phone service"],
        )

    with middle:
        internet_service = st.selectbox(
            "Internet service",
            ["DSL", "Fiber optic", "No"],
        )

        online_security = st.selectbox(
            "Online security",
            ["No", "Yes", "No internet service"],
        )

        online_backup = st.selectbox(
            "Online backup",
            ["No", "Yes", "No internet service"],
        )

        device_protection = st.selectbox(
            "Device protection",
            ["No", "Yes", "No internet service"],
        )

        tech_support = st.selectbox(
            "Tech support",
            ["No", "Yes", "No internet service"],
        )

        streaming_tv = st.selectbox(
            "Streaming TV",
            ["No", "Yes", "No internet service"],
        )

        streaming_movies = st.selectbox(
            "Streaming movies",
            ["No", "Yes", "No internet service"],
        )

    with right:
        contract = st.selectbox(
            "Contract",
            ["Month-to-month", "One year", "Two year"],
        )

        paperless_billing = st.selectbox(
            "Paperless billing",
            ["Yes", "No"],
        )

        payment_method = st.selectbox(
            "Payment method",
            [
                "Electronic check",
                "Mailed check",
                "Bank transfer (automatic)",
                "Credit card (automatic)",
            ],
        )

        monthly_charges = st.number_input(
            "Monthly charges ($)",
            min_value=0.0,
            max_value=200.0,
            value=70.0,
            step=0.5,
        )

        total_charges = st.number_input(
            "Total charges ($)",
            min_value=0.0,
            max_value=20000.0,
            value=840.0,
            step=1.0,
        )

    submitted = st.form_submit_button(
        "Predict churn",
        type="primary",
    )


# -------------------------------------------------
# Prediction result
# -------------------------------------------------
if submitted:
    customer_values = {
        "gender": gender,
        "SeniorCitizen": senior_citizen,
        "Partner": partner,
        "Dependents": dependents,
        "tenure": int(tenure),
        "PhoneService": phone_service,
        "MultipleLines": multiple_lines,
        "InternetService": internet_service,
        "OnlineSecurity": online_security,
        "OnlineBackup": online_backup,
        "DeviceProtection": device_protection,
        "TechSupport": tech_support,
        "StreamingTV": streaming_tv,
        "StreamingMovies": streaming_movies,
        "Contract": contract,
        "PaperlessBilling": paperless_billing,
        "PaymentMethod": payment_method,
        "MonthlyCharges": float(monthly_charges),
        "TotalCharges": float(total_charges),
    }

    customer = make_customer_row(
        customer_values,
        expected_features,
    )

    churn_probability = float(
        best_model.predict_proba(customer)[
            0,
            positive_class_index(best_model),
        ]
    )

    prediction = churn_probability >= final_threshold

    st.divider()
    st.subheader("Prediction result")

    first, second = st.columns(2)

    first.metric(
        "Churn probability",
        f"{churn_probability:.1%}",
    )

    second.metric(
        "Decision threshold",
        f"{final_threshold:.0%}",
    )

    st.progress(churn_probability)

    if prediction:
        st.error("Likely to churn")
        st.caption(
            "The churn probability meets or exceeds "
            "the selected decision threshold."
        )
    else:
        st.success("Unlikely to churn")
        st.caption(
            "The churn probability is below "
            "the selected decision threshold."
        )

    with st.expander("View data sent to the model"):
        st.dataframe(customer, use_container_width=True)