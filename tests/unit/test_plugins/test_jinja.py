import pytest

from litestar.plugins.jinja import JinjaTemplateEngine

def test_jinja_engine_is_importable() -> None:
    """Test that the JinjaTemplateEngine can be imported from plugins."""
    assert JinjaTemplateEngine is not None
