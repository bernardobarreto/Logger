import unittest
from should_dsl import should
from logger import Logger, ChangeStdout, InvalidLogFile


class TestLogger(unittest.TestCase):

    def setUp(self):
        self.logger = Logger()

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


if __name__ == "__main__":
    unittest.main()
