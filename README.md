# Countries
This python script takes a YAML file with a list of countries you've visited or lived in, and will produce an SVG of the world with those countries highlighted.

## Usage
First install the dependencies:
```sh
```

Next, edit `countries.yaml` as desired.
Finally, you can run the following command:
```sh
python3 countries.py
```

Your svg file can be found in the current directory as `countries.svg`.
If hosting this online, I recommend passing the output through an SVG optimiser to remove around 60% of the file size.

## Acknowledgements
The geoJSON file was generated from https://geojson-maps.kyd.au.
