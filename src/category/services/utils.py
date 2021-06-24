from typing import Any, Dict, List


class ChildParentService:

    hash_map = {}

    def child_parent_map(self, tree: List[Dict[str, Any]]):
        for item in tree:
            children = item.get("children")
            if children is None:
                continue
            for child in children:
                self.hash_map[child["name"]] = item["name"]
            self.child_parent_map(children)
        return self.hash_map
