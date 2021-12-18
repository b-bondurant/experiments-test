from artiq.experiment import *
import sys
import foo
# confirm location at import time
print(foo.__file__)
# submodule import
import foo.bar
print(foo.bar.__file__)


class TestExp(EnvExperiment):
    def build(self):
        self.setattr_device('scheduler')
        
    def run(self):
        # confirm locations at runtime
        print(foo.__file__)
        print(foo.bar.__file__)
        # double check scheduler status dict
        print(self.scheduler.get_status())
        # check the path
        print(sys.path)
