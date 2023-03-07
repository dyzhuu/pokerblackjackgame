import random
import time
import os
import pickle

def cls():
    """This is a function used for clearing the terminal"""
    os.system('cls' if os.name == 'nt' else 'clear')


# Define global values: this is so you can continue the game even if you quit to main menu.
bj_player_money = 1500
bj_restricted_values = []
p_player_money = 1500
bot_money = [1500, 1500, 1500, 1500, 1500]
bot_count = []
bot_num = 0
out = []

# Keeps the high score persistent (it stays even if you close the file)
try:
    with open('score (delete file to reset score).dat', 'rb') as file:  # imports the file data
        high_score = pickle.load(file)
except FileNotFoundError:  # resets the data if the file is not found
    high_score = {"Poker": 0, "Blackjack": 0}

# Defining the suit values (used in both games)
suit_dict = ['♠', '♣', '♥', '♦']


def hand_display(x):
    """Displays hand in a presentable format - converts list to string (used in both games)

    Keyword arguments:
    x -- the hand of the player (list of 5 cards)"""
    hand = x.copy()
    change_dict = {'10': 'T', '11': 'J', '12': 'Q', '13': 'K', '14': 'A'}
    for i in x:
        if i[:-1] in ['10', '11', '12', '13', '14']:
            hand[hand.index(i)] = change_dict[i[:-1]] + i[-1]
    return ' '.join(hand)

