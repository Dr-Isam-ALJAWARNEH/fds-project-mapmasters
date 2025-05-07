# Optimizing Sensor Locations in Urban Environments
### A Recommender System Based on Clustering and Multi-Source Data
 
This project analyzes the relationship between air quality (PM2.5) and urban mobility (taxi trip density) using spatio-temporal clustering techniques. It combines air pollution data and taxi activity data, performs feature engineering, and applies clustering algorithms to identify meaningful spatial regions and guide sensor placement.

##  Key Features  
- Temporal Aggregation: Groups both AQ and taxi data into 5-hour blocks to capture urban activity phases.
- Spatial Encoding: Uses Geohash for spatial grouping.
- Feature Engineering: Computes taxi density and average PM2.5 per region & time.
- Weighted Feature Creation: Combines mobility and pollution using a λ = 0.6 bias toward air quality.
- Clustering: Applies both DBSCAN and KMeans for spatial analysis.
- Evaluation: Uses Silhouette Score to assess cluster quality.
- Sensor Placement: Derives representative locations for air quality sensors from clustering results.
  
##  Technologies Used 
- Python (Pandas, NumPy, Matplotlib, scikit-learn)
- Geospatial Tools: pygeohash
- Clustering Algorithms: DBSCAN, KMeans
- Google Colab (for cloud-based execution)

##  How to Run 
1. Clone the repository
2. Install dependencies
3. Run the notebook:
    - Open clustering_analysis.ipynb in Jupyter Notebook or Google Colab.
    - Follow the code cells step by step to:
    - Load and merge data
    - Perform feature engineering
    - Apply clustering
    - Visualize results
    - Export sensor locations

##  Sample Output
- Clustered geospatial data by pollution and mobility.
- Geo-located sensor recommendations in sensor_candidates.csv.

##  Notes  
- The lambda = 0.6 weight was chosen to prioritize air quality over taxi density in cluster formation.
- Stratified sampling ensures spatial consistency in train-test splits.

---

