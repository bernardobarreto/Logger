import sys


class Logger(object):

    def __init__(self, file='python_log', method='a'):
        self._file = file
        self.method = method

    @property
    def file(self):
        return self._file

    @file.setter
    def file(self, new_file):
        if type(new_file) is str:
            self._file = new_file
        else:
            raise InvalidLogFile('need string or buffer, %s found' %(type(new_file)))

    def start_log(self):
        self.old_stdout = sys.stdout
        sys.stdout = ChangeStdout(sys.stdout, self._file, self.method)

    def stop_log(self):
        sys.stdout = self.old_stdout


class ChangeStdout(object):

    def __init__(self, stdout, file='python_log', method='a'):
        self.stdout = stdout
        self.log = file
        self.method = method

    def write(self, msg):
        self.stdout.write(msg)
        self.log_file = open(self.log, self.method)
        self.log_file.write("\n%s" %(msg))
        self.log_file.close()


class InvalidLogFile(Exception):
    pass
