# 📊 Social Media Insights Through Big Data Analytics

[![Live Demo](https://img.shields.io/badge/Live-Demo-success)](https://sentiment-prediction-through-social-media-insights-nxqd2niyr4c.streamlit.app/)

## 🚀 Live Application

**Try the deployed application here:**

https://sentiment-prediction-through-social-media-insights-nxqd2niyr4c.streamlit.app/

---

## 📌 Project Overview

Social media platforms generate massive volumes of user-generated content every day. Understanding user engagement patterns and emotional responses can help businesses, researchers, and platform developers make better data-driven decisions.

This project leverages **Machine Learning**, **Big Data Analytics**, and **Social Media Intelligence** to predict user emotions based on social media activity patterns.

Using an **XGBoost Classifier** integrated into a Scikit-Learn Pipeline, the model analyzes user behavior across different platforms and predicts emotional states such as:

* 😊 Happiness
* 😐 Neutral
* 😢 Sadness
* 😠 Anger
* 😰 Anxiety
* 😴 Boredom

The project has been deployed as a live interactive web application using **Streamlit**.

---

## 🎯 Objectives

* Analyze social media engagement behavior.
* Predict user emotions using Machine Learning.
* Identify platform-specific emotional trends.
* Study the relationship between engagement and emotional well-being.
* Build and deploy a real-world AI application.

---

## 🌐 Live Demo

### Application Link

👉 https://sentiment-prediction-through-social-media-insights-nxqd2niyr4c.streamlit.app/

Users can:

* Enter social media activity metrics
* Predict emotional states in real time
* Explore social media analytics insights
* Understand behavioral engagement patterns

---

## 📂 Dataset

### Source

Kaggle Social Media Usage Dataset

### Features Used

| Feature                    | Description                |
| -------------------------- | -------------------------- |
| Age                        | User age                   |
| Gender                     | User gender                |
| Platform                   | Social media platform      |
| Daily Usage Time (minutes) | Time spent on social media |
| Posts Per Day              | Daily posting activity     |
| Likes Received Per Day     | Daily likes received       |
| Comments Received Per Day  | Daily comments received    |
| Messages Sent Per Day      | Daily messages sent        |

### Target Variable

Emotion Categories:

* Anger
* Anxiety
* Boredom
* Happiness
* Neutral
* Sadness

---

## ⚙️ Machine Learning Workflow

### 1️⃣ Data Collection

* Dataset acquisition from Kaggle
* Initial data inspection and validation

### 2️⃣ Data Preprocessing

* Data cleaning
* Missing value handling
* Feature selection
* Data preparation

### 3️⃣ Exploratory Data Analysis (EDA)

* Platform usage analysis
* User behavior analysis
* Emotion distribution analysis
* Correlation analysis

### 4️⃣ Feature Engineering

Categorical Features:

* Gender
* Platform

Numerical Features:

* Age
* Daily Usage Time
* Posts Per Day
* Likes Received Per Day
* Comments Received Per Day
* Messages Sent Per Day

### 5️⃣ Data Transformation

Implemented using:

* StandardScaler
* OneHotEncoder
* ColumnTransformer

### 6️⃣ Model Training

Model Used:

**XGBoost Classifier**

Reasons for Selection:

* High predictive performance
* Efficient handling of structured datasets
* Strong generalization capability
* Robust against overfitting

### 7️⃣ Deployment

The trained model was deployed using:

* Streamlit
* GitHub
* Streamlit Community Cloud

---

## 🏗️ Project Architecture

```text
User Input
     ↓
Streamlit Frontend
     ↓
Scikit-Learn Pipeline
     ↓
Preprocessing Layer
     ↓
(StandardScaler + OneHotEncoder)
     ↓
XGBoost Classifier
     ↓
Emotion Prediction
```

---

## 📈 Model Performance

| Metric     | Score                 |
| ---------- | --------------------- |
| Model      | XGBoost Classifier    |
| Accuracy   | ~98%                  |
| Classes    | 6                     |
| Pipeline   | Scikit-Learn Pipeline |
| Deployment | Streamlit Cloud       |

---

## 🔍 Key Findings

### Platform-Based Trends

✅ Instagram interactions are predominantly associated with happiness.

✅ Twitter users show higher occurrences of anger and sadness.

✅ WhatsApp usage demonstrates mixed emotional patterns.

### Engagement Insights

✅ Moderate engagement correlates with positive emotional states.

✅ Excessive social media activity may contribute to anxiety.

✅ User engagement metrics significantly influence emotional prediction outcomes.

---

## 🖥️ Application Features

### Emotion Prediction

Predict emotional state based on:

* Age
* Gender
* Platform
* Usage behavior
* Interaction metrics

### Automated Preprocessing

* Feature scaling
* Categorical encoding
* Pipeline-based transformation

### Real-Time Prediction

* Instant predictions
* User-friendly interface
* Interactive web deployment

---

## 🛠️ Technologies Used

### Programming Language

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
Sentiment-Prediction-Through-Social-Media-Insights
│
├── app.py
├── emotion_model.pkl
├── label_encoder.pkl
├── requirements.txt
├── runtime.txt
├── README.md
└── .gitignore
```

---

## 🔮 Future Enhancements

* Real-time social media API integration
* NLP-based sentiment analysis
* Deep Learning emotion classification
* Interactive analytics dashboard
* Recommendation engine
* Multi-platform behavioral tracking

---

## 📚 Research Contribution

This project contributes to research in:

* Social Media Analytics
* Artificial Intelligence
* Machine Learning
* Big Data Analytics
* Emotion Classification

### Conference Publication

Research work associated with this project has been submitted/presented at:

**STAI 2026 Conference**

---

## 👨‍💻 Author

### Ayush Sankhyan

B.E. Computer Science Engineering (Hons.)
Specialization: Artificial Intelligence & Machine Learning

Chandigarh University

📧 Email: [sankhyanayush95@gmail.com](mailto:sankhyanayush95@gmail.com)

### Areas of Interest

* Artificial Intelligence
* Machine Learning
* Data Science
* Data Analytics
* Business Intelligence
* Predictive Modeling

---

## ⭐ Support

If you found this project useful:

⭐ Star the repository

🔗 Share the project

🚀 Try the live application

### Live App

https://sentiment-prediction-through-social-media-insights-nxqd2niyr4c.streamlit.app/
