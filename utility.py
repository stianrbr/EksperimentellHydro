from apread import APReader
import numpy as np
import os
import matplotlib.pyplot as plt
from settings import *

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
                    plt.plot()
                else:
                    plt.close("all")

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
                plt.savefig(calibration_results+self.filename.replace(".BIN", "_")+self.measurements.Channels[i].Name+"_calibration.png")
                plt.tight_layout()
                if show_plots:
                    plt.plot()
                else:
                    plt.close("all")

                m, b = np.polyfit(np.around(np.array(self.means),4), np.around(np.array(self.known_values),4), 1)
                # Rounding of data to match excel results used in lab
                plt.scatter(self.means, self.known_values)
                plt.title(self.title + " - "+self.measurements.Channels[i].Name+" measurement")
                Rx = np.linspace(min(self.means)-2*np.std(self.means), max(self.means)+2*np.std(self.means), 100)
                plt.plot(Rx, b+m*Rx, ls="dotted", label="Regression")
                plt.xlabel(self.cal_unit)
                plt.ylabel("Voltage [V]")
                plt.annotate(text=r'Line: {} $\cdot$ x + {}'.format(round(m,3), round(b,3)), xy=(0.25, 0.5), xycoords='axes fraction', fontsize="large")
                plt.savefig(calibration_results + self.filename.replace(".BIN", "") + self.measurements.Channels[i].Name + "_regression.png")
                if show_plots:
                    plt.plot()
                else:
                    plt.close("all")

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
        try:
            os.mkdir(towing_results)
        except FileExistsError:
            pass
    def plot_all_timeseries(self):
        for i in range(1, self.measurements.numChannels):
            plt.plot(self.measurements.Channels[i].Time.data, self.measurements.Channels[i].data)
            plt.title(self.title+"\n"+self.measurements.Channels[i].Name+" measurement - Full section")
            plt.xticks(np.arange(min(self.measurements.Channels[i].Time.data), max(self.measurements.Channels[i].Time.data) + 1, 5.0))
            plt.xlabel("Time [s]")
            plt.ylabel(self.measurements.Channels[i].unit)
            if self.measurements.Channels[i].Name != "Wave":
                plt.axvline(self.starttimes, ls="dotted", c="green", label="Data start")
                plt.axvline(self.endtimes, ls="dotted", c="red", label="Data end")
                plt.hlines(y=self.means[self.measurements.Channels[i].Name+" - Mean"], xmin=self.starttimes, xmax=self.endtimes, colors="red", label="Mean value \n ={} {}".format(round(self.means[self.measurements.Channels[i].Name+" - Mean"],2), self.measurements.Channels[i].unit))
                plt.legend(loc='upper right', bbox_to_anchor=(1.1, 1.05), fancybox=True, shadow=True)
            plt.savefig(towing_results+self.filename.replace(".BIN", "")+self.measurements.Channels[i].Name+"_full_measurement.png")
            if show_plots:
                plt.plot()
            else:
                plt.close("all")

    def plot_section_timeseries(self, plim):
        for i in range(1, self.measurements.numChannels):
            plt.plot(self.measurements.Channels[i].Time.data[int(self.starttimes*sampling_freq):int(self.endtimes*sampling_freq)], self.measurements.Channels[i].data[int(self.starttimes*sampling_freq):int(self.endtimes*sampling_freq)])
            plt.title(self.title+"\n"+self.measurements.Channels[i].Name+" measurement - Utilized section")
            plt.xlabel("Time [s]")
            plt.ylabel(self.measurements.Channels[i].unit)
            if self.measurements.Channels[i].Name != "Wave":
                mean = np.mean(self.measurements.Channels[i].data[int(self.starttimes*sampling_freq):int(self.endtimes*sampling_freq)])
                std_dev = np.std(self.measurements.Channels[i].data[int(self.starttimes*sampling_freq):int(self.endtimes*sampling_freq)], ddof=1)
                plt.axhline(y=mean, label="Mean value \n ={} {}".format(round(self.means[self.measurements.Channels[i].Name+" - Mean"],2), self.measurements.Channels[i].unit), c="red")
                plt.axhline(y=mean+plim*std_dev, ls="dotted", c="green", label=r'{}$\cdot \sigma$'.format(plim))
                plt.axhline(y=mean - plim * std_dev, ls="dotted", c="green")
                plt.legend(loc='upper right', bbox_to_anchor=(1.1, 1.05), fancybox=True, shadow=True)
            plt.tight_layout()

            plt.savefig(towing_results+self.filename.replace(".BIN", "")+self.measurements.Channels[i].Name+"_valid_section.png")
            if show_plots:
                plt.plot()
            else:
                plt.close("all")
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
                f.write("Std.dev: {}\n".format(std_dev))
                f.write("\n -------------------\n")


