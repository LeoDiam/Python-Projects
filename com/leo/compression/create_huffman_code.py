import pprint


def create_pq():
    return []


def add_last(pq, c):
    pq.append(c)


def root(pq):
    return 0


def set_root(pq, c):
    if len(pq) != 0:
        pq[0] = c


def get_data(pq, p):
    return pq[p]


def children(pq, p):
    if 2 * p + 2 < len(pq):
        return [2 * p + 1, 2 * p + 2]
    else:
        return [2 * p + 1]


def parent(p):
    return (p - 1) // 2


def exchange(pq, p1, p2):
    pq[p1], pq[p2] = pq[p2], pq[p1]


def insert_in_pq(pq, c):
    add_last(pq, c)
    i = len(pq) - 1
    while i != root(pq) and get_data(pq, i) < get_data(pq, parent(i)):
        p = parent(i)
        exchange(pq, i, p)
        i = p


def extract_last_from_pq(pq):
    return pq.pop()


def has_children(pq, p):
    return 2 * p + 1 < len(pq)


def extract_min_from_pq(pq):
    c = pq[root(pq)]
    set_root(pq, extract_last_from_pq(pq))
    i = root(pq)
    while has_children(pq, i):
        # Use the data stored at each child as the comparison key
        # for finding the minimum.
        j = min(children(pq, i), key=lambda x: get_data(pq, x))
        if get_data(pq, i) < get_data(pq, j):
            return c
        exchange(pq, i, j)
        i = j
    return c


def create_huffman_code(pq):
    while len(pq) > 1:
        # Extract the two minimum items from the priority queue.
        x = extract_min_from_pq(pq)
        y = extract_min_from_pq(pq)
        # Get all the [character, encoding] items associated with x;
        # as x is the left child of the new node, prepend '0'
        # to their encodings.
        for pair in x[1:]:
            pair[1] = '0' + pair[1]
        # Do the same for y; as y is the right child of the
        # new node, prepend '1' to their encodings.
        for pair in y[1:]:
            pair[1] = '1' + pair[1]
        # Insert a new node with the sum of the occurrences
        # of the two extracted nodes and the updated
        # [character, encoding] sequences.
        insert_in_pq(pq, [x[0] + y[0]] + x[1:] + y[1:])
    return extract_min_from_pq(pq)


text = "banana"

symb2freq = {}
for ch in text:
    # If ch is not in the frequency table
    # we have to create an entry for it
    # initialized to zero.
    if ch not in symb2freq:
        symb2freq[ch] = 0
    # Add one to the number of times we have
    # seen ch.
    symb2freq[ch] += 1

# The priority queue will be initialized with elements of the form:
# [value, [character, encoding]]
pq = create_pq()
for key, value in symb2freq.items():
    insert_in_pq(pq, [value, [key, '']])

hc = create_huffman_code(pq)

print("Huffman Code:")
pprint.pprint(hc)
