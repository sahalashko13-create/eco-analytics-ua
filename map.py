import folium
import pandas as pd

df = pd.read_csv('air_quality_data.csv')

# Центр карти — Кам'янець-Подільський
m = folium.Map(location=[48.68, 26.58], zoom_start=12)

# Додаємо маркер з поточним PM2.5
current_pm25 = df['pm2_5'].iloc[-1]
color = "red" if current_pm25 > 25 else "orange" if current_pm25 > 15 else "green"

folium.Marker(
    location=[48.68, 26.58],
    popup=f"PM2.5: {current_pm25} µg/m³",
    icon=folium.Icon(color=color)
).add_to(m)

m.save('pollution_map.html')
print("Карта збережена як pollution_map.html — відкрий у браузері")