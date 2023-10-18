import requests
import random
from colorama import Fore, Style, init

init(autoreset=True)

def get_user_choice(prompt, valid_choices):
    while True:
        user_input = input(prompt).strip().upper()
        if user_input in valid_choices:
            return user_input
        else:
            print(Fore.RED + "Please respond with 'Y' for Yes or 'N' for No." + Style.RESET_ALL)

def get_difficulty_choice():
    while True:
        user_input = input(
            "Choose the room difficulty:\n"
            "[ " + Fore.YELLOW + "0" + Style.RESET_ALL + " ] all\n"
            "[ " + Fore.YELLOW + "1" + Style.RESET_ALL + " ] info\n"
            "[ " + Fore.YELLOW + "2" + Style.RESET_ALL + " ] easy\n"
            "[ " + Fore.YELLOW + "3" + Style.RESET_ALL + " ] medium\n"
            "[ " + Fore.YELLOW + "4" + Style.RESET_ALL + " ] hard\n"
            "[ " + Fore.YELLOW + "5" + Style.RESET_ALL + " ] insane\n"
            "Choose an option (0-5): "
        ).strip()
        if user_input.isdigit() and int(user_input) in range(6):
            return int(user_input)
        else:
            print(Fore.RED + "Please choose a valid option (0-5)." + Style.RESET_ALL)

difficulty_options = {
    0: "all",
    1: "info",
    2: "easy",
    3: "medium",
    4: "hard",
    5: "insane"
}

# TryHackMe API URL
api_url = "https://tryhackme.com/api/hacktivities?page=1&order=newest&type=all&limit=100000"

user_choice_free = get_user_choice("Do you want " + Fore.GREEN + "only free" + Style.RESET_ALL + " rooms? [" + Fore.GREEN + "Y" + Style.RESET_ALL + " / " + Fore.GREEN + "N" + Style.RESET_ALL + "]: ", ["Y", "N"])

if user_choice_free == "Y":
    api_url += "&free=free"

user_choice_difficulty = get_difficulty_choice()
chosen_difficulty = difficulty_options[user_choice_difficulty]

while True:
    response = requests.get(api_url)

    if response.status_code == 200:
        data = response.json()

        rooms = [room for room in data["rooms"] if not room["userCompleted"]]

        if chosen_difficulty != "all":
            rooms = [room for room in rooms if room["difficulty"] == chosen_difficulty]

        available_rooms = {room["code"]: room for room in rooms}

        if available_rooms:
            random_room_code = random.choice(list(available_rooms.keys()))
            random_room = available_rooms[random_room_code]
            room_difficulty = random_room["difficulty"]

            print("\nRandomly chosen room: " + Fore.GREEN + random_room['title'] + Style.RESET_ALL)
            print("Room difficulty: " + Fore.GREEN + room_difficulty + Style.RESET_ALL)
            print("Room link: https://tryhackme.com/room/" + random_room_code)

            play_again = get_user_choice("\n\nDo you want to draw again? [" + Fore.GREEN + "Y " + Style.RESET_ALL +"/" + Fore.RED + " N" + Style.RESET_ALL + "]: ", ["Y", "N"])
            if play_again == "N":
                break
        else:
            print(Fore.RED + "You have completed all available rooms or no matching rooms are available." + Style.RESET_ALL)
            break
    else:
        print(Fore.RED + "Request to TryHackMe API failed." + Style.RESET_ALL)

