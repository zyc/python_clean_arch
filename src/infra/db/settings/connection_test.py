import pytest

from .connection import DBConnctionHandler


@pytest.mark.skip(reason="This test is not ready yet")
def test_create_database_engine():
    db_connection_handler = DBConnctionHandler()
    engine = db_connection_handler.get_engine()

    assert engine is not None

    # conn = engine.connect()

    # result = conn.execute(text("SELECT 2"))

    # print()
    # print()
    # print()
    # print(result.cursor.fetchone())
    # print(engine)
