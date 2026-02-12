import streamlit as st
import pandas as pd

# Language selection
language = st.selectbox("Select Language / भाषा चुनें / மொழியை தேர்வு செய்யவும்",
                        ["English", "தமிழ் (Tamil)", "हिंदी (Hindi)"])

# Language dictionary
translations = {
    "English": {
        "title": "🛒 Smart Grocery List App",
        "add_item": "Add Grocery Item",
        "item_name": "Item name",
        "quantity": "Quantity",
        "price": "Price per item",
        "add_button": "Add Item",
        "grocery_list": "Grocery List",
        "total_cost": "Total Cost",
        "clear": "Clear List",
        "added": "added successfully!",
        "cleared": "List cleared!"
    },
    "தமிழ் (Tamil)": {
        "title": "🛒 ஸ்மார்ட் மளிகை பட்டியல் செயலி",
        "add_item": "பொருள் சேர்க்கவும்",
        "item_name": "பொருள் பெயர்",
        "quantity": "அளவு",
        "price": "ஒரு பொருளின் விலை",
        "add_button": "சேர்க்கவும்",
        "grocery_list": "மளிகை பட்டியல்",
        "total_cost": "மொத்த செலவு",
        "clear": "பட்டியலை அழிக்கவும்",
        "added": "வெற்றிகரமாக சேர்க்கப்பட்டது!",
        "cleared": "பட்டியல் அழிக்கப்பட்டது!"
    },
    "हिंदी (Hindi)": {
        "title": "🛒 स्मार्ट किराना सूची ऐप",
        "add_item": "किराना वस्तु जोड़ें",
        "item_name": "वस्तु का नाम",
        "quantity": "मात्रा",
        "price": "प्रति वस्तु मूल्य",
        "add_button": "जोड़ें",
        "grocery_list": "किराना सूची",
        "total_cost": "कुल खर्च",
        "clear": "सूची साफ करें",
        "added": "सफलतापूर्वक जोड़ा गया!",
        "cleared": "सूची साफ कर दी गई!"
    }
}

t = translations[language]

st.title(t["title"])

# Initialize session state
if "grocery_list" not in st.session_state:
    st.session_state.grocery_list = []

st.header(t["add_item"])

item = st.text_input(t["item_name"])
quantity = st.number_input(t["quantity"], min_value=1, step=1)
price = st.number_input(t["price"], min_value=0.0, step=0.5)

if st.button(t["add_button"]):
    if item != "":
        total = quantity * price
        st.session_state.grocery_list.append([item, quantity, price, total])
        st.success(f"{item} {t['added']}")

# Display table
if st.session_state.grocery_list:
    df = pd.DataFrame(
        st.session_state.grocery_list,
        columns=["Item", "Quantity", "Price", "Total"]
    )

    st.header(t["grocery_list"])
    st.dataframe(df)

    grand_total = df["Total"].sum()
    st.subheader(f"{t['total_cost']}: ₹ {grand_total:.2f}")

# Clear list
if st.button(t["clear"]):
    st.session_state.grocery_list = []
    st.warning(t["cleared"])
