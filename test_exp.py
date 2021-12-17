from artiq.experiment import *
import foo
# confirm location at import time
print(foo.__file__)
# submodule import
import foo.bar
print(foo.bar.__file__)


class TestExp(EnvExperiment):
    def run(self):
        # confirm locations at runtime
        print(foo.__file__)
        print(foo.bar.__file__)
