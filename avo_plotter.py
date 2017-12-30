import numpy as np
import matplotlib.pyplot as plt

#from bruges.reflection import reflection as avo
from bruges.reflection import reflection as avo


def test_1():
    vp1 = 12250.
    vp2 = 11600.
    vs1 = 6620.
    vs2 = 4050.
    rho1 = 2.66
    rho2 = 2.34

    min_theta = 0
    max_theta = 100
    step_theta = 1

    theta = np.arange(min_theta, max_theta, step_theta)

    ref = avo.zoeppritz_rpp(vp1, vs1, rho1, vp2, vs2, rho2, theta)

    plt.plot(theta, ref, label="AVO")
    plt.axis([min_theta, max_theta, -1, 1])
    plt.xlabel('Theta')
    plt.ylabel('Ref')

    plt.legend()
    plt.show()
"""
    print("theta: ", theta)
    print(" ")
    print("reflectivity: ", ref)
"""



if __name__ == '__main__':
    test_1()
