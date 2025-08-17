import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent))

import uvicorn

if __name__ == "__main__":
    uvicorn.run("backend.main:app", host="localhost", port=8082, reload=True)
