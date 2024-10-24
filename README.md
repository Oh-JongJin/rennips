# rennips

A simple and lightweight progress "**spinner**" for Python iterables, similar to tqdm.



## Installation

```bash
pip install progressive-spinner
```



## Usage

```python
import time
from src.rennips import rennips


data = [x for x in range(50)]
for i in rennips(data, desc="Counting...", mode="SIMPLE"):
    time.sleep(0.05)
```



## Features

- Simple spinner animation (|/-\)
- Progress percentage
- Item count
- Elapsed time
- Works with any iterable
- Support for iterables without known length

