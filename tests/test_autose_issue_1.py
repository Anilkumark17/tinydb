from tinydb import TinyDB
from tinydb.storages import MemoryStorage
import pytest


def test_update_remove_string_doc_ids():
    db = TinyDB(storage=MemoryStorage)
    table = db.table('test')
    
    doc_id = table.insert({'value': 42})
    assert doc_id == 1

    # Acceptance criterion 1: update() with doc_ids=['1']
    updated_ids = table.update({'value': 100}, doc_ids=['1'])
    assert updated_ids == [1]
    assert table.get(doc_id=1)['value'] == 100

    # Acceptance criterion 2: remove() with doc_ids=['1']
    removed_ids = table.remove(doc_ids=['1'])
    assert removed_ids == [1]
    assert len(table) == 0


def test_update_remove_invalid_string_doc_ids():
    db = TinyDB(storage=MemoryStorage)
    table = db.table('test')
    
    table.insert({'value': 42})

    # Acceptance criterion 3: invalid document ID string raises ValueError
    with pytest.raises(ValueError):
        table.update({'value': 100}, doc_ids=['abc'])

    with pytest.raises(ValueError):
        table.remove(doc_ids=['abc'])
