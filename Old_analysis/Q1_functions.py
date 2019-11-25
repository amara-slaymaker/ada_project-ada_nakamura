import folium
import json

def map_vizualization(data, geo_json_data, legend, location=[48, -102], zoom_start=2):
    map_ = folium.Map(location, zoom_start)
    map_.choropleth(geo_data=geo_json_data, data=data,
             columns=['id', 'Log Value'],
             key_on='feature.id',
             fill_color='BuPu', fill_opacity=0.7, line_opacity=0.2,
             legend_name=legend)
    map_