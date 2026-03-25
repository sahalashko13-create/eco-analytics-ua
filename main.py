import streamlit as st
import pandas as pd
import folium
from streamlit_folium import st_folium
from sklearn.linear_model import LinearRegression
import numpy as np

# Назва додатка
st.set_page_config(page_title="Екологічна аналітика")
st.title("🌱 Веб-додаток: Екологічна аналітика")

# 1. ЗАВАНТАЖЕННЯ ДАНИХ
df = pd.read_csv('air_quality.csv')

# 2. ПОБУДОВА КАРТИ
st.subheader("Карта забруднення PM2.5 в Україні")
m = folium.Map(location=[48.3, 31.1], zoom_start=6)

latest_data = df[df['day'] == df['day'].max()]
for _, row in latest_data.iterrows():
    color = 'green' if row['pm25'] < 20 else 'red'
    folium.Marker(
        location=[row['lat'], row['lon']],
        popup=f"{row['city']}: {row['pm25']}",
        icon=folium.Icon(color=color)
    ).add_to(m)

# Відображаємо карту в Streamlit
st_folium(m, width=700, height=450)

# 3. АНАЛІЗ ТА ПРОГНОЗ
st.subheader("Аналіз трендів та Прогноз")
city = st.selectbox("Оберіть місто для прогнозу:", df['city'].unique())

city_data = df[df['city'] == city]
X = city_data[['day']].values
y = city_data['pm25'].values

model = LinearRegression()
model.fit(X, y)

prediction = model.predict([[4]])

st.write(f"📊 Поточний рівень PM2.5 у місті **{city}**: {y[-1]}")
st.success(f"🔮 Прогноз на завтра для міста **{city}**: {prediction[0]:.2f} PM2.5")

# Графік тренду
st.line_chart(city_data.set_index('day')['pm25'])