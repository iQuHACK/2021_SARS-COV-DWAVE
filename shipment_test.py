from shipment_mocking import create_mock_shipment
from shipment_analysis import estimate_shipment_value
from knapsack_solver import KnapsackSolver

NUM_SHIPMENTS = 10
NUM_VACCINE_DOSES = 200_000

SCALING_FACTOR = 10_000.

def main():
    knapsack = KnapsackSolver(SCALING_FACTOR)

    for _ in range(NUM_SHIPMENTS):
        shipment = create_mock_shipment()
        weight = shipment["doses"]
        value = estimate_shipment_value(shipment)
        print(f"Shipment: {shipment}, value: {value}")

        knapsack.add_item(shipment, weight, value)

    print("Solving...")
    knapsack.solve(NUM_VACCINE_DOSES)


if __name__ == "__main__":
    main()
