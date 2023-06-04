# NamedTreemap

jax.tree_map, but for all datatypes and with input names

## Getting Started

### Installation

```BASH
python3 -m pip install namedtreemap
```

### Examples

```PYTHON
import namedtreemap as ntm
from typing import Tuple, Any


def fn(prefix: Tuple[Any, ...], *items):
    print(prefix, items)
    return items[0] + 1


obj = {"3": {"2": [1, 2]}, "1": (0,)}
print("Original:", obj)  # Original: {'3': {'2': [1, 2]}, '1': (0,)}
obj = ntm.named_treemap(fn, obj, obj)
# ('3', '2', 0) (1, 1)   -   0 (int) is a list index
# ('3', '2', 1) (2, 2)   -   1 (int) is a list index
# ('1', 0.0) (0, 0)      -   0.0 (float) is a tuple index
print("Modified:", obj)  # Modified: {'3': {'2': [2, 3]}, '1': (1,)}
```