#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(16)

    """
    YOUR CODE HERE
    """
    storage = {}
    for w in range(len(weights)):
        current = weights[w]
        if current is not None:
            diff = limit - current
            storage[current] = w
            # Check storage for weight that equals limit
            if diff in storage:
                # print('Found an answer...')
                if current > diff:
                    print('Top: ', print_answer([storage[current], storage[diff]]))
                    return print_answer([storage[current], storage[diff]])
                else:
                    print('Bottom: ', print_answer([storage[diff], storage[current]]))
                    return print_answer([storage[diff], storage[current]])

    return None


def print_answer(answer):
    if answer is not None:
        # print(f'{answer[0]} {answer[1]}')
        return [(answer[0]), answer[1]]
    else:
        print("None")


get_indices_of_item_weights([ 4, 6, 10, 15, 16 ], 5, 21)
