# Optimizing Sensor Locations in Urban Environments  
### A Recommender System Based on Clustering and Multi-Source Data

##  Project Overview  
This project proposes a data-driven recommender system for optimal placement of air quality sensors in urban environments. By combining traffic density, industrial proximity, population exposure, and historical air quality data, the system identifies high-impact areas for sensor deployment. It uses clustering algorithms (K-Means, DBSCAN) and a weighted scoring system to recommend the most effective locations for environmental monitoring.

##  Team Members
- **Fatima Alketbi**  
- **Amna Alsuwaidi**
- **Ayesha Aldoobi**
- **Alanood ALMANSOORI**
  

##  Technologies and Tools   
- Google Colab / Jupyter Notebook  
- Libraries used for this project:  
  - `pandas`  
  - `geopandas`  
  - `matplotlib`  
  - `seaborn`  
  - `scikit-learn`  
  - `folium`  
  - `geopy`  
  - `shapely`

##  Dataset Requirements  
Place the datasets files in your working directory or upload them to your Colab environment  

##  How to Run the Project  
1. Open `code.ipynb` in Google Colab or Jupyter Notebook.  
2. Make sure all required datasets are uploaded.  
3. Run all cells in order:
   - Feature Engineering  
   - Clustering and Scoring  
   - Recommendation Mapping  
4. Final output:
   - Cluster visualizations  
   - Sensor recommendations  
   - An interactive map saved as `sensor_locations_map.html

##  Sample Output
- Scatter plots showing geohash-based sampling  
- Clustered regions highlighting sensor priority zones  
- Interactive HTML map displaying final recommended locations

##  Goal  
To support smart city planning and environmental health efforts by guiding efficient, data-backed sensor deployment.

---

