import numpy as np
import matplotlib.pyplot as plt
import tools 
import time

tl =tools.tools()

G = 6.68*10**(-11)
pi = np.pi

h0 = 70./(3.1*10**19)

pcrit = 3*h0**2/(8*pi*G)

sec_yr = 3600*24*365
dadt = lambda x: x*h0* np.sqrt(om_m/(x**3) + om_r/(x**4) + om_l)
om_m=0.308
om_r=10**-5
om_l=0.692
a = [1.]
t = [0]
dt = 10**7 * sec_yr

while True:
    if 0:
        print(a[0], t[0])
        time.sleep(0.1)
    if a[0] < 0:
        break
    da = dadt(a[0]) * dt

    a = [a[0] - da] + a
    t = [t[0] - dt] + t

while t[-1] < t[0] * -1:
    if a[-1] < 0:
        break
    da = dadt(a[-1]) * dt

    a += [a[-1] + da]
    t += [t[-1] + dt]

T0 = 2.73
T = [np.log(T0/(n**4))/10 for n in a]

t_yr = [t[i]/sec_yr for i in range(len(t))]

t_now=0

plt.ylim(0,a[-1]*1.05)
plt.plot(t_yr,a)
plt.plot(t_yr,T)
plt.plot([t_now, t_now], [1,0], color= "black", ls="--", alpha=0.4)
plt.text(t_yr[0],1,"Age: " +str(round(-t_yr[0]/(10**9),4)) + " billion years")
plt.savefig(tl.cameraroll + "expansioncurve")
