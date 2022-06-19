from .stack import Stack
import pytest
from contextlib import nullcontext as does_not_raise


@pytest.mark.parametrize("inp, out", [(2, does_not_raise()), (None, pytest.raises(TypeError)),
                                      ('klsjdf', pytest.raises(ValueError))])
def test_push(inp, out):
    stack = Stack()
    with out:
        assert stack.push(inp) is not None


@pytest.mark.parametrize("inp, out", [([1, 2], does_not_raise()), ([], pytest.raises(IndexError))])
def test_pop(inp, out):
    stack = Stack()
    for i in inp:
        stack.push(i)
    with out:
        assert stack.pop() is not None


@pytest.mark.parametrize("inp, out", [([1, 2], 2)])
def test_peek(inp, out):
    stack = Stack()
    for i in inp:
        stack.push(i)
    assert stack.peek() == out and stack.stack[-1] == out


@pytest.mark.parametrize("inp, out", [([1, 2], 2), ([], 0)])
def test_size(inp, out):
    stack = Stack()
    for i in inp:
        stack.push(i)
    assert stack.size() == out


@pytest.mark.parametrize("inp, out", [([1, 2], False), ([], True)])
def test_empty(inp, out):
    stack = Stack()
    for i in inp:
        stack.push(i)
    assert stack.empty() == out
