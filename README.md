# Grid Extension Specification <!-- omit in toc -->

- **Title:** Grid
- **Identifier:** <https://stac-extensions.github.io/grid/v1.1.0/schema.json>
- **Field Name Prefix:** grid
- **Scope:** Item
- **Extension [Maturity Classification](https://github.com/radiantearth/stac-spec/tree/master/extensions/README.md#extension-maturity):** Pilot
- **Owners**: @philvarner, @drwelby

---

- [Item Properties Fields](#item-properties-fields)
  - [Additional Field Information](#additional-field-information)
    - [grid:code](#gridcode)
      - [Military Grid Reference System (MGRS)](#military-grid-reference-system-mgrs)
      - [MODIS Sinusoidal Tile Grid](#modis-sinusoidal-tile-grid)
      - [Worldwide Reference System (WRS-1)](#worldwide-reference-system-wrs-1)
      - [Worldwide Reference System (WRS-2)](#worldwide-reference-system-wrs-2)
      - [Digital Orthophoto Quadrangle](#digital-orthophoto-quadrangle)
      - [Digital Orthophoto Quarter Quadrangle](#digital-orthophoto-quarter-quadrangle)
      - [Maxar ARD Tile Grid](#maxar-ard-tile-grid)
      - [EASE-DGGS](#ease-dggs)
      - [Copernicus Digital Elevation Model Grid](#copernicus-digital-elevation-model-grid)
      - [EEA Reference Grid](#eea-reference-grid)
- [Contributing](#contributing)
- [Running tests](#running-tests)
- [Grid Maps](#grid-maps)
  - [Landsat (WRS2)](#landsat-wrs2)
  - [Sentinel-2 (MGRS)](#sentinel-2-mgrs)
  - [Copernicus DEM (CDEM)](#copernicus-dem-cdem)
  - [NAIP (DOQQ)](#naip-doqq)

This document explains the Grid Extension to the [SpatioTemporal Asset Catalog](https://github.com/radiantearth/stac-spec) (STAC) specification.

The purpose of the Grid Extension is to provide fields related to gridded data products.

There are two main uses of the `grid:code` field defined in this specification. Both are
primarily for use in supporting a path for a user exploring a dataset from a UI where there
are too many results to display individually, where the user must first be presented with
summary / aggregated data, and then drill down to individual items.

The first
is that it allows for precise aggregation in a STAC API implementation of Items that cover
the same grid area. The STAC API [Aggregation Extension](https://github.com/radiantearth/stac-api-spec/pull/36)
is a work-in-progress, but will eventually support aggregating over this field.

The second aspect is that it helps for display to a user when a gridded dataset has Items
that have slightly different footprints for Items over the same grid square. For example,
Landsat 8 scenes for the same path/row grid square are often off by a few pixels from each
other, which makes them not match exactly. Some products with grids that are significantly
different from EPSG:4326 have footprints that are far from a square after reprojection, such
how MODIS sinusoidal grid squares become increasingly curved as they move away from the
equator and meridan. This can make the GeoJSON Polygon large, as more points must be added to
maintain an accurate reprojected shape. With a grid code defined for an Item, a UI could have
a pre-determined geometry at a reasonable resolution for that grid square, and display it
once for each all the Items in that grid square.

- Examples:
  - [Item example](examples/item.json): Shows the basic usage of the extension in a STAC Item
- [JSON Schema](json-schema/schema.json)
- [Changelog](./CHANGELOG.md)

## Item Properties Fields

| Field Name | Type   | Description                                                                 |
| ---------- | ------ | --------------------------------------------------------------------------- |
| grid:code  | string | **REQUIRED**. The identifier for the grid element associated with the Item. |

### Additional Field Information

#### grid:code

The field `grid:code` defines a unique value for each grid square in a gridding. The code
will be of the form `{grid designation}-{grid square code}`, where the grid designation is a
short alphanumeric code for the grid (e.g., MGRS) and code is a short encoded value for a
specific grid square. The encoded value for the square should consist of uppercase
alphanumeric characters, underscore (`_`) (preferred separator), or minus sign (`-`).

The grid code values below are recommended for these products. Implementers may also devise
proprietary systems for their own griddings.

##### Military Grid Reference System (MGRS)

- *Format String*: `MGRS-{grid zone designator}{latitude band}{square}`
- *Examples*: MGRS-35NKA, MGRS-35NKA1234, MGRS-35NKA123456, MGRS-35NKA12345678, MGRS-35NKA1234567890
- *Components*:
  - `grid zone designator`: UTM grid zone
  - `latitude band`: latitude band, lettered C-X (omitting the letters "I" and "O")
  - `square`: a pair of letters designating one of the 100km side grid squares within the grid
    zone and latitude band square, and optionally either 2, 4, 6, 8, or 10 additional digits
- *Products*: Sentinel-2
- *Reference*: <https://en.wikipedia.org/wiki/Military_Grid_Reference_System>
- *Related Extensions*: <https://github.com/stac-extensions/mgrs>

##### MODIS Sinusoidal Tile Grid

- *Format String*: `MSIN-{horizontal}{vertical}`
- *Example*: MSIN-2506
- *Components*:
  - `horizontal`: horizontal tile number
  - `vertical`: vertical tile number
- *Products*: many MODIS products, including MCD43A4, MxD11A1, and MxD13A1
- *Reference*: <https://modis-land.gsfc.nasa.gov/MODLAND_grid.html>

##### Worldwide Reference System (WRS-1)

- *Format String*: `WRS1-{path}{row}`
- *Example*: WRS1-097073
- *Components*:
  - `path`: path number for nominal satellite orbital track
  - `row`: latitudinal center line of a frame of imagery
- *Products*: Landsat 1-3
- *Reference*: <https://landsat.gsfc.nasa.gov/about/the-worldwide-reference-system/>

##### Worldwide Reference System (WRS-2)

- *Format String*: `WRS2-{path}{row}`
- *Example*: WRS2-097073
- *Components*:
  - `path`: path number for nominal satellite orbital tracks
  - `row`: latitudinal center line of a frame of imagery
- *Products*: Landsat 4, 5, 7, 8, and 9
- *Reference*: <https://landsat.gsfc.nasa.gov/about/the-worldwide-reference-system/>

##### Digital Orthophoto Quadrangle

Represents one U.S. Geological Survey (USGS) 7.5-minute quadrangle.
The names are based on that of the 7.5-minute quad.

- *Format String*: DOQ-{quadrangle}
- *Example*: DOQ-3510836
- *Components*:
  - `quadrangle`: code for the 7.5-minute quad
- *Products*: early USGS digital aerial photographs and satellite images
- *Reference*: <https://en.wikipedia.org/wiki/Digital_orthophoto_quadrangle>

##### Digital Orthophoto Quarter Quadrangle

Represents one U.S. Geological Survey (USGS) 7.5-minute quadrangle. The Digital Orthophoto
Quarter Quadrangle (DOQQ) represents one quarter of the quadrangle. The names are based on
that of the 7.5-minute quad, followed by NE, NW, SW, or SE for the DOQQ.

- *Format String*: `DOQQ-{quadrangle}{quarter}`
- *Example*: DOQQ-3510836SE
- *Components*:
  - `quadrangle`: code for the 7.5-minute quad
  - `quarter`: NW, NE, SE, SW
- *Products*: NAIP
- *Reference*: <https://en.wikipedia.org/wiki/Digital_orthophoto_quadrangle>

##### Maxar ARD Tile Grid

- *Format String*: `MXRA-Z{zone}-{quadkey}`
- *Example*: MXRA-Z14-120200003323
- *Components*:
  - `zone`: UTM zone
  - `quadkey`: 12-digit quadkey identifier
- *Products*: Maxar ARD images and derivatives
- *Reference*: [Maxar ARD Documentation](https://ard.maxar.com/docs/about/#the-maxar-data-grid)

##### EASE-DGGS

- *Format String*: `EASE-DGGS-L{level}.{row-column for each level}`
- *Example*: EASE-DGGS-L0.405963, EASE-DGGS-L6.405963.33.22.22.99.99.99
- *Components*:
  - `level`: Grid refinement level. Ranges from 0 to 6 with 6 being the most granular level.
  - `row-column for each level`: Grid cell row-column for each level in ascending level order (level 0 first), separated by ".".
- *Products*: unknown
- *Reference*: <https://www.tandfonline.com/doi/pdf/10.1080/20964471.2021.2017539>

##### Copernicus Digital Elevation Model Grid

- *Format String*: `CDEM-{northing}{easting}`
- *Example*: CDEM-S90W178
- *Components*:
  - `northing`: latitude coordinate in decimal degrees without the decimal `_00` part, e.g., `S50`.
  - `easting`: longitude coordinate in decimal degrees without the decimal `_00` part, e.g., `W125`.
- *Products*: Copernicus DEM GLO-30, GLO-90, and EEA-10 products in DGED format
- *Reference*: [Copernicus DEM Product Handbook](https://dataspace.copernicus.eu/sites/default/files/media/files/2024-06/geo1988-copernicusdem-spe-002_producthandbook_i5.0.pdf)

##### EEA Reference Grid

- *Format String*: `EEA-{resolution}{easting}{northing}`
- *Example*: EEA-100kmE31N36
- *Components*:
  - `resolution`: Recommended grid resolutions are `100m`, `1km`, `10km` and `100km`.
    Alternatively, `25m` or `250m` resolution can be used for analysis purposes,
    where the standard `100m` or `1km` grid cell size is not appropriate.
    The resolution is denoted in meter (`m`) for cell sizes below 1000 meters and
    kilometre (`km`) for cell sizes from 1000 meters and above.
  - `northing` and `easting`: Reflects the distance of the lower left grid cell corner
    from the false origin of the CRS. In order to reduce the length of the string,
    Easting (`E`) and Northing (`N`) values are divided by $10^n$
    (where $n$ is the number of zeros in the cell size value).
- *Products*: CLMS datasets, e.g. CLMS High Resolution Layer Tree Cover and Forests
- *Reference*: [About the EEA reference grid, Hermann Peifer, EEA, September 2011](https://www.eea.europa.eu/data-and-maps/data/eea-reference-grids-1/about-the-eea-reference-grid/eea_reference_grid_v1.pdf/at_download/file)
- *Related Extensions*: none

## Contributing

All contributions are subject to the
[STAC Specification Code of Conduct](https://github.com/radiantearth/stac-spec/blob/master/CODE_OF_CONDUCT.md).
For contributions, please follow the
[STAC specification contributing guide](https://github.com/radiantearth/stac-spec/blob/master/CONTRIBUTING.md) Instructions
for running tests are copied here for convenience.

## Running tests

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

## Grid Maps

This describes how to generate files that define the mapping from a grid code to
a geometry / footprint. The intention with these files is that they are used in
a web UI for displaying the footprint of a scene from a grid id, typically in
conjunction with the STAC API Aggregation Extension.

Because these files are intended to be downloaded by a web UI, creating a file that
is as small as possible is a primary concern. Compression (via either gzip or
brotli) is typically handled by the web server they are served from, but we want
to start with as small a file as possible before that. 

A few of the optimizations these use are:

1. The prefix is a separate field, and only the unique idenifier part is specified
   in the `cells` list. This cuts all of the duplicate instances of the prefix from the file.
2. Instead of a complete GeoJSON geometry defintion, only the coordinates are used. This cuts 
   all of the duplicate instances of the type field from the file.
3. Coordinate precision is set to 2 decimal places, which means it varies by no more than 1km at the equator.
4. JSON is output in compact mode, with no line breaks, indentation, or spaces around the `:` and `,` characters.

### Landsat (WRS2)

- [Landsat Landsat WRS 2 Descending Path Row Shapefile | U.S. Geological Survey](https://www.usgs.gov/media/files/landsat-wrs-2-descending-path-row-shapefile)

These are defined as Polygons or MultiPolygons (across the antimeridian), and are all converted to MultiPolygons.

```bash
curl -O https://d9-wret.s3.us-west-2.amazonaws.com/assets/palladium/production/s3fs-public/atoms/files/WRS2_descending_0.zip
unzip WRS2_descending_0.zip
ogr2ogr -f GeoJSON -t_srs EPSG:4326 wrs2.geojson WRS2_descending.shp
python ./scripts/grid_maker.py WRS2 PR 2 1 wrs2.geojson > grid_maps/wrs2.json
```

### Sentinel-2 (MGRS)

- [Sentinel-2 scene boundaries](https://sentinels.copernicus.eu/documents/247904/1955685/S2A_OPER_GIP_TILPAR_MPC__20151209T095117_V20150622T000000_21000101T000000_B00.kml)

This are defined as a GeometryCollection of Polygon and Points, which this converts to MultiPolygons.
Antimeridan-spanning cells are handled with multiple Polygons.

```bash
curl -O https://sentinels.copernicus.eu/documents/247904/1955685/S2A_OPER_GIP_TILPAR_MPC__20151209T095117_V20150622T000000_21000101T000000_B00.kml
ogr2ogr -f GeoJSON -t_srs EPSG:4326 mgrs.geojson S2A_OPER_GIP_TILPAR_MPC__20151209T095117_V20150622T000000_21000101T000000_B00.kml
python scripts/grid_maker.py MGRS Name 3 0 mgrs.geojson > grid_maps/mgrs.json
```

### Copernicus DEM (CDEM)

- [COP-DEM](https://spacedata.copernicus.eu/documents/20123/122407/GEO1988-CopernicusDEM-RP-002_GridFile_I4.0_ESA.zip)

These are all Polygons and have no antimeridian-spanning cells.

```bash
curl -O https://spacedata.copernicus.eu/documents/20123/122407/GEO1988-CopernicusDEM-RP-002_GridFile_I4.0_ESA.zip
unzip GEO1988-CopernicusDEM-RP-002_GridFile_I4.0_ESA.zip
ogr2ogr -f GeoJSON -t_srs EPSG:4326 cdem.geojson GEO1988-CopernicusDEM-RP-002_GridFile_I4.0_ESA.shp/GEO1988-CopernicusDEM-RP-002_GridFile_I4.0_ESA.shp
python scripts/grid_maker.py CDEM GeoCellID 0 0 cdem.geojson > grid_maps/cdem.json
```

### NAIP (DOQQ)

- [NAIP: NAIP Quarter Quad and Seamline Shapefiles](https://www.fpacbc.usda.gov/geo/customer-service/naip-quarter-quad-shapefiles/index.html)

These are all Polygons and within CONUS (no antimeridian-spanning cells).

To process:

1. Download all 48 (AK and HI are excluded) from
  [NAIP: NAIP Quarter Quad and Seamline Shapefiles](https://www.fpacbc.usda.gov/geo/customer-service/naip-quarter-quad-shapefiles/index.html)
  and put them in the scripts directory.
2. run:

```bash
cd scripts
./naip_zip_to_geojson.sh
./naip_merge.py > grid_maps/doqq.json
```

In the Tennessee 2018 geometries, NW3408508 is set with a null geometry. However,
this grid cell overlaps with Georgia, so it's picked up from those definitions.
