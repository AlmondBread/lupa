# lupa
Computations for a Black Hole Planet

## Output
```
outer radius:
r = c*(c + sqrt(c**2 + 8*g*h))/(4*g)
  = 4585485605800091.9999999999999991276823560539639101 meter 

mass:
M = c**2*(c**2 + c*sqrt(c**2 + 8*g*h) + 4*g*h)/(8*G*g)
  = 3087488414310262985839492164356267830172847.7937663 kilogram 

average density:
rho_avg = 0.0000076447048702226692250183450114952447478673725215432 kilogram / meter ** 3 

inner radius:
ri = 2**(1/3)*(-3*M/(pi*rho) + 4*r**3)**(1/3)/2
   = 4585485601626906.1098082312782251354808954586497216 meter 

wall thickness:
r-ri = 4173185.8901917687217739922014605953141885168603177 meter 

precision relationship:
drS/dr = 8*G*pi*r**2*rho/c**2
       = 1098799776.1325395376750941861661534849144111717316 dimensionless 

tolerance for outer radius:
dr = c**2*drS/(8*G*pi*r**2*rho)
   = 0.000000000018201678262434918787411605913766764521441529612956 meter
```
