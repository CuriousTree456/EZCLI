import library
import utilities

def biosExit():
    exit()

def biosLoadLibrary():
    if library.library == False:
        print("\033[31mLibrary not compiled!\033[0m")
        print("\033[5mLoading...\033[0m", end="\r")
        library.loadLibrary()
        print("Loading...")
        if library.library.tryFindCommandPath("bios exit"):
            print("\033[32mLoading successful!\033[0m\n")
        else:
            print("\033[31mFatal error: commands not initialise properly.\033[0m\n")
    else:
        print("\033[32mLibrary already loaded!\033[0m\n")