import json

features = []
for lat in range(-90, 90):
    edge = max(abs(lat), abs(lat + 1))
    width = 1 if edge <= 60 else 2 if edge <= 80 else 4
    for lon in range(-180, 180, width):
        code = f"{'N' if lat >= 0 else 'S'}{abs(lat):02d}{'E' if lon >= 0 else 'W'}{abs(lon):03d}"
        ring = [[lon, lat], [lon + width, lat], [lon + width, lat + 1], [lon, lat + 1], [lon, lat]]
        features.append({"type": "Feature", "properties": {"code": code},
                         "geometry": {"type": "Polygon", "coordinates": [ring]}})

print(json.dumps({"type": "FeatureCollection", "features": features}))
