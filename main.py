import matplotlib.pyplot as plt
from apread import APReader
plt.style.use("seaborn")

path = "Group5\\"

class Calibration_file:
    def __init__(self, filename, channel, starttimes, endtimes):
        self.filename = filename,
        self.channel = channel,
        self.startimes = starttimes,
        self.endtimes = endtimes
        self.time = APReader(filename).Channels[0].data
        self.reading = APReader(filename).Channels[channel].data
    def plot_timeseries(self):
        plt.plot(self.time, self.reading)
        plt.show()

class Towing_files:
    def __init__(self, filename, path):
        self.filename = filename,
        self.path = path


Cal_rtm = Calibration_file(filename=path+"cal_rtm.BIN", channel=1, starttimes=0, endtimes=-1)

Cal_rtm.plot_timeseries()

calibfiles = {
    "Calibration Rtm": "cal_rtm.BIN",
    "Towing speed 0.7 m/s \n Towing #1" : "V0_7_#1.BIN"
}
