import json
from typing import Any, Optional
from collections.abc import Sequence
import sys
from shapely import MultiPolygon
from shapely.geometry import mapping, shape

# Accepts these parameters
# 1 - The grid code prefix (e.g., WRS2)
# 2 - A comma-separated value in the Feature Properties that is the unique grid code value
# 3 - decimal precision, defaulting to 2
# 4 - The input GeoJSON FeatureCollection filename


def recursive_map(seq, func):
    for item in seq:
        if isinstance(item, Sequence):
            yield type(item)(recursive_map(item, func))
        else:
            yield func(item)


def geometry_type(type_: Optional[str]) -> Optional[str]:
    if not type_:
        print("Error: null geometry", file=sys.stderr)
        return None
    elif type_ in ["Polygon", "MultiPolygon"]:
        return type_
    elif type_ == "GeometryCollection":
        return "MultiPolygon"
    else:
        return None


def deduplicate_linestring(linestring: list[(float, float)]):
    return list(dict.fromkeys(((x[0], x[1]) for x in linestring)))


def simplify_geometry(
    geometry: dict[str, Any], decimal_precision: int, force_multipolygons: bool
) -> Optional[dict[str, Any]]:
    modified_geometry = None

    if not geometry:
        print("Error: null geometry", file=sys.stderr)
    elif geometry["type"] in ["Polygon", "MultiPolygon"]:
        coordinates = list(
            recursive_map(
                geometry["coordinates"],
                lambda x: round(x, decimal_precision)
                if decimal_precision
                else round(x),
            )
        )
        type_ = geometry["type"]
        if geometry["type"] == "Polygon":
            coordinates = [deduplicate_linestring(c) for c in coordinates]
            if force_multipolygons:
                type_ = "MultiPolygon"
                coordinates = [coordinates]
        else:  # MultiPolygon
            coordinates = [
                [deduplicate_linestring(c2) for c2 in c1] for c1 in coordinates
            ]
        modified_geometry = {
            "type": type_,
            "coordinates": coordinates,
        }
    elif geometry["type"] == "GeometryCollection":
        # used by Sentinel-2 grids
        # Extract the Polygons and make them into MultiPolygons
        modified_geometry = mapping(
            MultiPolygon(
                [
                    shape(simplify_geometry(g, decimal_precision, force_multipolygons))
                    for g in geometry["geometries"]
                    if g["type"] == "Polygon"
                ]
            )
        )

    return modified_geometry


prefix = sys.argv[1]
fields = sys.argv[2].split(",")
decimal_precision = int(sys.argv[3])
force_multipolygons = sys.argv[4] == "1"
filename_in = sys.argv[5]

with open(filename_in, "r") as f:
    geojson = json.loads(f.read())

grid_mapping = {
    "prefix": prefix,
    "cells": {
        f'{"".join(f["properties"][x] for x in fields)}': simplify_geometry(
            f["geometry"], decimal_precision, force_multipolygons
        )["coordinates"]
        for f in geojson["features"]
        if f.get("geometry")
    },
}

if force_multipolygons:
    grid_mapping["type"] = "MultiPolygon"
elif len(types := set(f["geometry"]["type"] for f in geojson["features"])) == 1:
    grid_mapping["type"] = geometry_type(types.pop())

print(json.dumps(grid_mapping, separators=(",", ":")))
