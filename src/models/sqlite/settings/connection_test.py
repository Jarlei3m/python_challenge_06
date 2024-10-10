import pytest
from sqlalchemy import Engine
from .connection import db_connection_handle 

@pytest.mark.skip(reason="db integration")
def test_connect_to_db():
    assert db_connection_handle.get_engine() is None

    db_connection_handle.connect_to_db()
    db_engine = db_connection_handle.get_engine()

    assert db_engine is not None
    assert isinstance(db_engine, Engine)
