import geopandas as gpd
import pandas as pd
import os
import matplotlib.pyplot as plt

shapefile = 'data/raw/DL_FIRE_SV/fire_nrt_SV-C2_630778.shp'
if not os.path.exists(shapefile):
    raise FileNotFoundError(f"Shapefile not found: {shapefile}")
# Load the shapefile
wildfire_data = gpd.read_file(shapefile)

# Check the first few rows of the data
print(wildfire_data.head())
# Check the columns of the data
print(wildfire_data.columns)

#Filter places where brightness is greater than 330
wildfire_filtered = wildfire_data[wildfire_data['BRIGHTNESS'] > 330]

#plot the filtered data using matplotlib
wildfire_filtered.plot(column='BRIGHTNESS', cmap='hot', legend=True, figsize=(10, 10))
plt.title('Wildfire Brightness')
plt.xlabel('LONGITUDE')
plt.ylabel('LATITUDE')
plt.savefig('outputs/maps/wildfire_brightness_map.png', dpi=300)
# Show the plot
#plt.show()

# Save the filtered data to a CSV file
output_csv = 'outputs/wildfire_filtered_data.csv'
wildfire_filtered.to_csv(output_csv, index=False)
# Print confirmation message
print(f"Filtered wildfire data saved to {output_csv}")