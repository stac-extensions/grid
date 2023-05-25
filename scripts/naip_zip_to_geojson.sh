#!/bin/bash

for f in *.zip
do
  [[ -e "$f" ]] || break
  unzip "$f"
done

for f in *.shp
do
  [[ -e "$f" ]] || break
  filename=$(basename -- "$f")
  filename_only="${filename%.*}"
  ogr2ogr -f GeoJSON -t_srs EPSG:4326 "$filename_only".geojson "$f"
done

for f in *.geojson
do
  [[ -e "$f" ]] || break
  filename=$(basename -- "$f")
  filename_only="${filename%.*}"
  echo "$filename"
  python ./grid_maker.py DOQQ APFONAME,QUADRANT 2 0 "$f" > "$filename_only.json"
done
