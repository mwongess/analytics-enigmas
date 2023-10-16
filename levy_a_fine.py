# Write a program that can be used by a policeman to determine if a vehicle has 
# exceeded the speed limit and to levy a fine. The policeman should enter the vehicles 
# speed and the speed limit. If the speed limit is exceeded by less than 30kph a fine of 
# Kshs. 2500 should be charged. Otherwise a fine of Kshs 4000 is charged. Your 
# program should then output (in a suitable format) the vehicle speed, the speed limit, 
# the excess speed and the fine levied.

def levy_a_fine():
    try:
        vehicle_speed = int(input("Enter the vehicle speed:"))
        speed_limit = int(input("Enter speed limit:"))
        
        excess_speed = vehicle_speed - speed_limit
        
        if excess_speed < 30:
            fine = 2500
        else:
            fine = 4000   
                 
    except ValueError:
        print("Enter a valid speed or limit!")

if __name__ == "__main__":
    levy_a_fine()