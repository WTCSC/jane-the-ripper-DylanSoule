import pytest
import jane_the_ripper

def test_crack_passwords():
    assert jane_the_ripper.crack_passwords('./hashes.txt', './wordlist.txt', 'md5') == {'e99a18c428cb38d5f260853678922e03': 'abc123',
        'eb0a191797624dd3a48fa681d3061212': 'master',
        'c33367701511b4f6020ec61ded352059': '654321',
        '40be4e59b9a2a2b5dffb918c0e86b3d7': 'welcome',
        '21b72c0b7adc5c7b4a50ffcb90d92dd6': 'matrix',
        'bf779e0933a882808585d19455cd7937': 'charlie',
        'a53f3929621dba1306f8a61588f52f55': 'edward',
        'f4f068e71e0d87bf0ad51e6214ab84e9': 'angel',
        'aa47f8215c6f30a0dcdb2a36a9f4168e': 'daniel',
        'fe546279a62683de8ca334b673420696': 'samsung',
        '74309fe83c9bc17a25ca74e69c3cf049': 'Password not found in wordlist',
        'b9e851d3be78ab9ed830f47fb5dec294': 'Password not found in wordlist',
        'ee7d692412c833694f6341aa54fb5ad9': 'Password not found in wordlist',
        '7037f707e8b53a3d183c1b0b5031e7c0': 'Password not found in wordlist',
        '9b66f29e6a3bf8f78003c3642305b7fa': 'Password not found in wordlist'}
    assert jane_the_ripper.crack_passwords('./hashes.txt', './wordlist.txt', 'sha256') == {'e99a18c428cb38d5f260853678922e03': 'Password not found in wordlist',
        'eb0a191797624dd3a48fa681d3061212': 'Password not found in wordlist',
        'c33367701511b4f6020ec61ded352059': 'Password not found in wordlist',
        '40be4e59b9a2a2b5dffb918c0e86b3d7': 'Password not found in wordlist',
        '21b72c0b7adc5c7b4a50ffcb90d92dd6': 'Password not found in wordlist',
        'bf779e0933a882808585d19455cd7937': 'Password not found in wordlist',
        'a53f3929621dba1306f8a61588f52f55': 'Password not found in wordlist',
        'f4f068e71e0d87bf0ad51e6214ab84e9': 'Password not found in wordlist',
        'aa47f8215c6f30a0dcdb2a36a9f4168e': 'Password not found in wordlist',
        'fe546279a62683de8ca334b673420696': 'Password not found in wordlist',
        '74309fe83c9bc17a25ca74e69c3cf049': 'Password not found in wordlist',
        'b9e851d3be78ab9ed830f47fb5dec294': 'Password not found in wordlist',
        'ee7d692412c833694f6341aa54fb5ad9': 'Password not found in wordlist',
        '7037f707e8b53a3d183c1b0b5031e7c0': 'Password not found in wordlist',
        '9b66f29e6a3bf8f78003c3642305b7fa': 'Password not found in wordlist'}
    assert jane_the_ripper.crack_passwords('bad_hash_path', './wordlist.txt', 'md5') == 'Wrong Path to Hash File, Please Try Again'
    assert jane_the_ripper.crack_passwords('./hashes.txt', 'bad_wordlist_path','md5') == 'Wrong Path to Wordlist, or hashing algorithm is not supported by hashlib, Please Try Again'
    assert jane_the_ripper.crack_passwords('./hashes.txt', './wordlist.txt', 'fake_algorithm') == 'Wrong Path to Wordlist, or hashing algorithm is not supported by hashlib, Please Try Again'
    