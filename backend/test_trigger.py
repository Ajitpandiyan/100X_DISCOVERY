"""Test trigger module for CI pipeline."""


def test_basic() -> None:
    """Basic test to ensure CI pipeline works."""
    assert True


def test_environment() -> None:
    """Test that we can import basic requirements."""
    import fastapi

    assert fastapi is not None