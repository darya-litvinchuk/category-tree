from category.services.utils import ChildParentService


def test_child_parent_map(tree, child_parent_map):
    service = ChildParentService()
    assert service.child_parent_map([tree]) == child_parent_map
