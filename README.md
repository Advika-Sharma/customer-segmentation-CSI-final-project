# 🛍️ Customer Segmentation App using Streamlit

This is a simple and interactive **Streamlit web application** that performs **customer segmentation using K-Means Clustering** on the `Mall_Customers.csv` dataset. It helps businesses group customers based on their **Annual Income** and **Spending Score**, offering insights to improve **targeted marketing** strategies.

---

## 🎯 Objective

Use **unsupervised machine learning (KMeans)** to group customers into clusters, allowing:
- Better understanding of customer behavior
- Targeted marketing strategies
- Personalized customer engagement

---

## 📂 Dataset Info

- 📁 `Mall_Customers.csv`
- 👥 200 customer records
- 📊 Features:
  - `CustomerID`
  - `Gender`
  - `Age`
  - `Annual Income (k$)`
  - `Spending Score (1-100)`
- 📌 Source: [Kaggle – Customer Segmentation](https://www.kaggle.com/datasets/vjchoudhary7/customer-segmentation-tutorial-in-python)

---

## 🧠 Tech Stack

| Category        | Tools Used                             |
|-----------------|-----------------------------------------|
| Programming     | Python 3.x                              |
| Web Framework   | Streamlit                               |
| Visualization   | Matplotlib, Seaborn                     |
| ML Algorithm    | KMeans Clustering (Scikit-Learn)        |
| Dependencies    | Listed in `requirements.txt`            |
| Deployment      | [Streamlit Cloud](https://streamlit.io/cloud) |

---

## 🚀 Features

- 📤 Upload `Mall_Customers.csv` interactively
- 📊 View income and spending distribution
- 🎯 Select number of clusters (`k`) using slider
- 🔍 Visualize customer segments
- 📥 Download segmented data as CSV

---

## 🛠 How to Run Locally

```bash
# 1. Clone this repository
git clone https://github.com/Advika-Sharma/customer-segmentation-CSI-final-project.git
cd customer-segmentation-CSI-final-project

# 2. Install dependencies
pip install -r requirements.txt

# 3. Run the Streamlit app
streamlit run customer_segmentation_app.py
