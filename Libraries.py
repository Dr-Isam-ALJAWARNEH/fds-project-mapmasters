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