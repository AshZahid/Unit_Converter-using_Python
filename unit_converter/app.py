
import streamlit as st

st.title("Unit Converter")


# Conversion function
def converter(value, unit_from, unit_to):
    conversions = {
        "meters_kilometers": 0.001,
        "kilometers_meters": 1000,
        "grams_kilograms": 0.001,
        "kilograms_grams": 1000
    }

    key = f"{unit_from}_{unit_to}"

    if key in conversions:
        conversion = conversions[key]
        return value * conversion
    else:
        return "Conversion not found"

# Input and Selection
value = st.number_input("Enter your value")

unit_from = st.selectbox("Convert from:", ["meters", "kilometers", "grams", "kilograms"])
unit_to = st.selectbox("Convert to:", ["meters", "kilometers", "grams", "kilograms"])

# Conversion Button
if st.button("Convert"):
    result = converter(value, unit_from, unit_to)
    st.write(f"Converted Value: {result}")
