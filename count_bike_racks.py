import geopandas as gpd

# Load bike rack points and ward boundaries
bikes = gpd.read_file('Bike_Parking.geojson')
wards = gpd.read_file('wards.geojson')

# Ensure both are using the same coordinate reference system
bikes = bikes.set_crs('EPSG:4326')
wards = wards.to_crs('EPSG:4326')

# Spatial join: assign each bike rack to a ward
joined = gpd.sjoin(bikes, wards, how='left', predicate='intersects')
print(joined.columns)

# Count bike racks per ward
counts = joined.groupby('WARD_right').size().reset_index(name='BIKE_COUNT')

# Merge counts back into ward polygons
wards_with_counts = wards.merge(counts, left_on='WARD', right_on='WARD_right', how='left')
wards_with_counts.drop(columns='WARD_right', inplace=True)
wards_with_counts['BIKE_COUNT'] = wards_with_counts['BIKE_COUNT'].fillna(0).astype(int)

# Save to new GeoJSON
wards_with_counts.to_file('wards_with_counts.geojson', driver='GeoJSON')

print("✅ Created 'wards_with_counts.geojson' with bike rack counts.")