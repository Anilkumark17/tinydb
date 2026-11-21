from tinydb import TinyDB
from tinydb.storages import MemoryStorage


def test_string_doc_id_update_is_a_no_op():
    db = TinyDB(storage=MemoryStorage)
    db.insert({"a": 1})
    assert db.update({"a": 2}, doc_ids=["1"]) == []
    assert db.get(doc_id=1)["a"] == 1


def test_string_doc_id_remove_is_a_no_op():
    db = TinyDB(storage=MemoryStorage)
    db.insert({"a": 1})
