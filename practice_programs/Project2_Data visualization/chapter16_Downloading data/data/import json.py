import json
from plotly.graph_objs import Scattergeo, Layout
from plotly import offline


filename = 'data/eq_1_day_m1.json'
with open(filename, encoding="utf-8")as f:
    all_eq_data = json.load(f)
    all_eq_dicts = all_eq_data['features']
    
    mags, lons, lats = [], [], []
    for eq_data in all_eq_dicts:
        mag = eq_data['properties']['mag']
        lon = eq_data['geometry']['coordinates'][0]
        lat = eq_data['geometry']['coordinates'][1]
        mags.append(mag)
        lons.append(lon)
        lats.append(lat)
        
print(mags[:10])
print(lons[:5])
print(lats[:5])
        
# Map the earthquakes.
data = [Scattergeo(lon=lons, lat=lats)]
my_layout = Layout(title='Global Earthquakes')

fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='global_earthquakes.html')
