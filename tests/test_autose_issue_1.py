from tinydb import TinyDB
from tinydb.storages import MemoryStorage


def test_update_with_string_doc_ids():
    db = TinyDB(storage=MemoryStorage)
    doc_id = db.insert({'val': 1})

    updated_ids = db.update({'val': 2}, doc_ids=[str(doc_id)])
    assert updated_ids == [doc_id]
    assert db.get(doc_id=doc_id)['val'] == 2


def test_remove_with_string_doc_ids():
    db = TinyDB(storage=MemoryStorage)
    doc_id = db.insert({'val': 1})

    removed_ids = db.remove(doc_ids=[str(doc_id)])
    assert removed_ids == [doc_id]
    assert len(db) == 0


def test_update_remove_non_existent_string_doc_ids():
    db = TinyDB(storage=MemoryStorage)
    db.insert({'val': 1})

    # Non-existent string ID in update
    updated_ids = db.update({'val': 99}, doc_ids=['99'])
    assert updated_ids == []
    assert db.get(doc_id=1)['val'] == 1

    # Non-existent string ID in remove
    removed_ids = db.remove(doc_ids=['99'])
    assert removed_ids == []
    assert len(db) == 1
