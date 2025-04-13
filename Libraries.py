# IN THIS PART I added the needed libraries
!pip install pygeohash
# Import Required Libraries
import os
import pandas as pd
import numpy as np
import geopandas as gpd
from sklearn.cluster import DBSCAN
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import mean_absolute_error
from geopy.distance import great_circle
import pygeohash as pgh
import folium
from folium.plugins import MarkerCluster
import matplotlib.pyplot as plt
import seaborn as sns
from shapely.geometry import Point
from shapely.ops import nearest_points
from google.colab import drive

# Step 1: Mount Drive & Load AQ and Taxi Data
 
# Mount Google Drive
drive.mount('/content/drive')
 
# Set path to datasets folder
base_path = '/content/drive/MyDrive/Datasets/'
 
# Load All Air Quality (AQ) Data
aq_dfs = []
 
# Loop through AQ_data_1.csv to AQ_data_19.csv
for i in range(1, 20):
    file_path = os.path.join(base_path, f"AQ_data_{i}.csv")
 
    if os.path.exists(file_path):
        df = pd.read_csv(file_path)
 
        # Rename and keep relevant columns
        df = df.rename(columns={
            'Latitude': 'latitude',
            'Longitude': 'longitude',
            'ReadingDateTimeUTC': 'timestamp',
            'PM25': 'pm25'
        })
        df = df[['latitude', 'longitude', 'timestamp', 'pm25']]
 
        # Print record count of the current AQ dataset
        print(f"✅ Loaded AQ_data_{i}.csv with {len(df)} records")
 
        aq_dfs.append(df)
    else:
        print(f" File not found: {file_path}")
 
# Combine all AQ files into a single DataFrame
aq_df = pd.concat(aq_dfs, ignore_index=True)
print(" Preview of Combined AQ Data:")
print(aq_df.head())
print(f" Total AQ Records Loaded: {len(aq_df)}")
 
# Load All Taxi Trips Data
taxi_file_path = os.path.join(base_path, 'Taxi_Trips.csv')
 
taxi_df = pd.read_csv(taxi_file_path, usecols=[
    'Trip Start Timestamp',
    'Trip Seconds',
    'Trip Miles',
    'Pickup Centroid Latitude',
    'Pickup Centroid Longitude'
])
 
# Rename columns for consistency
taxi_df = taxi_df.rename(columns={
    'Trip Start Timestamp': 'trip_start_timestamp',
    'Pickup Centroid Latitude': 'pickup_latitude',
    'Pickup Centroid Longitude': 'pickup_longitude',
    'Trip Seconds': 'trip_seconds',
    'Trip Miles': 'trip_miles'
})
 
print("\n✅ Preview of Taxi Trips Data:")
print(taxi_df.head())
print(f"✅ Total Taxi Records Loaded: {len(taxi_df)}")
