import pickle
from pathlib import Path
import streamlit as st  # 🎈 data web app development
import pandas as pd # read csv, df manipulation
import numpy as np # np mean, np random
from matplotlib import pyplot as plt
import seaborn as sns
import plotly.express  as px  # interactive charts
import time  # to simulate a real time data, time loop
import streamlit_authenticator as stauth

st.set_page_config(page_title="European hotel Customers Review",page_icon=':bar_chart:', layout="wide")

# --- USER AUTHENTICATION ---
#names= ["Shruti Ushire","Yash Jadhav"]
#usernames=["ShrutiU","YashJ"]

# load hashed passwords
#file_path = Path(__file__).parent / "hashed_pw.pkl"
#with file_path.open("rb") as file:
#hashed_passwords = pickle.load(file)

#authenticator = stauth.Authenticate(names, usernames, hashed_passwords,
#"Customers_Review", "abcdef", cookie_expiry_days=0)

#name, authentication_status, username = authenticator.login("Login", "main")

#if authentication_status == False:
 #   st.error("Username/password is incorrect")

#if authentication_status == None:
 #   st.warning("Please enter your username and password")

#if authentication_status:
   

# Importing data set
df = pd.read_csv('data.csv')
st.dataframe(df)
df.info()

# side bar
#authenticator.logout("Logout","sidebar")
#st.sidebar.title(f"Welcome{name}")

tab1 = st.tabs(["DASHBOARD"])

st.map(data=None, zoom=None, use_container_width=True)

# ---- SIDEBAR ----
st.sidebar.header("Please Filter Here:")
purpose_of_travel = st.sidebar.multiselect(
    "Select the purpose_of_travel:",
        options=df["purpose_of_travel"].unique(),
        default=df["purpose_of_travel"].unique()
    )

Gender = st.sidebar.multiselect(
        "Select the Customer Type:",
        options=df["Gender"].unique(),
        default=df["Gender"].unique(),
    )

satisfaction = st.sidebar.multiselect(
        "Select the satisfaction:",
        options=df["satisfaction"].unique(),
        default=df["satisfaction"].unique()
    )

Departure_Arrival_convenience= st.sidebar.multiselect(
        "Select the Customer Departure/Arrival  convenience:",
        options=df["Departure_Arrival_convenience"].unique(),
        default=df["Departure_Arrival_convenience"].unique(),
    )
df_selection = df.query(
        "purpose_of_travel == @purpose_of_travel & Gender  ==@Gender  & satisfaction == @satisfaction  &Departure_Arrival_convenience== @Departure_Arrival_convenience"
    )

    # ---- MAINPAGE ----
st.title(":bar_chart: European customers")
st.markdown("##")


st.write("***********************************************************************")
st.header('Box Plot')
col1,col2,col3,col4 =st.columns(4)
with col1:
        st.title('id')
        fig, ax = plt.subplots()
        ax.boxplot(df.iloc[:,0])
        st.pyplot(fig)
with col2:
            fig, ax = plt.subplots()
            ax.boxplot(df.iloc[:,2])
            st.pyplot(fig)
with col3:
        fig, ax = plt.subplots()
        ax.boxplot(df.iloc[:,6])
        st.pyplot(fig)
with col4:
        fig, ax = plt.subplots()
        ax.boxplot(df.iloc[:,7])
        st.pyplot(fig)


    #To make draw bar chart (satisfaction levels of people)
col1, col2 = st.columns(2)
with col1:
        
     t=df['satisfaction'].value_counts()
st.write(t)
with col2:
        st.header('satisfaction')
st.bar_chart(t)


    #
fig, ax = plt.subplots(2,2, figsize=(14, 12))
sns.countplot(data=df, x='Gender', hue='satisfaction', ax=ax[0][0])
sns.countplot(data=df, x='purpose_of_travel', hue='satisfaction', ax=ax[0][1])
sns.countplot(data=df, x='Type_of_Travel', hue='satisfaction', ax=ax[1][0])
sns.countplot(data=df, x='Type_Of_Booking', hue='satisfaction', ax=ax[1][1])
st.pyplot(fig)

    #
st.title("male female")
def df_countplot(df, target):
    f, axes = plt.subplots(1, 2, figsize=(15,5))
    ax1 = sns.countplot( x = target, data = df,  ax=axes[0])

    counts = df.groupby([target, 'satisfaction']).size().to_frame('Total')
    counts = counts.reset_index()
    ax2 = sns.barplot(data=counts, y='Total', x=target, hue='satisfaction', ax=axes[1])
    st.pyplot(f)
    #     return ax1

def pivot_satisfaction(df,target):
  df_rate = pd.pivot_table(
      df[['id',target,'satisfaction']],
      index       =[target],
      columns     =['satisfaction'],
      aggfunc     ="count",
      fill_value  =0,
  ).reset_index()

  df_rate.columns=[target,'neutral or dissatisfied','satisfied']

  df_rate['total'] = df_rate['neutral or dissatisfied'] + df_rate['satisfied']
  df_rate["satisfaction Rate"] = round((df_rate['satisfied']/df_rate['total'])*100,2)
  df_rate["dissatisfied Rate"] = round((df_rate['neutral or dissatisfied']/df_rate['total'])*100,2)
  return df_rate

    #
