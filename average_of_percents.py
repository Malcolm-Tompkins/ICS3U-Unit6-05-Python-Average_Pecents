#!/usr/bin/env python3

# Created by Malcolm Tompkins
# Created on June 10, 2021
# Converts percentage marks to level marks


def average_of_percents(user_marks):
    # Function that calculates the average
    average = sum(user_marks) / len(user_marks)
    return average


def main():
    # Function for input and output
    user_marks = []
    print("Enter your numbers one at a time, enter -1 to stop")
    user_mark = (input("Enter your number in percent: "))
    try:
        temp_mark = int(user_mark)
        user_marks.append(temp_mark)
        while (temp_mark != -1):
            user_mark = (input("Enter your number in percent: "))
            try:
                temp_mark = int(user_mark)
                if temp_mark != -1:
                    user_marks.append(temp_mark)
            except Exception:
                print("{} is not an integer".format(user_mark))
        print("Your marks are: {}".format(user_marks))
        final_average = average_of_percents(user_marks)
        print("The average of these numbers is: {:.0f}%".format(final_average))
    except Exception:
        print("{} is not an integer".format(user_mark))


if __name__ == "__main__":
    main()
