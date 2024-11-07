import unittest
from Module_12_1.module_12_1 import RunnerTest
from Module_12_2.Module_12_2 import TournamentTest

RaT_TS = unittest.TestSuite()
RaT_TS.addTest(unittest.TestLoader().loadTestsFromTestCase(RunnerTest))
RaT_TS.addTest(unittest.TestLoader().loadTestsFromTestCase(TournamentTest))

runner = unittest.TextTestRunner(verbosity=2)
runner.run(RaT_TS)