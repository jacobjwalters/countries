import yaml
import geopandas as gpd
import matplotlib.pyplot as plt
from matplotlib.patches import Patch

print("Loading configuration...")
with open("countries.yaml", "r") as file:
    data = yaml.safe_load(file)

lived_countries = data.get("Lived", [])
visited_countries = data.get("Visited", [])
resolution = data.get("Resolution", 1000)

lived_colour = data.get("Colours", {}).get("Lived", "#001604")
visited_colour = data.get("Colours", {}).get("Visited", "#00a871")
default_colour = data.get("Colours", {}).get("Default", "#f4f4f4")
background_colour = data.get("Colours", {}).get("Background", "#f5fffa")

print("Loading borders...")
file = data.get("File", "countries.geojson")
world = gpd.read_file(file).set_crs("EPSG:4326", allow_override=True).to_crs(epsg=3395)

print("Simplifying map...")
world["const"] = 0
world = world[world["COUNTRY"] != "Antarctica"]
world_geom = world.dissolve(by="const").geometry.simplify(resolution)

lived_geom = (
    world[world["COUNTRY"].isin(lived_countries)]
    .dissolve(by="const")
    .geometry.simplify(resolution)
)
visited_geom = (
    world[world["COUNTRY"].isin(visited_countries)]
    .dissolve(by="const")
    .geometry.simplify(resolution)
)

print("Generating output...")
fig, ax = plt.subplots(figsize=(14, 6))

world_geom.plot(ax=ax, color=default_colour)
visited_geom.plot(ax=ax, color=visited_colour, label="Visited")
lived_geom.plot(ax=ax, color=lived_colour, label="Lived in")

fig.set_facecolor(background_colour)
ax.set_axis_off()

visited_patch = Patch(color=visited_colour, label="Visited")
lived_patch = Patch(color=lived_colour, label="Lived in")

plt.legend(handles=[visited_patch, lived_patch], loc="lower left", frameon=False)

plt.savefig("countries.svg", format="svg", bbox_inches="tight")
print("Done. See `countries.svg` for output.")
