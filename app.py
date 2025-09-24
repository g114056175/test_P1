import streamlit as st
import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# --- 1. Core Modeling Function ---
def solve_simple_linear_regression(x_data, y_data):
    """
    Receives a set of X and Y data, calculates and returns the slope (m) and intercept (c).
    """
    x = np.array(x_data)
    y = np.array(y_data)

    mean_x = np.mean(x)
    mean_y = np.mean(y)

    numerator = np.sum((x - mean_x) * (y - mean_y))
    denominator = np.sum((x - mean_x)**2)
    
    # Handle case where denominator is zero to avoid division errors
    if denominator == 0:
        return 0, mean_y

    m = numerator / denominator
    c = mean_y - m * mean_x

    return m, c

# --- 2. Streamlit App UI ---
st.set_page_config(layout="wide")
st.title("HW1: Interactive Simple Linear Regression")
st.markdown("This application demonstrates Simple Linear Regression by allowing you to generate data and see how a model fits a line to it.")

# --- 3. Sidebar for User Inputs ---
with st.sidebar:
    st.header("Data Generation Parameters")
    
    # Sliders and number inputs for user to modify parameters
    true_a = st.slider("True Slope (a)", min_value=-10.0, max_value=10.0, value=2.0, step=0.1)
    true_b = st.slider("True Intercept (b)", min_value=-20.0, max_value=20.0, value=5.0, step=0.5)
    num_points = st.slider("Number of Points", min_value=10, max_value=500, value=100, step=10)
    noise_level = st.slider("Noise Level", min_value=0.0, max_value=20.0, value=2.0, step=0.5)

# --- 4. Data Generation ---
# Generate a sequence of X values
X_values = np.linspace(0, 40, num_points)

# Generate Y values based on the linear equation and add noise
y_true = true_a * X_values + true_b
y_noisy = y_true + np.random.randn(num_points) * noise_level

# Create a DataFrame for easy handling
data_df = pd.DataFrame({
    'X': X_values,
    'Y_Noisy': y_noisy,
    'Y_True': y_true
})

# --- 5. Modeling ---
# Solve for the best-fit line using our function
model_m, model_c = solve_simple_linear_regression(data_df['X'], data_df['Y_Noisy'])

# Generate the predicted Y values from our model
data_df['Y_Model'] = model_m * data_df['X'] + model_c


# --- 6. Evaluation & Visualization ---
col1, col2 = st.columns([0.6, 0.4]) # Create two columns for plot and results

with col1:
    st.subheader("Regression Plot")
    
    # Create a scatter plot of the noisy data
    fig = px.scatter(data_df, x='X', y='Y_Noisy', labels={'Y_Noisy': 'Data Points'})

    # Add the "Ground Truth" line
    fig.add_trace(go.Scatter(x=data_df['X'], y=data_df['Y_True'], mode='lines', name='Ground Truth Line', line=dict(color='green', width=3)))

    # Add the "Model Fit" line
    fig.add_trace(go.Scatter(x=data_df['X'], y=data_df['Y_Model'], mode='lines', name='Model Fit Line', line=dict(color='red', dash='dash', width=3)))
    
    fig.update_layout(
        legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1)
    )
    
    st.plotly_chart(fig, use_container_width=True)

with col2:
    st.subheader("Evaluation")
    st.markdown("Comparing the true parameters used to generate the data with the parameters calculated by the regression model.")
    
    st.markdown("---")
    
    # Display metrics
    eval_col1, eval_col2 = st.columns(2)
    with eval_col1:
        st.metric(label="True Slope (a)", value=f"{true_a:.2f}")
        st.metric(label="Model Slope (m)", value=f"{model_m:.2f}", delta=f"{(model_m - true_a):.2f}")
    
    with eval_col2:
        st.metric(label="True Intercept (b)", value=f"{true_b:.2f}")
        st.metric(label="Model Intercept (c)", value=f"{model_c:.2f}", delta=f"{(model_c - true_b):.2f}")

st.markdown("---")
st.subheader("Generated Data")
st.dataframe(data_df[['X', 'Y_Noisy']].head())
