import streamlit as st

# Simple calorie database (you can expand this later)
calorie_db = {
    "apple": 95,
    "banana": 105,
    "orange": 62,
    "rice (1 cup)": 206,
    "bread (1 slice)": 80,
    "egg": 78,
    "chicken breast (100g)": 165,
    "pizza slice": 285,
}

st.title("🍎 Calorie Tracker")

# Input
food_item = st.selectbox("Select a food item:", list(calorie_db.keys()))
quantity = st.number_input("How many servings?", min_value=0.0, step=0.5)

# Tracking
if 'total_calories' not in st.session_state:
    st.session_state.total_calories = 0

if st.button("Add to Daily Total"):
    calories = calorie_db[food_item] * quantity
    st.session_state.total_calories += calories
    st.success(f"Added {calories:.0f} calories from {food_item}")

st.markdown(f"### 🔢 Total Calories Today: {st.session_state.total_calories:.0f}")
