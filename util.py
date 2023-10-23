"""Module providing secondary functions."""
import datetime
import csv

current_time = datetime.datetime.now()
f = current_time.day + 1


def fibonacci_number(n):
    """Count Fibonacci numbers"""
    if n <= 2:
        return 1
    return fibonacci_number(n - 1) + fibonacci_number(n - 2)


def create_csv(data):
    """Save table in csv"""
    with open("transactions.csv", "w", newline='', encoding="utf-8") as file:
        writer = csv.writer(file, delimiter=";")
        writer.writerows(
            data
        )
