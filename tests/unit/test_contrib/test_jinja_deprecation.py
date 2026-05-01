import warnings

import pytest


def test_import_from_contrib_raises_deprecation_warning():
    with pytest.warns(DeprecationWarning, match="litestar.plugins.jinja"):
        from litestar.contrib.jinja import JinjaTemplateEngine


def test_bare_import_emits_no_warning():
    # Importing the module itself should NOT warn
    # Only accessing attributes should trigger the warning
    with warnings.catch_warnings():
        warnings.simplefilter("error")  # any warning = test failure
        import litestar.contrib.jinja  # noqa: F401


def test_identity_equality():
    # The same object must be returned from both paths
    import warnings
    with warnings.catch_warnings():
        warnings.simplefilter("ignore", DeprecationWarning)
        from litestar.contrib import jinja as contrib_jinja
    from litestar.plugins import jinja as plugins_jinja

    # 'is' check — not == but identical object
    with warnings.catch_warnings():
        warnings.simplefilter("ignore", DeprecationWarning)
        assert contrib_jinja.JinjaTemplateEngine is plugins_jinja.JinjaTemplateEngine
