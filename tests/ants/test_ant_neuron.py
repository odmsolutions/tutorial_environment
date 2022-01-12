import unittest
from unittest import mock
from ants.neuron import Neuron


class TestNeuron(unittest.TestCase):
    def test_single_input_output(self):
        # setup
        test_neuron = Neuron()
        synapse = mock.Mock()
        test_neuron.add_synapse(synapse)
        connection = test_neuron.add_input(0.67)
        # test
        connection(0.1)
        # assert
        synapse.assert_called_once_with(0.067)


if __name__ == "__main__":
    unittest.main()
