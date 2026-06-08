import time

RESET = "\033[0m"
RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
BLUE = "\033[34m"
MAGENTA = "\033[35m"
CYAN = "\033[36m"
WHITE = "\033[37m"

def display_clock():
    while True:
        current_time = time.strftime("%I:%M:%S %p")
        
        current_date = time.strftime("%d-%m-%Y")
        
        current_day = time.strftime("%A")
        
        print(f"{CYAN}Time: {GREEN}{current_time}    {YELLOW}Date: {MAGENTA}{current_date}    {RED}Day: {BLUE}{current_day}{RESET}", end="\r")
        
        time.sleep(1)

display_clock()
