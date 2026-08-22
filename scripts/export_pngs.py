import subprocess
import os
from pathlib import Path

CHROME = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
BASE = Path(r"C:\Users\smnk2\.gemini\antigravity\brain\752249c2-953d-4d40-a753-1ed6d83baaca\scratch\google-ecosystem-atlas\assets")

slides = [
    ("linkedin_slide_1.svg", "linkedin_slide_1.png", 1080, 1080),
    ("linkedin_slide_2.svg", "linkedin_slide_2.png", 1080, 1080),
    ("linkedin_slide_3.svg", "linkedin_slide_3.png", 1080, 1080),
    ("linkedin_slide_4.svg", "linkedin_slide_4.png", 1080, 1080),
    ("banner.svg", "banner.png", 1200, 630)
]

for svg_name, png_name, w, h in slides:
    svg_path = (BASE / svg_name).resolve()
    png_path = (BASE / png_name).resolve()
    
    cmd = [
        CHROME,
        "--headless",
        "--disable-gpu",
        f"--window-size={w},{h}",
        f"--screenshot={str(png_path)}",
        svg_path.as_uri()
    ]
    print(f"Rendering {svg_name} -> {png_name} ({w}x{h})...")
    res = subprocess.run(cmd, capture_output=True, text=True)
    if png_path.exists() and png_path.stat().st_size > 0:
        print(f"  SUCCESS: {png_name} ({png_path.stat().st_size} bytes)")
    else:
        print(f"  FAILED: {res.stderr}")

print("All PNG exports completed successfully!")
