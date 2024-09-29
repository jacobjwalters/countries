# Countries
This python script takes a YAML file with a list of countries you've visited or lived in, and will produce an SVG of the world with those countries highlighted.

## Usage
First install the dependencies:
```sh
pip install -r requirements.txt
```

Next, edit `countries.yaml` as desired.
Finally, you can run the following command:
```sh
python3 countries.py
```

Your svg file can be found in the current directory as `countries.svg`.
If hosting this online, I recommend passing the output through an SVG optimiser to remove around 60% of the file size. [SVGOMG](https://svgomg.net/) works well for this.

## Acknowledgements
The current geoJSON file is [Esri's World Countries Generalised](https://hub.arcgis.com/datasets/esri::world-countries-generalized) dataset. Previously, I used a build of Natural Earth's `countries-110m`, but this had many issues with borders (Crimea being displayed as russian territory instead of Ukrainian, French Guyana being displayed as part of France, etc). The new file is much more detailed, and has corrrect borders. You can adjust the scale (and resulting file size) in `countries.yaml`.
