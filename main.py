# Define three variables for the LaunchCode shuttle - one for the starting fuel level, another for the number of astronauts aboard, and the third for the altitude the shuttle reaches.

starting_fuel = 0
astronauts_aboard = 0
shuttle_altitude = 0

# Exercise #4: Construct while loops to do the following:

  # a. Query the user for the starting fuel level. Validate that the user enters a positive, integer value greater than 5000 but less than 30000. 

while starting_fuel <= 5000 or starting_fuel > 30000:
	starting_fuel = int(input("Enter starting fuel:"))

# b. Use a second loop to query the user for the number of astronauts (up to a maximum of 7). Validate the entry.

while astronauts_aboard <= 1 or astronauts_aboard > 7:
	astronauts_aboard = int(input("Enter the number of astronauts on board:"))
  
# c. Use a final loop to monitor the fuel status and the altitude of the shuttle. Each iteration, decrease the fuel level by 100 units for each astronaut aboard. Also, increase the altitude by 50 kilometers.

fuel_status = 0
altitude_status = shuttle_altitude + 50

for fuel_status in range(starting_fuel, 0, astronauts_aboard*-100):
	print("Fuel Status: ", fuel_status)

for altitude_status in range(0, shuttle_altitude, 50):
	print("Altitude Status: ", altitude_status)

# Exercise #5: Print the result with the phrase, The shuttle gained an altitude of ___ km and has ___ kg of fuel left. Fill in the blanks with the altitude and fuel level values.

# If the altitude is 2000 km or higher, add “Orbit achieved!” Otherwise add, “Failed to reach orbit.”
