from __future__ import annotations

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

for _name in __deprecated__:
    if _name in globals():
        del globals()[_name]

def __getattr__(name: str) -> Any:
    """Provide a deprecation warning when accessing the deprecated module.

    Args:
        name: The attribute name to access.

    Returns:
        The corresponding attribute from the new module location.

    Raises:
        AttributeError: If the attribute does not exist in the module.
    """
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
