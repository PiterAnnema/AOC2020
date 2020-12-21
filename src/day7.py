import re
import pprint


def findAllAncestors(parent_tree, child):
    if child in parent_tree:
        return {child}.union(*(findAllAncestors(parent_tree, parent) for parent in parent_tree[child]))

    return {child}


def countAllDescendants(child_tree, parent):
    return sum(count * (1 + countAllDescendants(child_tree, child)) for child, count in child_tree[parent].items())


def getTrees(filename):
    parent_pattern = re.compile(r'([\sa-z]*) bags? contain')
    child_pattern  = re.compile(r'(\d) ([\sa-z]*)\s')

    parent_tree = dict()
    child_tree = dict()
    with open(filename) as f:
        for line in f:
            parent = parent_pattern.search(line).group(1)
            children = child_pattern.findall(line)

            parent_tree[parent] = {color: int(count) for count, color in children}

            for count, child in children:
                if child not in child_tree:
                    child_tree[child] = dict()

                child_tree[child][parent] = count

    return parent_tree, child_tree


if __name__ == "__main__":
    parent_tree, child_tree = getTrees('data/day7.txt')

    print(len(findAllAncestors(child_tree, 'shiny gold')) - 1)
    print(countAllDescendants(parent_tree, 'shiny gold'))