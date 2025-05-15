"""Calculate the total cost of a holiday based on flight, hotel, and car rental costs."""


def plane_cost(city_flight: str) -> int:
    """Calculate the cost of a flight to a specified city.

    Args:
        city_flight (str): The destination city (Durban, Cape Town, or Johannesburg).

    Returns:
        int: The cost of the flight in Rand.

    Raises:
        ValueError: If the city is not one of the valid options.
    """
    city = city_flight.lower()
    if city == "durban":
        return 1500
    if city == "cape town":
        return 2000
    if city == "johannesburg":
        return 3000
    raise ValueError("Invalid city. Please choose Durban, Cape Town, or Johannesburg.")


def hotel_cost(num_nights: int) -> int:
    """Calculate the cost of a hotel stay based on the number of nights.

    Args:
        num_nights (int): Number of nights staying at the hotel.

    Returns:
        int: The total cost of the hotel stay in Rand.

    Raises:
        ValueError: If the number of nights is negative.
    """
    if num_nights < 0:
        raise ValueError("Number of nights cannot be negative.")
    if num_nights == 0:
        return 0
    return num_nights * 2500  # Cost per night is 2500 Rand


def car_rental_cost(rental_days: int) -> int:
    """Calculate the cost of a car rental based on the number of days.

    Args:
        rental_days (int): Number of days renting the car.

    Returns:
        int: The total cost of the car rental in Rand.

    Raises:
        ValueError: If the number of rental days is negative.
    """
    if rental_days < 0:
        raise ValueError("Number of rental days cannot be negative.")
    if rental_days == 0:
        return 0
    return rental_days * 1000  # Cost per day is 1000 Rand


def holiday_cost(city_flight: str, num_nights: int, rental_days: int) -> int:
    """Calculate the total cost of a holiday.

    Args:
        city_flight (str): The destination city.
        num_nights (int): Number of nights staying at the hotel.
        rental_days (int): Number of days renting the car.

    Returns:
        int: The total cost of the holiday in Rand.
    """
    flight_cost = plane_cost(city_flight)
    hotel_cost_total = hotel_cost(num_nights)
    car_rental_cost_total = car_rental_cost(rental_days)
    return flight_cost + hotel_cost_total + car_rental_cost_total


def main():
    """Run the holiday cost calculator with user input."""
    print("This program calculates the total cost of a holiday based on flight, "
          "hotel, and car rental costs.\n")
    print("Please enter the following details to calculate your holiday cost:\n")

    # Get user input for the city flight
    city_flight = input("Enter which city you want to know the price of between these three "
                        "(Durban, Cape Town, Johannesburg): ")

    # Calculate and display flight cost
    flight_cost = plane_cost(city_flight)
    print(f"The price of the flight to {city_flight} is {flight_cost} Rand")

    # Get user input for hotel stay
    num_nights = int(input("Enter the number of nights you will be staying at the hotel: "))

    # Calculate and display hotel cost
    hotel_cost_total = hotel_cost(num_nights)
    print(f"The cost of the hotel for {num_nights} nights is {hotel_cost_total} Rand")

    # Get user input for car rental
    rental_days = int(input("Enter the number of days you will be renting the car: "))

    # Calculate and display car rental cost
    car_rental_cost_total = car_rental_cost(rental_days)
    print(f"The cost of the car rental for {rental_days} days is {car_rental_cost_total} Rand")

    # Display total cost
    print("\n")
    total_cost = holiday_cost(city_flight, num_nights, rental_days)
    print(f"The total cost of the holiday is {total_cost} Rand")


if __name__ == "__main__":
    main()