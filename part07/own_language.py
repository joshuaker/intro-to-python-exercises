# Write your solution here

from string import ascii_uppercase
import operator
variables = {}
for letter in ascii_uppercase:
    variables[letter] = 0 #letter is string

def loop(program):
       for command in program:
            if command == 'END':
                break
            elif 'MOV' in command:
                parts = command.split(' ')
                if parts[2] not in ascii_uppercase:
                    variables[parts[1]] = int(parts[2])
                else:
                    variables[parts[1]] = variables[parts[2]]
            
            elif 'PRINT' in command:
                parts = command.split(' ')
                _print_.append(variables[parts[1]])
            
            elif 'ADD' in command:
                parts = command.split(' ')
                if parts[2] not in ascii_uppercase:
                    variables[parts[1]] += int(parts[2])
                else:
                    variables[parts[1]] += variables[parts[2]]

            elif 'SUB' in command:
                parts = command.split(' ')
                if parts[2] not in ascii_uppercase:
                    variables[parts[1]] -= int(parts[2])
                else:
                    variables[parts[1]] -= variables[parts[2]]

            elif 'MUL' in command:
                parts = command.split(' ')
                if parts[2] not in ascii_uppercase:
                    variables[parts[1]] *= int(parts[2])
                else:
                    variables[parts[1]] *= variables[parts[2]]

def run(program):
    _print_ = []

    for command in program:
        if command == 'END':
            break
        elif 'MOV' in command:
            parts = command.split(' ')
            if parts[2] not in ascii_uppercase:
                variables[parts[1]] = int(parts[2])
            else:
                variables[parts[1]] = variables[parts[2]]
        
        elif 'PRINT' in command:
            parts = command.split(' ')
            _print_.append(variables[parts[1]])
        
        elif 'ADD' in command:
            parts = command.split(' ')
            if parts[2] not in ascii_uppercase:
                variables[parts[1]] += int(parts[2])
            else:
                variables[parts[1]] += variables[parts[2]]

        elif 'SUB' in command:
            parts = command.split(' ')
            if parts[2] not in ascii_uppercase:
                variables[parts[1]] -= int(parts[2])
            else:
                variables[parts[1]] -= variables[parts[2]]

        elif 'MUL' in command:
            parts = command.split(' ')
            if parts[2] not in ascii_uppercase:
                variables[parts[1]] *= int(parts[2])
            else:
                variables[parts[1]] *= variables[parts[2]]

        elif 'JUMP' in command:
            parts = command.split(' ')
            index = parts.index('JUMP')
            location = parts[index+1] #location: string

            location_index = 0
            for item in program: #need to do this because the JUMP quit needs to be able to find 'quit: '
                if location in item:
                    location_index = program.index(item)
            command_index = program.index(command)
            #do i need to modify code depending on if JUMP is to earlier or after?

            loop(program[location_index:command_index+1])
            # small run def run_without_loop(program:)
            #but how does this smaller loop modify the variables dictionary
            # are you allowed to create a global variables?

            #can you create a slice of the original program, and then run that slice again and again?
        
        elif 'IF' in command:
            # split into parts; if first part is not TRUE, continue without processing second part
            parts = command.split('JUMP')
            commands = [] #list leading/trailing without whitespaces
            for item in parts:
                item = item.strip(' ')
            commands.append(item) #full list is [IF ..., location:str]

            operator_dictionary = {'==': operator.eq, '!=': operator.ne, '<': operator.lt, '<=': operator.le, '>': operator.gt, '>=': operator.ge}

            conditional_flag = False
            
            isolate = commands[0][3:] #slice off the first three index 'IF '
            for key, oper in operator_dictionary:
                if key in commands[0]:
                    isolate_variables = isolate.split(key)
                    operator_variables = []
                    for item in isolate_variables:
                        operator_variables.append(item.strip(' '))
                    #isolate_variables = ['A ', ' B']
                    #how to account for possibility that value is int

                    for i in range(len(operator_variables)):
                        if operator_variables[i] not in ascii_uppercase:
                            operator_variables[i] = int(operator_variables)
                    
                    conditional_flag = oper(operator_variables[0], operator_variables[1]) #returns a boolean

            if conditional_flag:
                pass


        else: #for location
            pass
            #does this actually need anythign?

    return _print_

['MOV A 1', 'MOV B 10', 'begin:', 'IF A >= B JUMP quit', 'PRINT A', 'PRINT B', 'ADD A 1', 'SUB B 1', 'JUMP begin', 'quit:', 'END']



notes = '''
currently working on making sure JUMP works as intended:
trying to make it so that a simplified JUMP without a conditional can work
testing this by jumping over a print command

not sure if I need to modify things depending on whether the jump location comes before or after the command
previously, when location is before jump, i had sliced it so that the function ignored what came after the jump(index)
i thought this would allow the loop to finish, and then continue on to the commands after the jump was called

but if the location is after, you want it to just [location:] all the way to the end, allowing the program to break early'''