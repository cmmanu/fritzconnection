import sys

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
