# Define three variables for the LaunchCode shuttle - one for the starting fuel level, another for the number of astronauts aboard, and the third for the altitude the shuttle reaches.

fuel = 0
astronauts_aboard = 0
shuttle_altitude = 0

# Exercise #4: Construct while loops to do the following:

  # a. Query the user for the starting fuel level. Validate that the user enters a positive, integer value greater than 5000 but less than 30000. 

while fuel <= 5000 or fuel > 30000:
	fuel = int(input("Enter starting fuel:"))

# b. Use a second loop to query the user for the number of astronauts (up to a maximum of 7). Validate the entry.

while astronauts_aboard <= 1 or astronauts_aboard > 7:
	astronauts_aboard = int(input("Enter the number of astronauts on board:"))


# c. Use a final loop to monitor the fuel status and the altitude of the shuttle. Each iteration, decrease the fuel level by 100 units for each astronaut aboard. Also, increase the altitude by 50 kilometers.

while fuel - astronauts_aboard*-100 > astronauts_aboard*100:
	fuel -= astronauts_aboard*100
	shuttle_altitude += 50
	print("Shuttle altitude: ", shuttle_altitude , "\nFuel Level: ", fuel)

# Exercise #5: Print the result with the phrase, The shuttle gained an altitude of ___ km and has ___ kg of fuel left. Fill in the blanks with the altitude and fuel level values.

print("The shuttle gained an altitude of", shuttle_altitude, "km and has", fuel, "kg of fuel left.")

# If the altitude is 2000 km or higher, add “Orbit achieved!” Otherwise add, “Failed to reach orbit.”

if shuttle_altitude >= 2000:
	print("Orbit achieved!")

else:
	print("Failed to reach orbit.")