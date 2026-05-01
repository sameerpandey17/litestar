import pytest

from litestar.plugins.jinja import JinjaTemplateEngine

def test_jinja_engine_is_importable():
    assert JinjaTemplateEngine is not None
