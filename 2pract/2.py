#-- coding: utf-8 --
import math
x = -2.235*(10**-2)
y = 2.23
z = 15.221
c = (((math.exp(abs(x-y)))*((abs(x-y))**(x+y)))/(math.atan(x)+math.atan(z)))+(((x**6)+((math.log(y))**2))**(1/3))
print(c)

#-- coding: utf-8 --
import math
x = -4.5
y = 0.75*(10**-4)
z = -0.845*(10**2)
c = (((9+(((x-y))**2))**(1/3))/((x**2)+(y**2)+2))-(math.exp(abs(x-y)))*((math.tan(z))**3)
print(c)

#-- coding: utf-8 --
import math
x = 1.825*(10**2)
y = 18.225
z = -3.298*(10**-2)
c = (abs((x**(y/x))-((y/x)**(1/3))))+(y-x)*(((math.cos(y))-(z/(y-x)))/(1+((y-x)**2)))
print(c)