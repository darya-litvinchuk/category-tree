import pytest

from category.models.category import DEFAULT_PARENT
from category.services.mptt import TreeNode

CATEGORY_1 = "1"
CATEGORY_1_1 = "1.1"
CATEGORY_1_2 = "1.2"
CATEGORY_1_3 = "1.3"
CATEGORY_1_3_1 = "1.3.1"


@pytest.fixture
def tree():
    return {
        "name": CATEGORY_1,
        "children": [
            {
                "name": CATEGORY_1_1,
            },
            {"name": CATEGORY_1_2, "children": []},
            {"name": CATEGORY_1_3, "children": [{"name": CATEGORY_1_3_1}]},
        ],
    }


@pytest.fixture
def child_parent_map():
    return {
        CATEGORY_1_1: CATEGORY_1,
        CATEGORY_1_2: CATEGORY_1,
        CATEGORY_1_3: CATEGORY_1,
        CATEGORY_1_3_1: CATEGORY_1_3,
    }


@pytest.fixture
def table():
    return [
        TreeNode(name=CATEGORY_1, left=1, right=10, parent_name=DEFAULT_PARENT),
        TreeNode(name=CATEGORY_1_1, left=2, right=3, parent_name=CATEGORY_1),
        TreeNode(name=CATEGORY_1_2, left=4, right=5, parent_name=CATEGORY_1),
        TreeNode(name=CATEGORY_1_3, left=6, right=9, parent_name=CATEGORY_1),
        TreeNode(name=CATEGORY_1_3_1, left=7, right=8, parent_name=CATEGORY_1_3),
    ]
