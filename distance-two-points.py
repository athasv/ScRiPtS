# https://stackoverflow.com/questions/19412462/getting-distance-between-two-points-based-on-latitude-longitude
# https://towardsdatascience.com/heres-how-to-calculate-distance-between-2-geolocations-in-python-93ecab5bbba4
from math import sin, cos, sqrt, atan2, radians
from sklearn.neighbors import DistanceMetric
import numpy as np

lat1, lon1, lat2, lon2, R = 20.9467,72.9520, 21.1702, 72.8311, 6373.0
coordinates_from = [lat1, lon1]
coordinates_to = [lat2, lon2]

dist = DistanceMetric.get_metric('haversine')
    
X = [[radians(lat1), radians(lon1)], [radians(lat2), radians(lon2)]]
distance_sklearn = R * dist.pairwise(X)
print('distance using sklearn: ', np.array(distance_sklearn).item(1))

