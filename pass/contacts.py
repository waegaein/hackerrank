#!/bin/python3

import os
import sys

#
# Complete the contacts function below.
#
class ContactIndex(object):
    def __init__(self, character):
        self.character = character
        self.prefix_count = 1
        self.next_indices = list()

        return

    def increment(self):
        self.prefix_count += 1

        return

    def add_next(self, next_index):
        self.next_indices.append(next_index)

        return

    def write_next(self, character):
        for next_index in self.next_indices:
            if character == next_index.character:
                next_index.increment()
                return next_index

        next_index_created = ContactIndex(character)
        self.add_next(next_index_created)

        return next_index_created

    def read_next(self, character):
        for next_index in self.next_indices:
            if character == next_index.character:
                return next_index

        return None


def contacts(queries):
    root_indices = dict()
    results = list()

    for query in queries:
        root_indices, results = process_query(query, root_indices, results)

    return results

def process_query(query, root_indices, results):
    operation = query[0]
    word = query[1]

    if operation == 'add':
        root_indices = process_add(word, root_indices)

    elif operation == 'find':
        results = process_find(word, root_indices, results)

    else:
        raise ValueError

    return root_indices, results

def process_add(word, root_indices):
    first = word[0]
    if first not in root_indices.keys():
        root_indices[first] = ContactIndex(first)
    else:
        root_indices[first].increment()

    current_index = root_indices[first]

    for character in word[1:]:
        current_index = current_index.write_next(character)

    return root_indices

def process_find(word, root_indices, results):
    first = word[0]
    if first not in root_indices.keys():
        results.append(0)
    else:
        current_index = root_indices[first]
        results.append(match_index(word, current_index))

    return results

def match_index(word, current_index):
    for character in word[1:]:
        current_index = current_index.read_next(character)
        if current_index is None:
            return 0

    return current_index.prefix_count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    queries_rows = int(input())

    queries = []

    for _ in range(queries_rows):
        queries.append(input().rstrip().split())

    result = contacts(queries)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
