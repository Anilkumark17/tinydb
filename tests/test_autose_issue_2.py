import pytest
from tinydb import TinyDB
from tinydb.table import Document
from tinydb.storages import MemoryStorage


def test_insert_multiple_duplicate_doc_id_raises_value_error():
    """
    When insert_multiple is called with documents containing doc_id values
    that already exist in the target table, it shall raise a ValueError.
    """
    db = TinyDB(storage=MemoryStorage)
    table = db.table('test')
    table.insert(Document({'name': 'first'}, doc_id=1))

    with pytest.raises(ValueError):
        table.insert_multiple([Document({'name': 'second'}, doc_id=1)])


def test_insert_or_insert_multiple_no_doc_id_assigns_new_id():
    """
    When insert or insert_multiple is called with a document that does not
    specify a doc_id or is a plain dictionary, it shall assign a new unique
    doc_id in the target table and return the assigned ID(s).
    """
    db = TinyDB(storage=MemoryStorage)
    table = db.table('test')

    id1 = table.insert({'name': 'dict'})
    assert id1 == 1
    assert table.get(doc_id=1) == {'name': 'dict'}

    ids = table.insert_multiple([{'name': 'dict2'}, {'name': 'dict3'}])
    assert ids == [2, 3]
    assert table.get(doc_id=2) == {'name': 'dict2'}
    assert table.get(doc_id=3) == {'name': 'dict3'}


def test_copy_documents_without_conflicting_explicit_ids():
    """
    When a document or a list of documents from a source database is copied
    to a destination database or table without preserving conflicting explicit
    doc_ids (or by assigning new IDs), it shall insert the documents successfully
    without raising an exception and without modifying existing records in the destination.
    """
    db_source = TinyDB(storage=MemoryStorage)
    db_dest = TinyDB(storage=MemoryStorage)

    source_table = db_source.table('source')
    dest_table = db_dest.table('dest')

    # Populate source with some documents having explicit IDs
    source_table.insert(Document({'val': 10}, doc_id=1))
    source_table.insert(Document({'val': 20}, doc_id=2))

    # Destination already has a document with ID 1
    dest_table.insert(Document({'val': 999}, doc_id=1))

    # Copy documents from source to dest without preserving conflicting explicit doc_ids
    # (i.e. converting to plain dictionaries so new unique IDs are assigned)
    docs_to_copy = [dict(doc) for doc in source_table.all()]
    inserted_ids = dest_table.insert_multiple(docs_to_copy)

    # Verify successful insertion, no exception raised, no modification to existing records
    assert len(dest_table) == 3
    assert dest_table.get(doc_id=1) == {'val': 999}
    assert inserted_ids == [2, 3]
    assert dest_table.get(doc_id=2) == {'val': 10}
    assert dest_table.get(doc_id=3) == {'val': 20}