def holtrop(Vvec, T, B, L, S, CP, CM, CB, lcb, CW, voldispl, Abt, Tf, hb, At, H, Cstern):
    # Function for estimating ship resistance using Holtrops empirical method.
    # Output is given as a matrix where columns 1,2 and 3 give velocity,
    # resistance and power requirement (without accounting for propeller
    # efficiency) respectively.
    ## Input explanation
    # Vvec: Velocity vector (m/s). Something like this:[9.8,10,11,12,13,13.5]
    # T: Draught at AP
    # B: Beam
    # L: Length of waterline
    # S: Wetted surface of hull
    # CP: Prismatic coefficient
    # CM: Midship section coefficient
    # CB: Block coefficient
    # lcb: Longitudinal center of buoyancy measured from 0.5L as percentage of L
    # CW: Waterplane area coefficient
    # voldispl: Displaced volume [m^3]
    # Abt: Transverse bulb area
    # Tf: Draught at FP
    # hb: Distance of bulb centre of volume from baseline
    # At: Area of submerged transom stern
    # H: Roughness height [micrometer]
    # Stern type indicator:
    # Cstern = -25: Pram with gondola
    # Cstern = -10: V-shaped sections
    # Cstern = 0  : Normal section shape. This can be assumed to be the case here
    # Cstern = 10 : U-shaped sections with Hogner stern

    # Constants
    g = 9.81  # Gravity
    rho = 1025  # Density seawater
    kinvisc = 1.883 * 10 ** -6  # Kinetic viscosity

    # Values valid for all velocities - USED IN WAVE MAKING RESISTANCE
    # CALCULATION
    # "Length of run"
    LR = L * (1 - CP + 0.06 * CP * lcb / (4 * CP - 1))
    iE = 1 + 89 * np.exp(
        -(L / B) ** 0.80856 * (1 - CW) ** 0.30484 * (1 - CP - 0.0225 * lcb) ** 0.6367 * (LR / B) ** 0.34574 * (
                    100 * voldispl / L ** 3) ** 0.16302)
    c3 = 0.56 * Abt ** 1.5 / (B * T * (0.31 * np.sqrt(Abt) + Tf - hb))
    c2 = np.exp(-1.89 * np.sqrt(c3))
    c5 = 1 - 0.8 * At / (B * T * CM)
    if L ** 3 / voldispl < 512:
        c15 = -1.69385
    elif L ** 3 / voldispl < 1726.91:
        c15 = -1.69385 + (L / voldispl ** (1 / 3) - 8) / 2.36
    else:
        c15 = 0

    # c7
    if B / L < 0.11:
        c7 = 0.229577 * (B / L) ** 0.33333
    elif B / L < 0.25:
        c7 = B / L
    else:
        c7 = 0.5 - 0.0625 * L / B

    # c1
    c1 = 2223105 * c7 ** 3.78613 * (T / B) ** 1.07961 * (90 - iE) ** -1.37565

    # c16
    if CP < 0.8:
        c16 = 8.07981 * CP - 13.8673 * CP ** 2 + 6.984388 * CP ** 3
    else:
        c16 = 1.73014 - 0.7067 * CP

    m1 = 0.0140407 * L / T - 1.75254 * voldispl ** (1 / 3) / L - 4.79323 * B / L - c16
    d = -0.9
    c17 = 6919.3 * CM ** -1.3346 * (voldispl / L ** 3) ** 2.00977 * (L / B - 2) ** 1.40692
    m3 = -7.2035 * (B / L) ** 0.326869 * (T / B) ** 0.605375
    # Note that the 'lambda' keyword is used in Python to define anomynous functions (not relevant to this).
    # We will therefore use 'my_lambda' to represent the lambda-value.
    if L / B < 12:
        my_lambda = 1.446 * CP - 0.03 * L / B
    else:
        my_lambda = 1.446 * CP - 0.36

    # Correlation factor for resistance - mainly a roughness allowance here
    if Tf / L > 0.04:
        c4 = 0.04
    else:
        c4 = Tf / L
    CA = 0.006 * (L + 100) ** -0.16 - 0.00205 + 0.003 * np.sqrt(L / 7.5) * CB ** 4 * c2 * (0.04 - c4)
    ks = H * 10 ** -6
    if H > 150:
        CA = CA + (0.105 * ks ** (1 / 3) - 0.005579) / L ** (1 / 3)
    CA = 0

    # Preallocating vectors
    FnVec = np.zeros(Vvec.size)
    Rvec = np.zeros(Vvec.size)
    RWAVectorOuter = np.zeros(Vvec.size)
    CWAVector = np.zeros(Vvec.size)

    Vcounter = 0
    for V in Vvec:
        # WAVE MAKING RESISTANCE
        FnOrig = V / np.sqrt(g * L)
        FnVec[Vcounter] = FnOrig

        if FnOrig > 0.4 and FnOrig < 0.5:
            FnVecInner = np.array([0.4, 0.55])
        else:
            FnVecInner = np.array([FnOrig])

        RWAVectorInner = np.zeros(FnVecInner.size)
        FnCounter = 0
        for Fn in FnVecInner:
            m4 = c15 * 0.4 * np.exp(-0.034 * Fn ** -3.29)

            if Fn < 0.4:
                RWAVectorInner[FnCounter] = c1 * c2 * c5 * voldispl * rho * g * np.exp(
                    m1 * Fn ** d + m4 * np.cos(my_lambda * Fn ** (-2)))
            elif Fn > 0.5:
                RWAVectorInner[FnCounter] = c17 * c2 * c5 * voldispl * rho * g * np.exp(
                    m3 * Fn ** d + m4 * np.cos(my_lambda * Fn ** (-2)))

            FnCounter += 1

        if RWAVectorInner.size > 1:
            # This only happens if Fn is between 0.4 and 0.5. Then the first
            # entry in RWA is for Fn = 0.4 and the second is for Fn = 0.55
            RWA = RWAVectorInner[0] + (FnOrig - 0.4) * (RWAVectorInner[1] - RWAVectorInner[0]) / 1.5
        else:
            RWA = RWAVectorInner[0]

            RWAVectorOuter[Vcounter] = RWA

        # RESISTANCE DUE TO BULBOUS BOW
        PB = 0.56 * np.sqrt(Abt) / (T - 1.5 * hb)
        FNI = V / np.sqrt(rho * (Tf - hb - 0.25) * np.sqrt(Abt) + 0.15 * V ** 2)
        RB = 0.11 * np.exp(-3 * PB ** -2) * FNI ** 3 * Abt * 1.5 * rho * g / (1 + FNI ** 2)

        # RESISTANCE DUE TO TRANSOM STERN
        FNT = V / np.sqrt(2 * g * At / (B + B * CW))
        if FNT < 5:
            c6 = 0.2 * (1 - 0.2 * FNT)
        else:
            c6 = 0
        RTR = 1 / 2 * rho * V ** 2 * c6

        # FRICTIONAL RESISTANCE ON HULL
        # Estimated wetted surface:
        S_estimate = L * (2 * T + B) * np.sqrt(CM) * (
                    0.453 + 0.4425 * CB - 0.2862 * CM - 0.00346 * B / T + 0.3696 * CW) + 2.38 * Abt / CB
        S_estimate = S
        c14 = 1 + 0.011 * Cstern
        k = -1 + 0.93 + 0.487118 * c14 * (B / L) ** 1.06806 * (T / L) ** 0.46106 * (L / LR) ** 0.121563 * (
                    L ** 3 / voldispl) ** 0.36486 * (1 - CP) ** -0.604247

        Rn = V * L / kinvisc
        CF = 0.075 / (np.log10(Rn) - 2) ** 2
        # deltaCF = (111*(H*V)**0.21 - 404)*CF**2; # Not used in Holtrop. CA used instead

        RF = 1 / 2 * rho * V ** 2 * S_estimate * CF * (1 + k)

        # CORRELATION FACTOR RESISTANCE (Mainly roughness allowance)
        RA = 1 / 2 * rho * V ** 2 * S_estimate * CA

        # TOTAL RESISTANCE AT GIVEN SPEED
        Rvec[Vcounter] = RWA + RB + RF + RTR + RA

        CWAVector[Vcounter] = RWA / (1 / 2 * rho * V ** 2 * S)

        Vcounter += 1

    Pvec = np.multiply(Rvec,
                       Vvec)  # Propulsion power required for keeping the ship moving at the specific speed (without accounting for propeller losses)

    # Figure 1
    plt.figure()
    plt.plot(FnVec, CWAVector)
    ax = plt.gca()
    ax.set(xlabel='Froude Number', ylabel='CWA',
           title='Wave making resistance coefficient, Holtrops method')

    # Figure 2
    plt.figure()
    plt.plot(Vvec * 3600 / 1852, Rvec / 1000)
    ax = plt.gca()
    ax.set(xlabel='Velocity [knots]', ylabel='Resistance [kN]',
           title='Total Resistance, Holtrops method')

    plt.show()

    return np.array([Vvec, Rvec, Pvec])


