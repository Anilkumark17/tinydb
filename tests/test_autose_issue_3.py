import pytest
from tinydb import TinyDB
from tinydb.storages import MemoryStorage

def test_get_with_document():
    db = TinyDB(storage=MemoryStorage)
    table = db.table('test')
    doc_id = table.insert({'value': 42})
    doc = table.get(doc_id=doc_id)

    assert table.get(doc_id=doc) == doc

def test_get_with_doc_ids_list():
    db = TinyDB(storage=MemoryStorage)
    table = db.table('test')
    id1 = table.insert({'value': 1})
    id2 = table.insert({'value': 2})
    doc1 = table.get(doc_id=id1)
    doc2 = table.get(doc_id=id2)

    docs = table.get(doc_ids=[doc1, id2])
    assert docs == [doc1, doc2]

def test_update_with_doc_ids_list():
    db = TinyDB(storage=MemoryStorage)
    table = db.table('test')
    id1 = table.insert({'value': 1})
    id2 = table.insert({'value': 2})
    doc1 = table.get(doc_id=id1)

    updated_ids = table.update({'value': 10}, doc_ids=[doc1, id2])
    assert sorted(updated_ids) == [id1, id2]
    assert table.get(doc_id=id1)['value'] == 10
    assert table.get(doc_id=id2)['value'] == 10

def test_remove_with_doc_ids_list():
    db = TinyDB(storage=MemoryStorage)
    table = db.table('test')
    id1 = table.insert({'value': 1})
    id2 = table.insert({'value': 2})
    doc1 = table.get(doc_id=id1)

    removed_ids = table.remove(doc_ids=[doc1, id2])
    assert sorted(removed_ids) == [id1, id2]
    assert len(table) == 0
