import streamlit as st

st.title("Unit Converter App")
st.markdown("### Covnter Lenght, Time and Kilometer")
st.write("Welcome! Select one of the list Item for Convert.....")

catergory = st.selectbox("Chosse Category", ["Lenght" , "Weight" , "Time"])

def Convert_Unit(category, value, unit):

    if catergory == "Lenght":
        if unit == "Kilometer to Miles":
            return value * 0.621371
        elif unit == "Miles to Kilometer":
            return value / 0.621371
    elif catergory == "Weight":
        if unit == "Kilogram to Pounds":
            return value * 2.20462
        elif unit == "Pounds to Kilogram":
            return value / 2.20462
    elif catergory == "Time":
        if unit == "Seconds to Minutes":
            return value / 60
        elif unit == "Minutes to Seconds":
            return value * 60
        elif unit == "Minutes to Hours":
            return value / 60
        elif unit == "Hours to Minutes":
            return value * 60
        elif unit == "Hours to Days":
            return value / 24
        elif unit == "Days to Hours":
            return value * 24

if catergory == "Lenght":
    unit = st.selectbox("Select Unit", ["Kilometer to Miles" , "Miles to Kilometer"])
elif catergory == "Weight":
    unit = st.selectbox("Select Unit", ["Kilogram to Pounds" , "Pounds to Kilogram"])
elif catergory == "Time":
    unit = st.selectbox("Select Unit", ["Seconds to Minutes" , "Minutes to Seconds" , "Minutes to Hours" , "Hours to Minutes" , "Hours to Days" , "Days to Hours"])

value = st.number_input("Enter Value to Convert") 

if st.button("Convert"):    
    result = Convert_Unit(catergory, value, unit)
    st.success(f"Converted Value is {result:.2f}")


