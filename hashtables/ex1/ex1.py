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
        diff = limit - current
        # Check storage for weight that matches diff
        if diff in storage:
            # Return index for each value
            return [w, storage[diff]]
        else:
            storage[current] = w
    
    return None


def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
        # return [(answer[0]), answer[1]]
    else:
        print("None")


get_indices_of_item_weights([ 4, 6, 10, 15, 16 ], 5, 21)
