import unittest
from integrator import Integrator
import mock_distributor as md
import mock_receiver as mr
import package as pk
import numpy

class TestIntegrator(unittest.TestCase):
    def setUp(self):
        self.integrator = Integrator()
        
    def test_integrated(self):
        packageA = pk.Package.make(value = numpy.array((1, 2, 3)), timestamp = 0)
        packageB = pk.Package.make(value = numpy.array((1, 2, 3)), timestamp = 2)
        self.integrator.handle(packageA)
        
        expected = (3, 6, 9)
        actual = tuple(self.integrator.handle(packageB).value)

        self.assertEqual(actual, expected)
