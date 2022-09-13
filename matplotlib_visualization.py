import matplotlib.pyplot as plt




def plot_scale(scale, font=1, axesfont=1, axeslabel=1, xtick=1, ytick=1, legend=1, title=1):
    SMALL_SIZE = 12
    MEDIUM_SIZE = 14
    BIGGER_SIZE = 16

    plt.rc('font', size=SMALL_SIZE * scale * font)  # controls default text sizes
    plt.rc('axes', titlesize=SMALL_SIZE * scale * axesfont)  # fontsize of the axes title
    plt.rc('axes', labelsize=BIGGER_SIZE * scale * axeslabel)  # fontsize of the x and y labels
    plt.rc('xtick', labelsize=MEDIUM_SIZE * scale * xtick)  # fontsize of the tick labels
    plt.rc('ytick', labelsize=MEDIUM_SIZE * scale * ytick)  # fontsize of the tick labels
    plt.rc('legend', fontsize=MEDIUM_SIZE * scale * legend)  # legend fontsize
    plt.rc('figure', titlesize=BIGGER_SIZE * scale * title)  # fontsize of the figure title

