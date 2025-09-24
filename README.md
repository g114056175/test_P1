# HW1: Interactive Simple Linear Regression Web App

This project is an interactive web application that demonstrates the principles of Simple Linear Regression. Users can dynamically generate a dataset by specifying parameters like slope, intercept, noise, and the number of data points. The application then calculates the best-fit line using the Ordinary Least Squares (OLS) method and visualizes both the original data and the model's regression line.

This project follows the CRISP-DM (Cross-Industry Standard Process for Data Mining) methodology.

---

## CRISP-DM Framework

### 1. Business Understanding
**Objective:** The primary goal is to create an educational tool for understanding Simple Linear Regression.
**Business Need:** Aspiring data scientists and students often learn the theory of linear regression but lack an intuitive, interactive way to see how parameters affect the model. This tool aims to bridge that gap by allowing users to:
- Visualize the relationship between a ground-truth line and a model-fitted line.
- Understand the impact of noise on the model's accuracy.
- See how the number of data points influences the reliability of the regression model.

### 2. Data Understanding
The data for this project is synthetically generated based on user inputs. This allows for a controlled environment to study the regression algorithm.
- **Data Source:** Generated in real-time by the application.
- **Data Attributes:**
    - **X (Independent Variable):** A sequence of numbers, typically ranging from 0 to a specified maximum.
    - **Y (Dependent Variable):** Generated based on the linear equation `Y = aX + b + noise`.
- **User-controlled Parameters:**
    - `a`: The true slope of the line.
    - `b`: The true intercept of the line.
    - `Noise`: The magnitude of random, normally distributed noise added to each data point.
    - `Number of Points`: The total number of data points to generate.

### 3. Data Preparation
Since the data is synthetic, the preparation process is straightforward.
1.  **Generate X values:** A simple array of numbers is created (e.g., from 0 to N-1).
2.  **Generate Y values:** The core preparation step involves applying the linear equation with noise:
    ```
    y_true = (a * x) + b
    y_noisy = y_true + (random_normal_values * noise_level)
    ```
    This creates a dataset that mimics real-world data, which rarely fits a perfect line.
3.  **Structure Data:** The generated X and Y values are typically stored in a Pandas DataFrame for easy manipulation and plotting.

### 4. Modeling
**Model Selection:** The model chosen is **Simple Linear Regression**, implemented from scratch using the Ordinary Least Squares (OLS) method.
**Implementation:** The algorithm calculates the optimal slope (`m`) and intercept (`c`) that minimize the sum of the squared differences between the actual Y values (`y_noisy`) and the values predicted by the model.
The formulas used are:
- **Slope (m):** `m = Σ((xᵢ - mean(x)) * (yᵢ - mean(y))) / Σ((xᵢ - mean(x))²)`
- **Intercept (c):** `c = mean(y) - m * mean(x)`
This calculation is implemented in a dedicated Python function within the application.

### 5. Evaluation
The model's performance is evaluated both quantitatively and qualitatively:
- **Quantitative Evaluation:** The application displays the "true" parameters (`a`, `b`) alongside the parameters calculated by the model (`m`, `c`). The user can directly compare them to see how well the model recovered the original line's characteristics.
- **Qualitative (Visual) Evaluation:** The application plots:
    - A scatter plot of the generated data points (`x`, `y_noisy`).
    - The "ground truth" line in one color (using `a` and `b`).
    - The model's fitted regression line in another color (using `m` and `c`).
    This visualization provides an immediate, intuitive understanding of the model's fit.

### 6. Deployment
**Framework:** The application is developed and deployed as a web application using the **Streamlit** framework.
**Deployment Steps:**
1.  **Code:** The entire application is contained within a single Python script (`app.py`).
2.  **Dependencies:** All required libraries are listed in `requirements.txt`.
3.  **Hosting:** The project code is hosted on GitHub at the specified repository: [https://github.com/huanchen1107/20250920_AutoDepl]https://github.com/g114056175/test_P1).
4.  **Execution:** The application can be run locally by executing `streamlit run app.py` in the terminal. It can also be deployed to cloud services like Streamlit Community Cloud for public access.

**Live Demo URL:** [https://testp1-3kmuvihdleeochorrzz28s.streamlit.app/](https://testp1-3kmuvihdleeochorrzz28s.streamlit.app/)

