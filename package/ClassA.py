from package.subpackage import ClassB

class ClassA():

    def __init__(self, happy):
        self.classB = ClassB(happy)

    def run(self):
        self.classB.run()
