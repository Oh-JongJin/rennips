# rennips

A minimalist Python progress **spinner** that provides a simple visual feedback for iterative processes with normal and simple display modes.

\> "*rennips*" is simply 'spinner' spelled backwards. 



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

