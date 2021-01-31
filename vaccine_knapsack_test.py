import dimod
import numpy as np

dqm = dimod.DiscreteQuadraticModel()

VACCINE_SHIPMENT_SIZE = 100_000  # Number of vaccines in one (individual) shipment
VACCINES_TO_DISTRIBUTE = 1_000_000

states = [
    ("OH", 3_095_781. / 5_666_150, 500_000),
    ("MA", 547_082. / 1_060_900, 500_000),
    ("CA", 911_004. / 1_553_900, 500_000),
]


total_items = VACCINES_TO_DISTRIBUTE // VACCINE_SHIPMENT_SIZE
dqm.add_variable(total_items, "leftover")

for state_name, vaccination_rate, max_capacity in states:
    item_name = state_name
    item_capacity = max_capacity // VACCINE_SHIPMENT_SIZE
    item_value = vaccination_rate * VACCINE_SHIPMENT_SIZE

    # Per-item constraint
    dqm.add_variable(item_capacity, item_name)

    # Objective
    dqm.set_linear(item_name, item_value * np.arange(item_capacity))

# Total constraint
# -(total_items - sum(item_weight for state in states) - leftover)**2
# -total_items**2 - 2 * (OH * MA + OH * CA + ...) + (2 * total_items - 1) * (OH + MA + ...)

offset = -total_items**2
for state_name, _, _ in states:
    for other_state_name, _, _ in states:
        # TODO(Turtle1331) finish this
        if state_name == other_state_name:
            #dqm.set_linear(state_name, )
            pass
        else:
            #dqm.set_quadratic(state_name, other_state_name, {(x, y): x, y for x in })
            pass
