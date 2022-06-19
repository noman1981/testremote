from .data_store import DataStore
import pytest
from contextlib import nullcontext as does_not_raise


@pytest.mark.parametrize("inp, out", [(('age', 2), does_not_raise()),
                                      ([('age1', 2), ('name', 'Haider')], does_not_raise()),
                                      ((None, 2), pytest.raises(TypeError)),
                                      ((1, [1, 2]), pytest.raises(TypeError))])
def test_insert(inp, out):
    store = DataStore()
    with out:
        assert store.insert(inp) is not None


@pytest.mark.parametrize("inp, out", [((1, 2), does_not_raise()),
                                      ((4, 2), pytest.raises(KeyError))])
def test_update(inp, out):
    store = DataStore()
    store.insert((1, 4))
    with out:
        assert store.update(inp[0], inp[1]) is not None


@pytest.mark.parametrize("inp, out", [(1, does_not_raise()), (2, pytest.raises(KeyError))])
def test_delete(inp, out):
    store = DataStore()
    store.insert((1, 2))
    with out:
        assert store.delete(inp) is not None


@pytest.mark.parametrize("inp, out", [([(1, 2)], False)])
def test_empty(inp, out):
    store = DataStore()
    store.insert(inp)
    assert store.is_empty() == out


@pytest.mark.parametrize("inp, out", [('na', {'name1': 'Haibat'})])
def test_filter(inp, out):
    store = DataStore()
    store.insert([('name1', 'Haibat'), ('name2', 'Haider'),
                  ('name3', 'Hussain'), ('age', '25')])
    assert store.filter(inp) == out
