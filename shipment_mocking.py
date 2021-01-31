import random


# Pallet capacity ranges for each shipment company
SHIPMENT_COMPANY_CAPACITIES = [
    ("FedEx truck", 5, 20),
    ("UPS truck", 5, 20),
]

VACCINE_TYPE_PALLET_SIZES = {
    "Pfizer": 3_600,
    "Moderna": 7_200,
}

VACCINE_TYPES = list(VACCINE_TYPE_PALLET_SIZES.keys())

STATES = ["OH", "MA", "CA"]


def create_mock_shipment():
    shipment = {
        "state": random.choice(STATES),
        "vaccine_type": random.choice(VACCINE_TYPES),
    }

    shipment["company"], capacity_min, capacity_max = random.choice(SHIPMENT_COMPANY_CAPACITIES)
    pallet_capacity = random.randint(capacity_min, capacity_max)
    pallet_size = VACCINE_TYPE_PALLET_SIZES[shipment["vaccine_type"]]
    shipment["doses"] = pallet_capacity * pallet_size

    return shipment


def main():
    for _ in range(3):
        print(create_mock_shipment())


if __name__ == "__main__":
    main()
