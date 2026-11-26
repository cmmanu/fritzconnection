import sys
from types import SimpleNamespace

import pytest

from ..cli.utils import get_cli_arguments, get_instance


@pytest.mark.parametrize(
    "argv, expected", [
        ([], False),
        (["--public-connection"], True),
    ]
)
def test_cli_public_connection_flag(mocker, argv, expected):
    mocker.patch.object(sys, "argv", ["fritzconnection"] + argv)
    args = get_cli_arguments()
    assert args.public_connection is expected

    cls = mocker.MagicMock()
    get_instance(cls, args)
    assert cls.call_args.kwargs["use_public_connection"] is expected


def test_get_instance_without_public_connection_argument(mocker):
    """Argument namespaces created without the new flag keep working."""
    args = SimpleNamespace(
        address="192.168.178.1", port=None, username=None, password=None,
        encrypt=False, use_cache=False, verify_cache=True,
        cache_directory=None, cache_format=None,
    )
    cls = mocker.MagicMock()
    get_instance(cls, args)
    assert cls.call_args.kwargs["use_public_connection"] is False
