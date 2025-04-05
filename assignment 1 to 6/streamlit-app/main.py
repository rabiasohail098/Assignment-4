import streamlit as st
import requests

# 🍕 Food Recommendation App
st.title("🍽️ Food Recommendation App")
st.write("Choose your favorite cuisine and get the best dishes with details!")

# Cuisine Options
cuisines = ["Italian", "Mexican", "Indian", "Chinese", "American"]
selected_cuisine = st.selectbox("Select a Cuisine:", cuisines)

# Sample Data (Replace with API later)
food_data = {
    "Italian": [
        {"name": "Pasta Carbonara", "image": "https://images.pexels.com/photos/28767857/pexels-photo-28767857/free-photo-of-rustic-spaghetti-dish-with-fresh-basil-and-cheese.jpeg?auto=compress&cs=tinysrgb&w=600", "calories": 450},
        {"name": "Margherita Pizza", "image": "https://images.pexels.com/photos/10068752/pexels-photo-10068752.jpeg?auto=compress&cs=tinysrgb&w=600", "calories": 300},
    ],
    "Mexican": [
        {"name": "Tacos", "image": "https://images.pexels.com/photos/18032209/pexels-photo-18032209/free-photo-of-tacos-on-table.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2", "calories": 250},
        {"name": "Burrito", "image": "https://images.pexels.com/photos/4955267/pexels-photo-4955267.jpeg?auto=compress&cs=tinysrgb&w=600", "calories": 500},
    ],
    "Indian": [
        {"name": "Butter Chicken", "image": "https://images.pexels.com/photos/9609844/pexels-photo-9609844.jpeg?auto=compress&cs=tinysrgb&w=600", "calories": 600},
        {"name": "Paneer Tikka", "image": "https://images.pexels.com/photos/29173103/pexels-photo-29173103/free-photo-of-delicious-grilled-paneer-skewers-with-chimichurri.jpeg?auto=compress&cs=tinysrgb&w=600", "calories": 350},
    ],
    "Chinese": [
        {"name": "Sweet & Sour Chicken", "image": "https://images.pexels.com/photos/6646268/pexels-photo-6646268.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2", "calories": 400},
        {"name": "Dim Sum", "image": "https://images.pexels.com/photos/7287719/pexels-photo-7287719.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2", "calories": 200},
    ],
    "American": [
        {"name": "Burger", "image": "https://images.pexels.com/photos/1639557/pexels-photo-1639557.jpeg?auto=compress&cs=tinysrgb&w=600", "calories": 550},
        {"name": "Fried Chicken", "image": "https://images.pexels.com/photos/1059943/pexels-photo-1059943.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2", "calories": 650},
    ],
}

# Show Recommendations
if selected_cuisine:
    st.subheader(f"Top Dishes for {selected_cuisine} Cuisine:")
    for dish in food_data[selected_cuisine]:
        st.image(dish["image"], width=300)
        st.write(f"🍽️ **{dish['name']}**")
        st.write(f"🔥 Calories: {dish['calories']} kcal")
        st.markdown("---")
