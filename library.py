from utilities import splitCommand
import engine

library = False
commandsToInject = [["bios load library", engine.biosLoadLibrary], ["bios exit", engine.biosExit], ["bios test lev", engine.biosLoadLibrary]]


# Classes
class trieNode:
    def __init__(self):
        self.children = {}
        self.isCommand = False
        self.engineReference = None

class commandLibrary:
    def __init__(self):
        self.root = trieNode()
    
    def addCommand(self, command):
        currentNode = self.root
        for word in splitCommand(command[0]):
            if word not in currentNode.children:
                currentNode.children[word] = trieNode()
            currentNode = currentNode.children[word]
        currentNode.isCommand = True
        currentNode.engineReference = command[1]
    
    def tryFindCommandPath(self, input):
        currentNode = self.root
        for word in splitCommand(input):
            if word not in currentNode.children:
                return None
            currentNode = currentNode.children[word]
        if currentNode.isCommand:
            return currentNode.engineReference
        else:
            return None

# Setup
def loadLibrary():
    global library
    library = commandLibrary()
    for command in commandsToInject:
        library.addCommand(command)