def win_animation():
    """This is a function that uses print and cls() with ASCII art to display an animation that plays when you
    beat the game (poker)"""
    cls()
    print("""
_   _____________________  _____  __  ___  ______  _____   __   ____
| | / /  _/ ___/_  __/ __ \/ _ \ \/ / / _ \/ __ \ \/ / _ | / /  / __/
| |/ // // /__  / / / /_/ / , _/\  / / , _/ /_/ /\  / __ |/ /__/ _/ 
|___/___/\___/ /_/  \____/_/|_| /_/ /_/|_|\____/ /_/_/ |_/____/___/ 


                           ▄▄
                           █▓▓
                           ██▄
                          ▓▓█▓▀▓
                       ░▄▀██████▓█▄
                       ░   ▀████  ▀▄
                        ░▄▄▄████▄  █
                         ▀███████▓▓▀
                          ░███████
                          ▓███ ███
                          ▓██▓ ▓██
                           ██   ██▄
                          ▄██   ███
                          ███   ███
                          ██▀   ▀██
                          ▀█     ▀█
                           █      ██
                           ▓      ▀▓▓▓
                          ▀▀""")
    time.sleep(.2)
    cls()
    print("""
_   _____________________  _____  __  ___  ______  _____   __   ____
| | / /  _/ ___/_  __/ __ \/ _ \ \/ / / _ \/ __ \ \/ / _ | / /  / __/
| |/ // // /__  / / / /_/ / , _/\  / / , _/ /_/ /\  / __ |/ /__/ _/ 
|___/___/\___/ /_/  \____/_/|_| /_/ /_/|_|\____/ /_/_/ |_/____/___/ 


                          ▄▓▄
                          ░▓▓
                          ▄▓█▓
                        ▄█░▓██
                       ▄███▀██ ▄
                        ▄░██▓▄▓▓
                       ▀ ▄████▓▀
                         ▓██▓▓█
                        ▓██▀ ██
                       ▄██▀░██▓
                       ██▀ ▓██
                       ██▄ ██▓
                        ██▓ ██▓
                         ▀█ ▓██
                          ▓█ ██
                        ▓▓▓▀ ▀█
                             ▄█
                            ▓█▓""")
    time.sleep(.2)
    cls()
    print("""
_   _____________________  _____  __  ___  ______  _____   __   ____
| | / /  _/ ___/_  __/ __ \/ _ \ \/ / / _ \/ __ \ \/ / _ | / /  / __/
| |/ // // /__  / / / /_/ / , _/\  / / , _/ /_/ /\  / __ |/ /__/ _/ 
|___/___/\___/ /_/  \____/_/|_| /_/ /_/|_|\____/ /_/_/ |_/____/___/ 


                               ▄██▓  ▄▄
                             ▄▄▄▄▓██████
                         ▄▓▄▄▓▓▓▓▓███▓██
                       ▓▓         ▀▄███▄
                                    ▀████▓▄
                                   ▄████▓▓█
                                   ███▀████
                                  ▓██▓ ███▀
                                  ███  ███
                                  ▓▓█  █▓
                                   █▀  ██▓
                                       ▀██░
                                        ▓█
                                         █
                                         █▄
                                        ▓█""")
    time.sleep(.2)
    cls()
    print("""
_   _____________________  _____  __  ___  ______  _____   __   ____
| | / /  _/ ___/_  __/ __ \/ _ \ \/ / / _ \/ __ \ \/ / _ | / /  / __/
| |/ // // /__  / / / /_/ / , _/\  / / , _/ /_/ /\  / __ |/ /__/ _/ 
|___/___/\___/ /_/  \____/_/|_| /_/ /_/|_|\____/ /_/_/ |_/____/___/ 


                         ▄
                        ▓██▄
                        ▀██▄
                         ▀█▓▄▄▄
                         █████▀▓▓▄
                        ██████   ▓▓
                         ▀████▄  █▀
                          ████████
                        ▄████████▓
                        ███▓▀████
                        ██▓  ████
                       ▓██    ███
                       ▀██▄   ████▓▄
                        ██▀   ▀▀▀▀▀▓█▓
                         █         ▄█
                         ██        ▀▀
                       ▄▓█▀""")
    time.sleep(.2)
    cls()
    print("""
_   _____________________  _____  __  ___  ______  _____   __   ____
| | / /  _/ ___/_  __/ __ \/ _ \ \/ / / _ \/ __ \ \/ / _ | / /  / __/
| |/ // // /__  / / / /_/ / , _/\  / / , _/ /_/ /\  / __ |/ /__/ _/ 
|___/___/\___/ /_/  \____/_/|_| /_/ /_/|_|\____/ /_/_/ |_/____/___/ 


                              ▄▄                        
                             ███▄         ▄▄█            
                             ▀███▓███▓▓▄▓▓▓▀▀▀           
                             ▄█▓█████  ▀                 
                       ▀█▄▄▄▄▓▀ ▀████                 
                        ▀▀▀▀▀    ▀███▄                 
                                 ▓█████                 
                                ███████            
                                ██████▀          
                                ██████                  
                                ██▓██                   
                              ▓██▀▓███▓▄                
                              █▀▀   ▀▓██▓▄                 
                             █▄        ▀▀▓▓▄             
                            ▀▓           ▄██▓              
                                         ▀▀▀                  """)
    time.sleep(.2)
    cls()
    print("""
_   _____________________  _____  __  ___  ______  _____   __   ____
| | / /  _/ ___/_  __/ __ \/ _ \ \/ / / _ \/ __ \ \/ / _ | / /  / __/
| |/ // // /__  / / / /_/ / , _/\  / / , _/ /_/ /\  / __ |/ /__/ _/ 
|___/___/\___/ /_/  \____/_/|_| /_/ /_/|_|\____/ /_/_/ |_/____/___/ 


                             ▄▓▓
                             ████▄▄
                            ▄▓██████
                       ▄▓▄▓▓███▓████
                       ▀▓██▓▀▀ █████
                         ▀    ████▄▄
                              ▄▓██████
                            ▄█████▓████
                           ▄███▓▀  ████
                           ██▓▀    ▓██▀
                           ▀██▄     ██▄
                            ███     ▓██
                            ▀██      ▀█
                              █      ▄█
                             ▄██
                           ░█▓▓▓""")
    time.sleep(.2)
    cls()
    print("""
_   _____________________  _____  __  ___  ______  _____   __   ____
| | / /  _/ ___/_  __/ __ \/ _ \ \/ / / _ \/ __ \ \/ / _ | / /  / __/
| |/ // // /__  / / / /_/ / , _/\  / / , _/ /_/ /\  / __ |/ /__/ _/ 
|___/___/\___/ /_/  \____/_/|_| /_/ /_/|_|\____/ /_/_/ |_/____/___/ 


                           ▄
                         ▓█▓   ▄ ▄▄
                        ▓█    ███▀▀▓▄▄
                       ▓█▄▄▄▄▄███▄▄▓▓█▓▄
                       ▀▀▀▀▀▓███████▀▀▓▓
                              █████▓
                              ▓████
                               ▓█████
                              ▄██████
                              ██████▓
                              █████▓
                              █████
                              ▀████
                               ▀████
                                ▀█▀▓█▄
                                ▄█   ██▄
                                █   ▓█▀▀
                               ▄██  ▀
                                ▀""")
    time.sleep(.2)
    cls()
    print("""
_   _____________________  _____  __  ___  ______  _____   __   ____
| | / /  _/ ___/_  __/ __ \/ _ \ \/ / / _ \/ __ \ \/ / _ | / /  / __/
| |/ // // /__  / / / /_/ / , _/\  / / , _/ /_/ /\  / __ |/ /__/ _/ 
|___/___/\___/ /_/  \____/_/|_| /_/ /_/|_|\____/ /_/_/ |_/____/___/ 


                             ▓█▓
                          ▄▄▄███
                         ▓███████▓
                         █████████
                         █▓████▓▀█▓
                         ████████▓█
                        ▄███████▓ █▓
                       ▄█▓█████▓  ██▄
                       ▀▀ █████  ░▀▓▓▓
                          ▀███      ▀
                          █████▓
                           █▀▓██
                           █▄ ▀██
                           ▓█ █▓
                                ▓██
                               ▄██▀""")
    time.sleep(.2)
    cls()
    print("""
_   _____________________  _____  __  ___  ______  _____   __   ____
| | / /  _/ ___/_  __/ __ \/ _ \ \/ / / _ \/ __ \ \/ / _ | / /  / __/
| |/ // // /__  / / / /_/ / , _/\  / / , _/ /_/ /\  / __ |/ /__/ _/ 
|___/___/\___/ /_/  \____/_/|_| /_/ /_/|_|\____/ /_/_/ |_/____/___/ 


                                ▄▓
                            ▄▄ ▓██▓
                       ▓█▓████████▄▄
                        ▀▓▓▄███████▓█▄▄
                          ██▓▀████▓ ▓▓▓
                         ▀▀▓  ███▓▓█▓
                            ▄▓█████
                            ███████░
                           ▄███████
                            ███▀▓▓▀
                            ██▓▄█▀
                            ▀▓███▓
                              ██▀▀▓▓▄
                             ▄█  ▓▓▓▓▓
                             █▀
                             ▓▓""")

    time.sleep(.2)
    cls()
    print("""
_   _____________________  _____  __  ___  ______  _____   __   ____
| | / /  _/ ___/_  __/ __ \/ _ \ \/ / / _ \/ __ \ \/ / _ | / /  / __/
| |/ // // /__  / / / /_/ / , _/\  / / , _/ /_/ /\  / __ |/ /__/ _/ 
|___/___/\___/ /_/  \____/_/|_| /_/ /_/|_|\____/ /_/_/ |_/____/___/ 


                                ▄▄
                                ███
                         ▓  ▄▄▓▄▓██▄▄
                       ░▄█▄█▓▓████████▄
                        ▀▓  ▀█████▀▀▓█▄
                               ▓███▀   ▓▓
                               ▄████▄ █▓
                              ▓████████
                              ▓█████▓▀▀
                              ▀████▓
                               ███▀
                               ▓█▓▓▄
                               █████
                                ██▀▀█
                                ██  ██
                                █▓ ▓▓
                               ▓█▓
                              ▀▓▀""")
    time.sleep(.2)
    cls()
    print("""
_   _____________________  _____  __  ___  ______  _____   __   ____
| | / /  _/ ___/_  __/ __ \/ _ \ \/ / / _ \/ __ \ \/ / _ | / /  / __/
| |/ // // /__  / / / /_/ / , _/\  / / , _/ /_/ /\  / __ |/ /__/ _/ 
|___/___/\___/ /_/  \____/_/|_| /_/ /_/|_|\____/ /_/_/ |_/____/___/ 


                               ▄██▓  ▄▄
                             ▄▄▄▄▓██████
                         ▄▓▄▄▓▓▓▓▓███▓██
                       ▓▓         ▀▄███▄
                                    ▀████▓▄
                                   ▄████▓▓█
                                   ███▀████
                                  ▓██▓ ███▀
                                  ███  ███
                                  ▓▓█  █▓
                                   █▀  ██▓
                                       ▀██░
                                        ▓█
                                         █
                                         █▄
                                        ▓█""")
    time.sleep(.2)
    cls()
    print("""
_   _____________________  _____  __  ___  ______  _____   __   ____
| | / /  _/ ___/_  __/ __ \/ _ \ \/ / / _ \/ __ \ \/ / _ | / /  / __/
| |/ // // /__  / / / /_/ / , _/\  / / , _/ /_/ /\  / __ |/ /__/ _/ 
|___/___/\___/ /_/  \____/_/|_| /_/ /_/|_|\____/ /_/_/ |_/____/___/ 


                         ▄
                        ▓██▄
                        ▀██▄
                         ▀█▓▄▄▄
                         █████▀▓▓▄
                        ██████   ▓▓
                         ▀████▄  █▀
                          ████████
                        ▄████████▓
                        ███▓▀████
                        ██▓  ████
                       ▓██    ███
                       ▀██▄   ████▓▄
                        ██▀   ▀▀▀▀▀▓█▓
                         █         ▄█
                         ██        ▀▀
                       ▄▓█▀""")
    time.sleep(.2)
    cls()
    print("""
_   _____________________  _____  __  ___  ______  _____   __   ____
| | / /  _/ ___/_  __/ __ \/ _ \ \/ / / _ \/ __ \ \/ / _ | / /  / __/
| |/ // // /__  / / / /_/ / , _/\  / / , _/ /_/ /\  / __ |/ /__/ _/ 
|___/___/\___/ /_/  \____/_/|_| /_/ /_/|_|\____/ /_/_/ |_/____/___/ 


                              ▄▄                        
                             ███▄         ▄▄█            
                             ▀███▓███▓▓▄▓▓▓▀▀▀           
                             ▄█▓█████  ▀                 
                       ▀█▄▄▄▄▓▀ ▀████                 
                        ▀▀▀▀▀    ▀███▄                 
                                 ▓█████                 
                                ███████            
                                ██████▀          
                                ██████                  
                                ██▓██                   
                              ▓██▀▓███▓▄                
                              █▀▀   ▀▓██▓▄                 
                             █▄        ▀▀▓▓▄             
                            ▀▓           ▄██▓              
                                         ▀▀▀                  """)
    time.sleep(.2)
    cls()
    print("""
_   _____________________  _____  __  ___  ______  _____   __   ____
| | / /  _/ ___/_  __/ __ \/ _ \ \/ / / _ \/ __ \ \/ / _ | / /  / __/
| |/ // // /__  / / / /_/ / , _/\  / / , _/ /_/ /\  / __ |/ /__/ _/ 
|___/___/\___/ /_/  \____/_/|_| /_/ /_/|_|\____/ /_/_/ |_/____/___/ 


                             ▄▓▓
                             ████▄▄
                            ▄▓██████
                       ▄▓▄▓▓███▓████
                       ▀▓██▓▀▀ █████
                         ▀      ████▄▄
                              ▄▓██████
                            ▄█████▓████
                           ▄███▓▀  ████
                           ██▓▀    ▓██▀
                           ▀██▄     ██▄
                            ███     ▓██
                            ▀██      ▀█
                              █      ▄█
                             ▄██
                           ░█▓▓▓""")
    time.sleep(.2)
    cls()
    print("""
_   _____________________  _____  __  ___  ______  _____   __   ____
| | / /  _/ ___/_  __/ __ \/ _ \ \/ / / _ \/ __ \ \/ / _ | / /  / __/
| |/ // // /__  / / / /_/ / , _/\  / / , _/ /_/ /\  / __ |/ /__/ _/ 
|___/___/\___/ /_/  \____/_/|_| /_/ /_/|_|\____/ /_/_/ |_/____/___/ 


                           ▄
                         ▓█▓  ▄ ▄▄
                        ▓█  ███▀▀▓▄▄
                       ▓█▄▄▄▄▄███▄▄▓▓█▓▄
                       ▀▀▀▀▀▓███████▀▀▓▓
                              █████▓
                              ▓████
                               ▓█████
                              ▄██████
                              ██████▓
                              █████▓
                              █████
                              ▀████
                               ▀████
                                ▀█▀▓█▄
                                ▄█   ██▄
                                █   ▓█▀▀
                               ▄██  ▀
                                ▀""")
    time.sleep(.2)
    cls()
    print("""
_   _____________________  _____  __  ___  ______  _____   __   ____
| | / /  _/ ___/_  __/ __ \/ _ \ \/ / / _ \/ __ \ \/ / _ | / /  / __/
| |/ // // /__  / / / /_/ / , _/\  / / , _/ /_/ /\  / __ |/ /__/ _/ 
|___/___/\___/ /_/  \____/_/|_| /_/ /_/|_|\____/ /_/_/ |_/____/___/ 


                             ▓█▓
                          ▄▄▄███
                         ▓███████▓
                         █████████
                         █▓████▓▀█▓
                         ████████▓█
                        ▄███████▓ █▓
                       ▄█▓█████▓  ██▄
                       ▀▀ █████  ░▀▓▓▓
                          ▀███      ▀
                          █████▓
                           █▀▓██
                           █▄ ▀██
                           ▓█ █▓
                                ▓██
                               ▄██▀""")
    time.sleep(.2)
    cls()
    print("""
_   _____________________  _____  __  ___  ______  _____   __   ____
| | / /  _/ ___/_  __/ __ \/ _ \ \/ / / _ \/ __ \ \/ / _ | / /  / __/
| |/ // // /__  / / / /_/ / , _/\  / / , _/ /_/ /\  / __ |/ /__/ _/ 
|___/___/\___/ /_/  \____/_/|_| /_/ /_/|_|\____/ /_/_/ |_/____/___/ 


                                ▄▓
                            ▄▄ ▓██▓
                       ▓█▓████████▄▄
                        ▀▓▓▄███████▓█▄▄
                          ██▓▀████▓ ▓▓▓
                         ▀▀▓  ███▓▓█▓
                            ▄▓█████
                            ███████░
                           ▄███████
                            ███▀▓▓▀
                            ██▓▄█▀
                            ▀▓███▓
                              ██▀▀▓▓▄
                             ▄█  ▓▓▓▓▓
                             █▀
                             ▓▓""")

    time.sleep(.2)
    cls()
    print("""
_   _____________________  _____  __  ___  ______  _____   __   ____
| | / /  _/ ___/_  __/ __ \/ _ \ \/ / / _ \/ __ \ \/ / _ | / /  / __/
| |/ // // /__  / / / /_/ / , _/\  / / , _/ /_/ /\  / __ |/ /__/ _/ 
|___/___/\___/ /_/  \____/_/|_| /_/ /_/|_|\____/ /_/_/ |_/____/___/ 


                                ▄▄
                                ███
                         ▓  ▄▄▓▄▓██▄▄
                       ░▄█▄█▓▓████████▄
                        ▀▓  ▀█████▀▀▓█▄
                               ▓███▀   ▓▓
                               ▄████▄ █▓
                              ▓████████
                              ▓█████▓▀▀
                              ▀████▓
                               ███▀
                               ▓█▓▓▄
                               █████
                                ██▀▀█
                                ██  ██
                                █▓ ▓▓
                               ▓█▓
                              ▀▓▀""")
    time.sleep(.2)
    cls()
    print("""
_   _____________________  _____  __  ___  ______  _____   __   ____
| | / /  _/ ___/_  __/ __ \/ _ \ \/ / / _ \/ __ \ \/ / _ | / /  / __/
| |/ // // /__  / / / /_/ / , _/\  / / , _/ /_/ /\  / __ |/ /__/ _/ 
|___/___/\___/ /_/  \____/_/|_| /_/ /_/|_|\____/ /_/_/ |_/____/___/ 


                               ▄██▓  ▄▄
                             ▄▄▄▄▓██████
                         ▄▓▄▄▓▓▓▓▓███▓██
                       ▓▓          ▀▄███▄
                                    ▀████▓▄
                                   ▄████▓▓█
                                   ███▀████
                                  ▓██▓ ███▀
                                  ███  ███
                                  ▓▓█  █▓
                                   █▀  ██▓
                                       ▀██░
                                        ▓█
                                         █
                                         █▄
                                        ▓█""")
    time.sleep(.2)
    cls()
    print("""
_   _____________________  _____  __  ___  ______  _____   __   ____
| | / /  _/ ___/_  __/ __ \/ _ \ \/ / / _ \/ __ \ \/ / _ | / /  / __/
| |/ // // /__  / / / /_/ / , _/\  / / , _/ /_/ /\  / __ |/ /__/ _/ 
|___/___/\___/ /_/  \____/_/|_| /_/ /_/|_|\____/ /_/_/ |_/____/___/ 


                         ▄
                        ▓██▄
                        ▀██▄
                         ▀█▓▄▄▄
                         █████▀▓▓▄
                        ██████   ▓▓
                         ▀████▄  █▀
                          ████████
                        ▄████████▓
                        ███▓▀████
                        ██▓  ████
                       ▓██    ███
                       ▀██▄   ████▓▄
                        ██▀   ▀▀▀▀▀▓█▓
                         █         ▄█
                         ██        ▀▀
                       ▄▓█▀""")
    time.sleep(.2)
    cls()
    print("""
_   _____________________  _____  __  ___  ______  _____   __   ____
| | / /  _/ ___/_  __/ __ \/ _ \ \/ / / _ \/ __ \ \/ / _ | / /  / __/
| |/ // // /__  / / / /_/ / , _/\  / / , _/ /_/ /\  / __ |/ /__/ _/ 
|___/___/\___/ /_/  \____/_/|_| /_/ /_/|_|\____/ /_/_/ |_/____/___/ 


                              ▄▄                        
                             ███▄          ▄▄█           
                             ▀███▓███▓▓▄▓▓▓▀▀▀           
                             ▄█▓█████  ▀                 
                       ▀█▄▄▄▄▓▀ ▀████                 
                        ▀▀▀▀▀    ▀███▄                 
                                 ▓█████                 
                                ███████            
                                ██████▀          
                                ██████                  
                                ██▓██                   
                              ▓██▀▓███▓▄                
                              █▀▀   ▀▓██▓▄                 
                             █▄        ▀▀▓▓▄             
                            ▀▓           ▄██▓              
                                       ▀▀▀                    """)
    time.sleep(.2)
    cls()
    print("""
_   _____________________  _____  __  ___  ______  _____   __   ____
| | / /  _/ ___/_  __/ __ \/ _ \ \/ / / _ \/ __ \ \/ / _ | / /  / __/
| |/ // // /__  / / / /_/ / , _/\  / / , _/ /_/ /\  / __ |/ /__/ _/ 
|___/___/\___/ /_/  \____/_/|_| /_/ /_/|_|\____/ /_/_/ |_/____/___/ 


                             ▄▓▓
                             ████▄▄
                            ▄▓██████
                       ▄▓▄▓▓███▓████
                       ▀▓██▓▀▀ █████
                         ▀    ████▄▄
                              ▄▓██████
                            ▄█████▓████
                           ▄███▓▀  ████
                           ██▓▀    ▓██▀
                           ▀██▄     ██▄
                            ███     ▓██
                            ▀██      ▀█
                              █      ▄█
                             ▄██
                           ░█▓▓▓""")
    time.sleep(.2)
    cls()
    print("""
_   _____________________  _____  __  ___  ______  _____   __   ____
| | / /  _/ ___/_  __/ __ \/ _ \ \/ / / _ \/ __ \ \/ / _ | / /  / __/
| |/ // // /__  / / / /_/ / , _/\  / / , _/ /_/ /\  / __ |/ /__/ _/ 
|___/___/\___/ /_/  \____/_/|_| /_/ /_/|_|\____/ /_/_/ |_/____/___/ 


                           ▄
                         ▓█▓   ▄ ▄▄
                        ▓█   ███▀▀▓▄▄
                       ▓█▄▄▄▄▄███▄▄▓▓█▓▄
                       ▀▀▀▀▀▓███████▀▀▓▓
                              █████▓
                              ▓████
                               ▓█████
                              ▄██████
                              ██████▓
                              █████▓
                              █████
                              ▀████
                               ▀████
                                ▀█▀▓█▄
                                ▄█   ██▄
                                █   ▓█▀▀
                               ▄██  ▀
                                ▀""")
    time.sleep(.2)
    cls()
    print("""
_   _____________________  _____  __  ___  ______  _____   __   ____
| | / /  _/ ___/_  __/ __ \/ _ \ \/ / / _ \/ __ \ \/ / _ | / /  / __/
| |/ // // /__  / / / /_/ / , _/\  / / , _/ /_/ /\  / __ |/ /__/ _/ 
|___/___/\___/ /_/  \____/_/|_| /_/ /_/|_|\____/ /_/_/ |_/____/___/ 



                          ▓█▓
                          ███▄
                        ▄██████
                       ▓█▀▓████
                       ▀▀▀████▓
                           ███
                         ▄▓████▄
                        ░██████▀
                        ██████▀
                       ██████
                       ██▓██
                       ▀▀██▓▄
                         ▀▓██▄
                         ▄▄███
                        ░▓▀▀▓█
                            ▄██
                           ▓▓▓▀""")
    time.sleep(.5)
    input("\n\nPress ENTER to return to menu")
    cls()

