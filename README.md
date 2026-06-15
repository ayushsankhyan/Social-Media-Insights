# 📊 Social Media Insights Through Big Data Analytics

An AI-powered emotion prediction and social media analytics system that leverages Machine Learning, Big Data Analytics, and interactive visualization techniques to analyze user engagement patterns and predict emotional states across different social media platforms.

---

## 🚀 Project Overview

The rapid growth of social media platforms has generated massive amounts of user-generated data. Understanding user behavior, engagement trends, and emotional responses has become increasingly important for businesses, researchers, and platform developers.

This project applies Big Data Analytics and Machine Learning techniques to analyze social media interactions and predict user emotions based on activity patterns such as posting frequency, likes, comments, messaging behavior, and platform usage.

Using an XGBoost Classifier integrated within a Scikit-Learn Pipeline, the system achieved approximately **98% classification accuracy** in predicting user emotions.

---

## 🎯 Objectives

* Analyze social media engagement patterns.
* Predict dominant user emotions using Machine Learning.
* Identify platform-specific emotional trends.
* Understand the relationship between user engagement and emotional well-being.
* Build an end-to-end deployable AI application.

---

## 📂 Dataset

Source: Kaggle Social Media Usage Dataset

### Features Used

| Feature                   | Description                     |
| ------------------------- | ------------------------------- |
| Age                       | User age                        |
| Gender                    | User gender                     |
| Platform                  | Social media platform used      |
| Daily Usage Time          | Daily usage duration in minutes |
| Posts Per Day             | Number of posts created daily   |
| Likes Received Per Day    | Average likes received          |
| Comments Received Per Day | Average comments received       |
| Messages Sent Per Day     | Average messages sent           |

### Target Variable

* Anger
* Anxiety
* Boredom
* Happiness
* Neutral
* Sadness

---

## ⚙️ Project Workflow

### 1. Data Collection

* Imported dataset from Kaggle
* Performed initial exploration and inspection

### 2. Data Preprocessing

* Missing value handling
* Feature selection
* Data cleaning
* Data validation

### 3. Exploratory Data Analysis (EDA)

* User behavior analysis
* Platform usage trends
* Emotion distribution analysis
* Correlation analysis

### 4. Feature Engineering

* Numerical feature scaling using StandardScaler
* Categorical feature encoding using OneHotEncoder

### 5. Model Development

Built a Scikit-Learn Pipeline consisting of:

Data Input

↓
ColumnTransformer

↓
StandardScaler + OneHotEncoder

↓
XGBoost Classifier

↓
Emotion Prediction

### 6. Model Evaluation

Performance Metrics:

* Accuracy Score
* Precision
* Recall
* F1 Score
* Classification Report

### Results

✅ Accuracy: ~98%

---

## 🤖 Machine Learning Model

### XGBoost Classifier

XGBoost was selected because:

* High predictive performance
* Handles complex relationships effectively
* Robust against overfitting
* Excellent performance on tabular datasets

---

## 🌐 Streamlit Web Application

The project includes a fully interactive Streamlit application that allows users to:

* Enter social media activity metrics
* Predict emotional state in real time
* Explore project insights
* Understand social media engagement patterns

### User Inputs

* Age
* Gender
* Platform
* Daily Usage Time
* Posts Per Day
* Likes Received Per Day
* Comments Received Per Day
* Messages Sent Per Day

### Output

Predicted Emotion:

* Happiness
* Neutral
* Sadness
* Anger
* Anxiety
* Boredom

---

## 📈 Key Findings

### Platform Analysis

* Instagram interactions are predominantly associated with Happiness.
* Twitter users show higher levels of Anger and Sadness.
* WhatsApp usage demonstrates mixed emotional patterns.

### Engagement Analysis

* Moderate engagement correlates with positive emotional states.
* Excessive social media usage may contribute to Anxiety.
* User interaction patterns significantly influence emotional predictions.

---

## 🛠️ Technologies Used

### Programming

* Python

### Machine Learning

* XGBoost
* Scikit-Learn

### Data Analysis

* Pandas
* NumPy

### Visualization

* Matplotlib
* Seaborn

### Deployment

* Streamlit

### Model Persistence

* Joblib

### Version Control

* Git
* GitHub

---

## 📁 Project Structure

```text
social-media-insights/
│
├── app.py
├── emotion_model.pkl
├── label_encoder.pkl
├── requirements.txt
├── README.md
│
└── notebooks/
```

---

## 🔮 Future Enhancements

* Real-time social media API integration
* Sentiment analysis using NLP
* Deep Learning-based emotion prediction
* Interactive analytics dashboard
* User behavior recommendation system
* Multi-platform data streaming

---

## 📚 Research Contribution

This project forms part of research work in Social Media Analytics and Artificial Intelligence and contributes toward understanding emotional behavior through data-driven methodologies.

---

## 👨‍💻 Author

Ayush Sankhyan

B.E. Computer Science Engineering (Hons.)
Specialization: Artificial Intelligence & Machine Learning

Chandigarh University

Email: [sankhyanayush95@gmail.com](mailto:sankhyanayush95@gmail.com)

---

## ⭐ If you found this project useful, consider giving it a star on GitHub.
