import logging
import string
from typing import Callable

import pytest

abet = string.ascii_lowercase


def decipher_mirror(word: str) -> str:
    """
    Decipher text in a mirrored alphabet
    :param word: mirrored lowercase word i.e. 'erloz'
    :return: deciphered word 'viola'
    """
    res = []
    for c in word:
        if c.lower() in abet:
            dc = abet[len(abet) - abet.index(c.lower()) - 1]
            res.append(dc if c.islower() else dc.upper())
        else:
            res.append(c)
    return "".join(res)


def decipher_swardkcab(word: str) -> str:
    """
    Decipher word (its backwards).

    :param word:
    :return:
    """
    return word[::-1]


def cipher_mirror(word: str) -> str:
    """
    Encipher text in a mirrored alphabet
    :param word:
    :return:
    """
    return decipher_mirror(word)


@pytest.mark.parametrize("code,plain", [["erloz", "viola"], ["Erloz", "Viola"], ["wrwm'g", "didn't"]])
def test_decipher_mirror(code: str, plain: str):
    assert decipher_mirror(code) == plain


def test_decipher_swardkcab():
    assert decipher_swardkcab("olleh") == "hello"


def decipher_text(decipherer: Callable[[str], str], text: str) -> str:
    """
    For every non-english word in a block of text, attempt to decipher it with decipherer.

    :param decipherer: a deciphering function
    :param text: a block of text
    :return: deciphered text.
    """
    import enchant.tokenize
    import enchant
    eng = enchant.Dict("en_US")
    tokenizer = enchant.tokenize.get_tokenizer("en_US")
    deciphered_text = text
    for word, pos in tokenizer(text):
        if not eng.check(word):
            res = decipherer(word)
            if eng.check(res):
                logging.debug(f"deciphering word({word}) -> decipher({res})")
                assert len(res) == len(word)
                deciphered_text = deciphered_text[:pos] + res + deciphered_text[pos + len(res) :]
            else:
                logging.debug(f"non-english word({word}) but decipher({res}) also not english")
    return deciphered_text


def test_decipher_text():
    c = cipher_mirror
    ciphertext = (
        f"When I {c('agreed')} to be involved {c('Timmy')}, I didn't know what I was {c('saying')} yes {c('to')}."
    )
    deciphered = decipher_text(decipher_mirror, ciphertext)
    assert deciphered == "When I agreed to be involved Timmy, I didn't know what I was saying yes to."
