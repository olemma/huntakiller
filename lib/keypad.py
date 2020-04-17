from typing import List

KeyPad = List[List[str]]
RowType = int
ColType = int


def make_keypad(block: str, row: RowType, col: ColType) -> KeyPad:
    """
    Given coordinates of some block of letters in a keypad, create the keypad.

    :param block: a block of letters i.e. 'mno' or 'def'
    :param row: the block's 0-index row in the keypad
    :param col: the block's 0-indexed column in the keypad
    :return: a 2d array representing a keypad. the 'yz' block is 'yzz' instead
    """
    abet = "abc def ghi jkl mno pqr stu vwx yzz".split()
    rot = abet.index(block) - (row * 3 + col)
    new_abet = abet[rot:] + abet[:rot]
    return [new_abet[3 * i : 3 * i + 3] for i in range(3)]


codebook = {"u": 0, "d": 2, "s": 1, "c": 1, "l": 2, "r": 0}


def decipher_keypad(pad: KeyPad, codes: str) -> str:
    """
    Given a pad, decipher a phrase using the stage-center keypad cipher thing

    :param pad: 2d array from make_keypad
    :param codes: a string of space separated codes in lower case i.e.
        'uc3 dl2 sc2 ul1'
    :return: a string of the deciphered letters
    """
    return "".join(pad[codebook[coord[0]]][codebook[coord[1]]][int(coord[2]) - 1] for coord in codes.split(" "))


def cipher_keypad(pad: KeyPad, phrase: str) -> str:
    """
    Given a pad, cipher a phrase using the stage-center-keypad cipher thing.

    :param pad: 2d array from make_keypad
    :param phrase: a lowercase phrase with spaces. i.e. 'let me know if you need help'
    :return: space separated codes for the phrase i.e. 'uc3 dl2 sc2'
    """
    fp = "".join([item for cell in pad for item in cell])
    return " ".join(
        "usd"[j[0]] + "rcl"[j[1]] + str(j[2] + 1)
        for j in [(i // 9, (i % 9) // 3, i % 3) for i in [fp.index(l) for l in phrase.replace(" ", "")]]
    )


def test_decipher_keypad():
    pad = make_keypad("mno", 0, 2)
    deciphered = decipher_keypad(
        pad,
        "uc3 dl2 sc2 ul1 dl2 uc2 ul2 ul3 sl2 ur3 dl3 dr1 ul3 sc3 ul2 dl2 dl2 dl1 ur2 dl2 uc3 sr1 ur2 ur3 dl1 ur3 ul2 ur1 sc2 ur2 ur3 sc1 dl3 sr3 ul3 ul1 ur2 ur3 ul1",
    )
    assert deciphered == "letmeknowifyouneedhelphidingthisfromhim"


def test_make_keypad():
    assert [["ghi", "jkl", "mno"], ["pqr", "stu", "vwx"], ["yzz", "abc", "def"]] == make_keypad("mno", 0, 2)
    assert [["ghi", "jkl", "mno"], ["pqr", "stu", "vwx"], ["yzz", "abc", "def"]] == make_keypad("ghi", 0, 0)
    assert [["pqr", "stu", "vwx"], ["yzz", "abc", "def"], ["ghi", "jkl", "mno"]] == make_keypad("abc", 1, 1)


def test_cipher_keypad():
    pad = make_keypad("mno", 0, 2)
    ciphered = cipher_keypad(pad, "let me know if you need help hiding this from him")
    assert (
        ciphered
        == "uc3 dl2 sc2 ul1 dl2 uc2 ul2 ul3 sl2 ur3 dl3 dr1 ul3 sc3 ul2 dl2 dl2 dl1 ur2 dl2 uc3 sr1 ur2 ur3 dl1 ur3 ul2 ur1 sc2 ur2 ur3 sc1 dl3 sr3 ul3 ul1 ur2 ur3 ul1"
    )
