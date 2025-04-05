import streamlit as st

st.title("💪 BMI Calculator")
st.write("Calculate your Body Mass Index (BMI) easily!")

height = st.number_input("Enter your height (in meters):", min_value=0.1, format="%.2f")
weight = st.number_input("Enter your weight (in kilograms):", min_value=1.0, format="%.2f")

if st.button("Calculate BMI"):
    if height > 0 and weight > 0:
        bmi = weight / (height ** 2)
        st.success(f"Your BMI is: {bmi:.2f}")

        if bmi < 18.5:
            st.warning("You're underweight. 🏃‍♂️🍽️")
        elif 18.5 <= bmi < 24.9:
            st.success("You have a normal weight. 🎯💪")
        elif 25 <= bmi < 29.9:
            st.info("You're overweight. ⚡🏋️‍♂️")
        else:
            st.error("You're obese. ⚠️ Consult a health expert.")
    else:
        st.error("Please provide valid height and weight.")
