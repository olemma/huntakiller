import string

abet = string.ascii_lowercase


def decipher_mirror(word: str) -> str:
    """
    Decipher text in a mirrored alphabet
    :param word: mirrored lowercase word i.e. 'erloz'
    :return: deciphred word 'viola'
    """
    return "".join(abet[len(abet) - abet.index(w) - 1] for w in word)


def test_decipher_mirror():
    assert decipher_mirror("erloz") == "viola"
