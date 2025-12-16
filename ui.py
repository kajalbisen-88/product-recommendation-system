import streamlit as st
import pandas as pd

st.set_page_config(page_title="Product Recommendation System")
st.title("🛒 Product Recommendation System")
st.write("Enter User ID to get product recommendations")

user_id = st.number_input("Enter User ID", min_value=1, step=1)

if st.button("Get Recommendation"):
    products = [
        ["Mobile", "Laptop", "Power Bank"],
        ["Shoes", "T-Shirt", "Jeans"],
        ["Books", "Notebook", "Pen"],
        ["Headphones", "Smart Watch", "Bluetooth Speaker"],
        ["Camera", "Tripod", "Memory Card"],
        ["Backpack", "Sunglasses", "Hat"]
    ]

    index = user_id % len(products)
    recs = products[index]

    st.success(f"Recommended Products for User ID {user_id}")
    for p in recs:
        st.write("👉", p)

    df = pd.DataFrame(recs, columns=["Recommended Product"])
    st.download_button(
        "⬇️ Download CSV",
        df.to_csv(index=False),
        file_name=f"user_{user_id}_recommendations.csv",
        mime="text/csv"
    )
