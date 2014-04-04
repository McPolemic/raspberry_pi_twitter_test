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
        message = """Four score and seven years ago, 
our fathers brought forth on this 
continent, a new nation, conceived 
in liberty and dedicated to the 
proposition that all men are 
created equal.""".replace("\n", "")
        output = self.s.message(message)
        expected_output = "\n".join(["Four score and sev",
                                     "en years ago, our ",
                                     "fathers brought fo",
                                     "rth on this contin"])
        assert_equal(expected_output, output)

    def test_message_can_be_forced_to_be_one_line(self):
        message = "This is 16 characters long"
        output = self.s.message(message, single_line=True)
        assert_equal("This is 16 charact", output)

    def test_multi_message_allows_multiple_messages(self):
        messages = "this is a test for now".split()
        output = self.s.multi_message(messages)
        assert_equal("this\nis\na\ntest", output)

    def test_multi_message_truncates_a_long_line(self):
        messages = ["Hi", "This is 16 characters long"]
        output = self.s.multi_message(messages)
        assert_equal("Hi\nThis is 16 charact", output)

    def test_scroll_message_lists_all_scrolled_messages(self):
        message = "This is 16 characters long"
        output = self.s.scroll_message(message)

        assert_equal(len(output), 9)
        assert_equal(output[0], "This is 16 charact")
        assert_equal(output[-1], "16 characters long")
