import packaging.version

import template_python


def test_version_is_valid() -> None:
    packaging.version.parse(template_python.__version__)
