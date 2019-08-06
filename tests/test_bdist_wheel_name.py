import subprocess
import sys

import pytest


@pytest.fixture(scope="module")
def dummy_dist(tmpdir_factory):
    basedir = tmpdir_factory.mktemp("dummy_dist")
    basedir.join("setup.py").write(
        """\
from setuptools import setup
setup(
    name='dummy_dist',
    version='1.0'
)
"""
    )
    return basedir


def test_basic(dummy_dist, monkeypatch, tmpdir):
    monkeypatch.chdir(dummy_dist)
    output = subprocess.check_output(
        [sys.executable, "setup.py", "-q", "bdist_wheel_name"]
    )
    assert output.strip() == b'dummy_dist-1.0-py3-none-any'
