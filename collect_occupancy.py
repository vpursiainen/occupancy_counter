import sys
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

if __name__ == '__main__':
    collect_occupancy(*sys.argv[1:])




