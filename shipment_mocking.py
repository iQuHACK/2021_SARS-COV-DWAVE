import random

MIN_SIZE = 10
MAX_SIZE = 20

sample_shipments = [
    {"state": "OH", "vaccine_type": "Moderna Pallet", "capacity": 14},
    {"state": "CA", "vaccine_type": "Moderna Kit   ", "capacity": 10},
    {"state": "CA", "vaccine_type": "Moderna Kit   ", "capacity": 20},
    {"state": "OH", "vaccine_type": "Moderna Pallet", "capacity": 19},
    {"state": "MA", "vaccine_type": "Moderna Kit   ", "capacity": 10},
    {"state": "MA", "vaccine_type": "Moderna Pallet", "capacity": 12},
    {"state": "CA", "vaccine_type": "Moderna Pallet", "capacity": 20},
    {"state": "OH", "vaccine_type": "Moderna Kit   ", "capacity": 19},
    {"state": "OH", "vaccine_type": "Moderna Pallet", "capacity": 17},
    {"state": "CA", "vaccine_type": "Moderna Pallet", "capacity": 17},
    
]

VACCINE_TYPE_SIZES = {
    "Moderna Kit   ": 100,
    "Moderna Pallet": 3_600,
}

VACCINE_TYPES = list(VACCINE_TYPE_SIZES.keys())
STATES = ["OH", "MA", "CA"]


def create_mock_shipment():
    shipment = {
        "state": random.choice(STATES),
        "vaccine_type": random.choice(VACCINE_TYPES),
    }

    capacity = random.randint(MIN_SIZE, MAX_SIZE)
    size = VACCINE_TYPE_SIZES[shipment["vaccine_type"]]
    shipment["doses"] = capacity * size

    return shipment

def next_sample_shipment():
    shipment = sample_shipments.pop(0)
    size = VACCINE_TYPE_SIZES[shipment["vaccine_type"]]
    shipment["doses"] = capacity * size

    return shipment


def main():
    for _ in range(10):
        print(create_mock_shipment())


if __name__ == "__main__":
    main()
