import unittest
from unittest import mock
from python_ants.neuron import Neuron

class TestNeuron(unittest.TestCase):
  def test_single_input_output(self):
    # setup
    test_neuron = Neuron()
    connection = test_neuron.add_input(weight=0.67)
    synapse = mock.Mock()
    # test
    connection(0.1)
    # assert
    synapse.assert_called_once_with(0.67)

if __name__ == "__main__":
  unittest.main()
