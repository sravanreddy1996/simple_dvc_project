import pytest

class NotInRangeError(Exception):
    def __init__(self, message="value not in range"):
        self.message_ = message
        super().__init__(self.message_)


def test_generic():
    a = 11
    # with pytest.raises(NotInRangeError):
    if a not in range(10, 20):
        raise NotInRangeError
    else:
        assert True
