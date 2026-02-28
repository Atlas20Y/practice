
def remove_duplicates_old(values: list) -> list:
    no_duplicates = []
    for v in values:
        if v not in no_duplicates:
            no_duplicates.append(v)
    return no_duplicates

def remove_duplicates(values: list) -> list:
    return []




assert remove_duplicates([1,2,2,3]) == [1,2,3]
assert remove_duplicates(list('aabbcccdd')) == list("abcd")