col1, col2 = st.columns(2)
with col1:
        
     t1=df['Gender'].value_counts()
st.write(t1)
with col2:
        st.header('Gender')
st.bar_chart(t1)

    #
st.title("Pupose of travel")
df_countplot(df,"purpose_of_travel")
t3=df['purpose_of_travel'].value_counts()
st.write(t3)

    #
st.title("Type of Travel")
df_countplot(df,"Type_of_Travel")
t4=df['Type_of_Travel'].value_counts()
st.write(t4)

    #
st.title("Type of Booking")
df_countplot(df,"Type_Of_Booking")
t4=df['Type_Of_Booking'].value_counts()
st.write(t4)

col1, col2 = st.columns(2)
with col1:
        
     t1=df['Gender'].value_counts()
st.write(t1)
with col2:
        st.header('Gender')
st.bar_chart(t1)

   
    #Numeric data visualization
st.title("numeric data viszalition")
fig, ax = plt.subplots(5,2, figsize=(14, 20))
sns.countplot(data=df, x='Hotel_wifi_service', hue='satisfaction', ax=ax[0][0])
sns.countplot(data=df, x='Departure_Arrival_convenience', hue='satisfaction', ax=ax[0][1])
sns.countplot(data=df, x='Ease_of_online_booking', hue='satisfaction', ax=ax[1][0])
sns.countplot(data=df, x='Hotel_location', hue='satisfaction', ax=ax[1][1])
sns.countplot(data=df, x='Food_and_drink', hue='satisfaction', ax=ax[2][0])
sns.countplot(data=df, x='Other_service', hue='satisfaction', ax=ax[2][1])
sns.countplot(data=df, x='Stay_comfort', hue='satisfaction', ax=ax[3][0])
sns.countplot(data=df, x='Common_Room_entertainment', hue='satisfaction', ax=ax[3][1])
sns.countplot(data=df, x='Checkin_Checkout_service', hue='satisfaction', ax=ax[4][0])
sns.countplot(data=df, x='Cleanliness', hue='satisfaction', ax=ax[4][1])
st.write(fig)

facet = sns.FacetGrid(df, hue = 'satisfaction', aspect = 4)
facet.map(sns.kdeplot, "Age", shade= True)
facet.add_legend()
st.pyplot(facet)

plt.rcParams["figure.figsize"] = [8,8]
plt.rcParams["figure.autolayout"] = True
sns.histplot(data = df, x = "Age", kde = True, hue = "satisfaction")

#Age and hotel wifi service
st.title("Age and hotel wife service")
df_countplot(df,"Hotel_wifi_service")
t5=df['Hotel_wifi_service'].value_counts()
st.write(t5)

#Age and common room entertaiment
st.title("Age and common room entertaiment")
df_countplot(df,"Common_Room_entertainment")
t6=df['Common_Room_entertainment'].value_counts()
st.write(t6)

 #Age and stay comfort
st.title("Age and stay comfort")
df_countplot(df,"Stay_comfort")
t7=df['Stay_comfort'].value_counts()
st.write(t7)

    #
def one_hot_encode (df_,variable,top_x_labels):
     for label in top_x_labels:
        df_[variable + '_' + label] = np.where(df[variable]==label,1,0)

    # Purpose_of_travel
one_hot = [x for x in df['purpose_of_travel'].value_counts().sort_values(ascending=False).head().index]
one_hot_encode(df,'purpose_of_travel',one_hot)
df = df.drop(['purpose_of_travel'], axis=1)

    # Type_of_travel
one_hot = [x for x in df['Type_of_Travel'].value_counts().sort_values(ascending=False).head().index]
one_hot_encode(df,'Type_of_Travel',one_hot)
df = df.drop(['Type_of_Travel'], axis=1)

# Type_of_booking
one_hot = [x for x in df['Type_Of_Booking'].value_counts().sort_values(ascending=False).head().index]
one_hot_encode(df,'Type_Of_Booking',one_hot)
df = df.drop(['Type_Of_Booking'], axis=1)

df = df.drop(['Age'], axis=1)


tab1 = st.tabs(["Feedback Form"])
st.header(":mailbox: Feedback Form for Customers!")

contact_form = """
<form action="https://formsubmit.co/shruti.dulu@gmail.com" method="POST">
     <input type="hidden" name="_captcha" value="false">
     <input type="text" name="name"placeholder="Your name" required>
     <input type="email" name="email" placeholder="Your email" required>
     <textarea name="message" placeholder="Your"></textarea>
     <button type="submit">Send</button>
</form>
"""

st.markdown(contact_form, unsafe_allow_html=True)

# Use Local CSS File
#def local_css(file_name):
#    with open(file_name) as f:
#        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


#local_css("style/style.css")




