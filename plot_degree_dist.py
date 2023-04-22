import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit


G = []
maximum_degree = 0


def power_law(x, c, gamma):
    return c*np.power(x, -gamma)




def readData(filename):
    fileObj = open(filename)
    while True:
        line = fileObj.readline()
        if not line: break
        r = line.split(',')
        r2 = []
        for i in r[:-1]:
            r2.append(int(i))
        G.append(r2)




def degreeDistFunc(A):
    n = len(A)
    degree_dist_list = []

    for i in range(n):
        degree_dist_list.append(sum(A[i]))
    
    global maximum_degree
    maximum_degree = max(degree_dist_list)
    histogram = [0 for i in range(maximum_degree+1)]
    
    for i in degree_dist_list:
        histogram[i] += 1

    histogram = [i/n for i in histogram]

    return histogram
    



def plot_degree_dist(A):
    y=  degreeDistFunc(A)
    x = [i for i in range(maximum_degree+1)]

    x = np.array(x)
    y = np.array(y)

    params, cover = curve_fit(power_law, x, y)
    y_fit = power_law(x, params[0], params[1])
    
    fig, ax = plt.subplots(1,2, figsize=(10,4))

    ax[0].grid(True)
    ax[0].set_title('Degree Distribution')
    ax[0].set_xlabel('k')
    ax[0].set_ylabel('p(k)')
    ax[0].plot(x, y_fit, 'r-.', linewidth=2.0, label='fitted data')
    ax[0].plot(x, np.power(x, -3.), 'g-.', label='x^-3')
    ax[0].plot(x, y, 'k.', label='real data')
    ax[0].legend()

    ax[1].grid(True)
    ax[1].set_title('Degree Distribution in logarithmic scale')
    ax[1].set_xlabel('k')
    ax[1].set_ylabel('p(k)')
    ax[1].plot(np.log(x), np.log(y))
    ax[1].plot(np.log(x), np.log(np.power(x, -3.0)), 'g-.', label='log(x^-3)', linewidth=2.0)

    plt.show()



def count_zeros():
    c = 0
    for node in G:
        if sum(node)==0:
            c += 1
    print('\nnodes with degree 0:', c)
    print('maximum degree:', maximum_degree)




def main():
    readData('adj1000.txt')
    plot_degree_dist(G)
    count_zeros()

main()