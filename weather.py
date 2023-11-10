import csv
from datetime import datetime
from pprint import pprint
from statistics import mean

DEGREE_SYBMOL = u"\N{DEGREE SIGN}C"


def format_temperature(temp):
    """Takes a temperature and returns it in string format with the degrees
        and celcius symbols.

    Args:
        temp: A string representing a temperature.
    Returns:
        A string contain the temperature and "degrees celcius."
    """
    return f"{temp}{DEGREE_SYBMOL}"


def convert_date(iso_string):
    """Converts and ISO formatted date into a human readable format.

    Args:
        iso_string: An ISO date string..
    Returns:
        A date formatted like: Weekday Date Month Year e.g. Tuesday 06 July 2021
    """

    date_obj = datetime.fromisoformat(iso_string)

    # Format the date as "Weekday Date Month Year" (e.g., "Tuesday 06 July 2021")
    formatted_date = date_obj.strftime("%A %d %B %Y")
    return formatted_date


# MY NOTE#
# To change the format of your datetime object, we'll simply need to pass in the
# appropriate format to the strftime() method.
# The format is expressed using special directives like the following:

# %Y – year with century (e.g., 2019).
# %y – year without century (e.g., 19).
# %B – month as a full name (e.g., March).
# %b – month as an abbreviated name (e.g., Mar).
# %m – month as a zero-padded integer (e.g., 03).
# %d – day of the month as a zero-padded integer (e.g., 25).
# %A – weekday as a full name (e.g., Monday).
# %a – weekday as an abbreviated name (e.g., Mon).


def convert_f_to_c(temp_in_farenheit):
    """Converts an temperature from farenheit to celcius.

    Args:
        temp_in_farenheit: float representing a temperature.
    Returns:
        A float representing a temperature in degrees celcius, rounded to 1dp.
    """
    # (100°F − 32) × 5/9 = 37.778°C
    temp_in_farenheit_float = 0.00

    if (isinstance(temp_in_farenheit, str)):
        converted_number = float(temp_in_farenheit)
        temp_in_farenheit_float = converted_number
    else:
        temp_in_farenheit_float = temp_in_farenheit

    return round((temp_in_farenheit_float - 32) * 5/9, 1)


def calculate_mean(weather_data):
    """Calculates the mean value from a list of numbers.

    Args:
        weather_data: a list of numbers.
    Returns:
        A float representing the mean value.
    """
    added_numbers = 0.00
    total_items = len(weather_data)
    for item in weather_data:

        if (isinstance(item, str)):
            converted_number = float(item)
            added_numbers += converted_number
        else:
            added_numbers += item
    return added_numbers / total_items


def load_data_from_csv(csv_file):
    """Reads a csv file and stores the data in a list.

    Args:
        csv_file: a string representing the file path to a csv file.
    Returns:
        A list of lists, where each sublist is a (non-empty) line in the csv file.
    """

    # output list to store all rows
    Output = []
    with open(csv_file, encoding="utf-8") as my_file:

        reader = csv.reader(my_file, delimiter=',')
        # store the headers in a separate variable,
        # move the reader object to point on the next row
        headings = next(reader)

        for row in reader:
            if (len(row) > 0):
                item1 = int(row[1])
                item2 = int(row[2])
                Output.append([row[0], item1, item2])

    return Output


def find_min(weather_data):
    """Calculates the minimum value in a list of numbers.

    Args:
        weather_data: A list of numbers.
    Returns:
        The minium value and it's position in the list. (In case of multiple matches, return the index of the *last* example in the list.)
    """

    # new_list = []
    # if (len(weather_data) > 0):
    #     for items in weather_data:
    #         converted_data = float(items)
    #         new_list.append(converted_data)

    #     min_number = min(new_list)
    #     last_min_numb_index = 0
    #     for numb in new_list:
    #         if (numb == min_number):
    #             last_min_numb_index = new_list.index(numb)

    #     result = (min_number, last_min_numb_index)
    #     return result
    # return ()
    if len(weather_data) == 0:
        return ()

    min_number = float(weather_data[0])
    last_min_numb_index = 0

    for item, num in enumerate(weather_data):
        converted_data = float(num)
        if converted_data <= min_number:
            min_number = converted_data
            last_min_numb_index = item

    return (min_number, last_min_numb_index)


def find_max(weather_data):
    """Calculates the maximum value in a list of numbers.

    Args:
        weather_data: A list of numbers.
    Returns:
        The maximum value and it's position in the list. (In case of multiple matches, return the index of the *last* example in the list.)
    """

    if len(weather_data) == 0:
        return ()

    max_number = float(weather_data[0])
    last_max_numb_index = 0

    for item, num in enumerate(weather_data):
        converted_data = float(num)
        if converted_data >= max_number:
            max_number = converted_data
            last_max_numb_index = item

    return (max_number, last_max_numb_index)


def generate_summary(weather_data):
    """Outputs a summary for the given weather data.

    Args:
        weather_data: A list of lists, where each sublist represents a day of weather data.
    Returns:
        A string containing the summary information.
    """

    min_temperature_list = []
    max_temperature_list = []

    for items in weather_data:
        min_temperature_list.append(items[1])
        max_temperature_list.append(items[2])

    min_temperature = find_min(min_temperature_list)
    max_temperature = find_max(max_temperature_list)

    average_min_temperature = calculate_mean(min_temperature_list)
    average_max_temperature = calculate_mean(max_temperature_list)

    min_temperature_celsius = convert_f_to_c(min_temperature[0])
    max_temperature_celsius = convert_f_to_c(max_temperature[0])

    average_min_temperature_celsius = convert_f_to_c(average_min_temperature)
    average_max_temperature_celsius = convert_f_to_c(average_max_temperature)

    day_min_value = ""
    day_max_value = ""

    for line in weather_data:
        if line[1] == min_temperature[0]:
            day_min_value = convert_date(line[0])
        if line[2] == max_temperature[0]:
            day_max_value = convert_date(line[0])

    result = (f"{len(weather_data)} Day Overview\n")
    result += (f"  The lowest temperature will be {
               min_temperature_celsius}°C, and will occur on {day_min_value}.\n")
    result += (f"  The highest temperature will be {
               max_temperature_celsius}°C, and will occur on {day_max_value}.\n")
    result += (f"  The average low this week is {
               average_min_temperature_celsius}°C.\n")
    result += (f"  The average high this week is {
               average_max_temperature_celsius}°C.\n")
    return result


def generate_daily_summary(weather_data):
    """Outputs a daily summary for the given weather data.

    Args:
        weather_data: A list of lists, where each sublist represents a day of weather data.
    Returns:
        A string containing the summary information.
    """

    formated_list = ""
    for item in weather_data:
        item_date = convert_date(item[0])
        newresult = f"---- {item_date} ----\n"
        min_temp = convert_f_to_c(item[1])
        newresult += f"  Minimum Temperature: {min_temp}°C\n"
        max_temp = convert_f_to_c(item[2])
        newresult += f"  Maximum Temperature: {max_temp}°C\n"
        newresult += f"\n"
        formated_list += newresult

    return (formated_list)
