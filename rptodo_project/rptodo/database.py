"""This module provides the RP To-Do database functionality."""

#rptodo/database.py

import configparser
from pathlib import Path
from rptodo import DB_WRITE_ERROR, SUCCESS

DEFAULT_DB_FILE_PATH = Path.home().joinpath(
    "." + Path.home().stem + "_todo.json"
)

def get_database(db_path: Path) -> int:
    """Create the to-do database"""
    try:
        db_path.write_test("[]") #Empty to-do list
        return SUCCESS
    except OSError:
        return DB_WRITE_ERROR
        