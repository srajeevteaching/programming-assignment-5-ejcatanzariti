# Emily Catanzariti
# CS151, Dr. Rajeev
# 11/22/2021
# Programming Assignment 5
# Programming Inputs: filename
# Programming Outputs:

import math

# index constants
TAXI_ID = 0
START_DATE = 1
END_DATE = 2
LENGTH_OF_TRIP = 3
DISTANCE = 4
COST = 5
PAYMENT_TYPE = 6
COMPANY = 7
PICKUP_LAT = 8
PICKUP_LONG = 9
DROPOFF_LAT = 10
DROPOFF_LONG = 11


# function to create list of lists
def list_of_lists(filename):
    file_list = []
    try:
        info_list = open(filename, "r")
        line_counter = 0
        for line in info_list:
            try:
                line_counter += 1
                each_trip = line.split(",")
                each_trip[TAXI_ID] = int(each_trip[TAXI_ID])
                each_trip[START_DATE] = each_trip[START_DATE].strip()
                each_trip[END_DATE] = each_trip[END_DATE].strip()
                each_trip[LENGTH_OF_TRIP] = float(each_trip[LENGTH_OF_TRIP])
                each_trip[DISTANCE] = float(each_trip[DISTANCE])
                each_trip[COST] = float(each_trip[COST])
                each_trip[PAYMENT_TYPE] = each_trip[PAYMENT_TYPE].strip()
                each_trip[COMPANY] = each_trip[COMPANY].strip()
                each_trip[PICKUP_LAT] = float(each_trip[PICKUP_LAT])
                each_trip[PICKUP_LONG] = float(each_trip[PICKUP_LONG])
                each_trip[DROPOFF_LAT] = float(each_trip[DROPOFF_LAT])
                each_trip[DROPOFF_LONG] = float(each_trip[DROPOFF_LONG])
                file_list.append(each_trip)
            except ValueError:
                print("error: skipping line", line_counter, "because of bad value")
            filename.close()
    except FileNotFoundError:
        print("sorry the file was not found")
    return file_list


# cash average
def cash_average(file_list):
    count = 0
    money_amount = 0
    for i in file_list:
        if file_list[i][PAYMENT_TYPE] == "cash":
            count += 1
            money_amount += file_list[i][COST]
    average1 = money_amount / count
    return average1


# credit card average
def credit_average(file_list):
    count = 0
    money_amount = 0
    for i in file_list:
        if file_list[i][PAYMENT_TYPE] == "credit card":
            count += 1
            money_amount += file_list[i][COST]
    average2 = money_amount / count
    return average2


# cost of cash or credit average user choice
def average_choice(file_list):
    print("would you like to find the average cost of cash or the average cost of credit?")
    choice = input("please enter cash or credit")
    choice = choice.strip().lower()
    if choice == "cash":
        average = cash_average(file_list)
    elif choice == "credit":
        average = credit_average(file_list)
    else:
        print("sorry, your input was invalid")
    return average


# function to find date trips on specified date (no input)
def trip_dates(date, file_list):
    count = 0
    for i in file_list:
        if date == file_list[i][START_DATE] or date == file_list[i][END_DATE]:
            count += 1
    return count


# user input for date
def date_choice(file_list):
    print("to choose a date, please enter separately the month, day, and year")
    year = str(input("please enter the year of the date in format yyyy"))
    month = str(input("please enter the month of the date, in format m or mm"))
    day = str(input("please enter the day of the date, in format d or dd"))
    date = year + "-" + month + "-" + day
    count_dates = trip_dates(date, file_list)
    return count_dates


# distance from location to file
def calculate_distance(distance, lat, lon, filename, file_list):
    new_list = []
    try:
        new_file = open(filename, "w")
        for i in file_list:
            lat2 = file_list[i][PICKUP_LAT]
            lon2 = file_list[i][PICKUP_LONG]
            lat3 = file_list[i][DROPOFF_LAT]
            lon3 = file_list[i][DROPOFF_LONG]
            distance1 = math.acos(math.sin(lat)*math.sin(lat2)+math.cos(lat)*math.cos(lat2)*math.cos(lon-lon2))*3959
            distance2 = math.acos(math.sin(lat)*math.sin(lat3)+math.cos(lat)*math.cos(lat3)*math.cos(lon-lon3))*3959
            if distance1 <= distance:
                new_list.append(file_list[i])
            if distance2 <= distance:
                new_list.append(file_list[i])
        for i in new_list:
            print(i, file=new_file)
        new_file.close()
    except FileNotFoundError:
        print("error: the file was not found")
    return new_file


# user input for distance calculation
def distance_choice(file_list):
    choice_distance = int(input("what is the distance in miles?"))
    print("for the location, please enter the latitude and longitude of your chosen location")
    latitude1 = float(input("what is the latitude of your location?"))
    if latitude1 < -90 or latitude1 > 90:
        print("sorry, that input is invalid. please try again.")
        latitude1 = float(input("what is the latitude of your location?"))
    longitude1 = float(input("what is the longitude of your location?"))
    if longitude1 < -180 or longitude1 > 180:
        print("sorry, that input is invalid, please try again.")
        longitude1 = float(input("what is the longitude of your location?"))
    new_file_name = input("what is the name of the new file you would like to create?")
    calculation = calculate_distance(choice_distance, latitude1, longitude1, new_file_name, file_list)
    return calculation


# main function
def main():
    file_name = input("what is the name of the file you would like to use?")
    main_list = list_of_lists(file_name)
    print("there are three choices you may choose from")
    print("you can count how many trips started or ended on a specific date - counter")
    print("you can determine the average cost of cash or credit - cost")
    print("or you can determine how many trips were within a distance of a certain location - distance")
    print("please choose one of these three options")
    choice = input("would you like to make a choice? please enter yes or no")
    choice = choice.strip().lower()
    while choice == "yes":
        choice1 = input("would you like to use counter, cost, or distance")
        choice1 = choice1.strip().lower()
        if choice1 == "counter":
            the_count_of_trips = date_choice(main_list)
            print("the count of trips that started or ended on your date is", the_count_of_trips)
        elif choice1 == "cost":
            average = average_choice(main_list)
            print("the average cost for your payment type was", average)
        elif choice1 == "distance":
            distance = distance_choice(main_list)
            print("the new file is", distance)
        else:
            print("sorry, your input was invalid, please try again")
        choice = input("would you like to make a choice? please enter yes or no")
    else:
        print("thank you for using this program :)")


# call main
main()
