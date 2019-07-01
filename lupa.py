
import pint
import mpmath
from sympy.solvers import solve
from sympy import symbols, diff

#######################
# setup the equations #
#######################

\
         g, G, c, h, r, ri, rho, rS, drS, M, pi = \
symbols('g, G, c, h, r, ri, rho, rS, drS, M, pi')

def schwarzschildRadius(G, M, c):
	return 2*G*M / c**2

def surfaceGravity(G, M, r):
	return G*M / r**2

def hollowSphereMass(ra, ri, rho):
	return 4*pi/3 * (ra**3 - ri**3) * rho

solutions = solve([ \
		schwarzschildRadius(G, M, c) - rS, \
		surfaceGravity(G, M, r) - g, \
		r + h - rS \
		], [r, M, rS])

# solution 0 is with a minus where we don't want it
radius_formula = solutions[1][0]
mass_formula = solutions[1][1]

# sloutions 1 and 2 of this cubic equation are complex, we pick solution 0
inner_radius_formula = solve( hollowSphereMass(r, ri, rho) - M, ri )[0]

drS_over_dM = diff(schwarzschildRadius(G, M, c), M)
dM_over_dr = diff(hollowSphereMass(r, ri, rho), r)
r_tolerance = drS/drS_over_dM/dM_over_dr

#######################
# fill in the numbers #
#######################

# initialize pint and mpmath and force them to work together
ureg = pint.UnitRegistry()
def Q(magnitude, unit=None): # physical quantity
	return ureg.Quantity(mpmath.mp.mpf(magnitude), unit)

mpmath.mp.dps = 50
sqrt = lambda x:x**0.5
m = ureg.meter
s = ureg.second
kg = ureg.kilogram

g = Q('9.8', m/s**2)
G = Q('6.67408e-11', m**3/kg/s**2)
c = Q('299792458.0', m/s)
h = Q('2.0', m)
rho = Q('2800.0', kg/m**3)
pi = Q(mpmath.pi)
drS = Q('0.02', m)

r = eval(str(radius_formula))
print("outer radius:")
print("r =", radius_formula)
print("  =", r, "\n")

M = eval(str(mass_formula))
print("mass:")
print("M =", mass_formula)
print("  =", M, "\n")

print("average density:")
print("rho_avg =", M/(r**3 * 4*pi/3), "\n")

ri = eval(str(inner_radius_formula))
print("inner radius:")
print("ri =", inner_radius_formula)
print("   =", ri, "\n")

print("wall thickness:")
print("r-ri =", r-ri, "\n")

drS_over_dr = eval(str(drS_over_dM * dM_over_dr))
print("precision relationship:")
print("drS/dr =", drS_over_dM * dM_over_dr)
print("       =", drS_over_dr, "\n")

dr = eval(str(r_tolerance))
print("tolerance for outer radius:")
print("dr =", r_tolerance)
print("   =", dr)

