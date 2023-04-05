import glob
import json


merged_contents = {"type": "Polygon", "prefix": "DOQQ", "cells": {}}

for fn in glob.glob("*.json"):
    with open(fn, "r") as f:
        merged_contents["cells"].update(json.loads(f.read())["cells"])

print(json.dumps(merged_contents, separators=(",", ":")))
