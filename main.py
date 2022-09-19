##
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

print("cell 1")
##

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
Tow_0_6_N1_meanRTM = Tow_0_6_N1.means["Rtm - Mean"]
Tow_0_6_N1_meanSpeed = Tow_0_6_N1.means["Speed - Mean"]
Tow_0_6_N1_meanSinkFP = Tow_0_6_N1.means["Sink_FP - Mean"]
Tow_0_6_N1_meanSinkAP = Tow_0_6_N1.means["Sink_AP - Mean"]
Tow_0_6_N1_stddevRTM = Tow_0_6_N1.std_devs["Rtm - Std.dev"]
Tow_0_6_N1_stddevSpeed = Tow_0_6_N1.std_devs["Speed - Std.dev"]
Tow_0_6_N1_stddevSinkFP = Tow_0_6_N1.std_devs["Sink_FP - Std.dev"]
Tow_0_6_N1_stddevSinkAP = Tow_0_6_N1.std_devs["Sink_AP - Std.dev"]

Tow_0_7_N1 = Towing_files(filename="V0_7_#1.BIN", starttimes=24, endtimes=42.4, title="V = 0.7 m/s - Run #1")
Tow_0_7_N1.write_statistics()
Tow_0_7_N1.plot_all_timeseries()
Tow_0_7_N1.plot_section_timeseries(1.96)
Tow_0_7_N1_meanRTM = Tow_0_7_N1.means["Rtm - Mean"]
Tow_0_7_N1_meanSpeed = Tow_0_7_N1.means["Speed - Mean"]
Tow_0_7_N1_meanSinkFP = Tow_0_7_N1.means["Sink_FP - Mean"]
Tow_0_7_N1_meanSinkAP = Tow_0_7_N1.means["Sink_AP - Mean"]
Tow_0_7_N1_stddevRTM = Tow_0_7_N1.std_devs["Rtm - Std.dev"]
Tow_0_7_N1_stddevSpeed = Tow_0_7_N1.std_devs["Speed - Std.dev"]
Tow_0_7_N1_stddevSinkFP = Tow_0_7_N1.std_devs["Sink_FP - Std.dev"]
Tow_0_7_N1_stddevSinkAP = Tow_0_7_N1.std_devs["Sink_AP - Std.dev"]

Tow_0_8_N1 = Towing_files(filename="V0_8_#1.BIN", starttimes=19.8, endtimes=33.8, title="V = 0.8 m/s - Run #1")
Tow_0_8_N1.write_statistics()
Tow_0_8_N1.plot_all_timeseries()
Tow_0_8_N1.plot_section_timeseries(1.96)
Tow_0_8_N1_meanRTM = Tow_0_8_N1.means["Rtm - Mean"]
Tow_0_8_N1_meanSpeed = Tow_0_8_N1.means["Speed - Mean"]
Tow_0_8_N1_meanSinkFP = Tow_0_8_N1.means["Sink_FP - Mean"]
Tow_0_8_N1_meanSinkAP = Tow_0_8_N1.means["Sink_AP - Mean"]
Tow_0_8_N1_stddevRTM = Tow_0_8_N1.std_devs["Rtm - Std.dev"]
Tow_0_8_N1_stddevSpeed = Tow_0_8_N1.std_devs["Speed - Std.dev"]
Tow_0_8_N1_stddevSinkFP = Tow_0_8_N1.std_devs["Sink_FP - Std.dev"]
Tow_0_8_N1_stddevSinkAP = Tow_0_8_N1.std_devs["Sink_AP - Std.dev"]

Tow_0_9_N1 = Towing_files(filename="V0_9_#1.BIN", starttimes=15.0, endtimes=27.2, title="V = 0.9 m/s - Run #1")
Tow_0_9_N1.write_statistics()
Tow_0_9_N1.plot_all_timeseries()
Tow_0_9_N1.plot_section_timeseries(1.96)
Tow_0_9_N1_meanRTM = Tow_0_9_N1.means["Rtm - Mean"]
Tow_0_9_N1_meanSpeed = Tow_0_9_N1.means["Speed - Mean"]
Tow_0_9_N1_meanSinkFP = Tow_0_9_N1.means["Sink_FP - Mean"]
Tow_0_9_N1_meanSinkAP = Tow_0_9_N1.means["Sink_AP - Mean"]
Tow_0_9_N1_stddevRTM = Tow_0_9_N1.std_devs["Rtm - Std.dev"]
Tow_0_9_N1_stddevSpeed = Tow_0_9_N1.std_devs["Speed - Std.dev"]
Tow_0_9_N1_stddevSinkFP = Tow_0_9_N1.std_devs["Sink_FP - Std.dev"]
Tow_0_9_N1_stddevSinkAP = Tow_0_9_N1.std_devs["Sink_AP - Std.dev"]

