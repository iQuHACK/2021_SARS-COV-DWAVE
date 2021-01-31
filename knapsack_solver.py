from dimod import DiscreteQuadraticModel, ExactSolver
from dwave.system import LeapHybridDQMSampler
import numpy as np


class KnapsackSolver(object):
    def __init__(self, max_weight=None):
        self.max_weight = max_weight  # Can be specified here or at solve()
        self.dqm = DiscreteQuadraticModel()
        self.offset = 0
        self.num_items = 0
        self.item_info = []
        self.item_weight = []
        self.item_value = []
        self.item_states = []


    def add_item(self, info, weight, value, quantity=1):
        states = quantity + 1

        self.num_items += 1
        self.item_info.append(info)
        self.item_weight.append(weight)
        self.item_value.append(value)
        self.item_states.append(states)

        self.dqm.add_variable(states)


    def _init_biases(self):
        for item_a in range(self.num_items):
            states_a = self.item_states[item_a]
            for item_b in range(self.num_items):
                states_b = self.item_states[item_b]

                if item_a == item_b:
                    self.dqm.set_linear(item_a, np.zeros(states_a))
                else:
                    self.dqm.set_quadratic(item_a, item_b, np.zeros((states_a, states_b)))


    def _build_objective(self):
        for item in range(self.num_items):
            value = self.item_value[item]
            states = self.item_states[item]

            biases = self.dqm.get_linear(item)
            biases += -value * np.arange(states)
            self.dqm.set_linear(item, biases)

    def _build_constraint(self):
        lagrange = sum(w * q for w, q in zip(self.item_weight, self.item_states))
        self.offset = lagrange * self.max_weight ** 2

        for item_a in range(self.num_items):
            weight_a = self.item_weight[item_a]
            states_a = self.item_states[item_a]
            for item_b in range(item_a, self.num_items):
                weight_b = self.item_weight[item_b]
                states_b = self.item_states[item_b]

                if item_a == item_b:
                    biases = self.dqm.get_linear(item_a)
                    lin_term = np.arange(states_a)
                    biases += lagrange * ((weight_a * lin_term)**2 - 2 * self.max_weight * weight_a * lin_term)
                    self.dqm.set_linear(item_a, biases)
                else:
                    biases = self.dqm.get_quadratic(item_a, item_b, array=True)
                    quad_term = np.arange(states_a).reshape(states_a, 1) * np.arange(states_b).reshape(1, states_b)
                    biases += lagrange * (2 * weight_a * weight_b * quad_term)
                    self.dqm.set_quadratic(item_a, item_b, biases)


    def _build_dqm(self):
        self._init_biases()
        self._build_objective()
        self._build_constraint()


    def solve(self, max_weight=None, debug=False):
        self.max_weight = self.max_weight or max_weight
        if not self.max_weight or self.max_weight <= 0:
            raise ValueError("KnapsackSolver needs a positive value for max_weight")

        self._build_dqm()

        if debug:
            for item in range(self.num_items):
                print(self.dqm.get_linear(item))

            for item_a in range(self.num_items):
                for item_b in range(item_a, self.num_items):
                    if item_a != item_b:
                        print(item_a, item_b, self.dqm.get_quadratic(item_a, item_b))

        sampler = LeapHybridDQMSampler()
        sampleset = sampler.sample_dqm(self.dqm)
        # TODO
        print(sampleset)
        return sampleset


def main():
    knapsack = KnapsackSolver()

    # Simple knapsack
    knapsack.add_item("1g $4", 1, 4)
    knapsack.add_item("2g $5", 2, 5, 2)
    knapsack.add_item("3g $7", 3, 7)
    knapsack.add_item("4g $10", 4, 10)

    knapsack.solve(4)


if __name__ == "__main__":
    main()
