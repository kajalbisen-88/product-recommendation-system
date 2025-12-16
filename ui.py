import streamlit as st
import requests

st.set_page_config(page_title="Product Recommendation System")

st.title("🛒 Product Recommendation System")

st.write("Enter User ID to get product recommendations")

# User input
user_id = st.number_input("Enter User ID", min_value=1, step=1)

# Button
if st.button("Get Recommendation"):
    try:
        url = "http://127.0.0.1:8000/recommend"   # FastAPI endpoint
        response = requests.post(url, json={"user_id": user_id})

        if response.status_code == 200:
            data = response.json()
            st.success("Recommended Products:")
            for product in data["recommendations"]:
                st.write("👉", product)
        else:
            st.error("API error occurred")

    except Exception as e:
        st.error("❌ API not running. Please start FastAPI server first.")
