
import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

st.set_page_config(page_title="Customer Segmentation App", layout="wide")

st.title("🛍️ Customer Segmentation using K-Means Clustering")
st.markdown("Upload the **Mall_Customers.csv** dataset to visualize and cluster customers based on Annual Income and Spending Score.")

uploaded_file = st.file_uploader("Upload CSV file", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.subheader("Dataset Overview")
    st.dataframe(df.head())

    st.markdown("### 📊 Distribution Plots")
    fig1, ax1 = plt.subplots()
    sns.histplot(df['Annual Income (k$)'], kde=True, ax=ax1, color="skyblue")
    ax1.set_title("Annual Income Distribution")
    st.pyplot(fig1)

    fig2, ax2 = plt.subplots()
    sns.histplot(df['Spending Score (1-100)'], kde=True, ax=ax2, color="orange")
    ax2.set_title("Spending Score Distribution")
    st.pyplot(fig2)

    st.markdown("### 🧪 Apply K-Means Clustering")
    X = df[['Annual Income (k$)', 'Spending Score (1-100)']]
    k = st.slider("Select number of clusters (k)", 2, 10, 5)
    model = KMeans(n_clusters=k, random_state=42)
    df['Cluster'] = model.fit_predict(X)

    st.success("Clustering Applied Successfully!")

    st.markdown("### 📌 Cluster Visualization")
    fig3, ax3 = plt.subplots()
    sns.scatterplot(data=df, x='Annual Income (k$)', y='Spending Score (1-100)', hue='Cluster', palette='Set2', s=100, ax=ax3)
    ax3.set_title("Customer Segments")
    st.pyplot(fig3)

    st.markdown("### 📥 Download Segmented Data")
    csv = df.to_csv(index=False).encode('utf-8')
    st.download_button("Download Clustered Data as CSV", data=csv, file_name='segmented_customers.csv', mime='text/csv')
else:
    st.info("👆 Please upload a valid CSV file to get started.")
