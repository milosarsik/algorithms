def merge_alternately_two_pointers(word1, word2):
    # Two pointers / string building
    # Time Complexity: O(n + m)
    # Space Complexity: O(n + m)
    res = []
    i, j = 0, 0

    while i < len(word1) or j < len(word2):
        if i < len(word1):
            res.append(word1[i])
            i += 1

        if j < len(word2):
            res.append(word2[j])
            j += 1

    return "".join(res)


def merge_alternately_by_index(word1, word2):
    # Index scan
    # Time Complexity: O(n + m)
    # Space Complexity: O(n + m)
    res = []
    max_length = max(len(word1), len(word2))

    for i in range(max_length):
        if i < len(word1):
            res.append(word1[i])

        if i < len(word2):
            res.append(word2[i])

    return "".join(res)


word1 = "abc"
word2 = "pqr"

print("two pointers:", merge_alternately_two_pointers(word1, word2))
print("index scan:", merge_alternately_by_index(word1, word2))

word1 = "ab"
word2 = "pqrs"

print("two pointers:", merge_alternately_two_pointers(word1, word2))
print("index scan:", merge_alternately_by_index(word1, word2))

word1 = "abcd"
word2 = "pq"

print("two pointers:", merge_alternately_two_pointers(word1, word2))
print("index scan:", merge_alternately_by_index(word1, word2))
