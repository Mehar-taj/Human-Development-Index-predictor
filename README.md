# 🌍 Human Development Index (HDI) Predictor

> A Machine Learning web application that predicts the **Human Development Index (HDI)** of a country using **Life Expectancy, Mean Years of Schooling, Expected Years of Schooling, and Gross National Income (GNI) Per Capita**.

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python)
![Flask](https://img.shields.io/badge/Flask-Web%20Framework-black?logo=flask)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-Machine%20Learning-orange?logo=scikitlearn)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-blue?logo=pandas)
![NumPy](https://img.shields.io/badge/NumPy-Numerical%20Computing-blue?logo=numpy)
![License](https://img.shields.io/badge/License-Educational-green)

---

## 📖 Overview

The **Human Development Index (HDI)** is a composite index developed by the **United Nations Development Programme (UNDP)** to measure the overall development of a country.

It evaluates three important dimensions:

- 🏥 **Health** – Life Expectancy
- 🎓 **Education** – Mean Years of Schooling & Expected Years of Schooling
- 💰 **Standard of Living** – Gross National Income (GNI) Per Capita

This project applies **Machine Learning (Linear Regression)** to predict the HDI score based on these indicators and provides an interactive **Flask web application** for users.

---

# 🚀 Features

- Predict Human Development Index (HDI)
- Interactive Flask Web Application
- User-Friendly Interface
- Machine Learning Prediction
- Real-Time Prediction Results
- HDI Category Classification
- Responsive Design

---

# 🛠 Tech Stack

| Category | Technologies |
|----------|--------------|
| Programming Language | Python |
| Machine Learning | Scikit-learn |
| Data Analysis | Pandas, NumPy |
| Visualization | Matplotlib, Seaborn |
| Backend | Flask |
| Frontend | HTML5, CSS3 |
| Model Storage | Pickle |
| Version Control | Git & GitHub |

---

# 📊 Dataset Features

The model is trained using the following input features:

- Life Expectancy
- Mean Years of Schooling
- Expected Years of Schooling
- Gross National Income (GNI) Per Capita

### Output

- Predicted HDI Score

---

# 📈 HDI Classification

| HDI Score | Classification |
|-----------|---------------|
| 0.800 – 1.000 | Very High Human Development |
| 0.700 – 0.799 | High Human Development |
| 0.550 – 0.699 | Medium Human Development |
| Below 0.550 | Low Human Development |

---

# ⚙️ Machine Learning Workflow

```
Dataset Collection
        │
        ▼
Data Preprocessing
        │
        ▼
Exploratory Data Analysis
        │
        ▼
Feature Selection
        │
        ▼
Train/Test Split
        │
        ▼
Linear Regression Model
        │
        ▼
Model Evaluation
        │
        ▼
Model Serialization (.pkl)
        │
        ▼
Flask Web Application
        │
        ▼
HDI Prediction
```

---

# 📂 Project Structure

```
Human-Development-Index-Predictor
│
├── Dataset
│
├── Training
│   ├── HumDevIndex.ipynb
│   └── HDI.pkl
│
├── Flask
│   ├── app.py
│   ├── HDI.pkl
│   ├── templates
│   │   ├── home.html
│   │   ├── index.html
│   │   └── result.html
│   │
│   └── static
│       └── css
│           └── style.css
│
├── README.md
├── requirements.txt
└── .gitignore
```

---

# 🖥️ Application Screens

## 🏠 Home Page

> *(Insert Home Page Screenshot)*

---

## 📋 Prediction Page

> *(Insert Prediction Page Screenshot)*

---

## 📊 Prediction Result

> *(Insert Result Screenshot)*

---

# 🚀 Installation

## Clone the Repository

```bash
git clone https://github.com/Mehar-taj/Human-Development-Index-predictor.git
```

## Navigate to the Project

```bash
cd Human-Development-Index-predictor
```

## Install Dependencies

```bash
pip install -r requirements.txt
```

## Run the Flask Application

```bash
cd Flask
python app.py
```

Open your browser and visit:

```
http://127.0.0.1:5000
```

---

# 💡 Future Enhancements

- 🌍 Country Selection
- 📊 Interactive Charts
- 📈 Compare Multiple ML Models
- ☁️ Cloud Deployment
- 📱 Mobile-Friendly Interface
- 🗄️ Prediction History

---

# 📚 Learning Outcomes

This project helped me gain practical experience in:

- Machine Learning
- Data Preprocessing
- Exploratory Data Analysis
- Linear Regression
- Model Evaluation
- Flask Web Development
- HTML & CSS
- Git & GitHub
- End-to-End ML Project Development

---

# 👨‍💻 Author

**Mehar Taj**

Machine Learning Project

SmartBridge Program

GitHub: https://github.com/Mehar-taj

---

# ⭐ If you found this project useful, consider giving it a star!