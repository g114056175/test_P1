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
3.  **Hosting:** The project code is hosted on GitHub at the specified repository: [https://github.com/g114056175/test_P1](https://github.com/g114056175/test_P1).
4.  **Execution:** The application can be run locally by executing `streamlit run app.py` in the terminal. It can also be deployed to cloud services like Streamlit Community Cloud for public access.

**Live Demo URL:** [https://testp1-3kmuvihdleeochorrzz28s.streamlit.app/](https://testp1-3kmuvihdleeochorrzz28s.streamlit.app/)

---

## 開發歷程 (Prompt-Response Development Log)

本專案是透過與 Gemini AI 互動，以下達指令 (Prompt) 的方式逐步建構完成。以下記錄了主要的「使用者指令」與「AI 回應摘要」。

### 1. 專案啟動與需求定義

**使用者指令:**
> "說明這個作業 HW1: write python to solve simple linear reg"，並隨後補充： "1. CRISP-DM 2. allow user to modify a in ax+b, noise, number of points 3. streamlit or flask web, 框架 deployment..."

**AI 回應摘要:**
> 理解使用者需要建立一個包含前端互動、後端演算法、並遵循 CRISP-DM 框架的網頁應用。計畫選擇 Streamlit 作為前端框架，並規劃了 `README.md` (遵循 CRISP-DM), `app.py` (應用程式碼), `requirements.txt` (相依性) 三個核心檔案的結構。首先，建立了符合 CRISP-DM 結構的 `README.md`。

### 2. 核心應用程式開發

**使用者指令:**
> (在 README.md 建立後，隱含的下一步)

**AI 回應摘要:**
> 接著，編寫了 `app.py` 的完整程式碼，實現了：
> 1.  使用 Streamlit 建構互動式側邊欄，讓使用者能調整真實的斜率、截距、資料點數量與雜訊大小。
> 2.  根據使用者輸入即時生成資料。
> 3.  實作 `solve_simple_linear_regression` 函數來計算模型的最佳擬合線。
> 4.  使用 Plotly 視覺化，同時呈現資料散佈點、真實線與模型擬合線。
> 最後，建立了 `requirements.txt` 檔案以定義專案的相依性。

### 3. 專案檔案同步至 GitHub

**使用者指令:**
> "幫我做這些步驟 將vscode 同步到我的github 倉庫"

**AI 回應摘要:**
> 根據使用者先前提供的 GitHub 倉庫資訊，執行了 `git remote set-url`, `git add`, `git commit`, `git push` 等一系列指令，將本地建立的所有專案檔案首次同步上傳到使用者的 GitHub 倉庫。

### 4. 部署上線與修正

**使用者指令:**
> "似乎無法看到如https://aiotda.streamlit.app/ 的demo... (README 中的連結也是錯誤的)"

**AI 回應摘要:**
> 向使用者解釋了「程式碼託管 (GitHub)」與「應用程式部署 (Streamlit Cloud)」的區別，並提供了在 Streamlit 平台上部署的詳細步驟。同時，修正了 `README.md` 中錯誤的 GitHub 倉庫連結，並將修正同步到 GitHub。

### 5. 完成部署並更新文件

**使用者指令:**
> "在streamlit 上用完了 連結為 https://.../ 幫我修改本地vscode內的檔案 如readme的說明並同步到github"

**AI 回應摘要:**
> 將使用者提供成功的 Streamlit Live Demo 連結，更新至 `README.md` 的「Deployment」章節中，並將此最終更新同步到 GitHub。

### 6. 最終文件整理

**使用者指令:**
> "從作業開始後的prompt作簡單整理，僅保留對於作業有關聯的題詞(去除修正bug、對專業知識的提問)，並給我agent所做的大致步驟說明。"

**AI 回應摘要:**
> 接收到使用者對於文件記錄的精煉化要求。重新整理了整個開發歷程，合併、刪減了部分指令，並在每個使用者指令後方，詳細補充了 AI 的處理步驟摘要，最終形成前述的「Prompt-回應」開發日誌，並將此最終版本同步至 GitHub。