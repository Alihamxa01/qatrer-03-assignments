
import streamlit as st

# Define conversion factors for length units
length_conversion_factors = {
    "meters": 1,
    "kilometers": 0.001,
    "centimeters": 100,
    "millimeters": 1000,
    "inches": 39.3701,
    "feet": 3.28084,
    "yards": 1.09361,
    "miles": 0.000621371
}

# Define conversion formulas for temperature units
def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32

def fahrenheit_to_celsius(f):
    return (f - 32) * 5/9

def celsius_to_kelvin(c):
    return c + 273.15

def kelvin_to_celsius(k):
    return k - 273.15

# Define conversion rates for currency (example rates)
currency_conversion_rates = {
    "AED , United Arab Emirates Dirham": 3.67,  # United Arab Emirates Dirham
    "AUD": 1.35,  # Australian Dollar
    "BHD": 0.38,  # Bahraini Dinar
    "CAD": 1.25,  # Canadian Dollar
    "CHF": 0.92,  # Swiss Franc
    "CNY": 6.45,  # Chinese Yuan
    "DZD": 135.0,  # Algerian Dinar
    "DJF": 178.0,  # Djiboutian Franc
    "EGP": 30.5,  # Egyptian Pound
    "EUR": 0.85,  # Euro
    "GBP": 0.73,  # British Pound
    "INR": 74.5,  # Indian Rupee
    "IQD": 1460.0,  # Iraqi Dinar
    "JOD": 0.71,  # Jordanian Dinar
    "JPY": 110.0,  # Japanese Yen
    "KES": 115.0,  # Kenyan Shilling
    "KMF": 450.0,  # Comorian Franc
    "KWD": 0.31,  # Kuwaiti Dinar
    "LBP": 15000.0,  # Lebanese Pound
    "LYD": 4.85,  # Libyan Dinar
    "MAD": 10.2,  # Moroccan Dirham
    "MUR": 45.0,  # Mauritian Rupee
    "OMR": 0.39,  # Omani Rial
    "PKR": 280.0,  # Pakistani Rupee
    "QAR": 3.64,  # Qatari Riyal
    "SAR": 3.75,  # Saudi Riyal
    "SDG": 580.0,  # Sudanese Pound
    "SOS": 570.0,  # Somali Shilling
    "SYP": 2500.0,  # Syrian Pound
    "TND": 3.15,  # Tunisian Dinar
    "USD": 1.0,  # US Dollar
    "YER": 250.0   # Yemeni Rial
}




