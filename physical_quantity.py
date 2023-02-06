

class PhysicalQuantity():
    def __init__(self, data, uncertainty): # data should be using astropy units
        self.data = data
        self.uncertainty = uncertainty
        self.unit = data.unit