def hollenbach(Vsvec, L, Lwl, Los, B, TF, TA, CB, S, Dp, NRud, NBrac, NBoss, NThr):
    ###########################################################
    #                    Hollenbach.py
    ###########################################################
    # Alle input er i SI enheter
    # Forklaring til noen utvalgte parametre:
    # Vvec: Velocity vector [m/s]. Something like this:[9.8,10,11,12,13,13.5]
    # L = Length between perpendiculars [m]
    # Lwl = Length of waterline [m]
    # Los = Length over Surface [m] (se kompendiet)
    # B = Beam [m]
    # TF = Dypgang ved FP [m]
    # TA = Dypgang ved AP [m]
    # CB = Block coefficient
    # S = Wetted surface of hull
    # Dp = Propelldiameter [m]
    # Nrud = Antall ror [-]
    # NBrac = Antall braketter [-]
    # NBoss = Antall propellboss [-]
    # NThr = Antall tunnelthrustere [-]

    # Output er en matrise der første kollonne er hastighetsverdiene man puttet
    # inn, og de neste kolonnene gir motstand og effektbehov for hver
    # hastighet.

    T = (TF + TA) / 2
    Fi = (CB / L) * ((B / 2) * (TF + TA)) ** 0.5
    k = 0.6 * Fi + 145 * Fi ** 3.5

    rho = 1025  # Density, seawater
    gravk = 9.81  # Gravity
    nu = 1.1395E-6  # Viscosity

    # Calculation of 'Froude length', Lfn:
    if Los / L < 1:
        Lfn = Los
    elif Los / L >= 1 and Los / L < 1.1:
        Lfn = L + 2 / 3 * (Los - L)
    elif Los / L >= 1.1:
        Lfn = 1.0667 * L

    ###########################################################
    # Constants from Hollenbachs paper:
    ###########################################################

    # 'Mean' resistance coefficients
    a = np.array([-0.3382, 0.8086, -6.0258, -3.5632, 9.4405, 0.0146, 0, 0, 0, 0])
    # a1 means a[0] and so on (Python arrays starts at 0)
    b = np.array([[-0.57424, 13.3893, 90.5960],
                  [4.6614, -39.721, -351.483],
                  [-1.14215, -12.3296, 459.254]])  # b12 means b[0,1]
    d = np.array([0.854, -1.228, 0.497])
    e = np.array([2.1701, -0.1602])
    f = np.array([0.17, 0.20, 0.60])
    g = np.array([0.642, -0.635, 0.150])

    # 'Minimum' resistance coefficients
    a_min = np.array([-0.3382, 0.8086, -6.0258, -3.5632, 0, 0, 0, 0, 0, 0])
    b_min = np.array([[-0.91424, 13.3893, 90.5960],
                      [4.6614, -39.721, -351.483],
                      [-1.14215, -12.3296, 459.254]])
    d_min = np.array([0, 0, 0])
    e_min = np.array([1, 0])
    f_min = np.array([0.17, 0.2, 0.6])
    g_min = np.array([0.614, -0.717, 0.261])

    # Preallocating vectors to later store results for plotting
    CFsvec = np.zeros(Vsvec.size)
    CRvec = np.zeros(Vsvec.size)
    C_Tsvec = np.zeros(Vsvec.size)
    R_T_meanvec = np.zeros(Vsvec.size)
    CR_minvec = np.zeros(Vsvec.size)
    C_Ts_minvec = np.zeros(Vsvec.size)
    R_T_minvec = np.zeros(Vsvec.size)
    P_E_meanvec = np.zeros(Vsvec.size)
    P_E_minvec = np.zeros(Vsvec.size)

    cc = 0
    # Loop over velocities
    for Vs in Vsvec:
        # Froude's number
        Fn = Vs / np.sqrt(gravk * Lfn)

        Fnkrit = np.dot(d, np.array([1, CB, CB ** 2]))
        c1 = Fn / Fnkrit
        c1_min = Fn / Fnkrit

        Rns = Vs * L / nu  # Reynold's number for ship
        CFs = 0.075 / (np.log10(Rns) - 2) ** 2  # ITTC friction line for ship

        # Calculation of C_R for given ship
        # Mean value

        CRFnkrit = np.max(np.array([[1.0], [(Fn / Fnkrit) ** c1]]))

        kL = e[0] * L ** e[1]

        # There is an error in the hollenbach paper and in Minsaas' 2003 textbook, which
        # is corrected in this formula by dividing by 10
        CRstandard = np.dot(np.array([1, CB, CB ** 2]), np.dot(b, np.array([1, Fn, Fn ** 2]) / 10))

        CR_hollenbach = CRstandard * CRFnkrit * kL * np.prod(
            np.array([T / B, B / L, Los / Lwl, Lwl / L, (1 + (TA - TF) / L),
                      Dp / TA, (1 + NRud), (1 + NBrac), (1 + NBoss), (1 + NThr)] ** a))

        CR = CR_hollenbach * B * T / S  # Resistance coefficient, scaled for wetted surface
        C_Ts = CFs + CR  # Total resistance coeff. ship
        R_T_mean = C_Ts * rho / 2 * Vs ** 2 * S  # Total resistance to the ship

        ###########################################################
        # Minimum values

        # There is an error in the hollenbach paper and in Minsaas' 2003 textbook, which
        # is corrected in this formula by dividing by 10
        CRstandard_min = np.dot(np.array([1, CB, CB ** 2]), np.dot(b_min, np.array([1, Fn, Fn ** 2])) / 10)

        CR_hollenbach_min = CRstandard_min * np.prod(np.array([T / B, B / L, Los / Lwl, Lwl / L, (1 + (TA - TF) / L),
                                                               Dp / TA, (1 + NRud), (1 + NBrac), (1 + NBoss),
                                                               (1 + NThr)] ** a_min))

        CR_min = CR_hollenbach_min * B * T / S

        # Total resistance coefficient of the ship
        C_Ts_min = CFs + CR_min
        # Total resistance
        R_T_min = C_Ts_min * rho / 2 * Vs ** 2 * S

        # Propulsion power
        P_E_mean = R_T_mean * Vs  # [W]
        P_E_min = R_T_min * Vs  # [W]


        # Store results for plotting
        CFsvec[cc] = CFs
        CRvec[cc] = CR
        C_Tsvec[cc] = C_Ts
        R_T_meanvec[cc] = R_T_mean
        CR_minvec[cc] = CR_min
        C_Ts_minvec[cc] = C_Ts_min
        R_T_minvec[cc] = R_T_min
        P_E_meanvec[cc] = P_E_mean
        P_E_minvec[cc] = P_E_min

        cc += 1


    return np.array([Vsvec, R_T_meanvec, R_T_minvec, CRvec, CR_minvec])


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