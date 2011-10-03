import unittest
import subprocess
from should_dsl import should
from logger import Logger, ChangeStdout, InvalidLogFile


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

    def it_has_a_writing_method(self):
        self.logger.method |should| equal_to('a')

    def it_allows_change_the_writing_method(self):
        self.logger.method = 'w'
        self.logger.method |should| equal_to('w')

    def it_writes_stdout_to_the_log_file(self):
        self.logger.start_log()
        print "a message to stdout"
        self.logger.stop_log()
        log_file_content = open("python_log").read()
        log_file_content |should| include("a message to stdout")


if __name__ == "__main__":
    unittest.main()
