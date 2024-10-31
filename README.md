# rennips

A minimalist Python progress **spinner** that provides a simple visual feedback for iterative processes with normal and simple display modes.

\> "*rennips*" is simply 'spinner' spelled backwards. 

Check out on [**PyPI**](https://pypi.org/project/rennips/0.1.0/)



## Installation

```bash
pip install rennips
```



## Usage

```python
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
```



## Features

- Simple spinner animation (**|, /, -, \\**)
- Progress percentage
- Item count
- Elapsed time
- Works with any iterable
- Support for iterables without known length



## Roadmap

Future features and improvements planned for Rennips:

### Short-term Goals
- [x] Big mode: ~~Large-scale spinner display for better visibility in terminal~~ Big spinner animation
- [ ] Manual spinner control: Support for non-iterable progress tracking, allowing start/stop/update operations
