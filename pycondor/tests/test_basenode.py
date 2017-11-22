
import pytest

from pycondor.basenode import BaseNode


def test_BaseNode_extra_lines_raises():
    with pytest.raises(TypeError) as excinfo:
        BaseNode('test_basenode', extra_lines=1111)
    error = 'extra_lines must be of type str, list, or tuple'
    assert error == str(excinfo.value)


def test_BaseNode_extra_lines_str():
    extra_lines_str = 'single extra line'
    basenode = BaseNode('test_basenode', extra_lines=extra_lines_str)
    assert basenode.extra_lines == [extra_lines_str]


def test_BaseNode_hadchildren():
    basenode = BaseNode('test_basenode')
    assert basenode.haschildren() is False

    child_node = BaseNode('child_basenode')
    basenode.add_child(child_node)
    assert basenode.haschildren() is True


def test_BaseNode_hasparents():
    basenode = BaseNode('test_basenode')
    assert basenode.hasparents() is False

    parent_node = BaseNode('parent_basenode')
    basenode.add_parent(parent_node)
    assert basenode.hasparents() is True
