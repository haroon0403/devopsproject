import time
from datetime import datetime

LOG_FILE = "/shared/log.txt"

while True:
    with open(LOG_FILE, "a") as f:
        f.write(f"Logger heartbeat at {datetime.now()}\n")
    time.sleep(5)

