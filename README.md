# 🩺 **Breast Cancer Classification – Machine Learning Project**

This project predicts whether a breast tumor is **Benign** or **Malignant** using Machine Learning.
It is built with **Logistic Regression** and deployed as a **Streamlit Web App**.
The model analyzes 30 medical features (mean, se, worst) from the Breast Cancer Wisconsin Dataset.

---

## 🚀 **Project Overview**

This project covers the complete ML pipeline:

* ✔ Exploratory Data Analysis (EDA)
* ✔ Data Preprocessing
* ✔ Feature Scaling using **StandardScaler**
* ✔ Model Training using **Logistic Regression**
* ✔ Saving the Model using **Pickle (.pkl)**
* ✔ Building a Web App using **Streamlit**
* ✔ UI Design in Python
* ✔ Local development in **Spyder**
* ✔ Machine Learning-based real-time predictions

---

## 🧠 **Tech Stack Used**

| Category                 | Tools / Libraries            |
| ------------------------ | ---------------------------- |
| Programming Language     | **Python**                   |
| ML Algorithm             | **Logistic Regression**      |
| Feature Scaling          | **StandardScaler (sklearn)** |
| Model Saving             | **Pickle (.pkl)**            |
| Web App Framework        | **Streamlit**                |
| IDE Used                 | **Spyder (Anaconda)**        |
| Data Analysis            | **NumPy, Pandas**            |
| Visualization (optional) | Matplotlib / Seaborn         |

---

## 📊 **Machine Learning Workflow**

### **1️⃣ Exploratory Data Analysis (EDA)**

* Checked missing values
* Analyzed class imbalance
* Visualized key features
* Checked correlations

### **2️⃣ Data Preprocessing**

* Converted dataset into NumPy arrays
* Selected all 30 useful features
* Applied scaling with *StandardScaler*

### **3️⃣ Model Training**

* Used **Logistic Regression** for binary classification
* Achieved strong accuracy on test data
* Tuned hyperparameters

### **4️⃣ Saving the Model**

Model and scaler saved using Pickle:

```
logistic_model.pkl
scaler.pkl
```

### **5️⃣ Streamlit Web App**

Users enter 30 medical feature values and the app predicts:

* **Benign Tumor**
* **Malignant Tumor**

The model runs in real-time with scaled inputs.

---

## 🖥️ **How to Run Locally**

### **Install Dependencies**

```bash
pip install numpy pandas scikit-learn streamlit
```

### **Run Streamlit App**

```bash
streamlit run app.py
```

---

## 🌐 **Live Web App**

The project is deployed on **Streamlit Cloud**:
👉 *[Breast Cancer Prediction Web App](https://breastcancerclassification-8nasgblr5jlcvbmgtfp9hz.streamlit.app/)*

---

## 🧪 **Features Used for Prediction**

* radius_mean, texture_mean, perimeter_mean, area_mean
* … and 30 total numerical medical features
* (mean, se, worst groups)

---

## 🎯 **Project Goal**

To build a simple, accurate, accessible Machine Learning tool that helps classify breast cancer tumor types using logistic regression.

---

## 🤝 **Contributions**

Pull requests are welcome!
Feel free to report issues or suggest improvements.

---

## ⭐ **If you like this project, don’t forget to give it a star!**
