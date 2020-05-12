def is_unique(test: str):
    # start at 1 so index is always ahead of the loop
    i = 1
    for letter in test:
        # catch index out of bounds
        if i > len(test):
            return True

        substr = test[i:]
        if letter in substr:
            return False

        i += 1

    # if we fell through here, it means we never entered the loop
    return True


def is_unique_slow(test: str):
    hashmap = dict()

    # the ascii table, minus crap nobody uses
    for i in range(ord(" "), ord("~")):
        hashmap[chr(i)] = False

    for letter in test:
        if hashmap[letter]:
            return False

        hashmap[letter] = True

    return True
