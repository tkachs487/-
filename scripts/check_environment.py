import os
import platform
import sys
from pathlib import Path

print("OS:", platform.platform())
print("Python:", sys.version.split()[0])
for name in ("PIL", "numpy", "cv2"):
    try:
        module = __import__(name)
        print(name, getattr(module, "__version__", "installed"))
    except ImportError:
        print(name, "not installed")
studio = os.getenv("AGF_STUDIO_PATH")
print("AGF Studio:", "path verified" if studio and Path(studio).is_file() else "not configured")
