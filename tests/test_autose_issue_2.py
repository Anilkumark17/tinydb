import pytest
from tinydb import TinyDB
from tinydb.table import Document
from tinydb.storages import MemoryStorage


def test_insert_duplicate_doc_id_raises_value_error():
    db = TinyDB(storage=MemoryStorage)
    table = db.table('test')

    doc_id = table.insert({'value': 1})
    doc = Document({'value': 2}, doc_id=doc_id)

    with pytest.raises(ValueError):
        table.insert(doc)

    with pytest.raises(ValueError):
        table.insert_multiple([doc])


def test_copy_documents_without_preserving_source_ids():
    db_src = TinyDB(storage=MemoryStorage)
    src_table = db_src.table('src')
    src_table.insert({'a': 1})
    src_table.insert({'a': 2})
    docs = src_table.all()

    db_dest = TinyDB(storage=MemoryStorage)
    dest_table = db_dest.table('dest')
    dest_table.insert({'a': 99})  # Existing document

    # Copy documents without preserving source doc_ids (e.g. by wrapping in dict)
    new_docs = [dict(doc) for doc in docs]
    dest_table.insert_multiple(new_docs)

    assert len(dest_table) == 3
    assert dest_table.get(doc_id=1) == {'a': 99}
    assert dest_table.get(doc_id=2)['a'] in (1, 2)
    assert dest_table.get(doc_id=3)['a'] in (1, 2)


def test_insert_multiple_mixed_documents_and_dicts():
    db = TinyDB(storage=MemoryStorage)
    table = db.table('test')

    existing_id = table.insert({'x': 0})

    plain_dict = {'x': 1}
    doc_with_id = Document({'x': 2}, doc_id=99)

    table.insert_multiple([plain_dict, doc_with_id])

    assert len(table) == 3
    assert table.get(doc_id=existing_id) == {'x': 0}
    assert table.get(doc_id=2) == {'x': 1}
    assert table.get(doc_id=99) == {'x': 2}
