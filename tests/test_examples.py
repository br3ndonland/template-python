from examples import __version__


def test_version() -> str:
    assert __version__ == "0.1.0"
    return __version__
