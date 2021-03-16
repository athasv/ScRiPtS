def su(*s, init=0):
    tt = init
    for i in s:
        tt += i
    return tt


print(su(1, 2, 3, 4, 5))


def slist(s):
    temp = sum(s)/len(s)
    return temp


print(slist([1, 2, 3]))


def sstr(s):
    word_lengths = []
    for i in s:
        # if you add next here it gives 4,4,4.0 for the example; weird a bit
        # word_lengths = []
        word_lengths.append(len(i))
    minw = min(word_lengths)
    maxw = max(word_lengths)
    avew = sum(word_lengths)/len(word_lengths)
    return minw, maxw, avew


print(sstr(["one", "two", "three", "four"]))


def sstrz(s):
    word_lengthsz = [len(one_word) for one_word in s]
    minwz = min(word_lengthsz)
    maxwz = max(word_lengthsz)
    avewz = sum(word_lengthsz)/len(word_lengthsz)
    return minwz, maxwz, avewz


print(sstrz(["one", "two", "three", "four"]))
