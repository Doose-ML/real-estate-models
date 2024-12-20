import streamlit as st
import pandas as pd
import joblib

model_pipeline = joblib.load('property_prices_ .joblib')
model_pipeline1 = joblib.load('investments_suitability.joblib')

st.title('Real Estate Prediction Model')

model_choice = st.radio('select a model to use', ('Investments Suitability', 'Property Price Prediction'))

if model_choice == 'Property Price Prediction':
    Bedrooms= st.number_input('bedrooms',min_value =0.0, step=1.0)
    Bathrooms= st.number_input('bathrooms',min_value =0.0, step=1.0)
    Toilets = st.number_input('toilets',min_value =0.0, step=1.0)
    Parking_space= st.number_input('parking_space',min_value =0.0, step=0.5)

    Title = st.selectbox('title', [' ','Block of Flats', 'Detached Bungalow', 'Detached Duplex', 'Semi Detached Bungalow', 'Semi Detached Duplex', 'Terraced Bungalow', 'Terraced Duplexes'])
    Town = st.selectbox('town', [' ','Aba', 'Abeokuta North', 'Abeokuta South', 'Abraka', 'Ado-Ekiti', 'Ado-Odo/Ota', 'Afijio', 'Agbara', 'Agbara-Igbesa', 'Agege', 'Ajah', 'Akinyele', 'Akure', 'Alimosho', 'Amuwo Odofin', 'Aniocha South', 'Apapa', 'Apo', 'Arepo', 'Asaba', 'Asokoro District', 'Ayobo', 'Badagry', 'Bwari', 'Calabar', 'Central Business District', 'Chikun', 'Dakibiyu', 'Dakwo', 'Danja', 'Dape', 'Dei-Dei', 'Dekina', 'Diplomatic Zones', 'Duboyi', 'Durumi', 'Dutse', 'Ede South', 'Egbe', 'Egbeda', 'Egor', 'Ejigbo', 'Eket', 'Eko Atlantic City', 'Eleme', 'Enugu', 'Epe', 'Ethiope West', 'Ewekoro', 'Gaduwa', 'Galadimawa', 'Garki', 'Gbagada', 'Gudu', 'Guzamala', 'Guzape District', 'Gwagwalada', 'Gwarinpa', 'Ibadan', 'Ibadan North', 'Ibadan North-East', 'Ibadan North-West', 'Ibadan South-West', 'Ibafo', 'Ibarapa North', 'Ibeju', 'Ibeju Lekki', 'Idimu', 'Ido', 'Idu Industrial', 'Ifako-Ijaiye', 'Ifo', 'Ijaiye', 'Ijebu Ode', 'Ijede', 'Ijesha', 'Ijoko', 'Ikeja', 'Ikorodu', 'Ikot Ekpene', 'Ikotun', 'Ikoyi', 'Ikpoba Okha', 'Ikwerre', 'Ilorin East', 'Ilorin South', 'Ilorin West', 'Ilupeju', 'Imota', 'Ipaja', 'Isheri', 'Isheri North', 'Isolo', 'Jabi', 'Jahi', 'Jikwoyi', 'Jos North', 'Jos South', 'KM 46', 'Kabusa', 'Kado', 'Kaduna North', 'Kaduna South', 'Kafe', 'Kagini', 'Kano', 'Karmo', 'Karsana', 'Karshi', 'Karu', 'Katampe', 'Kaura', 'Keffi', 'Ketu', 'Kosofe', 'Kubwa', 'Kuje', 'Kukwaba', 'Kurudu', 'Kusada', 'Kyami', 'Lagos Island', 'Lekki', 'Life Camp', 'Lokogoma District', 'Lokoja', 'Lugbe District', 'Mabushi', 'Magboro', 'Magodo', 'Maitama District', 'Mararaba', 'Maryland', 'Mbora (Nbora)', 'Mowe Ofada', 'Mowe Town', 'Mpape', 'Mushin', 'Nasarawa', 'Nassarawa', 'Nyanya', 'Obafemi Owode', 'Obio-Akpor', 'Ogijo', 'Ogudu', 'Ohaji/Egbema', 'Ojo', 'Ojodu', 'Ojota', 'Oke-Aro', 'Oke-Odo', 'Okene', 'Okpe', 'Oluyole', 'Oredo', 'Orile', 'Orozo', 'Oshodi', 'Osogbo', 'Ovia North-East', 'Owerri Municipal', 'Owerri North', 'Owerri West', 'Oyigbo', 'Oyo West', 'Paikoro', 'Port Harcourt', 'Sagamu', 'Sango Ota', 'Shomolu', 'Simawa', 'Surulere', 'Udu', 'Ughelli North', 'Ughelli South', 'Uhunmwonde', 'Umuahia', 'Utako', 'Uvwie', 'Uyo', 'Victoria Island (VI)', 'Warri', 'Wumba', 'Wuse', 'Wuse 2', 'Wuye', 'Yaba', 'Yenagoa', 'Yewa South'])
    state = st.selectbox('state', [' ','Abia', 'Abuja', 'Akwa Ibom', 'Anambara', 'Bayelsa', 'Borno', 'Cross River', 'Delta', 'Edo', 'Ekiti', 'Enugu', 'Imo', 'Kaduna', 'Kano', 'Katsina', 'Kogi', 'Kwara', 'Lagos', 'Nasarawa', 'Niger', 'Ogun', 'Osun', 'Oyo', 'Plateau', 'Rivers'])

    
    input_data_price = pd.DataFrame({
        'bedrooms':[Bedrooms],
        'bathrooms':[Bathrooms],
        'toilets':[Toilets],
        'parking_space':[Parking_space],
        'title':[Title],
        'town':[Town],
        'state':[state]
    })
    if st.button('predict price'):
        predicted_price = model_pipeline.predict(input_data_price)[0]
        st.success(f'The predicted property price is: { predicted_price:.2f}')

elif model_choice =='Investments Suitability':
    st.title('investment suitability prediction')
    st.write('provide details of the property')

    Location = st.selectbox('Location',[ ' ','Kano', 'Lagos Mainland', 'Kaduna', 'Lagos Island', 'Ibadan'],index = 0)
    Security_Rating= st.selectbox('Security Rating',[' ','Medium', 'High', 'Low'],index = 0)
    Infrastructure= st.selectbox('Infrastructure',[' ','Poor', 'Fair', 'Good'],index = 0)

    price = st.number_input('price')
    Rental_Yield = st.number_input('Rental Yield')

    
    input_data_suitability = pd.DataFrame({
        'Location':[Location],
        'Security Rating':[Security_Rating],
        'Infrastructure':[Infrastructure],
        'price':[price],
        'Rental Yield':[Rental_Yield]

    })
    if st.button('predict suitability'):
        predicted_price = model_pipeline1.predict(input_data_suitability)
        categories = ['Low','Medium','High']
        result = categories[predicted_price[0]] 
        st.success(f'investment suitability: {result}')



	

