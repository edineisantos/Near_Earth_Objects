from models import NearEarthObject, CloseApproach

# Creating a sample NearEarthObject
neo = NearEarthObject(designation='2020 FK', name='One REALLY BIG fake asteroid', diameter=12.345, hazardous=True)

# Displaying attributes of NearEarthObject
print(neo._designation)
print(neo.name)
print(neo.diameter)
print(neo.hazardous)
print(neo)

# Creating a sample CloseApproach
ca_time = "2020-Jan-01 12:30"
ca = CloseApproach(designation='2020 FK', time=ca_time, distance=0.25, velocity=56.78)
ca.neo = neo  # Linking the CloseApproach to the NearEarthObject

# Displaying attributes of CloseApproach
print(type(ca.time))
print(ca.time_str)
print(ca.distance)
print(ca.velocity)
print(ca)