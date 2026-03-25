# Basic Imports
import library
import utilities

# Header in the CLI
print("=================================")
print("|█████  █████  █████  █      ███|")
print("|█         █   █      █       █ |")
print("|█████    █    █      █       █ |")
print("|█       █     █      █       █ =========")
print("|█████  █████  █████  █████  ███  v1.0.0|")
print("=========================================")
print("")
print("A useful template created by Caleb van Bruchem for a base CLI. Feel free to modify and add to it, and if you feel stuck, check out the repo on https://github.com/CuriousTree456/EZCLI\n")

def bios(command):
    if command == "bios exit":
        exit()
    elif command == "bios load library":
        if library.library == False:
            print("\033[31mLibrary not loaded!\033[0m")
            print("\033[5mLoading...\033[0m", end="\r")
            library.loadLibrary()
            print("Loading...   ")
            if library.library.tryFindCommandPath("bios exit"):
                print("\033[32mLoading successful!\033[0m\n")
            else:
                print("\033[31mFatal error: commands not initialise properly.\033[0m\n")
        else:
            print("\033[32mLibrary already loaded!\033[0m\n")
    else:
        print("\033[31mSpecified bios command does not exist.\033[0m")
        if (library.library == False):
            print("\033[33mWarning: the library is not loaded!\033[0m")
            print("\033[33mThe command you are trying to access is probably in the library.\033[0m")
            print("\033[33mTo load the library, enter this command:\033[0m")
            print("\033[1mbios load library\033[0m\n")
        else:
            print("\n")

def setup():
    print("\033[5mLoading...\033[0m", end="\r")
    library.loadLibrary()
    print("Loading...       ")
    if library.library.tryFindCommandPath("bios exit"):
        print("\033[32mLoading successful!\033[0m\n")

setup()
while True:
    userInput = input("> ").lower()

    if library.library == False:
        bios(userInput)
    else:
        words = utilities.splitCommand(userInput)
        if not words:
            print("\033[31mCommand does not contain readable words.\033[0m\n")
            continue
        else:
            engineFunction = library.library.tryFindCommandPath(userInput)
            if engineFunction != None:
                engineFunction()
            else:
                print("\033[31mCommand does not exist or is not registered with the engine.\033[0m")
                print("\033[31mHere are some similar commands that you may have meant:\033[0m\n")
                possibleCommands = utilities.findTop3Commands(userInput)
                print(f"\033[33m{possibleCommands[0]}\033[0m")
                print(f"\033[33m{possibleCommands[1]}\033[0m")
                print(f"\033[33m{possibleCommands[2]}\033[0m\n")