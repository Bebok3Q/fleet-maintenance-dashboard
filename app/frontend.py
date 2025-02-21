import streamlit as st
import requests

API_URL = "http://127.0.0.1:8000/api/vehicles/"
st.title("Fleet Maintenance Dashboard")

with st.form(key="add_vehicle_form"):
    vehicle_name = st.text_input("Vehicle Name")
    vehicle_vin = st.text_input("Vehicle VIN")
    vehicle_mileage = st.number_input("Vehicle Mileage", min_value=0.0, step=1.0)
    submit_button = st.form_submit_button(label="Add Vehicle")

    if submit_button:
        payload = {
            "name": vehicle_name,
            "vin": vehicle_vin,
            "mileage": vehicle_mileage
        }
        response = requests.post(API_URL, json=payload)
        if response.status_code == 200:
            st.success("Vehicle added succesfully!")
        else:
            st.error("Failed to add vehicle.")

response = requests.get(API_URL)
if response.status_code == 200:
    vehicles = response.json()
    if vehicles:
        st.subheader("Vehicles list")
        for vehicle in vehicles:
            st.write(f'**{vehicle['name']}** - {vehicle['vin']} - {vehicle['mileage']} miles')
else:
    st.error("Failed to fetch vehicle data.")