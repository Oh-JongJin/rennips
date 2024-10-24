import time
from src.rennips import rennips


data = [x for x in range(50)]
for i in rennips(data, desc="Counting...", mode="SIMPLE"):
    time.sleep(0.05)