Tow_0_9_N2 = Towing_files(filename="V0_9#2.BIN", starttimes=17.0, endtimes=28.0, title="V = 0.9 m/s - Run #2")
Tow_0_9_N2.write_statistics()
Tow_0_9_N2.plot_all_timeseries()
Tow_0_9_N2.plot_section_timeseries(1.96)
Tow_0_9_N2_meanRTM = Tow_0_9_N2.means["Rtm - Mean"]
Tow_0_9_N2_meanSpeed = Tow_0_9_N2.means["Speed - Mean"]
Tow_0_9_N2_meanSinkFP = Tow_0_9_N2.means["Sink_FP - Mean"]
Tow_0_9_N2_meanSinkAP = Tow_0_9_N2.means["Sink_AP - Mean"]
Tow_0_9_N2_stddevRTM = Tow_0_9_N2.std_devs["Rtm - Std.dev"]
Tow_0_9_N2_stddevSpeed = Tow_0_9_N2.std_devs["Speed - Std.dev"]
Tow_0_9_N2_stddevSinkFP = Tow_0_9_N2.std_devs["Sink_FP - Std.dev"]
Tow_0_9_N2_stddevSinkAP = Tow_0_9_N2.std_devs["Sink_AP - Std.dev"]

Tow_0_9_N3 = Towing_files(filename="V0_9#3.BIN", starttimes=19.5, endtimes=29.9, title="V = 0.9 m/s - Run #3")
Tow_0_9_N3.write_statistics()
Tow_0_9_N3.plot_all_timeseries()
Tow_0_9_N3.plot_section_timeseries(1.96)
Tow_0_9_N3_meanRTM = Tow_0_9_N3.means["Rtm - Mean"]
Tow_0_9_N3_meanSpeed = Tow_0_9_N3.means["Speed - Mean"]
Tow_0_9_N3_meanSinkFP = Tow_0_9_N3.means["Sink_FP - Mean"]
Tow_0_9_N3_meanSinkAP = Tow_0_9_N3.means["Sink_AP - Mean"]
Tow_0_9_N3_stddevRTM = Tow_0_9_N3.std_devs["Rtm - Std.dev"]
Tow_0_9_N3_stddevSpeed = Tow_0_9_N3.std_devs["Speed - Std.dev"]
Tow_0_9_N3_stddevSinkFP = Tow_0_9_N3.std_devs["Sink_FP - Std.dev"]
Tow_0_9_N3_stddevSinkAP = Tow_0_9_N3.std_devs["Sink_AP - Std.dev"]

Tow_0_9_N4 = Towing_files(filename="V0_9#4.BIN", starttimes=21.0, endtimes=32.5, title="V = 0.9 m/s - Run #4")
Tow_0_9_N4.write_statistics()
Tow_0_9_N4.plot_all_timeseries()
Tow_0_9_N4.plot_section_timeseries(1.96)
Tow_0_9_N4_meanRTM = Tow_0_9_N4.means["Rtm - Mean"]
Tow_0_9_N4_meanSpeed = Tow_0_9_N4.means["Speed - Mean"]
Tow_0_9_N4_meanSinkFP = Tow_0_9_N4.means["Sink_FP - Mean"]
Tow_0_9_N4_meanSinkAP = Tow_0_9_N4.means["Sink_AP - Mean"]
Tow_0_9_N4_stddevRTM = Tow_0_9_N4.std_devs["Rtm - Std.dev"]
Tow_0_9_N4_stddevSpeed = Tow_0_9_N4.std_devs["Speed - Std.dev"]
Tow_0_9_N4_stddevSinkFP = Tow_0_9_N4.std_devs["Sink_FP - Std.dev"]
Tow_0_9_N4_stddevSinkAP = Tow_0_9_N4.std_devs["Sink_AP - Std.dev"]

