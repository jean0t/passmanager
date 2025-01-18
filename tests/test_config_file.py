import sys

sys.dont_write_bytecode = True

from src.config import Config
from pathlib import Path


def test_app_path():
    path = Path().home() / ".passmng"

    assert path == Config.app_path


def test_database_path():
    path = Path().home() / ".passmng" / "database.db"

    assert path == Config.database_path


def test_if_directory_is_created():
    path = Path().home() / "test_creation_of_directory"
    Config.configure_environment(path)

    assert path.exists()
    path.rmdir()
