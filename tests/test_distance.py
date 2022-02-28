"""Test Distance module."""
from mlproject.distance import haversine


def test_haversine_function():
    """Test haversine function."""
    assert haversine(0, 0, 0, 0) == 0

    # Le Wagon location
    lat1, lon1 = 48.865070, 2.380009
    # Insert your coordinates from google maps here -- Buenos Aires
    lat2, lon2 = -34.55278770849123, -58.467115615170805
    distance = haversine(lon1, lat1, lon2, lat2)

    assert round(distance, 2) == 11052.2
