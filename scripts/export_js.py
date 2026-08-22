import json
from pathlib import Path

base = Path(r"C:\Users\smnk2\.gemini\antigravity\brain\752249c2-953d-4d40-a753-1ed6d83baaca\scratch\google-ecosystem-atlas\data")
json_path = base / "google_ecosystem.json"
js_path = base / "google_ecosystem.js"

with open(json_path, "r", encoding="utf-8") as f:
    data = json.load(f)

with open(js_path, "w", encoding="utf-8") as f:
    f.write("window.GOOGLE_ECOSYSTEM_DATA = " + json.dumps(data) + ";\n")

print("Created google_ecosystem.js successfully.")
