import streamlit as st
import pickle
import numpy as np
import gdown
import os 

if not os.path.exists("model.pkl"):
    url = "https://drive.google.com/uc?id=1XUrq4cCmMUdAMEctuvHSgQa2uhvzILuQ"
    gdown.download(url, "model.pkl", quiet=False)

model = pickle.load(open("model.pkl","rb"))

location_list = pickle.load(open("location_list.pkl","rb"))
encode_map = pickle.load(open("encode_map.pkl","rb"))

st.title("House Rent Prediction")
st.text("This app predicts the rent of house in indian cities. Fill the information to predict your rent.")

Amount = st.number_input("Enter house price(INR): ",100000.0,15000000000.0)

location = st.selectbox("Select location",location_list)
location_num = encode_map[location]


carpet_area = st.number_input("Carpet Area(in sqft): ",1.0,800000.0)
bathroom = st.slider("No. of Washrooms: ",1,10)
balcony = st.slider("No. of Balconies: ",1,10)
super_area = st.slider("Super Area(in sqft): ",1.0,10000.0)
floor_number = st.slider("Floor Number : ",1,200)
total_floors = st.slider("Total no. of floors: ",floor_number,200)

carpet_area_missing = 0
super_area_missing = 0

#Transaction
Transaction_list = ['New Property','Rent/Lease', 'Resale','Other','Unknown']
Transaction = st.selectbox("Select transaction type: ",Transaction_list)
Transaction_features = np.zeros(5)

for i in range(0,len(Transaction_list)):
  if Transaction == Transaction_list[i]:
    Transaction_features[i] = 1
    break

Transaction_New_Property = Transaction_features[0]
Transaction_Rent_Lease = Transaction_features[1]
Transaction_Resale = Transaction_features[2]
Transaction_Other = Transaction_features[3]
Transaction_Unknown = Transaction_features[4]

Transaction_features = np.zeros(5)

#Furnishing
Furnishing_list = ['Furnished','Semi Furnished','Unfurnished','Unknown']
Furnishing = st.selectbox("Select Furnishing: ",Furnishing_list)
Furnishing_features = np.zeros(4)

for i in range(0,len(Furnishing_list)):
  if Furnishing == Furnishing_list[i]:
    Furnishing_features[i] = 1
    break

Furnishing_Furnished = Furnishing_features[0]
Furnishing_Semi_Furnished = Furnishing_features[1]
Furnishing_Unfurnished = Furnishing_features[2]
Furnishing_Unknown = Furnishing_features[3]

Furnishing_features = np.zeros(4)

#facing
facing_list = ['East','West','North','South','North East','North West','South East','South West','Unknown']
facing = st.selectbox("Facing direction: ",facing_list)
facing_features = np.zeros(9)

for i in range(0,len(facing_list)):
  if facing == facing_list[i]:
    facing_features[i] = 1
    break

facing_East = facing_features[0]
facing_West = facing_features[1]
facing_North = facing_features[2]
facing_South = facing_features[3]
facing_North_East = facing_features[4]
facing_North_West = facing_features[5]
facing_South_East = facing_features[6]
facing_South_West = facing_features[7]
facing_Unknown = facing_features[8]

facing_features = np.zeros(9)

#Ownership
Ownership_list = ['Cooperative Society','Freehold','Leasehold','Power of Attorney','Unknown']
Ownership = st.selectbox("Select Ownership type: ",Ownership_list)
Ownership_features = np.zeros(5)

for i in range(0,len(Ownership_list)):
  if Ownership == Ownership_list[i]:
    Ownership_features[i] = 1
    break

Owner_cooperative = Ownership_features[0]
Owner_freehold = Ownership_features[1]
Owner_leasehold = Ownership_features[2]
Owner_power_of_attorney = Ownership_features[3]
Owner_Unknown = Ownership_features[4]

Ownership_features = np.zeros(5)

if st.button("Predict Rent"):
  y_predict = model.predict([[Amount,location_num,carpet_area,bathroom,balcony,super_area,floor_number,total_floors,carpet_area_missing,super_area_missing,
                             Transaction_New_Property,Transaction_Other,Transaction_Rent_Lease,Transaction_Resale,Transaction_Unknown,Furnishing_Furnished,
                             Furnishing_Semi_Furnished,Furnishing_Unfurnished,Furnishing_Unknown,facing_East,facing_North,facing_North_East,facing_North_West,
                             facing_South,facing_South_East,facing_South_West,facing_Unknown,facing_West,Owner_cooperative, Owner_freehold,Owner_leasehold,
                              Owner_power_of_attorney,Owner_Unknown]])
  prediction = y_predict[0]
  st.success(f"House rent: ₹ {round(prediction,2)}")


