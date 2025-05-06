from flask import Flask, send_from_directory
app = Flask(__name__)

@app.route('/')
def home():
    return send_from_directory('.', 'index.html')

@app.route('/data/parks')
def get_parks():
    return send_from_directory('.', 'parks.geojson')

@app.route('/data/bikes')
def get_bikes():
    return send_from_directory('.', 'Bike_Parking.geojson')

@app.route('/data/wards')
def get_wards():
    return send_from_directory('.', 'wards_with_counts.geojson')

if __name__ == '__main__':
    app.run(debug=True)