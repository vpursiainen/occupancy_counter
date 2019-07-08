from datetime import datetime
from mongodb_occupancy_data_model import OccupancyData
from mongodb_connection_controller import connect_to_mongodb, disconnect_from_mongodb
import time

def store_occupancy(number_of_occupants):
    cl = connect_to_mongodb()
    od = OccupancyData(occupancy = number_of_occupants, collectedAt = datetime.utcfromtimestamp(time.time()))
    od.save()
    disconnect_from_mongodb(cl)

def get_occupancy():
    cl = connect_to_mongodb()
    occ = OccupancyData.objects.order_by('-collectedAt').first()
    disconnect_from_mongodb(cl)
    return occ.occupancy