Tow_0_9_N5 = Towing_files(filename="V0_9#5.BIN", starttimes=17.0, endtimes=28.5, title="V = 0.9 m/s - Run #5")
Tow_0_9_N5.write_statistics()
Tow_0_9_N5.plot_all_timeseries()
Tow_0_9_N5.plot_section_timeseries(1.96)
Tow_0_9_N5_meanRTM = Tow_0_9_N5.means["Rtm - Mean"]
Tow_0_9_N5_meanSpeed = Tow_0_9_N5.means["Speed - Mean"]
Tow_0_9_N5_meanSinkFP = Tow_0_9_N5.means["Sink_FP - Mean"]
Tow_0_9_N5_meanSinkAP = Tow_0_9_N5.means["Sink_AP - Mean"]
Tow_0_9_N5_stddevRTM = Tow_0_9_N5.std_devs["Rtm - Std.dev"]
Tow_0_9_N5_stddevSpeed = Tow_0_9_N5.std_devs["Speed - Std.dev"]
Tow_0_9_N5_stddevSinkFP = Tow_0_9_N5.std_devs["Sink_FP - Std.dev"]
Tow_0_9_N5_stddevSinkAP = Tow_0_9_N5.std_devs["Sink_AP - Std.dev"]


Tow_1_0_N1 = Towing_files(filename="V1_0_#1.BIN", starttimes=16.3, endtimes=26.2, title="V = 1.0 m/s - Run #1")
Tow_1_0_N1.write_statistics()
Tow_1_0_N1.plot_all_timeseries()
Tow_1_0_N1.plot_section_timeseries(1.96)
Tow_1_0_N1_meanRTM = Tow_1_0_N1.means["Rtm - Mean"]
Tow_1_0_N1_meanSpeed = Tow_1_0_N1.means["Speed - Mean"]
Tow_1_0_N1_meanSinkFP = Tow_1_0_N1.means["Sink_FP - Mean"]
Tow_1_0_N1_meanSinkAP = Tow_1_0_N1.means["Sink_AP - Mean"]
Tow_1_0_N1_stddevRTM = Tow_1_0_N1.std_devs["Rtm - Std.dev"]
Tow_1_0_N1_stddevSpeed = Tow_1_0_N1.std_devs["Speed - Std.dev"]
Tow_1_0_N1_stddevSinkFP = Tow_1_0_N1.std_devs["Sink_FP - Std.dev"]
Tow_1_0_N1_stddevSinkAP = Tow_1_0_N1.std_devs["Sink_AP - Std.dev"]

Tow_1_1_N1 = Towing_files(filename="V1_1_#1.BIN", starttimes=22, endtimes=30, title="V = 1.1 m/s - Run #1")
Tow_1_1_N1.write_statistics()
Tow_1_1_N1.plot_all_timeseries()
Tow_1_1_N1.plot_section_timeseries(1.96)
Tow_1_1_N1_meanRTM = Tow_1_1_N1.means["Rtm - Mean"]
Tow_1_1_N1_meanSpeed = Tow_1_1_N1.means["Speed - Mean"]
Tow_1_1_N1_meanSinkFP = Tow_1_1_N1.means["Sink_FP - Mean"]
Tow_1_1_N1_meanSinkAP = Tow_1_1_N1.means["Sink_AP - Mean"]
Tow_1_1_N1_stddevRTM = Tow_1_1_N1.std_devs["Rtm - Std.dev"]
Tow_1_1_N1_stddevSpeed = Tow_1_1_N1.std_devs["Speed - Std.dev"]
Tow_1_1_N1_stddevSinkFP = Tow_1_1_N1.std_devs["Sink_FP - Std.dev"]
Tow_1_1_N1_stddevSinkAP = Tow_1_1_N1.std_devs["Sink_AP - Std.dev"]

