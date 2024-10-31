import time
import argparse
from rennips import rennips


parser = argparse.ArgumentParser(description="rennips mode selector")

mode_group = parser.add_mutually_exclusive_group()
mode_group.add_argument("-n", "--normal", action="store_true", help="Run normal mode")
mode_group.add_argument("-s", "--simple", action="store_true", help="Run simple mode")
mode_group.add_argument("-b", "--big", action="store_true", help="Run big mode")

args = parser.parse_args()

if args.simple:
    mode = "simple"
elif args.big:
    mode = "big"
else:
    mode = "normal"


data = [x for x in range(50)]
for i in rennips(data, desc="Counting...", mode=mode):
    time.sleep(0.05)