def poker():
    """This function starts POKER, it is called from the main menu"""
    cls()

    # Defining the names of the hand ranks, to be used when announcing winner, and their hand ranking
    rank_dict = {
        1: "Royal Flush",
        2: "Straight Flush",
        3: "Four of a Kind",
        4: "Full House",
        5: "Flush",
        6: "Straight",
        7: "Three of a kind",
        8: "Two Pair",
        9: "Pair",
        10: "High Card",
    }

    # Defining bot names
    bot_name = ["Daniel J. D'arby", 'Tyler Blevins', 'Felix Kjellberg', 'William Smith', 'X Æ A-Xii Musk']

    def poker_round(reset):
        """This function calls for one round (game) of poker, where there is one cycle of betting

        Keyword Arguments:
        reset -- determines whether to reset the player balance to $1500 or not. If not, game proceeds with current
        balance."""
        cls()
        # Declaring variables and global variables (global variables are used in so they can be used even if you return
        # to the main menu and play another game)
        global high_score, p_player_money, bot_money, bot_count, bot_num, out
        poker_restricted_values = []
        bot_bet = [0, 0, 0, 0, 0]
        player_bet = 0
        bot_status = ["", "", "", "", ""]
        bot_hand = [[], [], [], [], []]
        show_rank = False
        finish_game = 0
        tie = False

        # Determines whether to reset the game (it can be continued even if the play quits to main menu)
        if reset:
            # Resets values
            p_player_money = 1500
            bot_money = [1500, 1500, 1500, 1500, 1500]
            bot_count = []
            bot_num = 0
            out = []
            # Prompt for number of opponents to face against
            bot_num = input("Choose the number of bots to play against (1 - 5): ")
            while bot_num not in ['1', '2', '3', '4', '5']:
                cls()
                print("Please enter a whole number from 1 to 5.\n")
                time.sleep(.2)
                bot_num = input("Choose the number of bots to play against (1 - 5): ")
            bot_num = int(bot_num)
            # Creates a list from integer
            for i in range(bot_num):
                bot_count.append(i)

        # Removes bots that are 'out' from the game
        if out:  # If there are variables in out; out is not empty
            for i in out:
                if i in bot_count:
                    bot_count.remove(i)
            bot_num = len(bot_count)

        def generate_card():
            """This function generates a unique card from deck of cards. A deck of cards includes 52 cards as it doesn't
            have jokers, and the cards range from 1 - 13 with 4 suits"""
            rand_card_num = random.randint(2, 14)
            suit = suit_dict[random.randint(0, 3)]
            while f"{rand_card_num}{suit}" in poker_restricted_values:
                rand_card_num = random.randint(2, 14)
                suit = suit_dict[random.randint(0, 3)]
            poker_restricted_values.append(f"{rand_card_num}{suit}")
            return f"{rand_card_num}{suit}"

        # Returns hand, but only numbers as str (used for print)
        def number(x):
            """This function returns the player hand as a list with the suit removed (values are strings)
            e.g ['4♠', '5♠', '6♠', '7♠', '8♠'] -> ['4', '5', '6', '7', '8']

            Keyword arguments:
            x -- the hand of the player"""
            return [x[0][:-1], x[1][:-1], x[2][:-1], x[3][:-1], x[4][:-1]]

        def int_number(x):
            """This function returns the player hand as a list with the suit removed (values are integers)
            e.g ['4♠', '5♠', '6♠', '7♠', '8♠'] -> [4, 5, 6, 7, 8]

            Keyword arguments:
            x -- the hand of the player"""
            return [int(x[0][:-1]), int(x[1][:-1]), int(x[2][:-1]), int(x[3][:-1]), int(x[4][:-1])]

        def ranking(x):
            """This is a function that determines the rank value of a player hand. The lower the value that is returned,
            the better the player hand is

            Keyword arguments:
            x -- the hand of the player"""
            if player_hand == x and player_status == "fold" and not show_rank:
                return 11  # If the main player has folded; show_hand used to ignore so rank can be showed in results
            consecutive_list = []
            hand = x.copy()
            hand_number = int_number(hand)
            hand_suit = [hand[0][-1:], hand[1][-1:], hand[2][-1:], hand[3][-1:], hand[4][-1:]]
            for j in range(5):
                consecutive_list.append((min(hand_number)) + j)  # Creates Consecutive List
            if sorted(hand_number) == [10, 11, 12, 13, 14] and hand_suit.count(hand_suit[0]) == 5:
                return 1  # Royal Flush
            elif sorted(hand_number) == consecutive_list and hand_suit.count(hand_suit[0]) == 5:
                return 2  # Straight Flush
            elif sorted(hand_number) == [2, 3, 4, 5, 14] and hand_suit.count(hand_suit[0]) == 5:
                return 2  # Straight Flush (lower end)
            elif hand_number.count(hand_number[0]) == 4 or hand_number.count(hand_number[1]) == 4:
                return 3  # Four of a Kind
            elif hand_number.count(sorted(hand_number)[0]) == 3 and hand_number.count(sorted(hand_number)[4]) == 2:
                return 4  # Full House
            elif hand_number.count(sorted(hand_number)[0]) == 2 and hand_number.count(sorted(hand_number)[4]) == 3:
                return 4  # Full House
            elif hand_suit.count(hand_suit[0]) == 5:
                return 5  # Flush
            elif sorted(hand_number) == consecutive_list or sorted(hand_number) == [2, 3, 4, 5, 14]:
                return 6  # Consecutive 2,3,4,5,14 as A is also 1
            elif hand_number.count(sorted(hand_number)[2]) == 3:
                return 7  # Three of a Kind
            elif hand_number.count(sorted(hand_number)[1]) == 2 and hand_number.count(sorted(hand_number)[3]) == 2:
                return 8  # Two Pairs
            elif (hand_number.count(sorted(hand_number)[1]) == 2 or hand_number.count(sorted(hand_number)[2]) == 2
                  or hand_number.count(sorted(hand_number)[3]) == 2):
                return 9  # Pair
            else:
                return 10  # High Card

        def find_repeating(hand):
            """This function finds the highest repeating value in a hand. It prioritises how many times the card repeats
            and then prioritises how high the card is,
            e.g. in [4, 4, 5, 5, 6] function will return 5

            Keyword arguments:
            hand -- player hand"""
            if not hand:
                return 0
            hand_number = int_number(hand)
            number_top = []
            for y in sorted(hand_number):
                if hand_number.count(y) > 1 and y not in number_top:
                    number_top.append(y)
            if not number_top:  # if list is empty
                return 0
            for j in reversed(sorted(number_top)):
                if hand_number.count(j) > 2:
                    return j
                elif hand_number.count(j) == 2 and j is number_top[0]:
                    return max(number_top)

        # x percent chance to return as True
        def percent_chance(x):
            """A random chance for something to happen. If 60 is entered as the arguement, there is a 60% chance that
            the function will return as True.

            Keyword arguments:
            x -- percent chance for function to return as True"""
            if random.randint(1, 100) <= x:
                return True
            else:
                return False

        def raise_or_call(bet_num, chance, limit, j):
            """This function determines what the bot should do when betting in regards to its current conditions

            Keyword arguments:
            bet_num -- the value of the current bet
            chance -- the percentage chance for the bot to raise
            limit -- the maximum value the bot can raise to
            j - the index value of the bot"""
            if bet_num > bot_money[j]:
                return bet_num, bot_money[j], "low"  # If insufficient credits, so bets max
            elif percent_chance(chance) and bet_num < limit and bet_num + 75 <= bot_money[j]:
                bet_num += random.randint(1, 3) * 25
                return bet_num, bet_num, "raise"
            else:
                return bet_num, bet_num, "call"

        def fold(rank, bet1, bet2, chance, j):
            """Determines whether a bet should fold or not depending on its current conditions

            Keyword arguments
            rank - the rank value of the bot (how good the bot hand is)
            bet1 - if the bet exceeds this value and the player hand is better, there is a 40% chance to fold
            bet2 - if the bet exceeds this value and player hand is the same rank, there is a {chance} chance to fold
            chance -- the chance to fold if player hand is the same
            j -- the index value of the bot hand"""
            if ranking(player_hand) in [1, 2, 3, 4] and bet > bet1 and percent_chance(50):
                return True
            elif ranking(player_hand) < rank and bet > bet1 and percent_chance(40):
                return True
            elif ranking(player_hand) == rank and bet > bet2 and percent_chance(chance):
                return True
            elif find_repeating(player_hand) > find_repeating(bot_hand[j]) and percent_chance(40):
                return True
            else:
                return False

        def bet_status(j):
            """Displays the bot action for that current round

            Keyword arguments
            j -- the index of the bot"""
            if bot_status[j] == "fold":
                return f"{bot_name[j]} folds with a bet of ${bot_bet[j]}"
            elif bot_status[j] == "low":
                return f"{bot_name[j]} has an insufficient balance, so calls for ${bot_bet[j]}"
            elif bot_status[j] == "call":
                return f"{bot_name[j]} calls for ${bot_bet[j]}"
            elif bot_status[j] == "raise":
                return f"{bot_name[j]} raises bet to ${bot_bet[j]}"

        # The bots make decisions on whether the call, raise or fold due to game and hand conditions
        def bet_round(bet_num, limit_1, limit_2, limit_3, limit_4, last_chance):
            """The bots make decisions on whether to call, raise or fold due to current conditions. This function makes
            the decisions on what to do for that round for each bot, and changes the bet etc accordingly.

            Keyword arguments:
            bet_num -- the current bet value
            limit_1 -- the maximum value the bot will raise to if it has a ranking of 1, 2 or 3
            limit_2 -- the maximum value the bot will raise to if it has a ranking of 4, 5, 6 or 7
            limit_3 -- the maximum value the bot will raise to if it has a ranking of 8
            limit_4 -- the maximum value the bot will raise to if it has a ranking of 9
            last_chance -- the chance for a bot to bet if it has the worst hand (High Card)"""
            cls()
            for j in bot_count:
                time.sleep(.05)
                if bot_status[j] != "fold":
                    skip_round = False
                    if bot_num == 1:
                        if player_status == "fold":
                            bet_num, bot_bet[j], bot_status[j] = raise_or_call(bet_num, 0, 0, j)
                        elif ranking(bot_hand[j]) < 9:
                            bet_num, bot_bet[j], bot_status[j] = raise_or_call(bet_num, 33, 0, j)
                        elif ranking(bot_hand[j]) == 9 or percent_chance(50):
                            bet_num, bot_bet[j], bot_status[j] = raise_or_call(bet_num, 0, 0, j)
                        else:
                            bot_status[j] = "fold"
                        skip_round = True
                    elif player_status == "fold":
                        if bot_status.count("fold") == bot_num - 1 and bot_status.count("fold") != 0:
                            skip_round = True
                            bet_num, bot_bet[j], bot_status[j] = raise_or_call(bet_num, 0, 0, j)
                    if not skip_round:
                        if ranking(bot_hand[j]) in [1, 2, 3]:
                            if player_status == "call" and 400 < bet_num <= bot_money[j]:
                                bet_num = bot_money[j]
                                bot_bet[j] = bet_num
                                bot_status[j] = "call"
                            else:
                                bet_num, bot_bet[j], bot_status[j] = raise_or_call(bet_num, 50, limit_1 * 100, j)

                        elif ranking(bot_hand[j]) in [4, 5, 6, 7]:
                            bet_num, bot_bet[j], bot_status[j] = raise_or_call(bet_num, 75, limit_2 * 100, j)

                        elif ranking(bot_hand[j]) == 8:
                            if fold(8, 400, 500, 20, j):
                                bot_status[j] = "fold"
                            else:
                                bet_num, bot_bet[j], bot_status[j] = raise_or_call(bet_num, 60, limit_3 * 100, j)

                        elif ranking(bot_hand[j]) == 9:
                            if fold(9, 300, 350, 30, j):
                                bot_status[j] = "fold"
                            else:
                                bet_num, bot_bet[j], bot_status[j] = raise_or_call(bet_num, 45, limit_4 * 100, j)

                        elif ranking(bot_hand[j]) == 10:
                            if percent_chance(last_chance):
                                if bet_num >= random.randint(100, 250):
                                    bot_status[j] = "fold"
                                else:
                                    bet_num, bot_bet[j], bot_status[j] = raise_or_call(bet_num, 0, 0, j)
                            else:
                                bot_status[j] = "fold"
                    print(bet_status(j))
            time.sleep(.2)
            print(f"\n\nCurrent Bet: ${bet_num}")
            time.sleep(.2)
            print(f"Pot size: ${sum(bot_bet) + player_bet}\n")
            return bet_num, bot_bet, bot_status

        # Prompt for player bet
        def player_call(bet_num):
            """Prompts for the player to bet, and adjusts the bet values accordingly

            Keyword arguments
            bet_num -- the current value of the bet"""
            if raise_amount >= 4 or bet_num >= p_player_money:
                bet_prompt = input("\nWould you like to 'call' or 'fold'?: ").lower().strip()
                while bet_prompt not in ["call", "fold"]:
                    cls()
                    print(f"Current Bet: ${bet_num}")
                    print(f"Pot size: ${sum(bot_bet) + player_bet}\n")
                    print("Please enter either 'call' or 'fold'\n")
                    time.sleep(.2)
                    bet_prompt = input("Would you like to 'call' or 'fold'?: ").lower().strip()
            else:
                bet_prompt = input("Would you like to 'call', 'raise' or 'fold'?: ").lower().strip()
                while bet_prompt not in ["call", "raise", "fold"]:
                    cls()
                    print(f"Current Bet: ${bet_num}")
                    print(f"Pot size: ${sum(bot_bet) + player_bet}\n")
                    time.sleep(.2)
                    print("Please enter either 'call', 'raise' or 'fold'\n")
                    time.sleep(.2)
                    bet_prompt = input("Would you like to 'call', 'raise' or 'fold'?: ").lower().strip()
            if bet_prompt == 'fold':
                return bet_num, bet_num, "fold"
            elif bet_prompt == "call" and bet_num >= p_player_money:
                cls()
                print(f"You have less cash than the current bet, automatically called for ${p_player_money} ")
                input("Press ENTER to continue")
                return bet_num, p_player_money, "low"
            elif bet_prompt == 'raise':
                cls()
                while True:
                    try:
                        bet_num = float(input(f"How much do you want to raise? {bet + 1} - {p_player_money}: "))
                        while bet_num <= bet or bet_num > p_player_money or bet_num != int(bet_num):
                            cls()
                            print(f"Please bet an integer value within {bet + 1} - {p_player_money}\n")
                            time.sleep(.2)
                            bet_num = float(input(f"How much do you want to raise? {bet + 1} - {p_player_money}: "))
                        bet_int_num = int(bet_num)
                        return bet_int_num, bet_int_num, "raise"
                    except ValueError:
                        cls()
                        print(f"Please enter an integer value within {bet_num + 1} - {p_player_money}\n")
                        time.sleep(.2)
            else:
                return bet_num, bet_num, "call"

        def rearrange_hand(x):
            """Swaps out 1 - 3 different random cards for other ones if a bot has the worst hand (High Card)

            x - the hand of the bot"""
            bot_hand_list = []
            for _ in range(3):
                new_hand = x
                restricted_swaps_bot = []
                for _ in range(random.randint(1, 3)):
                    swap_index = random.randint(0, 4)
                    while swap_index in restricted_swaps_bot:
                        swap_index = random.randint(0, 4)
                    new_hand[swap_index] = generate_card()
                    restricted_swaps_bot.append(swap_index)
                bot_hand_list.append(new_hand)
            return bot_hand_list[random.randint(0, 2)]

        def high_hand(x, y):
            """Determines which player / bot has the highest card (determines winner if rank is same)

            Keyword Arguments
            x -- the hand of the first player
            y -- the hand of the second player"""
            x_number = int_number(x)
            y_number = int_number(y)
            x_number = (sorted(x_number))
            y_number = (sorted(y_number))
            for j in reversed(range(5)):
                if x_number[j] > y_number[j]:
                    return x
                elif y_number[j] > x_number[j]:
                    return y
            return x

        cls()

        print("Your opponent(s):")
        # Generates cards for opponents and player
        for i in bot_count:
            bot_hand[i] = [generate_card(), generate_card(), generate_card(), generate_card(), generate_card()]
            print(f"{bot_name[i]}")
        player_hand = [generate_card(), generate_card(), generate_card(), generate_card(), generate_card()]

        time.sleep(.2)
        print(f"\nYour Hand: {hand_display(player_hand)}")
        print(f"Your Balance: ${p_player_money}\n")
        time.sleep(.2)
        input("Press ENTER to continue")

        # Sets Ante
        bet = 50
        for i in bot_count:
            bot_bet[i] = 50
        player_bet = 50

        # First round of betting
        cls()
        print(f"Your Hand: {hand_display(player_hand)}\n")
        time.sleep(.2)
        fold_prompt = input("Would you like to 'bet' or 'fold'?: ").lower().strip()
        while fold_prompt not in ["bet", "fold"]:
            cls()
            print(f"Your Hand: {hand_display(player_hand)}\n")
            time.sleep(.2)
            print("Please enter 'bet' or 'fold'\n")
            time.sleep(.2)
            fold_prompt = input("Would you like to 'bet' or 'fold'?: ").lower().strip()
        if fold_prompt == 'bet':
            cls()
            while True:
                try:
                    bet_amount = float(input(f"How much do you want to bet? {bet} - {p_player_money}: "))
                    while bet_amount < bet or bet_amount > p_player_money or bet_amount != int(bet_amount):
                        cls()
                        print(f"Please enter an integer value within {bet} - {p_player_money}\n")
                        time.sleep(.2)
                        bet_amount = float(input(f"How much do you want to bet? {bet} - {p_player_money}: "))
                    bet = int(bet_amount)
                    player_status = "call"
                    break
                except ValueError:
                    cls()
                    print(f"Please enter an integer within {bet} - {p_player_money}\n")
                    time.sleep(.2)
        else:
            player_status = "fold"
        player_bet = bet
        bot_status[bot_count[0]] = "raise"
        raise_amount = 0
        while "raise" in bot_status or player_status == "raise":
            if player_status == "raise":
                raise_amount += 1
            bet, bot_bet, bot_status = bet_round(bet, 2, 2, 2, 2, 65)
            if bot_status.count("fold") == bot_num:
                player_status = "call"
                break
            elif player_status != "fold":
                bet, player_bet, player_status = player_call(bet)

        cls()
        print("Round Concluded")
        time.sleep(1)

        # Swap 1-3 randomized cards if bot has bad hand
        for i in bot_count:
            if ranking(bot_hand[i]) == 10 and bot_status[i] != "fold" and len(poker_restricted_values) < 48:
                bot_hand[i] = rearrange_hand(bot_hand[i])

        # Player replacing cards
        if player_status != "fold" and bot_status.count("fold") != bot_num:
            cls()
            print(f"Your Hand: {hand_display(player_hand)}\n")
            time.sleep(.2)
            exchange = input("Do you want to replace any cards (Y/N): ").strip().upper()
            while exchange not in ["Y", "N"]:
                cls()
                print("Please enter either 'Y' or 'N'\n")
                time.sleep(.2)
                print(f"Your Hand: {hand_display(player_hand)}\n")
                time.sleep(.2)
                exchange = input("Do you want to replace any cards (Y/N): ").strip().upper()
            if exchange == "Y":
                cls()
                print(f"Your Hand: {hand_display(player_hand)}\n")
                number_swaps = input("How many cards to replace? (1 - 3): ")
                while number_swaps not in ['1', '2', '3']:
                    cls()
                    print(f"Your Hand: {hand_display(player_hand)}\n")
                    time.sleep(.2)
                    print("Please enter an integer from 1 - 3\n")
                    time.sleep(.2)
                    number_swaps = input("How many cards to replace? (1 - 3): ")
                restricted_swaps = []
                for i in range(int(number_swaps)):
                    cls()
                    print(f"Your Hand: {hand_display(player_hand)}\nPositions: 1  2  3  4  5\n")
                    swap = input(f"Swap {i + 1} - Choose a position 1 - 5: ")
                    while swap not in ['1', '2', '3', '4', '5'] or swap in restricted_swaps:
                        cls()
                        if swap not in ['1', '2', '3', '4', '5']:
                            print("Please enter an integer from 1 - 5")
                        elif swap in restricted_swaps:
                            print("You cannot choose this position again")
                        time.sleep(.2)
                        print(f"\nYour Hand: {hand_display(player_hand)}\nPositions: 1  2  3  4  5\n")
                        time.sleep(.2)
                        swap = input(f"Swap {i + 1} - Choose a position 1 - 5: ")
                    swap = int(swap)
                    player_hand[swap - 1] = "? "
                    restricted_swaps.append(str(swap))
                    cls()
                    print(f"Your Hand: {hand_display(player_hand)}\nPositions: 1  2  3  4  5\n")
                for i in range(5):
                    if player_hand[i] == "? ":
                        player_hand[i] = generate_card()
                time.sleep(.5)
                print("Your new hand is:", f"{hand_display(player_hand)}")
                time.sleep(.2)
                input("\nPress ENTER to continue")
            else:
                cls()
                print("No cards exchanged")
                time.sleep(1)

        # Second round of betting
        if bot_status.count("fold") != bot_num:
            cls()
            print("Second round of betting begins\n")
            time.sleep(.2)
            if player_status != "fold":
                print(f"\nYour Hand: {hand_display(player_hand)}\n\n\nCurrent Bet: ${bet}")
                print(f"Pot size: ${sum(bot_bet) + player_bet}\n")
                bet, player_bet, player_status = player_call(bet)
            bot_status[bot_count[0]] = "raise"
            raise_amount = 0
            while "raise" in bot_status or player_status == "raise":
                if player_status == "raise":
                    raise_amount += 1
                bet, bot_bet, bot_status = bet_round(bet, 99, 5, 3.75, 3, 50)
                if bot_status.count("fold") == bot_num:
                    player_status = "call"
                    break
                elif player_status != "fold":
                    bet, player_bet, player_status = player_call(bet)

        # Determines who has the best hand
        if bot_status.count("fold") == bot_num and player_status == "fold":
            tie = True
        elif bot_status.count("fold") != bot_num:
            call_index = []
            for i in bot_count:
                if bot_status[i] != "fold":
                    call_index.append(i)
            index_rank = []
            sorted_index = []
            for i in call_index:
                index_rank.append(ranking(bot_hand[i]))
            sorted_rank = (sorted(index_rank))
            for i in range(len(call_index)):
                ind = index_rank.index(sorted_rank[i])
                index_rank[ind] = "?"
                sorted_index.append(call_index[ind])
            # Determines bot with best hand
            if bot_num != 1:
                if bot_status.count("fold") == bot_num - 1:
                    win_bot = sorted_index[0]
                elif bot_status.count("fold") < bot_num:
                    current_best = bot_hand[sorted_index[0]]
                    if sorted_rank[0] == sorted_rank[1]:
                        for i in range(len(sorted_index)):
                            if sorted_rank[i] == sorted_rank[0]:
                                high = high_hand(current_best, bot_hand[sorted_index[i]])
                                current_best = high
                                win_bot = bot_hand.index(high)
                    else:
                        win_bot = sorted_index[0]
                    final_hands = []
                    for i in call_index:
                        final_hands.append(number(bot_hand[i]))
                    if final_hands.count(number(current_best)) > 1:
                        tie = True
            else:
                win_bot = bot_count[0]
            win = bot_hand[win_bot]
            # Compares bot hand with player hand, see who has the best hand
            if player_status != "fold":
                if ranking(player_hand) < sorted_rank[0]:
                    win = player_hand
                elif ranking(player_hand) == max(sorted_rank):
                    win = high_hand(player_hand, win)
        else:
            win = player_hand

        cls()

        # Displays final results: the hands, the ranking of each opponent, and the overall winner
        print("Round Results:\n")
        show_rank = True
        print(f"You had a {rank_dict[ranking(player_hand)]}: {hand_display(player_hand)}")
        time.sleep(.2)
        for i in bot_count:
            print(f"{bot_name[i]} had a {rank_dict[ranking(bot_hand[i])]}: {hand_display(bot_hand[i])}")
            time.sleep(.2)
        time.sleep(1)
        if tie:
            if bot_status.count("fold") == bot_num and player_status == "fold":
                "Everyone Folded, so match is void."
            else:
                print(f"\n\nYou tied with {bot_name[win_bot]}, who also had a {rank_dict[ranking(bot_hand[win_bot])]}")
        elif win == player_hand:
            if player_status != "low":
                for i in bot_count:
                    p_player_money += bot_bet[i]
                    bot_money[i] -= bot_bet[i]
            elif player_status == "low":
                for i in bot_count:
                    if bot_bet[i] < bot_bet[win_bot]:
                        p_player_money += bot_bet[i]
                        bot_money[i] -= bot_bet[i]
                    else:
                        p_player_money += player_bet
                        bot_money[i] -= player_bet
            print(f"\n\nYou win with a {rank_dict[ranking(win)]}: {hand_display(player_hand)}")
        elif win == bot_hand[win_bot]:
            if bot_status[win_bot] != "low":
                bot_money[win_bot] += player_bet
                p_player_money -= player_bet
                for i in bot_count:
                    if i != win_bot:
                        bot_money[win_bot] += bot_bet[i]
                        bot_money[i] -= bot_bet[i]
            elif bot_status[win_bot] == "low":
                if player_bet < bot_bet[win_bot]:
                    bot_money[win_bot] += player_bet
                    p_player_money -= player_bet
                else:
                    bot_money[win_bot] += bot_bet[win_bot]
                    p_player_money -= bot_bet[win_bot]
                for i in bot_count:
                    if i != win_bot:
                        if bot_bet[i] < bot_bet[win_bot]:
                            bot_money[win_bot] += bot_bet[i]
                            bot_money[i] -= bot_bet[i]
                        else:
                            bot_money[win_bot] += bot_bet[win_bot]
                            bot_money[i] -= bot_bet[win_bot]
            print(f"\n\n{bot_name[win_bot]} wins with a {rank_dict[ranking(win)]}: {hand_display(bot_hand[win_bot])}")
        # If winner wins with high card, prints their highest card
        if ranking(win) == 10:
            time.sleep(.2)
            print("High Card:", max(int_number(win)))
            time.sleep(.2)
        print(f"\n\nYour Balance: ${p_player_money}\n")
        time.sleep(.5)

        # Calculates who still has enough money to carry on
        for i in bot_count:
            if bot_money[i] < 50:
                time.sleep(.5)
                out.append(i)
                print(f"{bot_name[i]} has withdrawn due to having insufficient credts.")

        # Sets high score (if current score is higher than best)
        if p_player_money > high_score["Poker"]:
            high_score["Poker"] = p_player_money
            with open('score (delete file to reset score).dat', 'wb') as export_file:  # exports file
                pickle.dump(high_score, export_file)

        # See if player has beat all opponents and if they want to continue playing
        for i in bot_count:
            if bot_money[i] < 50:
                finish_game += 1
        if finish_game == bot_num:  # Victory Message
            input("\nPress ENTER to continue")
            cls()
            print("CONGRATULATIONS!")
            time.sleep(1)
            print("\nYou beat everyone and dominated the Casino!")
            time.sleep(2)
            victory_graphic = input("\nDo you want to view the victory animation? (Y/N): ").strip().upper()
            while victory_graphic not in ["Y", "N"]:
                cls()
                print("Please enter either 'Y' or 'N'")
                victory_graphic = input("\n\nDo you want to view the victory animation? (Y/N): ").strip().upper()
            if victory_graphic == "Y":
                cls()
                time.sleep(.5)
                win_animation()
                poker_menu()
            elif victory_graphic == "N":
                poker_menu()
        if p_player_money >= 50:
            repeat = input("\nDo you want to continue the game? (Y/N): ").strip().upper()
            while repeat not in ["Y", "N"]:
                print("\nPlease enter either 'Y' or 'N'")
                repeat = input("\nDo you want to continue the game? (Y/N): ").strip().upper()
            if repeat == "Y":
                poker_round(False)
            elif repeat == "N":
                poker_menu()
        else:
            print("\nYou have insufficient credits , returning back to main menu")
            time.sleep(2)
            poker_menu()

    def poker_menu():
        """Function that displays the poker menu"""
        cls()
        time.sleep(.05)
        print("""
_ _ _ ____ _    ____ ____ _  _ ____    ___ ____    ___  ____ _  _ ____ ____   /
| | | |___ |    |    |  | |\/| |___     |  |  |    |__] |  | |_/  |___ |__/  /
|_|_| |___ |___ |___ |__| |  | |___     |  |__|    |    |__| | \_ |___ |  \ .  """)
        time.sleep(.1)
        menu_selection = input(f"""
High Score: ${high_score["Poker"]}
Balance: ${p_player_money}\n
    Press '1' to START NEW GAME
    Press '2' to CONTINUE GAME
    Press '3' to view INSTRUCTIONS
    Press '4' to view HAND RANKING
    Press '5' to return to CASINO MENU\n\nEnter Here: """)
        if menu_selection not in ['1', '2', '3', '4', '5', '02496']:
            print("\nPlease enter either '1', '2', '3', '4' or '5'\n")
            time.sleep(1)
            poker_menu()
        if menu_selection == '1':  # New Game
            poker_round(True)
            time.sleep(.5)
        elif menu_selection == '2':  # Continue Game
            if p_player_money < 50:
                print("\nYou have insufficient credits, must create a new game.")
                time.sleep(1)
                poker_menu()
            if not bot_count:
                print("\nYou cannot continue an non-existing game.")
                time.sleep(1)
                poker_menu()
            time.sleep(.5)
            poker_round(False)
        elif menu_selection == '3':  # Instructions
            cls()
            if input("View Instructions\n\nEnter 'YES' to confirm: ").strip().upper() == "YES":
                cls()
                print("You will have a starting balance of $1500")
                time.sleep(1.5)
                print("\nYour goal is to get as much money as you can")
                time.sleep(1.5)
                print("\nWhen you bet, you have three options : Call, Fold or Raise")
                time.sleep(2)
                print("To 'Call' is to match the current bet on the table.")
                time.sleep(2)
                print(
                    "To 'Fold' is to give up for that round, and so you lose the money you bet for that round.")
                time.sleep(2)
                print("To 'Raise' is to increase the current bet. You can only do this 4 times per round")
                time.sleep(2)
                print("""\nThe match CANNOT continue until everyone has matched the bet, so if the current bet 
is too high and you feel like it is too much of a risk to proceed, you have to fold.""")
                time.sleep(5)
                print("""\nIf the bet is higher than your balance, you can still bet, but if you win,
you will only get the amount that you bet.""")
                time.sleep(4)
                print("""\nThere will be two betting rounds in total, with one interval in-between where you
can choose to replace three different cards of your choosing.""")
                time.sleep(5)
                print(
                    "\nThe player with the best hand (See 'HAND RANKING') wins the bet cash for that round.")
                time.sleep(2)
                print("\nHave Fun! (If you manage to win the game, there will be a surprise waiting for you...)")
                time.sleep(2)
                input("\nPress ENTER to return to menu")
            poker_menu()
        elif menu_selection == '4':  # Hand ranking
            cls()
            if input("View Hand Rankings\n\nEnter 'YES' to confirm: ").strip().upper() == "YES":
                cls()
                print("""1. Royal flush
A, K, Q, J, 10, all the same suit.
A♦ K♦ Q♦ J♦ 10♦""")
                time.sleep(1.5)
                print("""\n2. Straight flush
Five cards in a row, all in the same suit.
8♣ 7♣ 6♣ 5♣ 4♣""")
                time.sleep(1.5)
                print("""\n3. Four of a kind
All four cards of the same rank.
J♥ J♦ J♠ J♣ 7♦""")
                time.sleep(1.5)
                print("""\n4. Full house
Three of a kind with a pair.
10♥ 10♦ 10♠ 9♣ 9♦""")
                time.sleep(1.5)
                print("""\n5. Flush
Any five cards of the same suit, but not consecutive.
4♠ J♠ 8♠ 2♠ 9♠""")
                time.sleep(1.5)
                print("""\n6. Straight
Five consecutive cards, but not of the same suit.
9♣ 8♦ 7♠ 6♦ 5♥""")
                time.sleep(1.5)
                print("""\n7. Three of a kind
Three cards of the same rank.
7♣ 7♦ 7♠ K♣ 3♦""")
                time.sleep(1.5)
                print("""\n8. Two pair
Two different pairs.
4♠ 4♣ 3♣ 3♦ Q♣""")
                time.sleep(1.5)
                print("""\n9. Pair
Two cards of the same rank.
A♥ A♦ 8 4♣ 7♥""")
                time.sleep(1.5)
                print("""\n10. High Card
When you haven't made any of the hands above, the highest card plays.
In the example below, the jack plays as the highest card.
3♦ J♣ 8♠ 4♥ 2♠""")
                time.sleep(2)
                input("\nPress ENTER to return to menu")
            poker_menu()
        elif menu_selection == '02496':  # Easter egg: Victory animation
            win_animation()
            main_menu()
        else:  # Return to menu
            main_menu()

    poker_menu()


