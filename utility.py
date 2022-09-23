from apread import APReader
import numpy as np
import os
import matplotlib.pyplot as plt
from settings import *
from matplotlib_visualization import*
plot_scale(1, title=1.5)


class Calibration_file:
    """
    Class: Calibration_file

    """
    def __init__(self, filename, relevant_channel, starttimes, endtimes, known_values, cal_unit, title):
        self.filename = filename
        self.startimes = starttimes
        self.endtimes = endtimes
        self.known_values = known_values
        self.cal_unit = cal_unit
        self.title = title
        self.measurements = APReader(path+filename)
        self.time = self.measurements.Channels[0].data
        self.relevant_channel = relevant_channel
        self.means = []
        try:
            os.mkdir(calibration_results)
        except FileExistsError:
            pass
    def plot_timeseries(self):
        """
        Function: plot_timeseries
        :return:
        """
        for i in range(1, self.measurements.numChannels):
            if self.measurements.Channels[i].Name == self.relevant_channel:
                plt.plot(self.time, self.measurements.Channels[i].data)
                plt.tight_layout()
                if show_plots:
                    plt.show()
                else:
                    plt.close()
                    plt.cla()
                    plt.clf()

    def calibration(self):
        for i in range(1, self.measurements.numChannels):
            if self.measurements.Channels[i].Name == self.relevant_channel:
                fig = plt.figure()
                ax = plt.subplot(111)
                ax.plot(self.time, self.measurements.Channels[i].data)
                ax.set_xticks(np.arange(min(self.time), max(self.time) + 1, 10.0))
                fig.suptitle("Calibration - " + self.measurements.Channels[i].Name)
                for start, end in zip(self.startimes, self.endtimes):
                    data_section = self.measurements.Channels[i].data[int(start * sampling_freq):int(end * sampling_freq)]
                    sec_mean = np.mean(data_section)
                    self.means.append(sec_mean)
                    if start == self.startimes[0]:
                        ax.axvline(start, ls="dotted", c="green", label="Cal. start")
                        ax.axvline(end, ls="dotted", c="red", label="Cal. end")
                        ax.hlines(y=sec_mean, xmin=start, xmax=end, colors="red", label="Mean value")
                    ax.axvline(start, ls="dotted", c="green")
                    ax.axvline(end, ls="dotted", c="red")
                    ax.hlines(y=sec_mean, xmin=start, xmax=end, colors="red")
                ax.legend(loc='upper right', bbox_to_anchor=(1.1, 1.05), fancybox=True, shadow=True)
                ax.set_xlabel("Time [s]")
                ax.set_ylabel("Voltage [V]")
                plt.tight_layout()
                plt.savefig(calibration_results+self.filename.replace(".BIN", "_")+self.measurements.Channels[i].Name+"_calibration.png")

                if show_plots:
                    plt.show()
                else:
                    fig.clear()
                    plt.close(fig)

                m, b = np.polyfit(np.around(np.array(self.means),4), np.around(np.array(self.known_values),4), 1)
                # Rounding of data to match excel results used in lab
                fig = plt.figure()
                ax = plt.subplot(111)
                ax.scatter(self.means, self.known_values)
                fig.suptitle(self.title + " - "+self.measurements.Channels[i].Name+" measurement")
                Rx = np.linspace(min(self.means)-2*np.std(self.means), max(self.means)+2*np.std(self.means), 100)
                ax.plot(Rx, b+m*Rx, ls="dotted", label="Regression")
                ax.set_ylabel(self.cal_unit)
                ax.set_xlabel("Voltage [V]")
                ax.annotate(text=r'Line: {} $\cdot$ x + {}'.format(round(m,3), round(b,3)), xy=(0.25, 0.5), xycoords='axes fraction', fontsize="large")
                plt.tight_layout()
                plt.savefig(calibration_results + self.filename.replace(".BIN", "") + self.measurements.Channels[i].Name + "_regression.png")
                if show_plots:
                    plt.show()
                else:
                    fig.clear()
                    plt.close(fig)

                with open(calibration_results+self.filename.replace(".BIN", ".txt"),"w") as f:
                    f.write("\n -------------------\n"+self.title + " - "+self.measurements.Channels[i].Name+"\n -------------------\n")
                    f.write("{:<20}{:>20}\n".format("Mean value", "Known Value"))
                    for mean, kv in zip(self.means, self.known_values):
                        f.write("{:<20}{:20}\n".format(mean, kv))
                    f.write("\n -------------------\n")
                    f.write("Regression line: {} * x + {}\n".format(m, b))
                    f.write("\n -------------------\n")
