# 🌍 Human Development Index (HDI) Predictor

A Machine Learning-based web application that predicts the **Human Development Index (HDI)** score of a country using **Life Expectancy, Mean Years of Schooling, Expected Years of Schooling, and Gross National Income (GNI) Per Capita**.

This project was developed using **Python, Scikit-learn, Flask, HTML, CSS, and Machine Learning** as part of the **SmartBridge Machine Learning Program**.

---

## 📌 Project Overview

The Human Development Index (HDI) is a composite statistic developed by the United Nations to measure the overall development of a country. It considers three major dimensions:

- 🏥 Health (Life Expectancy)
- 🎓 Education (Mean & Expected Years of Schooling)
- 💰 Standard of Living (GNI Per Capita)

This application predicts the HDI score using a trained **Linear Regression** model and classifies the country's development level.

---

## ✨ Features

- Predict Human Development Index (HDI) Score
- Classify Development Level
- Interactive Flask Web Application
- User-friendly Interface
- Machine Learning Model using Linear Regression
- Fast and Accurate Predictions

---

## 🛠 Technologies Used

- Python
- Flask
- NumPy
- Pandas
- Matplotlib
- Seaborn
- Scikit-learn
- HTML
- CSS
- Pickle

---

## 📊 Machine Learning Workflow

1. Dataset Collection
2. Data Preprocessing
3. Exploratory Data Analysis (EDA)
4. Feature Selection
5. Train-Test Split
6. Linear Regression Model Training
7. Model Evaluation
8. Model Serialization using Pickle
9. Flask Web Application Deployment

---

## 📥 Input Parameters

The user provides the following values:

- Life Expectancy
- Mean Years of Schooling
- Expected Years of Schooling
- Gross National Income (GNI) Per Capita

---

## 📤 Output

The application predicts:

- HDI Score

It also classifies the country into one of the following categories:

| HDI Score | Category |
|-----------|----------|
| 0.800 – 1.000 | Very High Human Development |
| 0.700 – 0.799 | High Human Development |
| 0.550 – 0.699 | Medium Human Development |
| Below 0.550 | Low Human Development |

---

## 📂 Project Structure

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
├── requirements.txt
├── README.md
└── .gitignore
```

---

## 🚀 Installation

### Clone the Repository

```bash
git clone https://github.com/Mehar-taj/Human-Development-Index-predictor.git
```

### Navigate to the Project

```bash
cd Human-Development-Index-predictor
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run the Flask Application

```bash
cd Flask
python app.py
```

### Open in Browser

```
http://127.0.0.1:5000
```

---

## 📸 Application Screenshots

### Home Page

(Add Screenshot Here)

### Prediction Page

(Add Screenshot Here)

### Result Page

(Add Screenshot Here)

---

## 🎯 Future Enhancements

- Bootstrap-based Responsive UI
- Country Selection Feature
- Interactive Data Visualization
- Model Comparison with Multiple Algorithms
- Cloud Deployment
- Prediction History

---

## 🎓 Learning Outcomes

Through this project, I learned:

- Data Preprocessing
- Exploratory Data Analysis
- Machine Learning with Linear Regression
- Model Serialization using Pickle
- Flask Web Development
- HTML & CSS Integration
- Git and GitHub Version Control

---

## 👨‍💻 Author

**Mehar Taj**

Machine Learning Project

SmartBridge Program

---

## 📄 License

This project is developed for educational purposes under the SmartBridge Machine Learning Program.