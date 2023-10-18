# Random Room Sorter for TryHackMe

## Project Description

This is a simple Python program that allows users to randomly pick an available room on TryHackMe. It provides options to filter rooms by difficulty and free availability. The program uses TryHackMe's public API to fetch room information.

## Usage

1. Make sure you have Python installed on your system.
2. Install the dependencies using `pip install -r requirements.txt`.
3. Run the program using `python random-room.py`.
4. Follow the instructions to choose your filter preferences.
5. The program will randomly select an available room and display its information.

## Notes

- This program uses TryHackMe's public API to fetch available rooms. However, due to potential limitations in API data accuracy, it might happen that the program selects rooms that have already been completed. So, please be aware that the accuracy of results may vary.
