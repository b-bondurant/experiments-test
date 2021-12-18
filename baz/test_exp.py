from artiq.experiment import *
import sys
from foo.foo import Foo
from foo.bar.bar import Bar


class TestExp(EnvExperiment):
    def build(self):
        self.setattr_device('scheduler')
        
    def run(self):
        Foo()
        Bar()
        # double check scheduler status dict
        print(self.scheduler.get_status())
        # check the path
        print(sys.path)
