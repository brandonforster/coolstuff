def is_unique(test: str) -> bool:
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


def is_unique_slow(test: str) -> bool:
    hashmap = dict()

    # the ascii table, minus crap nobody uses
    for i in range(ord(" "), ord("~")):
        hashmap[chr(i)] = False

    for letter in test:
        if hashmap[letter]:
            return False

        hashmap[letter] = True

    return True


def is_palindrome(test: str) -> bool:
    sort = sorted(test)
    letterfreq = dict()
    for letter in sort:
        if letter not in letterfreq:
            letterfreq[letter] = 1
        else:
            letterfreq[letter] += 1

    # palindromes must have exactly the same number of letters, except for potentially one letter.
    # init the letter count to the first letter in the dict
    lettercount = letterfreq[sort[0]]
    mismatch = False

    for freq in letterfreq.values():
        if freq != lettercount:
            # if there was already a mismatch, this is not a palindrome
            if mismatch:
                return False
            else:
                mismatch = True

    return True
