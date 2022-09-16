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

Tow_0_6_N1 = Towing_files(filename="V0_6_#1.BIN", starttimes=70.4, endtimes=92.0, title="V = 0.6 m/s - Run #1")
Tow_0_6_N1.write_statistics()
Tow_0_6_N1.plot_all_timeseries()
Tow_0_6_N1.plot_section_timeseries(1.96)


Tow_0_7_N1 = Towing_files(filename="V0_7_#1.BIN", starttimes=24, endtimes=42.4, title="V = 0.7 m/s - Run #1")
Tow_0_7_N1.write_statistics()
Tow_0_7_N1.plot_all_timeseries()
Tow_0_7_N1.plot_section_timeseries(1.96)

Tow_0_8_N1 = Towing_files(filename="V0_8_#1.BIN", starttimes=19.8, endtimes=33.8, title="V = 0.8 m/s - Run #1")
Tow_0_8_N1.write_statistics()
Tow_0_8_N1.plot_all_timeseries()
Tow_0_8_N1.plot_section_timeseries(1.96)

Tow_0_9_N1 = Towing_files(filename="V0_9_#1.BIN", starttimes=15.0, endtimes=27.2, title="V = 0.9 m/s - Run #1")

Tow_0_9_N1.write_statistics()
Tow_0_9_N1.plot_all_timeseries()
Tow_0_9_N1.plot_section_timeseries(1.96)

Tow_0_9_N2 = Towing_files(filename="V0_9#2.BIN", starttimes=17.0, endtimes=28.0, title="V = 0.9 m/s - Run #2")
Tow_0_9_N2.write_statistics()
Tow_0_9_N2.plot_all_timeseries()
Tow_0_9_N2.plot_section_timeseries(1.96)

Tow_0_9_N3 = Towing_files(filename="V0_9#3.BIN", starttimes=19.5, endtimes=29.9, title="V = 0.9 m/s - Run #3")
Tow_0_9_N3.write_statistics()
Tow_0_9_N3.plot_all_timeseries()
Tow_0_9_N3.plot_section_timeseries(1.96)

Tow_0_9_N4 = Towing_files(filename="V0_9#4.BIN", starttimes=21.0, endtimes=32.5, title="V = 0.9 m/s - Run #4")
Tow_0_9_N4.write_statistics()
Tow_0_9_N4.plot_all_timeseries()
Tow_0_9_N4.plot_section_timeseries(1.96)

Tow_0_9_N5 = Towing_files(filename="V0_9#5.BIN", starttimes=17.0, endtimes=28.5, title="V = 0.9 m/s - Run #5")
Tow_0_9_N5.write_statistics()
Tow_0_9_N5.plot_all_timeseries()
Tow_0_9_N5.plot_section_timeseries(1.96)


Tow_1_0_N1 = Towing_files(filename="V1_0_#1.BIN", starttimes=16.3, endtimes=26.2, title="V = 1.0 m/s - Run #1")
Tow_1_0_N1.write_statistics()
Tow_1_0_N1.plot_all_timeseries()
Tow_1_0_N1.plot_section_timeseries(1.96)

Tow_1_1_N1 = Towing_files(filename="V1_1_#1.BIN", starttimes=22, endtimes=30, title="V = 1.1 m/s - Run #1")
Tow_1_1_N1.write_statistics()
Tow_1_1_N1.plot_all_timeseries()
Tow_1_1_N1.plot_section_timeseries(1.96)

Tow_1_2_N1 = Towing_files(filename="V1_2#1.BIN", starttimes=18.5, endtimes=24.5, title="V = 1.2 m/s - Run #1")
Tow_1_2_N1.write_statistics()
Tow_1_2_N1.plot_all_timeseries()
Tow_1_2_N1.plot_section_timeseries(1.96)

Tow_1_3_N1 = Towing_files(filename="V1_3#1.BIN", starttimes=41.5, endtimes=46.2, title="V = 1.3 m/s - Run #1")
Tow_1_3_N1.write_statistics()
Tow_1_3_N1.plot_all_timeseries()
Tow_1_3_N1.plot_section_timeseries(1.96)

Tow_1_4_N1 = Towing_files(filename="V1_4#1.BIN", starttimes=18.0, endtimes=21.5, title="V = 1.4 m/s - Run #1")
Tow_1_4_N1.write_statistics()
Tow_1_4_N1.plot_all_timeseries()
Tow_1_4_N1.plot_section_timeseries(1.96)

"""
To do list:
* Create plot of C_RTM versus speed and Froude
    * Add uncertainty bars
    
* Calculate residual resistance

* 
"""

