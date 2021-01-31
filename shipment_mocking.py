import random


MIN_SIZE = 10
MAX_SIZE = 20

VACCINE_TYPE_SIZES = {
    "Pfizer Kit    ": 975,
    "Moderna Kit   ": 100,
    "Pfizer Pallet ": 7_200,
    "Moderna Pallet": 3_600,
}

VACCINE_TYPES = list(VACCINE_TYPE_SIZES.keys())
STATES = ["OH", "MA", "CA"]


def create_mock_shipment():
    shipment = {
        "State": random.choice(STATES),
        "Vaccine Type": random.choice(VACCINE_TYPES),
    }

    capacity = random.randint(MIN_SIZE, MAX_SIZE)
    size = VACCINE_TYPE_SIZES[shipment["Vaccine Type"]]
    shipment["Doses"] = capacity * size

    return shipment


def main():
    for _ in range(10):
        print(create_mock_shipment())


if __name__ == "__main__":
    main()
