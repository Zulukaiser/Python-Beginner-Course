name_list= []
validCommands = ['a', 'r', 'u', 'v', 'x']
object_list = []
validExercises = ['squat', 'bench_press', 'deadlift']

def showText():
    print('Welcome to Powerliifting Data Collector!\n')
    print('Available actions:\na - Add Lifter\nr - Remove Lifter\nu - Update Lifter\nv - View Lifters\nx - Exit Program\n')

def evaluate(cmd):
    # Check if command is valid, if not then print "Invalid action '{cmd}'. Try again!" and return False. If cmd is valid then return True
    # Code start (4 Lines of code)

    # Code end

def ieCommand(cmd):
    if cmd == 'a':
        name = input('Enter new lifter name: ')
        if name not in name_list and name != '':
            # Instatiate an Athlete Object with the name of the lifter
            # Code start (1 Line of code)
            obj = 
            # Code end
            object_list.append(obj)
            name_list.append(name)
        else:
            if name == '':
                print('Not a name, enter a valid name!')
            else: print(f"Lifter '{name}' already exists!")
    if cmd == 'r':
        name = input('Enter lifter name to remove: ')
        if name in name_list:
            object_list.pop(name_list.index(name))
            name_list.remove(name)
        else: print(f"Lifter '{name}' does not exist!")
    if cmd == 'u':
        name = input('Enter lifter name to update: ')
        if name not in name_list:
            print('This lifter does not exist!')
            return
        exercise = input("Enter lift (one of 'squat', 'bench press', 'deadlift'): ")
        if exercise in validExercises:
            weight = input('Enter weight(s): ').split(' ')
            try:
                weights = []
                for i in weight:
                    weights.append(float(i))
            except:
                print('Invalid weights!')
            if exercise == 'squat':
                object_list[name_list.index(name)].squat = weights
            if exercise == 'bench press':
                object_list[name_list.index(name)].bench = weights
            if exercise == 'deadlift':
                object_list[name_list.index(name)].lift = weights
        else: print('Not a valid exercise!')
    if cmd == 'v':
        for i in object_list:
            print(f'------------------------------\nName: {i.name}\nsquat: {i.squat}\nbench press: {i.bench}\ndeadlift: {i.lift}\n')
        print('\n')
    if cmd == 'x':
        print('Bye!')
        quit()


class Athlete:

    def __init__(self, name):
        self.name = name
        self.squat = []
        # Add a 'bench' and 'lift' attribute to the class in same fashion as 'squat'
        # Code start (2 Lines of code)

        # Code end

if __name__ == '__main__':
    while True:
        showText()
        cmd = input('Enter action: ')
        valid = evaluate(cmd)
        if valid:
            ieCommand(cmd)