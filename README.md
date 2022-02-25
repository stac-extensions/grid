# Grid Extension Specification

- **Title:** Grid
- **Identifier:** <https://stac-extensions.github.io/grid/v1.0.0/schema.json>
- **Field Name Prefix:** grid
- **Scope:** Item
- **Extension [Maturity Classification](https://github.com/radiantearth/stac-spec/tree/master/extensions/README.md#extension-maturity):** Proposal
- **Owner**: @philvarner

This document explains the Grid Extension to the [SpatioTemporal Asset Catalog](https://github.com/radiantearth/stac-spec) (STAC) specification.

TODO

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

- *Format String*: MSIN-H{horizontal}V{vertical}
- *Example*: MSIN-H25V06
- *Components*:
  - horizontal:
  - vertical:
- *Products*: many MODIS products, including MCD43A4, MxD11A1, and MxD13A1
- *Reference*: <https://modis-land.gsfc.nasa.gov/MODLAND_grid.html>
- *Related Extensions*: none

##### Worldwide Reference System (WRS-1) 

- *Format String*: WRS1-{path}{row}
- *Example*: WRS1-097073
- *Components*:
  - path:
  - row:
- *Products*: Landsat 1-3
- *Reference*: <https://landsat.gsfc.nasa.gov/about/the-worldwide-reference-system/>
- *Related Extensions*: none

##### Worldwide Reference System (WRS-2) 

- *Format String*: WRS2-{path}{row}
- *Example*: WRS2-097073
- *Components*:
  - path:
  - row:
- *Products*: Landsat 4, 5, 7, 8, and 9
- *Reference*: <https://landsat.gsfc.nasa.gov/about/the-worldwide-reference-system/>
- *Related Extensions*: none

##### Digital Orthophoto Quadrangle

- *Format String*: DOQ-{quadrangle}
- *Example*: DOQ-3510836
- *Components*:
  - quadrangle:
- *Products*: early USGS digital aerial photographs and satellite images 
- *Reference*: <https://en.wikipedia.org/wiki/Digital_orthophoto_quadrangle>
- *Related Extensions*: none

It represents one U.S. Geological Survey (USGS) 7.5-minute quadrangle. The Digital Orthophoto Quarter Quadrangle, (DOQQ) represents one quarter of the quadrangle. The names are based on that of the 7.5-minute quad

##### Digital Orthophoto Quarter Quadrangle

- *Format String*: DOQ-{quadrangle}{quarter}
- *Example*: DOQ-3510836SE
- *Components*:
  - quadrangle:
  - quarter: NW, NE, SE, SW
- *Products*: NAIP
- *Reference*: <https://en.wikipedia.org/wiki/Digital_orthophoto_quadrangle>
- *Related Extensions*: none

It represents one U.S. Geological Survey (USGS) 7.5-minute quadrangle. The Digital Orthophoto Quarter Quadrangle, (DOQQ) represents one quarter of the quadrangle. The names are based on that of the 7.5-minute quad, followed by NE, NW, SW, or SE for the DOQQ. The DOQQ’s scale is 1:12,000 scale or 1"=1,000', with 1-meter pixel resolution, and accuracy of +/ 33 feet. Individual states may have DOQ's that have higher accuracy standards depending on additional post-processing.

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
