import statistics
import data_to_color as d2c

# Takes in array of size 60 with frequences
class frequency_plot:
    def __init__(self):
        self.high = 0
        self.low = 0
        self.intensities = [0]*60
        self.initialized = False

    def update(self, input_data, output_data):
        median = statistics.median(sorted(input_data))
        max_frequency = max(input_data)
        min_frequency = min(input_data)
        if max_frequency >= 4* median:   ## Done to avoid very dominant nodes maybe implement better solution
            max_frequency = 2*median    #TODO better?
        if self.initialized == False:
            self.high = max_frequency
            self.low = min_frequency
            self.initialized = True
        else:
            self.high = self.high*0.9 + 0.1*max_frequency
            self.low = self.low*0.9 + 0.1*min_frequency
        for index in range(len(input_data)):
            intensity = int((input_data[index]-self.low)/(self.high - self.low)*10)
            intensity = min(9, intensity)
            intensity = max(0, intensity)
            self.intensities[index] = intensity
        d2c.data_to_bytearray(self.intensities, output_data)