Tow_1_2_N1 = Towing_files(filename="V1_2#1.BIN", starttimes=18.5, endtimes=24.5, title="V = 1.2 m/s - Run #1")
Tow_1_2_N1.write_statistics()
Tow_1_2_N1.plot_all_timeseries()
Tow_1_2_N1.plot_section_timeseries(1.96)
Tow_1_2_N1_meanRTM = Tow_1_2_N1.means["Rtm - Mean"]
Tow_1_2_N1_meanSpeed = Tow_1_2_N1.means["Speed - Mean"]
Tow_1_2_N1_meanSinkFP = Tow_1_2_N1.means["Sink_FP - Mean"]
Tow_1_2_N1_meanSinkAP = Tow_1_2_N1.means["Sink_AP - Mean"]
Tow_1_2_N1_stddevRTM = Tow_1_2_N1.std_devs["Rtm - Std.dev"]
Tow_1_2_N1_stddevSpeed = Tow_1_2_N1.std_devs["Speed - Std.dev"]
Tow_1_2_N1_stddevSinkFP = Tow_1_2_N1.std_devs["Sink_FP - Std.dev"]
Tow_1_2_N1_stddevSinkAP = Tow_1_2_N1.std_devs["Sink_AP - Std.dev"]

Tow_1_3_N1 = Towing_files(filename="V1_3#1.BIN", starttimes=41.5, endtimes=46.2, title="V = 1.3 m/s - Run #1")
Tow_1_3_N1.write_statistics()
Tow_1_3_N1.plot_all_timeseries()
Tow_1_3_N1.plot_section_timeseries(1.96)
Tow_1_3_N1_meanRTM = Tow_1_3_N1.means["Rtm - Mean"]
Tow_1_3_N1_meanSpeed = Tow_1_3_N1.means["Speed - Mean"]
Tow_1_3_N1_meanSinkFP = Tow_1_3_N1.means["Sink_FP - Mean"]
Tow_1_3_N1_meanSinkAP = Tow_1_3_N1.means["Sink_AP - Mean"]
Tow_1_3_N1_stddevRTM = Tow_1_3_N1.std_devs["Rtm - Std.dev"]
Tow_1_3_N1_stddevSpeed = Tow_1_3_N1.std_devs["Speed - Std.dev"]
Tow_1_3_N1_stddevSinkFP = Tow_1_3_N1.std_devs["Sink_FP - Std.dev"]
Tow_1_3_N1_stddevSinkAP = Tow_1_3_N1.std_devs["Sink_AP - Std.dev"]

Tow_1_4_N1 = Towing_files(filename="V1_4#1.BIN", starttimes=18.0, endtimes=21.5, title="V = 1.4 m/s - Run #1")
Tow_1_4_N1.write_statistics()
Tow_1_4_N1.plot_all_timeseries()
Tow_1_4_N1.plot_section_timeseries(1.96)
Tow_1_4_N1_meanRTM = Tow_1_4_N1.means["Rtm - Mean"]
Tow_1_4_N1_meanSpeed = Tow_1_4_N1.means["Speed - Mean"]
Tow_1_4_N1_meanSinkFP = Tow_1_4_N1.means["Sink_FP - Mean"]
Tow_1_4_N1_meanSinkAP = Tow_1_4_N1.means["Sink_AP - Mean"]
Tow_1_4_N1_stddevRTM = Tow_1_4_N1.std_devs["Rtm - Std.dev"]
Tow_1_4_N1_stddevSpeed = Tow_1_4_N1.std_devs["Speed - Std.dev"]
Tow_1_4_N1_stddevSinkFP = Tow_1_4_N1.std_devs["Sink_FP - Std.dev"]
Tow_1_4_N1_stddevSinkAP = Tow_1_4_N1.std_devs["Sink_AP - Std.dev"]

print("cell 2")
##

mean_speeds = np.array([Tow_0_6_N1_meanSpeed, Tow_0_7_N1_meanSpeed, Tow_0_8_N1_meanSpeed, Tow_0_9_N1_meanSpeed, Tow_0_9_N2_meanSpeed,
                        Tow_0_9_N3_meanSpeed, Tow_0_9_N4_meanSpeed, Tow_0_9_N5_meanSpeed,
                        Tow_1_0_N1_meanSpeed, Tow_1_1_N1_meanSpeed, Tow_1_2_N1_meanSpeed, Tow_1_3_N1_meanSpeed, Tow_1_4_N1_meanSpeed])

