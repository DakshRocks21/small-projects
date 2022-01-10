class Colours():
    def red(self, message): return ("\033[91m {}\033[00m" .format(message))
    def green(self, message): return ("\033[92m {}\033[00m" .format(message))
    def yellow(self, message): return ("\033[93m {}\033[00m" .format(message))
    def lightpurple(self, message): return ("\033[94m {}\033[00m" .format(message))
    def purple(self, message): return ("\033[95m {}\033[00m" .format(message))
    def cyan(self, message): return ("\033[96m {}\033[00m" .format(message))
    def lightGray(self, message): return ("\033[97m {}\033[00m" .format(message))
    def black(self, message): return ("\033[98m {}\033[00m" .format(message))
