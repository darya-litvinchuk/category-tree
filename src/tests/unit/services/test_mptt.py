import pytest

from category.models.category import DEFAULT_PARENT
from category.services.mptt import Tree
from tests.unit.services.conftest import CATEGORY_1, CATEGORY_1_3, CATEGORY_1_3_1


@pytest.mark.parametrize(
    "child, parent",
    [
        (
            CATEGORY_1,
            DEFAULT_PARENT,
        ),
        (
            CATEGORY_1_3,
            CATEGORY_1,
        ),
        (
            CATEGORY_1_3_1,
            CATEGORY_1_3,
        ),
    ],
)
def test__parent(child_parent_map, child, parent):
    service = Tree(child_parent_map)
    assert service._parent(child) == parent


def test_mptt(child_parent_map, tree, table):
    service = Tree(child_parent_map)
    assert service.mptt([], [tree]) == table
