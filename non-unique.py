def non_unique(a):
    b = []
    for i in a:
        if a.count(i) > 1:
            b.append(i)
    return b


if __name__ == '__main__':
    assert list(non_unique([1, 2, 3, 1, 3])) == [1, 3, 1, 3], "1st example"
    assert list(non_unique([1, 2, 3, 4, 5])) == [], "2nd example"
    assert list(non_unique([5, 5, 5, 5, 5])) == [5, 5, 5, 5, 5], "3rd example"
    assert list(non_unique([10, 9, 10, 10, 9, 8])) == [
        10, 9, 10, 10, 9], "4th example"
    print("It is all good. Let's check it now")
