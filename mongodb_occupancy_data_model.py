import mongoengine as me 

class OccupancyData(me.Document):
    collectedAt = me.DateTimeField(required=True)
    occupancy = me.IntField(required=True) 

