class Input:
    def __init__(self, weight, trigger) -> None:
        self.weight = weight
        self.value = 0
        self.trigger = trigger

    def set_value(self, value) -> None:
        self.value = value * self.weight
        self.trigger()


class Neuron:
    def __init__(self) -> None:
        self.inputs = []
        self.synapses = []

    def add_input(self, weight):
        new_input = Input(weight, self.trigger)
        self.inputs.append(new_input)
        return new_input.set_value

    def trigger(self):
        total_activation = sum(item.value for item in self.inputs)
        for synapse in self.synapses:
            synapse(total_activation)

    def add_synapse(self, synapse):
        self.synapses.append(synapse)
