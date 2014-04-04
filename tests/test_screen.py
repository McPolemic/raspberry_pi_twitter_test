from nose.tools import assert_equal
from screen import *

class TestScreen:
    def setUp(self):
        self.s = Screen(width=18, height=4)

    def test_init_screen(self):
        assert self.s

    def test_format_single_short_message(self):
        message = "A short message"
        output = self.s.message(message)
        assert_equal(message, output)

    def test_format_single_long_message_to_two_lines(self):
        message = "This is 16 characters long"
        output = self.s.message(message)
        assert_equal("This is 16 charact\ners long", output)

    def test_message_truncates_really_long_line(self):
        #XXX: Fill out
        pass
