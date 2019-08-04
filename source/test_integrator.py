
import unittest
from integrator import Integrator
import mock_distributor as md
import mock_receiver as mr
import package as pk
import numpy

class TestIntegrator(unittest.TestCase):
    def setUp(self):
        self.distributor = md.MockDistributor()
        self.unit = Integrator()
        self.receiver = mr.MockReceiver()

        self.distributor.connect(self.unit)
        self.unit.connect(self.receiver)
        
    def test_integrated(self):
        expected = (3, 6, 9)

        valueA = pk.PackageValue(numpy.array((1, 2, 3)))
        timeA = 0
        package = pk.Package.make(value = valueA, timestamp = timeA)
        self.distributor.distribute(package)

        valueB = pk.PackageValue(numpy.array((1, 2, 3)))
        timeB = 2
        package = pk.Package.make(value = valueB, timestamp = timeB)
        self.distributor.distribute(package)

        actual = tuple(self.receiver.package.value.values)
        self.assertEqual(actual, expected)
