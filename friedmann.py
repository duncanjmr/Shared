import numpy as np
import matplotlib.pyplot as plt
import tools
tls = tools.tools()

h0=69./(3.08*10**19)
om_m=0.308
om_l=0.692
om_r=10**-5

a1 = om_r/om_m
a2 = (om_m/om_l)**(1./3)

t1= a1**2/(2.*h0*np.sqrt(om_r))
t2 = 2./3*(a2**(3./2) - a1**(3./2))/(h0*np.sqrt(om_m)) + t1

sec_yr = 365*24*3600

ax = np.linspace(0,3*10**10*sec_yr,100)

ar = lambda t: np.sqrt(2*h0*np.sqrt(om_r)*t)
am = lambda t: (3./2*h0*np.sqrt(om_m)*(t-t1) + a1**(3./2))**(2./3)
al = lambda t: a2*np.exp(h0*np.sqrt(om_l)*(t-t2))

age = 1/(np.sqrt(om_l)*h0)*np.log(1/a2) + t2
print(age)

c=3*10**8
ac = lambda t: c*t/(c*age)

if False:
    plt.plot(ax/sec_yr, ar(ax),c="b")
    plt.plot(ax/sec_yr, am(ax),c="g")
    plt.plot(ax/sec_yr, al(ax),c="r")
    plt.ylim(0,1)
    plt.savefig(tls.picdir + 'test')
else:
    tau=np.linspace(0,11)
    t=10**tau*sec_yr
    alfr = np.log10(ar(t))
    alfm = np.log10(am(t))
    alfl = np.log10(al(t))
    alfc = np.log10(ac(t))

    plt.plot(tau,alfr)
    plt.plot(tau,alfm)
    plt.plot(tau, alfl)
    plt.plot(tau, alfc)
    tcmb = 3*10**5
    plt.plot([np.log10(tcmb)]*2, [min(alfr),1], ls="--", color="black", alpha=0.4)
    plt.savefig(tls.picdir+"logtest")


