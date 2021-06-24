from dataclasses import dataclass
from typing import Any, Dict, List, Optional

from category.models.category import DEFAULT_PARENT


@dataclass
class TreeNode:
    name: str
    left: int
    right: Optional[int] = None
    parent_name: Optional[str] = DEFAULT_PARENT

    def set_right(self, right: int):
        self.right = right

    def set_parent(self, parent_name: str):
        self.parent_name = parent_name

    def __str__(self):
        return f"{self.name} ({self.left}, {self.right}); parent {self.parent_name}"


@dataclass
class Tree:
    child_parent_map: Dict[str, str]
    iterator: int = 0

    def _parent(self, item_name: str):
        name = self.child_parent_map.get(item_name)
        if not name:
            return DEFAULT_PARENT
        return name

    def mptt(self, table: List[TreeNode], tree: List[Dict[str, Any]]) -> List[TreeNode]:
        # Modified Preorder Tree Traversal Algorithm
        for item in tree:
            self.iterator += 1

            if item.get("children"):
                index = len(table)
                table.append(TreeNode(item["name"], self.iterator))

                if len(item["children"]) > 0:
                    self.mptt(table, item["children"])
            else:
                index = len(table)
                table.append(TreeNode(item["name"], self.iterator))

            self.iterator += 1

            table[index].set_right(self.iterator)
            table[index].set_parent(self._parent(item["name"]))

        return table
