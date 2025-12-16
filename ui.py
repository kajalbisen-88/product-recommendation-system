import streamlit as st
import requests

st.set_page_config(page_title="Product Recommendation System")
st.title("🛒 Product Recommendation System")
st.write("Enter User ID to get product recommendations")

# User input
user_id = st.number_input("Enter User ID", min_value=1, step=1)

# Button to get recommendations
if st.button("Get Recommendation"):
    try:
        # Replace this with your FastAPI URL
        url = "http://127.0.0.1:8000/recommend"  # Local machine
        # For Colab, use ngrok URL instead:
        # url = "http://abcd1234.ngrok.io/recommend"

        # Make POST request
        response = requests.post(url, json={"user_id": user_id})

        if response.status_code == 200:
            data = response.json()
            st.success(f"Recommended Products for User ID {user_id}:")
            for product in data["recommendations"]:
                st.write("👉", product)
        else:
            st.error(f"API error occurred: {response.status_code}")

    except Exception as e:
        st.error(f"❌ API not running. Details: {e}")
 
