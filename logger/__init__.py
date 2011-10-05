import sys


class Logger(object):

    def __init__(self, file='python_log', method='a'):
        self._file = file
        self._method = method
        self.state = False

    @property
    def file(self):
        return self._file

    @file.setter
    def file(self, new_file):
        if type(new_file) is str:
            self._file = new_file
        else:
            raise InvalidLogFile("need string, %s found" %(type(new_file)))

    @property
    def method(self):
        return self._method

    @method.setter
    def method(self, new_method):
        if new_method in ['a','w']:
            self._method = new_method
        else:
            raise InvalidLogMethod("avaible methods: 'a' and 'w', got %s" %(new_method))

    def start_log(self):
        self.old_stdout = sys.stdout
        self.state = True
        sys.stdout = _ChangeStdout(sys.stdout, self._file, self.method)

    def stop_log(self):
        if self.state:
            sys.stdout = self.old_stdout
        else:
            raise InvalidOperation("Logging hasn't been started")


class _ChangeStdout(object):

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


class InvalidLogMethod(Exception):
    pass


class InvalidOperation(Exception):
    pass
