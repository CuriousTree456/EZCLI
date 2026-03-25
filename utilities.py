import re
import library
import Levenshtein

def splitCommand(baseCommand):
    words = re.split(r'[\s_,]+', baseCommand)
    return [w for w in words if w]

def findTop3Commands(input):
    commands = []
    for cmd in library.commandsToInject:
        commands.append(cmd[0])
    orderedCommands = sorted(commands, key=lambda command: Levenshtein.distance(command, input))
    return [orderedCommands[0], orderedCommands[1], orderedCommands[2]]