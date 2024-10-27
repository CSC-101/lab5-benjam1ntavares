import numbers

import data

# Write your functions for each part in the space below.

# Part 1
   # The function for Part 1 should be within the class in data.py.


# Part 2
   # The function for Part 2 should be within the class in data.py.


# Part 3
#######################################################################################################################
# the add time funciton takes two time values and adds them together returning a time value in minutes seconds and hours
# extra minutes and extra hours initially defined as zero but will be changed if needed

def time_add(time1:data.Time, time2:data.Time) -> data.Time:
    total_hours = time1.hour + time2.hour
    total_minutes = time1.minute + time2.minute
    total_seconds = time1.second + time2.second

    if total_seconds >= 60:
        total_minutes = total_minutes + total_seconds // 60
        total_seconds = total_seconds % 60
    if total_minutes >= 60:
        total_hours = total_hours + total_minutes // 60
        total_minutes = total_minutes % 60
    return data.Time(total_hours, total_minutes, total_seconds)


# Part 4
#######################################################################################################################
# the is_decending function takes a single parameter type list[float] and returns a boolean expression indidcating if
# the elements within the list are in decending order

def is_decending(input_list:list[float]) -> bool:
    filtered_list = []
    for i in range(len(input_list)-1):
        if input_list[i] > input_list[i+1]:
            filtered_list.append(input_list[i])
    filtered_list.append(input_list[-1])
    return filtered_list == input_list


# Part 5
#######################################################################################################################
# largest between will take three parameters, a list of integers, lower(a lower bound), upper(an upper bound) both of
# type int. the goal of this function is to check the values at a certain index in the list. it will give the upper and
# lower bounds of the input list and it will check every value between those indexes to see which one is the largest

# I have chosen to correct the bounds if the input bounds are out of range.
# - if the upper bound is less than the lower bound, upper and lower will automatically be switched
# - if the upper or lower bound are greater than the length of the list, the bound that is greater will be set to the
#   lowest or highest possible index respectively.

def largest_between(numbers: list[int], lower: int, upper: int) -> int:
    largest_number = numbers[lower]
    largest_index = lower
    if lower > upper:
        lower, upper = upper, lower
    if upper >= len(numbers):
        upper = len(numbers) - 1
    if lower >= len(numbers):
        lower = numbers[0]
    for i in range(lower, upper+1):
        if numbers[i] > largest_number:
            largest_number = numbers[i]
            largest_index = i
    return largest_index

# Part 6
