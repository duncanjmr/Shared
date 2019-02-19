from astropy import units as u

class constants:
    def __init__(self):
        self._load_constants()
        self.u = u

    def _load_constants(self):
        self.e = 2.71828
        self.pi = 3.1415
        
        self.k = 1.3807*10**-23 * u.kg *u.m**2 /(u.K * u.s**2)
        self.k_J = 1.3807*10**-23 * u.J / u.K
        self.k_ev = 8.617*10**-5 * u.eV / u.K
        
        self.h = 6.6261 * 10**-34 * u.kg * u.m**2 / u.s
        self.h_J = 6.6261 * 10**-34 * u.J * u.s

        self.c = 3*10**8 * u.m/u.s

        self.G = 6.67408 * 10**-11 * u.m**3 / (u.kg * u.s**2)
        
        
c = constants()
