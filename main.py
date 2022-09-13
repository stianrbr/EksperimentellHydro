import os
from utility import *
from matplotlib_visualization import*

plt.style.use("seaborn")
plt.rcParams["figure.figsize"] = (15, 5)
plot_scale(1, title=1.5)

try:
    os.mkdir(results)
except FileExistsError:
    pass


Cal_rtm = Calibration_file(filename="cal_rtm.BIN", relevant_channel="Rtm",
                           starttimes=[24, 54, 96, 134], endtimes=[42,80, 125, 162],
                           known_values=[0*g, 1*g, 2*g, 3*g], cal_unit="Force [N]", title="Calibration")
Cal_rtm.plot_timeseries()
Cal_rtm.calibration()

Cal_sinkFP = Calibration_file(filename="cal_sinkFP.BIN", relevant_channel="Sink_FP",
                           starttimes=[9.6, 28.7, 50.7, 65.6], endtimes=[22.9, 45.8, 62, 74.7],
                           known_values=[0, 0.1, 0.2, 0.3], cal_unit="Distance [m]", title="Calibration")
Cal_sinkFP.plot_timeseries()
Cal_sinkFP.calibration()

Cal_WP = Calibration_file(filename="cal_wp.BIN", relevant_channel="Wave",
                           starttimes=[1.9, 23.0, 45.0, 65.6, 87.7, 122.2], endtimes=[13.7, 35.7, 58.8, 79.4, 110.8, 151.5],
                           known_values=[0, 0.05, 0.1, 0.15, 0.2, 0.25], cal_unit="Elevation [m]", title="Calibration")
Cal_WP.plot_timeseries()
Cal_WP.calibration()

print(Cal_rtm.means)

Tow_file = Towing_files(filename="V0_7_#1.BIN", starttimes=24, endtimes=42.4, title="V = 0.7 m/s - Run #1")

Tow_file.plot_all_timeseries()

Tow_file.write_statistics()

Tow_file.plot_section_timeseries(1.96)

print(Tow_file.means)
print(Tow_file.std_devs)