class Towing_files:
    def __init__(self, filename, starttimes, endtimes, title):
        self.filename = filename
        self.measurements = APReader(path+filename)
        self.title = title
        self.starttimes = starttimes
        self.endtimes = endtimes
        self.means = {}
        self.std_devs = {}
        self.maxes = {}
        try:
            os.mkdir(towing_results)
        except FileExistsError:
            pass
    def plot_all_timeseries(self):
        for i in range(1, self.measurements.numChannels):
            fig = plt.figure()
            ax = plt.subplot(111)
            ax.plot(self.measurements.Channels[i].Time.data, self.measurements.Channels[i].data)
            fig.suptitle(self.title+"\n"+self.measurements.Channels[i].Name+" measurement - Full section")
            ax.set_xticks(np.arange(min(self.measurements.Channels[i].Time.data), max(self.measurements.Channels[i].Time.data) + 1, 5.0))
            ax.set_xlabel("Time [s]")
            ax.set_ylabel(self.measurements.Channels[i].unit)
            if self.measurements.Channels[i].Name != "Wave":
                ax.axvline(self.starttimes, ls="dotted", c="green", label="Data start")
                ax.axvline(self.endtimes, ls="dotted", c="red", label="Data end")
                ax.hlines(y=self.means[self.measurements.Channels[i].Name+" - Mean"], xmin=self.starttimes, xmax=self.endtimes, colors="red", label="Mean value \n ={} {}".format(round(self.means[self.measurements.Channels[i].Name+" - Mean"],2), self.measurements.Channels[i].unit))
                plt.legend(loc='upper right', bbox_to_anchor=(1.1, 1.05), fancybox=True, shadow=True)
            plt.tight_layout()
            plt.savefig(towing_results+self.filename.replace(".BIN", "")+self.measurements.Channels[i].Name+"_full_measurement.png")
            if show_plots:
                plt.show()
            else:
                plt.cla()
                fig.clear()
                plt.close('all')

    def plot_section_timeseries(self, plim):
        for i in range(1, self.measurements.numChannels):
            fig = plt.figure()
            ax = plt.subplot(111)
            ax.plot(self.measurements.Channels[i].Time.data[int(self.starttimes*sampling_freq):int(self.endtimes*sampling_freq)], self.measurements.Channels[i].data[int(self.starttimes*sampling_freq):int(self.endtimes*sampling_freq)])
            fig.suptitle(self.title+"\n"+self.measurements.Channels[i].Name+" measurement - Utilized section")
            ax.set_xlabel("Time [s]")
            ax.set_ylabel(self.measurements.Channels[i].unit)

            mean = np.mean(self.measurements.Channels[i].data[int(self.starttimes*sampling_freq):int(self.endtimes*sampling_freq)])
            std_dev = np.std(self.measurements.Channels[i].data[int(self.starttimes*sampling_freq):int(self.endtimes*sampling_freq)], ddof=1)
            ax.axhline(y=mean, label="Mean value \n ={} {}".format(round(self.means[self.measurements.Channels[i].Name+" - Mean"],2), self.measurements.Channels[i].unit), c="red")
            plt.legend(loc='upper right', bbox_to_anchor=(1.1, 1.05), fancybox=True, shadow=True)
            plt.tight_layout()
            plt.savefig(towing_results+self.filename.replace(".BIN", "")+self.measurements.Channels[i].Name+"_valid_section.png")
            if show_plots:
                plt.show()
            else:
                fig.clear()
                plt.close(fig)
    def write_statistics(self):
        with open(towing_results+self.filename.replace(".BIN", ".txt"),"w") as f:
            f.write("\n -------------------\n"+self.title+"\n -------------------\n")
            f.write("Start time: {}\n".format(self.starttimes))
            f.write("End time: {}\n -------------------\n".format(self.endtimes))
            for i in range(1, self.measurements.numChannels):
                data_section = self.measurements.Channels[i].data[int(self.starttimes*sampling_freq):int(self.endtimes*sampling_freq)]
                f.write(self.measurements.Channels[i].Name+"\n -------------------\n")
                mean = np.mean(data_section)
                self.means[self.measurements.Channels[i].Name+" - Mean"] = mean
                f.write("Mean: {}\n".format(mean))
                std_dev = np.std(data_section, ddof=1)
                self.std_devs[self.measurements.Channels[i].Name+" - Std.dev"] = std_dev
                self.maxes[self.measurements.Channels[i].Name+" - abs(max)"] = np.max(np.abs(data_section))
                f.write("Std.dev: {}\n".format(std_dev))
                f.write("\n -------------------\n")


def Froude_number(U, g, L):
    """
    Calculate Froude number from velocity
    :param U: Velocity
    :param g: gravitational acc.
    :param L: Length of ship
    :return: Froude number
    """
    return U/np.sqrt(g*L)

def C_TM(RTM, rho, U, S):
    """
    Non-dimensionalize towing resistance
    :param RTM: Dimensional resistance
    :param rho: Water density
    :param U: Velocity
    :param S: Wetted surface
    :return: Non-dimensional resistance
    """
    return RTM/((1/2)*rho*(U**2)*S)

def Rn(V, L, nu):
    return V*L/nu
def C_RM(C_TM, V, Cb, Lwl, T_Ap, T_Fp, B):
    phi = Cb/Lwl * np.sqrt((T_Ap+T_Fp)*B)
    k = 0.6*phi+145*phi**3.5  # MARINTEK form factor
    C_FM = 0.075/(np.log10(Rn(V, Lwl, nu))-2)**2
    C_R = C_TM-(1+k)*C_FM
    return C_R

