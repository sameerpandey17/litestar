from __future__ import annotations

import warnings
from typing import TYPE_CHECKING

from litestar.utils.deprecation import warn_deprecation

from litestar.plugins.jinja import *  # noqa: F401, F403
from litestar.plugins import jinja as _new_module

if TYPE_CHECKING:
    from typing import Any

__deprecated__ = {
    "JinjaTemplateEngine",
    "P",
    "T",
}

for name in __deprecated__:
    if name in globals():
        del globals()[name]

def __getattr__(name: str) -> Any:
    if name in __deprecated__:
        warn_deprecation(
            version="3.0.0b0",
            deprecated_name=f"litestar.contrib.jinja.{name}",
            kind="import",
            removal_in="3.0.0",
            alternative=f"litestar.plugins.jinja.{name}",
        )
        return getattr(_new_module, name)
    raise AttributeError(f"module 'litestar.contrib.jinja' has no attribute {name!r}")