def blackjack():
    """This function starts BLACKJACK, it is called from the main menu"""
    cls()

    def blackjack_round(reset):
        """This function commences one round/ game of blackjack

        Keyword arguments
        reset -- decides whether to reset the player balances (to $1500) or not"""
        cls()
        global high_score, bj_player_money

        # Decides if game resets or not
        if reset:
            bj_player_money = 1500
            bj_restricted_values = []

        win = False
        tie = False
        split_bool = False
        surrender = False
        dd_count = 0

        # Generates cards to a GLOBAL variable (unlike poker, blackjack requires keeping track of the cards played, so
        # in theory, the same deck will used even if you accidentally quit)
        def generate_card():
            """Generates a random card from a deck of 52 cards (value of 1 - 13 with 4 suits) This also keeps track of
            the cards and tells the player when a new deck is being added"""
            global bj_restricted_values
            rand_num = random.randint(2, 14)
            suit = suit_dict[random.randint(0, 3)]
            while f"{rand_num}{suit}" in bj_restricted_values:
                if len(bj_restricted_values) == 52:
                    cls()
                    print("INTERMISSION: ran out of cards, a new deck will now be added")
                    input("\n\nPress ENTER if you understand")
                    bj_restricted_values = []
                    cls()
                rand_num = random.randint(2, 14)
                suit = suit_dict[random.randint(0, 3)]
            bj_restricted_values.append(f"{rand_num}{suit}")
            return f"{rand_num}{suit}"

        def number(x):
            """List of card values (converts A to a value of 11 and J, K, Q to 10)

            Keyword arguments
            x -- the player hand"""
            new_list = []
            for i in x:
                if int(i[:-1]) == 14:
                    new_list.append(11)
                elif int(i[:-1]) >= 10:
                    new_list.append(10)
                else:
                    new_list.append(int(i[:-1]))
            return new_list

        def check_for_a(x):
            """If the hand value exceeds 21, value of Ace (11) turns into 1

            Keyword arguments
            x -- the player hand"""
            if sum(number(x)) > 21:
                if 11 in number(x):
                    x[number(x).index(11)] = '1' + x[number(x).index(11)][-1]
            return x

        def result(player, dealer):
            """Determines whether the player wins the game, or ties
            The first bool determines whether the player ties or not
            The second bool determines whether the player wins or not
            The tie will always be calculated first by the program.

            Keyword arguments
            player -- the player hand
            dealer -- the dealer hand"""
            if not (sum(number(player)) > 21 and sum(number(dealer)) < 21):
                if sum(number(player)) == sum(number(dealer)) or (
                        sum(number(player)) > 21 and sum(number(dealer)) > 21):
                    return True, False
                elif sum(number(player)) > sum(number(dealer)) or sum(number(dealer)) > 21:
                    return False, True
            return False, False

        def hand_message(x, dd):
            """This determines what to display and the appropriate values to use depending on the player hand and how
            many times the player has previously doubled down.

            x -- the player hand
            dd -- whether the player has already doubled down this round or not"""
            if split_bool and x == split_1:
                print(f"\nHand #1: {hand_display(x)} \nHand Value: {sum(number(x))}\n")
            elif split_bool and x == split_2:
                print(f"\nHand #2: {hand_display(x)} \nHand Value: {sum(number(x))}\n")
            else:
                print(f"\nYour Hand: {hand_display(x)} \nHand Value: {sum(number(x))}\n")
            if split_bool and dd_count == 0 and not dd:
                print(f"Doubling down increases bet from ${bet} ---> ${int(bet * 1.5)}")
            elif split_bool and dd_count == 1 and not dd:
                print(f"Doubling down increases bet from ${bet} ---> ${int(bet * (2 / 1.5))}")
            elif not split_bool and not dd:
                print(f"Doubling down increases bet from ${bet} ---> ${int(bet * 2)}")

        def action(bet_num, x, dd, dc):
            """Player prompt on the actions that they want to undergo

            Keyword arguments
            bet_num -- the value of the bet
            x -- the player hand
            dd -- if the player has doubled down for that hand already or not
            dc -- the number of times the player has doubled down for the whole game (if split)"""
            cls()
            print("Dealer hand: '?'", dealer_hand[1])
            hand_message(x, dd)
            act = input("Would you like to 'hit', 'stand', double down ('dd') or 'surrender': ").lower().strip()
            while act not in ["hit", "stand"]:
                cls()
                if act == "dd":
                    condition = [(bj_player_money / 1.5), (bj_player_money / (4 / 3))]
                    if dd:
                        print("You can only double down once per hand\n")
                    elif split_bool and dc in [0, 1] and condition[dc] < bet_num:
                        print(f"Your total balance is too low to double your bet.\n")
                    elif not split_bool and bj_player_money / 2 < bet_num:
                        print(f"Your total balance is too low to double your bet.\n")
                    else:
                        break
                if act == "surrender" and (len(x)) > 2:
                    print("Cannot Surrender, hand has more than two cards.\n")
                else:
                    break
                print("Please enter either 'hit', 'stand', 'dd' or 'surrender'\n\nDealer hand: '?'", dealer_hand[1])
                hand_message(x, dd)
                act = input("Would you like to 'hit', 'stand', double down ('dd') or 'surrender': ").lower().strip()
            cls()
            if act == "hit":
                x.append(generate_card())
            elif act == "dd":
                x.append(generate_card())
                print("Bet for current hand doubled")
                time.sleep(.2)
                if split_bool:
                    dc += 1
                    if dc == 1:
                        bet_num = int(bet_num * 1.5)
                    elif dc == 2:
                        bet_num = int(bet_num * 2 / 1.5)
                else:
                    bet_num *= 2
                time.sleep(.2)
                print(f"\nNew total bet: ${bet_num}")
                dd = True
            if act in ["hit", "dd"]:
                if (hand_display(x).strip()[-3:-1]) == '10':
                    print(hand_display(x).strip()[-3:], "added to hand")
                else:
                    print(hand_display(x).strip()[-2:], "added to hand")
                input("\nPress ENTER to continue")
            check_for_a(x)
            return bet_num, x, act, dd, dc

        def status(x):
            """The status of the current hand

            Keyword arguments
            x -- the hand"""
            if sum(number(x)) == 21:
                return "bj"
            if sum(number(x)) > 21:
                return "bust"
            return "proceed"

        def prompt_hand(bet_num, x, surrender_bool, dc):
            """Prompts for player action

            Keyword arguments
            bet_num -- the current bet value
            x -- player hand
            surrender_bool -- whether the player has surrendered or not
            dc -- total amount of times player has doubled down"""
            act = ""
            dd = False
            while status(x) == "proceed" and act != "stand" and not surrender_bool:
                bet_num, x, act, dd, dc = action(bet_num, x, dd, dc)
                cls()
                if act == "surrender":
                    surrender_bool = True
                if status(x) == "bust":
                    print("Hand Value:", sum(number(x)))
                    time.sleep(.2)
                    print("\nHand Bust")
                    time.sleep(1)
            return bet_num, x, surrender_bool, dc

        # Decides bet
        while True:
            try:
                print(f"Balance: ${bj_player_money}")
                time.sleep(.2)
                bet = float(input(f"\nHow much do you want to bet? 1 - {bj_player_money}: "))
                while bet < 1 or bet > bj_player_money or bet != int(bet):
                    cls()
                    print("Please enter an integer value within the allocated range")
                    time.sleep(.2)
                    bet = float(input(f"\nHow much do you want to bet? 1 - {bj_player_money}: "))
                bet = int(bet)
                break
            except ValueError:
                cls()
                print("Please enter an integer value within the allocated range\n")

        # Generates cards
        player_hand = check_for_a([generate_card(), generate_card()])
        dealer_hand = check_for_a([generate_card(), generate_card()])

        # Sees if player has identical values and if so, prompts for split
        if status(player_hand) == "proceed" and sum(number(dealer_hand)) != 21:
            if player_hand[0][:-1] == player_hand[1][:-1] and bj_player_money / 2 >= bet:
                cls()
                print("Dealer hand: '?'", dealer_hand[1])
                print("\nYour hand:", hand_display(player_hand), "\nHand Value:", sum(number(player_hand)))
                print(f"\nSplitting your hand increases bet from ${bet} ---> ${int(bet * 2)}")
                split = input("\nWould you like to split your hand (and double bet) 'Y'/'N': ").strip().upper()
                while split not in ["Y", "N"]:
                    cls()
                    print("Must enter 'Y' or 'N'")
                    print("\nDealer hand: '?'", dealer_hand[1])
                    print("\nYour hand:", hand_display(player_hand), "\nHand Value:", sum(number(player_hand)))
                    print(f"\nSplitting your hand increases bet from ${bet} ---> ${int(bet * 2)}")
                    split = input("Would you like to split your hand (and double bet) 'Y'/'N': ").strip().upper()
                if split == "Y":
                    cls()
                    split_bool = True
                    split_1 = [player_hand[0], generate_card()]
                    split_2 = [player_hand[1], generate_card()]
                    print("Hand Split")
                    bet *= 2
                    time.sleep(.2)
                    print(f"\nNew total bet: ${bet}")
                    time.sleep(.2)
                    input("\nPress ENTER to continue")

            # Player action
            if sum(number(dealer_hand)) != 21:
                if split_bool:
                    bet, split_1, surrender, dd_count = prompt_hand(bet, split_1, surrender, dd_count)
                    bet, split_2, surrender, dd_count = prompt_hand(bet, split_2, surrender, dd_count)
                elif not split_bool:
                    bet, player_hand, surrender, dd_count = prompt_hand(bet, player_hand, surrender, dd_count)

                # Draw cards for dealer until hand value >= 17
                if sum(number(dealer_hand)) < 17:
                    while sum(number(dealer_hand)) < 17:
                        dealer_hand.append(generate_card())

                # Determines winner, or tie
                if split_bool:
                    tie, win = result(split_1, dealer_hand)
                    if not win and tie:
                        tie, win = result(split_2, dealer_hand)
                        tie = True
                    elif not win:
                        tie, win = result(split_2, dealer_hand)
                else:
                    tie, win = result(player_hand, dealer_hand)

        # Displays winner and appropriate message for contextual conditions.
        # Also adds/subtracts money
        if not surrender:
            cls()
            if status(dealer_hand) == "bj" and status(player_hand) != "bj" and not split_bool:
                print("Dealer Blackjack!\n")
                time.sleep(2)
            elif split_bool and status(dealer_hand) == 'bj' and status(split_1) != 'bj' and status(split_2) != "bj":
                print("Dealer Blackjack!\n")
                time.sleep(2)
            elif status(player_hand) == 'bj':
                print("Blackjack!\n")
                time.sleep(2)
            else:
                input("Press ENTER to view results")
        cls()
        if split_bool:
            print("Hand #1:", hand_display(split_1), "\nHand Value:", sum(number(split_1)))
            print("\nHand #2:", hand_display(split_2), "\nHand Value:", sum(number(split_2)))
        else:
            print("Your hand:", hand_display(player_hand), "\nYour Hand Value:", sum(number(player_hand)))
        time.sleep(.5)
        print("\nDealer hand:", hand_display(dealer_hand), "\nDealer Hand Value:", sum(number(dealer_hand)))
        time.sleep(.5)
        if surrender:
            print("\n\nLoss due to forfeit")
            bj_player_money -= int(bet / 2)
        elif split_bool and (status(split_1) == "bj" or status(split_2) == "bj"):
            if status(dealer_hand) == "bj":
                print("\n\nYou tied as the dealer also got a blackjack")
            else:
                print("\n\nCongrats, you win!")
                if dd_count == 1:
                    bj_player_money += int(bet / 1.5)
                else:
                    bj_player_money += int(bet / 2)
        elif status(player_hand) == "bj":
            if status(dealer_hand) == "bj":
                print("\n\nYou tied as the Dealer also got blackjack")
            else:
                print("\n\nCongrats, you win!")
                bj_player_money += int(bet * 1.5)
        elif tie:
            print("\n\nYou tied with the dealer")
        elif win and status(dealer_hand) == "bust":
            print("\n\nCongrats, you win! - Dealer Bust")
            bj_player_money += bet
        elif win:
            print("\n\nCongrats, you win!")
            if split_bool and dd_count == 1:
                bj_player_money += int(bet / 1.5)
            elif split_bool:
                bj_player_money += int(bet / 2)
            else:
                bj_player_money += bet
        elif status(dealer_hand) == "bj":
            print("\n\nYou lose. Better luck next time!")
            bj_player_money -= int(bet * 1.5)
        else:
            print("\n\nYou lose. Better luck next time!")
            bj_player_money -= bet

        if bj_player_money <= 0:
            bj_player_money = 0

        # Displays New Balance
        time.sleep(1)
        print(f"\nNew Balance: {bj_player_money}")
        time.sleep(.5)

        # Sets High Score
        if bj_player_money > high_score["Blackjack"]:
            high_score["Blackjack"] = bj_player_money
            with open('score (delete file to reset score).dat', 'wb') as export_file:
                pickle.dump(high_score, export_file)

        # Prompt for if the player wants to continue the game or not
        if bj_player_money > 0:
            repeat = input("\nDo you want to continue the game? (Y/N): ").strip().upper()
            while repeat not in ["Y", "N"]:
                cls()
                print("Please enter either 'Y' or 'N'")
                repeat = input("\nDo you want to continue the game? (Y/N): ").strip().upper()
            if repeat == "Y":
                blackjack_round(False)
            elif repeat == "N":
                blackjack_menu()
        else:
            print("\nYou have insufficient credits , returning back to main menu")
            time.sleep(3)
            blackjack_menu()

    def blackjack_menu():
        """Function that displays the menu for blackjack"""
        cls()
        time.sleep(.05)
        print("""
_ _ _ ____ _    ____ ____ _  _ ____    ___ ____    ___  _    ____ ____ _  _  _ ____ ____ _  _   /
| | | |___ |    |    |  | |\/| |___     |  |  |    |__] |    |__| |    |_/   | |__| |    |_/   /
|_|_| |___ |___ |___ |__| |  | |___     |  |__|    |__] |___ |  | |___ | \_ _| |  | |___ | \_ .""")
        time.sleep(.1)
        menu_selection = input(f"""
High Score: ${high_score["Blackjack"]}
Balance: ${bj_player_money}\n
    Press '1' to START NEW GAME
    Press '2' to CONTINUE GAME
    Press '3' to view INSTRUCTIONS
    Press '4' to return to CASINO MENU\n\nEnter Here: """)
        while menu_selection not in ['1', '2', '3', '4', '02496']:
            print("\nPlease enter either '1', '2', '3' or '4'\n")
            time.sleep(1)
            blackjack_menu()
        if menu_selection == '1':  # New Game
            blackjack_round(True)
        elif menu_selection == '2':  # Continue game
            if bj_player_money == 0:
                print("\nYou have insufficient credits, must create a new game.")
                time.sleep(1)
                blackjack_menu()
            if high_score["Blackjack"] == 0:
                print("\nYou cannot continue an non-existing game.")
                time.sleep(1)
                blackjack_menu()
            time.sleep(1)
            blackjack_round(False)
        elif menu_selection == '3':  # Instructions
            cls()
            if input("View Instructions\n\nEnter 'YES' to confirm: ").strip().upper() == "YES":
                cls()
                print("You will have a starting balance of $1500")
                time.sleep(1.5)
                print("\nYour goal is to get as much money as you can")
                time.sleep(2)
                print("\nThe aim of the game is to get the highest combination that does not exceed 21")
                time.sleep(2.5)
                print("\nIf you exceed 21, you automatically lose, and go 'bust'.")
                time.sleep(2)
                print("\nHaving a combination that adds to 21 exactly is called a blackjack.")
                time.sleep(2)
                print("\nIf you get a blackjack, you win 1.5 times the bet.")
                time.sleep(2)
                print("\nIf the dealer gets a blackjack, you lose 1.5 times the bet")
                time.sleep(3)
                print("\nYou will begin the game with two cards, and so will the dealer")
                time.sleep(1.5)
                print("\nOne of the dealer's cards will be revealed.")
                time.sleep(1.5)
                print("""\nWhen you finish with your hand, the dealer will add cards until they have a total 
value that is greater than 17. (It is possible for the dealer to go bust as well)""")
                time.sleep(1)
                input("\nPress ENTER to continue")
                cls()
                print("All cards are worth their displayed values, with the exception of J, Q, K and A:")
                time.sleep(2)
                print("\nPicture cards (J, Q, K) are worth 10 each.")
                time.sleep(1.5)
                print("\nAces (A) are worth 11, but if your hand exceeds 21, it will convert into 1.")
                time.sleep(2.5)
                print("\nThis will be signalled by the display changing from 'A' to '1'.")
                time.sleep(1.5)
                input("\nPress ENTER to continue")
                cls()
                print("You will be given four choices which regarding what to do with your hand.")
                time.sleep(1.5)
                print("\nTo 'hit' is to add a new card to your current hand.")
                time.sleep(2)
                print("\nTo 'stand' is to leave your hand as it is, and continue.")
                time.sleep(2)
                print("""\nTo double down or 'dd' is to double the bet for your current hand, and hit 
(gain a new card). This can only be applied once per hand""")
                time.sleep(4)
                print("""\nTo 'surrender' is to forfeit the round, and in doing so, you only have to give up
half of your current bet. This is a good option when you have a bad hand or if you think the dealer has a blackjack.""")
                time.sleep(5.5)
                print("\nSurrendering is only applicable when you have 2 cards.")
                time.sleep(2)
                print("""\n\nIf you have two cards of the same value, you will be prompted to 'split' your hand. 
This means that you will essentially have two hands, and you play as separate player for each.""")
                time.sleep(6.5)
                print("""\nThe cards will be split into two new hands, one of the original cards will be in each
new hand, in each, and each hand will gain a new card.""")
                time.sleep(3)
                print("\nSplits can only occur once per round and cannot happen to dealers.")
                time.sleep(2)
                print("\nWhen you split, each hand will have its own bet, so essentially you double your bet.")
                time.sleep(2)
                print("\nIf you double down when split, only the bet of that hand will double, not total bet.")
                time.sleep(2)
                print("""\nHowever, since this is two different hands, when you win, you will only win the 
amount bet by the hand with the highest bet, and not your total bet.""")
                time.sleep(4)
                print("e.g. if total bet is $200 ($100 for each hand), you only gain $100 upon winning.")
                time.sleep(2)
                input("\nPress ENTER to return to menu")
            blackjack_menu()
        elif menu_selection == '02496':  # Easter egg
            win_animation()
            blackjack_menu()
        else:  # Return to menu
            main_menu()

    blackjack_menu()


