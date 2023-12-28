import pytest


def test_emoji_import():
    try:
        import emoji

    except ImportError:
        pytest.fail("emoji not installed")

    print(emoji.emojize(":thumbs_up:"))
