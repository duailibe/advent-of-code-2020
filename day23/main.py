import itertools
from dataclasses import dataclass


@dataclass
class Node:
    label: int
    next: "Node"


def linkedlist(cups):
    cups = iter(cups)
    head = node = Node(next(cups), next=None)
    lookup = {head.label: head}
    for label in cups:
        lookup[label] = Node(label, next=None)
        node.next = lookup[label]
        node = node.next
    node.next = head
    return head, lookup


def move(curr, lookup, max_label):
    pickup = []
    for _ in range(3):
        pickup.append(curr.next)
        curr.next = curr.next.next

    dest_label = ((curr.label - 2) % max_label) + 1
    while dest_label in [p.label for p in pickup]:
        dest_label = ((dest_label - 2) % max_label) + 1

    dest = lookup[dest_label]
    pickup[-1].next = dest.next
    dest.next = pickup[0]

    return curr.next


def part1(labels):
    node, lookup = linkedlist(labels)
    for _ in range(100):
        node = move(node, lookup, len(labels))

    node = lookup[1].next
    result = ""
    while node.label != 1:
        result += str(node.label)
        node = node.next
    return result


def part2(labels):
    ncups = 1000000
    node, lookup = linkedlist(
        itertools.chain(labels, range(max(labels) + 1, ncups + 1))
    )
    for _ in range(10000000):
        node = move(node, lookup, ncups)

    node = lookup[1].next
    return node.label * node.next.label


if __name__ == "__main__":
    labels = list(map(int, "253149867"))

    print("Part 1:", part1(labels))
    print("Part 2:", part2(labels))
