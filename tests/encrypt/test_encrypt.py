from challenges.challenge_encrypt_message import encrypt_message
import pytest


def test_encrypt_message():
    assert encrypt_message("abcabc", 3) == "cba_cba"
    assert encrypt_message("abcabc", 2) == "cbac_ba"
    assert encrypt_message("abc", 9) == "cba"
    with pytest.raises(TypeError):
        encrypt_message(3, 3)
        encrypt_message("a", "a")
