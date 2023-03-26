from __future__ import annotations
from dataclasses import dataclass

MAX_KEYS = 3 
J = MAX_KEYS // 2  

@dataclass
class Node:
    keys: list[int]
    children: list[Node]

def add(node: Node, k: int) -> Node:
    if len(node.keys) == MAX_KEYS:
        node = _split(Node([], [node]), 0)
    return _insert(node, k)

def _insert(node: Node, k: int) -> Node:
    i = next((i for i, key in enumerate(node.keys) if k < key), len(node.keys))

    if not node.children:  
        return Node(node.keys[:i] + [k] + node.keys[i:], node.children)

    if len(node.children[i].keys) ==  MAX_KEYS:
        node = _split(node, i)
        i = i + 1 if k > node.keys[i] else i

    new_child = _insert(node.children[i], k)
    return Node(node.keys, node.children[:i] + [new_child] + node.children[i+1:])

def _split(node: Node, i: int) -> Node:
    child = node.children[i]
    keys_before, key, keys_after = child.keys[:J], child.keys[J], child.keys[J + 1:]
    children_before, children_after = child.children[:J + 1], child.children[J + 1:]

    return Node(
        node.keys[:i] + [key] + node.keys[i:],
        node.children[:i] + [
            Node(keys_before, children_before),
            Node(keys_after, children_after),
        ] + node.children[i + 1:],
    )

def search(node: Node, k: int) -> bool:
    if not node.children:
        return k in node.keys

    return next(
        True if k == key else search(child, k)
        for key, child in zip(node.keys + [10 ** 10], node.children)
        if k <= key
    )
    

def pp(node: Node, indent: int = 0) -> str:
    return "\n".join("  " * indent + line for line in [
        f"- {node.keys} {'' if node.children else ''}",
        *[f"  {pp(child, indent + 1)}" for child in node.children],
    ])

def main():
    b = Node([], [])
    print('==================================')
    list = [3,5,7,10,13,15,16,20,17]
    print('Tạo cây B-Tree bậc 4 với input: ', list)
    for i in [3,5,7,10,13,15,16,20,17]:
        print('\nThêm khoá: ', i)
        b = add(b,i)
        print(pp(b))
    key = 20
    print('Tìm kiếm khoá: ', key)
    if (search(b,key)) == False:
        print('Không tìm thấy!')
    else:
        print('Tìm thấy trong cây')



if __name__ == '__main__':
  main()