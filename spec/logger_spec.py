import unittest
import subprocess
from should_dsl import should
from logger import Logger, InvalidOperation


class TestLogger(unittest.TestCase):

    def setUp(self):
        self.logger = Logger()

    def tearDown(self):
        subprocess.call(["rm", "-f", "python_log"])

    def it_has_a_log_file(self):
        self.logger.file |should| equal_to('python_log')

    def it_allows_change_the_log_file(self):
        self.logger.file = 'testing_logger'
        self.logger.file |should| equal_to('testing_logger')

    def it_raises_an_exception_with_a_invalid_log_file(self):
        def foo(): self.logger.file = 1
        foo |should| throw(ValueError)

    def it_has_a_writing_method(self):
        self.logger.method |should| equal_to('a')

    def it_allows_change_the_writing_method(self):
        self.logger.method = 'w'
        self.logger.method |should| equal_to('w')

    def it_raises_an_exception_with_a_invalid_log_method(self):
        def bar(): self.logger.method = 'x'
        bar |should| throw(ValueError)

    def it_writes_stdout_to_the_log_file(self):
        self.logger.start_log()
        print "a message to stdout"
        self.logger.stop_log()
        log_file_content = open("python_log").read()
        log_file_content |should| include("a message to stdout")

    def it_raises_an_exception_when_stop_log_before_start_it(self):
        self.logger.stop_log |should| throw(InvalidOperation)


if __name__ == "__main__":
    unittest.main()
