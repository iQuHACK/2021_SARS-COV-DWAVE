import random


# Round randomly generated shipment capacities to the nearest thousand
ROUND_CAPACITY = 1_000

# Capacity ranges for each shipment company
SHIPMENT_COMPANY_CAPACITIES = [
    ("FedEx", 500_000, 1_000_000),
    ("UPS", 500_000, 1_000_000),
    ("United Airlines", 500_000, 1_000_000),
    ("Delta Air Lines", 500_000, 1_000_000),
]

VACCINE_TYPES = [
    "Pfizer",
    "Moderna",
]

STATES = ["OH", "MA", "CA"]


def create_mock_shipment():
    shipment = {
        "state": random.choice(STATES),
        "vaccine_type": random.choice(VACCINE_TYPES),
    }

    shipment["company"], capacity_min, capacity_max = random.choice(SHIPMENT_COMPANY_CAPACITIES)
    shipment["capacity"] = random.randint(capacity_min // ROUND_CAPACITY, capacity_max // ROUND_CAPACITY) * ROUND_CAPACITY

    return shipment


def main():
    for _ in range(3):
        print(create_mock_shipment())


if __name__ == "__main__":
    main()
