#libraries
import pandas as pd 
import numpy as np 
import scipy 
import math
import matplotlib
import matplotlib.pyplot as plt
from scipy.stats import mannwhitneyu as MW

# main body
def main():
    main_file = pd.read_csv(".\SkewedData.csv")
    output_file = open("Output_file.csv", "w")
    
    main_file.dropna(inplace = True)
    
    groups = main_file["Group"].unique()
    groups = sorted(groups)
    MW_Return(main_file, groups, output_file)
    
    baw_plot(main_file[["Group", "GPA"]], groups)
    return


#functions
    #data plotter
def baw_plot(data, groups):
    plot_data = []
    for i in groups:
        plot_data.append(data[data["Group"] == i]["GPA"])
    plt.boxplot(plot_data, vert = True, tick_labels = groups)
    plt.title("Whisker and Box Plot of Cohorts")
    plt.xlabel("Cohort")
    plt.ylabel("GPA Distribution")
    plt.ylim([0, 5])
    plt.savefig("BAWP.tif")
    plt.clf
    return

    #data output
def MW_Return(data, groups, output_file):
    output_file.write("Subgroup")
    for i in range(0, len(groups)):
        output_file.write(f",{groups[i]}")
    output_file.write("\n")
    for i in range(0, len(groups)):
        output_file.write(f"{groups[i]}")
        for j in range(0, len(groups)):
            text = MW_tester(data, groups[i], groups[j])
            output_file.write(f",{text}")
        output_file.write("\n")
    return

    #mann whitney U-test
def MW_tester(data, groupA, groupB):
    dataA = data[data["Group"] == groupA]["GPA"]
    dataB = data[data["Group"] == groupB]["GPA"]
    if len(dataA) < 4 and len(dataB) < 4:
        return "Too small"
    else:
        u, p = MW(dataA, dataB)
    del dataA, dataB
    return p

main()