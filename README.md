# Human Activity Recognition using Machine Learning

This project implements multiple machine learning algorithms to recognize human activities using sensor data. It is based on the IEEE research paper:

📄 **“Implementation of Machine Learning Algorithms for Human Activity Recognition”**  
📚 *Presented at the 3rd International Conference on Signal Processing and Communication (ICPSC), IEEE 2021*

---

## 📦 Dataset

- **Source**: [UCI HAR Dataset](https://archive.ics.uci.edu/ml/datasets/human+activity+recognition+using+smartphones)
- **Sensors**: Accelerometer and gyroscope from smartphones
- **Subjects**: 30 individuals performing daily activities
- **Activities classified**:
  - Walking
  - Walking Upstairs
  - Walking Downstairs
  - Sitting
  - Standing
  - Laying

---


---

## 🧠 ML Algorithms Used

The following classifiers were implemented and evaluated:

- ✅ **Random Forest** *(Best Accuracy ~92%)*
- K-Nearest Neighbors (KNN)
- Decision Tree
- Gradient Boosting
- Bagging
- Support Vector Machine (SVM) – Linear, Polynomial, RBF Kernels
- Linear Discriminant Analysis (LDA)

---

## 🧪 Feature Extraction

Time-domain features were extracted using **overlapping windowing**:
- Window size: **250 ms**
- Overlap: **25%**
- Features extracted:
  - Mean Absolute Value (MAV)
  - Root Mean Square (RMS)
  - Variance
  - Skewness
  - Kurtosis

---

## 📊 Evaluation Metrics

- **Accuracy**
- **Precision**
- **Recall**
- **F1-Score**

Evaluation was done using **5-fold Stratified Cross-Validation**.

---

## 🚀 Results (Sample)

| Classifier           | Accuracy (%) |
|----------------------|--------------|
| Random Forest        | **92.71**     |
| KNN                  | 92.54        |
| Polynomial SVM       | 92.48        |
| Bagging              | 92.48        |
| Gradient Boosting    | 89.65        |
| Decision Tree        | 89.76        |
| LDA                  | 86.64        |
| Linear SVM           | 78.55        |

---


Heres the output in the webapp:

<img width="1103" height="819" alt="Screenshot 2025-07-16 155858" src="https://github.com/user-attachments/assets/864ed173-16d6-475a-a0fa-994958ff7f63" />

<img width="956" height="563" alt="Screenshot 2025-07-16 155935" src="https://github.com/user-attachments/assets/b124facd-67ae-474e-886a-30c1992e63fd" />