# Custom CSS for styling
st.markdown(
    """
    <style>
    .stTextInput>div>div>input {
        background-color: #f0f2f6;
        color: black;
        border-radius: 10px;
        padding: 10px;
    }
    .stSelectbox>div>div>select {
        background-color: #f0f2f6;
        color: #262730;
        border-radius: 10px;
        padding: 10px;
    }
    .stButton>button {
        background-color: #4CAF50;
        color: white;
        border-radius: 10px;
        padding: 10px 20px;
        font-size: 16px;
    }
    .stMarkdown {
        font-size: 18px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# App Title
st.title("📐 Multi-Unit Converter")

# Initialize session state for history
if "length_history" not in st.session_state:
    st.session_state.length_history = []

if "temperature_history" not in st.session_state:
    st.session_state.temperature_history = []

if "currency_history" not in st.session_state:
    st.session_state.currency_history = []

# Create tabs for each converter
tab1, tab2, tab3 = st.tabs(["Length Converter", "Temperature Converter", "Currency Converter"])

# Length Converter
with tab1:
    st.markdown("### Length Converter")
    col1, col2, col3 = st.columns(3)

    with col1:
        length_value_input = st.text_input("Value", placeholder="e.g., 2849.22", key="length_value")

    with col2:
        length_input_unit = st.selectbox("From", options=list(length_conversion_factors.keys()), key="length_from")

    with col3:
        length_output_unit = st.selectbox("To", options=list(length_conversion_factors.keys()), key="length_to")

    if st.button("Convert Length", key="length_convert"):
        try:
            length_value = float(length_value_input)
            if length_input_unit == length_output_unit:
                st.warning("Please select different units for conversion.")
            else:
                # Convert input value to meters first
                value_in_meters = length_value / length_conversion_factors[length_input_unit]
                # Convert meters to the desired output unit
                converted_value = value_in_meters * length_conversion_factors[length_output_unit]
                result = f"{length_value} {length_input_unit} = {converted_value:.4f} {length_output_unit}"
                st.success(f"✅ **Converted Value:** {converted_value:.4f} {length_output_unit}")

                # Save the conversion to history
                st.session_state.length_history.append(result)
        except ValueError:
            st.error("⚠️ Please enter a valid numeric value.")

    # Display Length History
    if st.session_state.length_history:
        st.markdown("---")
        st.markdown("### Length Conversion History")
        for i, entry in enumerate(st.session_state.length_history, 1):
            st.markdown(f"{i}. {entry}")

# Temperature Converter
with tab2:
    st.markdown("### Temperature Converter")
    col1, col2, col3 = st.columns(3)

    with col1:
        temp_value_input = st.text_input("Value", placeholder="e.g., 100", key="temp_value")

    with col2:
        temp_input_unit = st.selectbox("From", options=["Celsius", "Fahrenheit", "Kelvin"], key="temp_from")

    with col3:
        temp_output_unit = st.selectbox("To", options=["Celsius", "Fahrenheit", "Kelvin"], key="temp_to")

    if st.button("Convert Temperature", key="temp_convert"):
        try:
            temp_value = float(temp_value_input)
            if temp_input_unit == temp_output_unit:
                st.warning("Please select different units for conversion.")
            else:
                # Convert input value to Celsius first
                if temp_input_unit == "Celsius":
                    celsius = temp_value
                elif temp_input_unit == "Fahrenheit":
                    celsius = fahrenheit_to_celsius(temp_value)
                elif temp_input_unit == "Kelvin":
                    celsius = kelvin_to_celsius(temp_value)

                # Convert Celsius to the desired output unit
                if temp_output_unit == "Celsius":
                    converted_value = celsius
                elif temp_output_unit == "Fahrenheit":
                    converted_value = celsius_to_fahrenheit(celsius)
                elif temp_output_unit == "Kelvin":
                    converted_value = celsius_to_kelvin(celsius)

                result = f"{temp_value} {temp_input_unit} = {converted_value:.4f} {temp_output_unit}"
                st.success(f"✅ **Converted Value:** {converted_value:.4f} {temp_output_unit}")

                # Save the conversion to history
                st.session_state.temperature_history.append(result)
        except ValueError:
            st.error("⚠️ Please enter a valid numeric value.")

    # Display Temperature History
    if st.session_state.temperature_history:
        st.markdown("---")
        st.markdown("### Temperature Conversion History")
        for i, entry in enumerate(st.session_state.temperature_history, 1):
            st.markdown(f"{i}. {entry}")

# Currency Converter
with tab3:
    st.markdown("### Currency Converter")
    col1, col2, col3 = st.columns(3)

    with col1:
        currency_value_input = st.text_input("Value", placeholder="e.g., 100", key="currency_value")

    with col2:
        currency_input_unit = st.selectbox("From", options=list(currency_conversion_rates.keys()), key="currency_from")

    with col3:
        currency_output_unit = st.selectbox("To", options=list(currency_conversion_rates.keys()), key="currency_to")

    if st.button("Convert Currency", key="currency_convert"):
        try:
            currency_value = float(currency_value_input)
            if currency_input_unit == currency_output_unit:
                st.warning("Please select different currencies for conversion.")
            else:
                # Convert input value to USD first
                value_in_usd = currency_value / currency_conversion_rates[currency_input_unit]
                # Convert USD to the desired output currency
                converted_value = value_in_usd * currency_conversion_rates[currency_output_unit]
                result = f"{currency_value} {currency_input_unit} = {converted_value:.4f} {currency_output_unit}"
                st.success(f"✅ **Converted Value:** {converted_value:.4f} {currency_output_unit}")

                # Save the conversion to history
                st.session_state.currency_history.append(result)
        except ValueError:
            st.error("⚠️ Please enter a valid numeric value.")

    # Display Currency History
    if st.session_state.currency_history:
        st.markdown("---")
        st.markdown("### Currency Conversion History")
        for i, entry in enumerate(st.session_state.currency_history, 1):
            st.markdown(f"{i}. {entry}")

# Footer
st.markdown("---")
st.markdown("***__Made By ALI HAMZA__***")
