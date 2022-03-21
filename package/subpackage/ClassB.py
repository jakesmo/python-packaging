from package import Spinner # import from parent package
import time
import sys

class ClassB():
    def __init__(self, happy):
        self.happy = happy

    def run(self):
        sys.stdout.write(":-")
        with Spinner():
            time.sleep(5)
        sys.stdout.write(")" if self.happy else "(")
        sys.stdout.write("\n")