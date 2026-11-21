from tinydb import TinyDB, where
from tinydb.storages import MemoryStorage


def test_search_limit_with_matching_documents():
    db = TinyDB(storage=MemoryStorage)
    table = db.table('test')
    table.insert_multiple({'value': 1} for _ in range(10))

    results = table.search(where('value') == 1, limit=5)
    assert len(results) == 5


def test_search_limit_none_or_absent():
    db = TinyDB(storage=MemoryStorage)
    table = db.table('test')
    table.insert_multiple({'value': 1} for _ in range(10))

    results_none = table.search(where('value') == 1, limit=None)
    results_absent = table.search(where('value') == 1)

    assert len(results_none) == 10
    assert len(results_absent) == 10
    assert results_none == results_absent


def test_search_limit_does_not_affect_subsequent_unlimited_search():
    db = TinyDB(storage=MemoryStorage)
    table = db.table('test')
    table.insert_multiple({'value': 1} for _ in range(10))

    limited_results = table.search(where('value') == 1, limit=5)
    assert len(limited_results) == 5

    unlimited_results = table.search(where('value') == 1)
    assert len(unlimited_results) == 10
