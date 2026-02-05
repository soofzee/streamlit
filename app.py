# connecting import statement
import streamlit as st

st.title("Hello World")

# st.header("This is a header") 
# st.subheader("This is a subheader")

# st.text("Hello 3D Educators!!!")

# st.success("Success")

# st.info("Information")

# st.warning("Warning")

# st.error("Error")

# exp = ZeroDivisionError("Trying to divide by Zero")
# st.exception(exp)


# from PIL import Image  # Import Image from Pillow
# img = Image.open("C:/Users/OSAMA/OneDrive/3DEducators/Him.png") # Open the image file
# st.image(img, width=200) # Display the image with a specified width

# # Create a radio button to select gender
# status = st.radio("Select Gender:", ['Male', 'Female'])

# # Display the selected option using success message
# if status == 'Male':
#     st.success(status)
# else:
#     st.success(status)


# # Create a dropdown menu for selecting a hobby
# hobby = st.selectbox("Select a Hobby:", ['Dancing', 'Reading', 'Sports'])

# # Display the selected hobby
# st.write("Your hobby is:", hobby)


# # Create a multiselect box for choosing hobbies
# hobbies = st.multiselect("Select Your Hobbies:", ['Dancing', 'Reading', 'Sports'])

# # Display the number of selected hobbies
# st.write("You selected", len(hobbies), "hobbies")

# # A simple button that does nothing
# st.button("Click Me")

# # A button that displays text when clicked
# if st.button("About"):
#     st.text("Welcome to 3D Educators!")

# # import numpy as np
# # import pandas as pd
# # chart_data = pd.DataFrame(
# #      np.random.randn(20, 3),
# #      columns=['a', 'b', 'c'])

# # st.line_chart(chart_data)

# Title of the app
st.title("BMI Calculator")

# Input: Weight in kilograms
weight = st.number_input("Enter your weight (kg):", min_value=0.0, format="%.2f")

# Input: Height format selection
height_unit = st.radio("Select your height unit:", ['Centimeters', 'Meters', 'Feet'])

# Input: Height value based on selected unit
height = st.number_input(f"Enter your height ({height_unit.lower()}):", min_value=0.0, format="%.2f")

# Calculate BMI when button is pressed
if st.button("Calculate BMI"):
    try:
        # Convert height to meters based on selected unit
        if height_unit == 'Centimeters':
            height_m = height / 100
        elif height_unit == 'Feet':
            height_m = height / 3.28
        else:
            height_m = height

        # Prevent division by zero
        if height_m <= 0:
            st.error("Height must be greater than zero.")
        else:
            bmi = weight / (height_m ** 2)
            st.success(f"Your BMI is {bmi:.2f}")

            # BMI interpretation
            if bmi < 16:
                st.error("You are Extremely Underweight")
            elif 16 <= bmi < 18.5:
                st.warning("You are Underweight")
            elif 18.5 <= bmi < 25:
                st.success("You are Healthy")
            elif 25 <= bmi < 30:
                st.warning("You are Overweight")
            else:
                st.error("You are Extremely Overweight")
    except:
        st.error("Please enter valid numeric values.")
