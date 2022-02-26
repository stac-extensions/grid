# Grid Extension Specification

- **Title:** Grid
- **Identifier:** <https://stac-extensions.github.io/grid/v1.0.0/schema.json>
- **Field Name Prefix:** grid
- **Scope:** Item
- **Extension [Maturity Classification](https://github.com/radiantearth/stac-spec/tree/master/extensions/README.md#extension-maturity):** Proposal
- **Owner**: @philvarner

This document explains the Grid Extension to the [SpatioTemporal Asset Catalog](https://github.com/radiantearth/stac-spec) (STAC) specification.

The purpose of the Grid Extension is to provide fields related to gridded data products.

There are two main uses of the `grid:code` field defined in this specification. The first
is that it allows for precise aggregation in databases that support is of the number of
Items that exist for a specific grid square. 

slightly different footprints -- Landsat 8 are often off by a few pixels from each other.
MODIS sinusoidal is a continuous curve in EPSG:4326

Allow display of a pre-calculated geometry and a reasonable resolution?

- Examples:
  - [Item example](examples/item.json): Shows the basic usage of the extension in a STAC Item
- [JSON Schema](json-schema/schema.json)
- [Changelog](./CHANGELOG.md)

## Item Properties Fields

| Field Name | Type   | Description                                  |
| ---------- | ------ | -------------------------------------------- |
| grid:code  | string | **REQUIRED**. The identifier for the grid element associated with the Item. |

### Additional Field Information

#### grid:code

This is a much more detailed description of the field `grid:code`...

{grid}-{code}

##### Military Grid Reference System (MGRS)

- *Format String*: MGRS-{grid zone designator}{latitude band}{square}
- *Example*: MGRS-35NKA
- *Components*:
  - grid zone designator: UTM grid zone
  - latitude band: latitude band, lettered C-X (omitting the letters "I" and "O") 
  - square: a pair of letters designating one of the 100km side grid squares within the grid zone + latitude band square. 
- *Products*: Sentinel-2
- *Reference*: <https://en.wikipedia.org/wiki/Military_Grid_Reference_System>
- *Related Extensions*: <https://github.com/stac-extensions/mgrs>

##### MODIS Sinusoidal Tile Grid

- *Format String*: MSIN-{horizontal}{vertical}
- *Example*: MSIN-2506
- *Components*:
  - horizontal: horizontal tile number
  - vertical: vertical tile number
- *Products*: many MODIS products, including MCD43A4, MxD11A1, and MxD13A1
- *Reference*: <https://modis-land.gsfc.nasa.gov/MODLAND_grid.html>
- *Related Extensions*: none

##### Worldwide Reference System (WRS-1) 

- *Format String*: WRS1-{path}{row}
- *Example*: WRS1-097073
- *Components*:
  - path: path number for nominal satellite orbital track
  - row: latitudinal center line of a frame of imagery
- *Products*: Landsat 1-3
- *Reference*: <https://landsat.gsfc.nasa.gov/about/the-worldwide-reference-system/>
- *Related Extensions*: none

##### Worldwide Reference System (WRS-2) 

- *Format String*: WRS2-{path}{row}
- *Example*: WRS2-097073
- *Components*:
  - path: path number for nominal satellite orbital tracks
  - row: latitudinal center line of a frame of imagery
- *Products*: Landsat 4, 5, 7, 8, and 9
- *Reference*: <https://landsat.gsfc.nasa.gov/about/the-worldwide-reference-system/>
- *Related Extensions*: none

##### Digital Orthophoto Quadrangle

- *Format String*: DOQ-{quadrangle}
- *Example*: DOQ-3510836
- *Components*:
  - quadrangle: code for the 7.5-minute quad
- *Products*: early USGS digital aerial photographs and satellite images 
- *Reference*: <https://en.wikipedia.org/wiki/Digital_orthophoto_quadrangle>
- *Related Extensions*: none

Represents one U.S. Geological Survey (USGS) 7.5-minute quadrangle. The Digital
Orthophoto Quarter Quadrangle (DOQQ) represents one quarter of the quadrangle.
The names are based on that of the 7.5-minute quad.

##### Digital Orthophoto Quarter Quadrangle

- *Format String*: DOQ-{quadrangle}{quarter}
- *Example*: DOQ-3510836SE
- *Components*:
  - quadrangle: code for the 7.5-minute quad
  - quarter: NW, NE, SE, SW
- *Products*: NAIP
- *Reference*: <https://en.wikipedia.org/wiki/Digital_orthophoto_quadrangle>
- *Related Extensions*: none

Represents one U.S. Geological Survey (USGS) 7.5-minute quadrangle. The Digital Orthophoto
Quarter Quadrangle (DOQQ) represents one quarter of the quadrangle. The names are based on
that of the 7.5-minute quad, followed by NE, NW, SW, or SE for the DOQQ.

## Contributing

All contributions are subject to the
[STAC Specification Code of Conduct](https://github.com/radiantearth/stac-spec/blob/master/CODE_OF_CONDUCT.md).
For contributions, please follow the
[STAC specification contributing guide](https://github.com/radiantearth/stac-spec/blob/master/CONTRIBUTING.md) Instructions
for running tests are copied here for convenience.

### Running tests

The same checks that run as checks on PR's are part of the repository and can be run locally to verify that changes are valid. 
To run tests locally, you'll need `npm`, which is a standard part of any [node.js installation](https://nodejs.org/en/download/).

First you'll need to install everything with npm once. Just navigate to the root of this repository and on 
your command line run:
```bash
npm install
```

Then to check markdown formatting and test the examples against the JSON schema, you can run:
```bash
npm test
```

This will spit out the same texts that you see online, and you can then go and fix your markdown or examples.

If the tests reveal formatting problems with the examples, you can fix them with:
```bash
npm run format-examples
```
