
import os
from pathlib import Path

folder = "logs"
markerImages = Path(folder).iterdir()
for mi in markerImages:
    fileName = str(mi)
    os.remove(fileName)