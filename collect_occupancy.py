import sys
from time import localtime, strftime
from mongodb_occupancy_data_controller import store_occupancy, get_occupancy

def collect_occupancy(command, occupancy_change):
    old_occupancy = get_occupancy()
    if command in ["a", "add", "Add", "+"]:
        new_occupancy = old_occupancy + int(occupancy_change)
    elif command in ["r", "remove", "Remove", "-"]:
        new_occupancy = old_occupancy - int(occupancy_change)
    elif command in ["set", "Set", "s"]:
        new_occupancy = int(occupancy_change)
    store_occupancy(new_occupancy)
    print("Current occupancy is " + str(new_occupancy))
    print()

#if __name__ == '__main__':
    #collect_occupancy(*sys.argv[1:])


while 1:
    try:
        x, y = input("Enter your operation: ").split()  
    except ValueError:
        print("Input Error!")
        continue
    else:
        #print("Operation: ", x) 
        #print("Number of people: ", y)
        print("Time: ",strftime("%Y-%m-%d %H:%M:%S", localtime()))
        collect_occupancy(x,y)

