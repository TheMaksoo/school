import csv
arrivalFile = open("opdracht13\\arrivals.csv", "r", encoding="UTF-8")
arrivalInfo = csv.DictReader(arrivalFile)
arrivalList = list(arrivalInfo)

flights = 0
passengers = 0
airlineCount = 0
airlinePassengers = 0

airline = input("Airline brand: ")
amountOfPassengers = input("Min amount of passengers:")
for arrival in arrivalList:
    flights += 1
    passengers += int(arrival['passengers'])
    print(f"At {arrival['arrival']} a {arrival['airline']} flight from the city of {arrival['origin']} has landed, carrying {arrival['passengers']} passengers.")

    if airline.lower() == arrival['airline'].lower():
        airlineCount += 1

        if int(arrival['passengers']) >= int(amountOfPassengers):
            airlinePassengers +=int(arrival['passengers'])


print("--------------")
print(f"Flights: {flights}")
print(f"Passengers: {passengers}")
print(f"Average passengers: {passengers / flights}")
print("--------------")
print(f"Amount of flight from arline {airline.upper()}: {airlineCount}")
print(f"Amount of passengers for {airline.upper()}: {airlinePassengers}")
arrivalFile.close()