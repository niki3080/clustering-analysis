import matplotlib.pyplot as plt
from cycler import cycler
import seaborn as sns


DIMRED = "#D31111"
TEXTCOLOR = "#333333"

COLOR = sns.color_palette("Blues")[1]
COLORLINE = sns.color_palette("Blues")[5]

MEANPROPS = {
    "marker": "o",
    "markeredgecolor": "red",
    "markerfacecolor": DIMRED,
    "markersize": 7,
}

BOXPLOT_STYLE = {
    "showmeans": True,
    "meanprops": MEANPROPS,
    "boxprops": {"edgecolor": "black", "linewidth": 0.5},
    "whiskerprops": {"color": "black", "linewidth": 0.5},
    "capprops": {"color": "black", "linewidth": 0.5},
    "medianprops": {"color": "black", "linewidth": 1},
    "flierprops": {
        "marker": "o",
        "markeredgecolor": "black",
        "markerfacecolor": "white",
        "markersize": 1,
        "alpha": 0.5,
    },
}

def apply_tab10_cycle():
    plt.rcParams.update({
        "axes.prop_cycle": cycler(color=plt.get_cmap("tab10").colors),
    })