stddev_speeds = np.array([Tow_0_6_N1_stddevSpeed, Tow_0_7_N1_stddevSpeed, Tow_0_8_N1_stddevSpeed, Tow_0_9_N1_stddevSpeed, Tow_0_9_N2_stddevSpeed,
                        Tow_0_9_N3_stddevSpeed, Tow_0_9_N4_stddevSpeed, Tow_0_9_N5_stddevSpeed,
                        Tow_1_0_N1_stddevSpeed, Tow_1_1_N1_stddevSpeed, Tow_1_2_N1_stddevSpeed, Tow_1_3_N1_stddevSpeed, Tow_1_4_N1_stddevSpeed])



mean_RTMs = np.array([Tow_0_6_N1_meanRTM, Tow_0_7_N1_meanRTM, Tow_0_8_N1_meanRTM, Tow_0_9_N1_meanRTM, Tow_0_9_N2_meanRTM,
                        Tow_0_9_N3_meanRTM, Tow_0_9_N4_meanRTM, Tow_0_9_N5_meanRTM,
                        Tow_1_0_N1_meanRTM, Tow_1_1_N1_meanRTM, Tow_1_2_N1_meanRTM, Tow_1_3_N1_meanRTM, Tow_1_4_N1_meanRTM])

mean_SinkFPs = np.array([Tow_0_6_N1_meanSinkFP, Tow_0_7_N1_meanSinkFP, Tow_0_8_N1_meanSinkFP, Tow_0_9_N1_meanSinkFP,
                        Tow_1_0_N1_meanSinkFP, Tow_1_1_N1_meanSinkFP, Tow_1_2_N1_meanSinkFP, Tow_1_3_N1_meanSinkFP, Tow_1_4_N1_meanSinkFP])

mean_SinkAPs = np.array([Tow_0_6_N1_meanSinkAP, Tow_0_7_N1_meanSinkAP, Tow_0_8_N1_meanSinkAP, Tow_0_9_N1_meanSinkAP,
                        Tow_1_0_N1_meanSinkAP, Tow_1_1_N1_meanSinkAP, Tow_1_2_N1_meanSinkAP, Tow_1_3_N1_meanSinkAP, Tow_1_4_N1_meanSinkAP])

run_number = np.arange(1, 14)

run_number_ticks = ["1", "2", "3", "4a", "4b", "4c", "4d", "4e", "5", "6", "7", "8", "9"]

##
# Comparison of velocities
plt.plot(run_number, planned_speeds_repeated, ls="dotted", label="Planned")
plt.scatter(run_number, mean_speeds, zorder=99, label="Mean measured")
plt.errorbar(run_number, mean_speeds, yerr=stddev_speeds, fmt="none", label="Std.dev", zorder=100, c="red")
plt.title("Planned vs measured velocity")
plt.legend(loc='lower right', bbox_to_anchor=(1.1, 0.2), fancybox=True, shadow=True)
plt.xticks(run_number,run_number_ticks)
plt.show()

##
# Plotting of dimensional resistance

plt.scatter(mean_speeds, mean_RTMs)
plt.title("Towing resistance versus towing velocity")
plt.show()

##
# Plotting of non-dimensional resistance

plt.scatter(Froude_number(mean_speeds, g, L_wl_m), C_TM(mean_RTMs, rho, mean_speeds, S_m))
plt.title("Towing resistance coefficient versus Froude numbers")
plt.show()


##
# Plotting of residual resistance

plt.scatter(Froude_number(mean_speeds, g, L_wl_m), C_RM(C_TM(mean_RTMs, rho, mean_speeds, S_m), mean_speeds, C_b_m, L_wl_m, T_m, T_m, B_m))
plt.title("Residual resistance versus Froude numbers")
plt.show()
"""
To do list:
* Create plot of C_RTM versus speed and Froude
    * Add uncertainty bars
    
* Calculate residual resistance

* 
"""

##
print(planned_speeds)
print(np.around(Froude_number(planned_speeds, g, L_wl_m),2))
print(np.around(Rn(planned_speeds, L_wl_m, nu),3))


##
plt.ticklabel_format(axis="y", style="scientific")
plt.plot(given_froude, given_holtrop, label="Holtrop")
plt.plot(given_froude, given_hollenbach, label="Hollenbach")
plt.scatter(Froude_number(mean_speeds, g, L_wl_m), C_RM(C_TM(mean_RTMs, rho, mean_speeds, S_m), mean_speeds, C_b_m, L_wl_m, T_m, T_m, B_m))
plt.legend(loc="best")



plt.show()