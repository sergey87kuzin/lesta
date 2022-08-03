def even(value):
    return not value & 1


def test():
    assert even(2)
    assert not even(25)
    assert even(-2)
    assert even(0)


if __name__ == '__main__':
    test()
