class Earthquake:
    """
    Set up the seismic info for a certain point
    """
    def __init__(self, data):
        self.name = data['properties']['place'].replace(',', '-')
        self.longitude = data['geometry']['coordinates'][0]
        self.latitude = data['geometry']['coordinates'][1]
        self.depth = data['geometry']['coordinates'][2]
        self.magnitude = data['properties']['mag']
