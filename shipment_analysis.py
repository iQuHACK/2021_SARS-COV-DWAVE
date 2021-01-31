STATE_VACCINATION_RATES = {
    "OH": 3_095_781. / 5_666_150,
    "MA": 547_082. / 1_060_900,
    "CA": 911_004. / 1_553_900,
}


def estimate_shipment_value(shipment):
    # Estimate value as the expected amount of administered vaccines
    vaccination_rate = STATE_VACCINATION_RATES[shipment["state"]]
    administered = int(shipment["doses"] * vaccination_rate)
    return administered


def main():
    import shipment_mocking as mock

    for i in range(3):
        shipment = mock.create_mock_shipment()
        estimated_value = estimate_shipment_value(shipment)
        print(f"Shipment: {shipment}")
        print(f"Estimated value: {estimated_value}")


if __name__ == "__main__":
    main()
