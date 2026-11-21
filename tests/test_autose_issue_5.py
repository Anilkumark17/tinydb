from tinydb import TinyDB, where
from tinydb.storages import MemoryStorage


def test_table_len_returns_total_records():
    db = TinyDB(storage=MemoryStorage)
    table = db.table('test')
    assert len(table) == 0

    table.insert({'a': 1})
    table.insert({'a': 2})
    assert len(table) == 2


def test_table_count_with_query_condition():
    db = TinyDB(storage=MemoryStorage)
    table = db.table('test')
    table.insert({'type': 'fruit', 'name': 'apple'})
    table.insert({'type': 'fruit', 'name': 'banana'})
    table.insert({'type': 'vegetable', 'name': 'carrot'})

    assert table.count(where('type') == 'fruit') == 2
    assert table.count(where('type') == 'vegetable') == 1
    assert table.count(where('type') == 'meat') == 0


def test_table_count_without_query_condition():
    db = TinyDB(storage=MemoryStorage)
    table = db.table('test')
    assert table.count() == 0

    table.insert({'a': 1})
    table.insert({'a': 2})
    assert table.count() == 2


def test_table_count_success_without_error():
    db = TinyDB(storage=MemoryStorage)
    table = db.table('test')
    table.insert({'x': 10})

    # Should execute successfully without raising runtime or type errors
    res_no_cond = table.count()
    res_with_cond = table.count(where('x') == 10)

    assert res_no_cond == 1
    assert res_with_cond == 1
