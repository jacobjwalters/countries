import yaml
import geopandas as gpd
import matplotlib.pyplot as plt
from matplotlib.patches import Patch

with open('visited_countries.yaml', 'r') as file:
    data = yaml.safe_load(file)

lived_countries = data.get('Lived', [])
visited_countries = data.get('Visited', [])

hl  = data.get('Colours', {}).get('Lived', '#11f48e')
hl2 = data.get('Colours', {}).get('Visited', '#b7f4d9')
bg  = data.get('Colours', {}).get('Default', '#f4f4f4')

file = data.get('File', 'countries-110m.geojson')
world = gpd.read_file(file).set_crs('ESRI:53001', allow_override=True).to_crs(epsg=3395)

world = world[world['name'] != 'Antarctica']
lived_geom = world[world['name'].isin(lived_countries)]
visited_geom = world[world['name'].isin(visited_countries)]


fig, ax = plt.subplots(figsize=(14, 6))
world.plot(ax=ax, color=bg)
visited_geom.plot(ax=ax, color=hl2, label='Visited', legend=True)
lived_geom.plot(ax=ax, color=hl, label='Lived in', legend=True)
ax.set_axis_off()

visited_patch = Patch(color=hl2, label='Visited')
lived_patch = Patch(color=hl, label='Lived in')
plt.legend(handles=[visited_patch, lived_patch], loc='lower left', frameon=False)

plt.savefig('countries.svg', format='svg', bbox_inches='tight')
