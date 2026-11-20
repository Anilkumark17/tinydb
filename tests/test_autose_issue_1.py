from tinydb import TinyDB
from tinydb.storages import MemoryStorage


def test_update_string_doc_ids():
    db = TinyDB(storage=MemoryStorage)
    table = db.table('test')
    doc_id = table.insert({'value': 1})

    updated_ids = table.update({'value': 2}, doc_ids=[str(doc_id)])
    assert updated_ids == [doc_id]
    assert table.get(doc_id=doc_id)['value'] == 2


def test_remove_string_doc_ids():
    db = TinyDB(storage=MemoryStorage)
    table = db.table('test')
    doc_id = table.insert({'value': 1})

    removed_ids = table.remove(doc_ids=[str(doc_id)])
    assert removed_ids == [doc_id]
    assert len(table) == 0


def test_update_remove_nonexistent_string_doc_ids():
    db = TinyDB(storage=MemoryStorage)
    table = db.table('test')
    table.insert({'value': 1})

    assert table.update({'value': 2}, doc_ids=['99']) == []
    assert table.remove(doc_ids=['99']) == []
    assert len(table) == 1