def main_menu():
    """Function that displays the main menu, which can then lead into the respective games poker and blackjack"""
    cls()
    time.sleep(.05)
    print("""
_ _ _ ____ _    ____ ____ _  _ ____    ___ ____    ___ _  _ ____    ____ ____ ____ _ _  _ ____
| | | |___ |    |    |  | |\/| |___     |  |  |     |  |__| |___    |    |__| [__  | |\ | |  |
|_|_| |___ |___ |___ |__| |  | |___     |  |__|     |  |  | |___    |___ |  | ___] | | \| |__| """)
    time.sleep(.1)
    menu_selection = input(f"""
Poker High Score: ${high_score["Poker"]}
Blackjack High Score: ${high_score["Blackjack"]}\n
    Press '1' to launch POKER
    Press '2' to launch BLACKJACK
    Press '3' to EXIT\n\nEnter Here: """)
    while menu_selection not in ['1', '2', '3', '02496']:
        print("\nPlease enter either '1' or '2' or '3'\n")
        time.sleep(1)
        main_menu()
    if menu_selection == '1':
        poker()
    elif menu_selection == '2':
        blackjack()
    elif menu_selection == '3':
        cls()
        time.sleep(.1)
        print("Thanks for your visit at the CASINO")
        time.sleep(.5)
        print("\nWe hope you had a pleasurable experience and will return next time!")
        time.sleep(1.5)
        exit()
    elif menu_selection == '02496':
        win_animation()
        main_menu()


main_menu()
