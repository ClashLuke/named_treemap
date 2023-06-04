import typing
from typing import Dict, Callable, Any

KeyType = typing.TypeVar("KeyType")
InValueType = typing.TypeVar("InValueType")
OutValueType = typing.TypeVar("OutValueType")


def named_flatten(*x: Any, prefix=()) -> Dict[KeyType, InValueType]:
    if not isinstance(x[0], (dict, list, tuple)):
        return {prefix: x}
    if isinstance(x[0], dict):
        keys = x[0].keys()
    elif isinstance(x[0], (list, tuple)):
        keys = range(len(x[0]))
    out = {}
    for key in keys:
        appended = float(key) if isinstance(x[0], tuple) else key
        out.update(named_flatten(*[val[key] for val in x], prefix=prefix + (appended,)))
    return out


def _unflatten(dct: Any) -> Any:
    if not isinstance(dct, dict):
        return dct
    for key in dct.keys():
        break
    else:
        return dct
    if isinstance(key, str):
        return {k: _unflatten(v) for k, v in dct.items()}
    out = [_unflatten(v) for k, v in sorted(dct.items())]
    if isinstance(key, int):
        return out
    return tuple(out)


def named_unflatten(values: Dict[KeyType, InValueType]) -> Any:
    out = {}
    if not values:
        return values
    for prefix, val in values.items():
        if not prefix:  # one item
            return val
        tmp = out
        for key in prefix[:-1]:
            if isinstance(key, str):
                if key not in tmp:
                    tmp[key] = {}
            tmp = tmp[key]
        tmp[prefix[-1]] = val
    return _unflatten(out)


def dict_map_name(fn: Callable[[KeyType, InValueType], OutValueType], x: Dict[KeyType, InValueType]  #
                  ) -> Dict[KeyType, OutValueType]:
    return {k: fn(k, v) for k, v in x.items()}


def dict_map(fn: Callable[[InValueType], OutValueType], x: Dict[KeyType, InValueType]) -> Dict[KeyType, OutValueType]:
    return {k: fn(v) for k, v in x.items()}


def _index(idx: int):
    return lambda x: x[idx]


def named_treemap(fn: Callable[[KeyType, InValueType], OutValueType], *x: Any, unpack_0: bool = True) -> Any:
    inputs = named_flatten(*x)
    outputs = dict_map_name(lambda p, v: named_flatten(fn(p, *v)), inputs)
    for val in outputs.values():
        break
    else:
        return {}
    out = {k: dict_map(_index(k), outputs) for k in val.keys()}

    def _unpack(x):
        unpack = False
        if unpack_0:
            for inner in x.values():
                unpack = isinstance(inner, (tuple, list)) and len(inner) == 1
                break
        if not unpack:
            return x
        return dict_map(_index(0), x)

    out = dict_map(_unpack, out)
    out = dict_map(named_unflatten, out)
    return named_unflatten(out)
