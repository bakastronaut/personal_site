import numpy as np
import matplotlib.pyplot as plt

N = 500
n_max = 10
theta = np.complex(np.pi/2.25)
n1 = np.linspace(1,n_max,N).reshape(1,N)
n1 = np.vstack([n1 for _ in range(N)])
n2 = np.linspace(1,n_max,N).reshape(N,1)
n2 = np.hstack([n2 for _ in range(N)])

##theta_t = np.arcsin(n1*np.sin(theta_i)/n2)

a = np.cos(theta)
b = np.sqrt(1 - (n1/n2*np.sin(theta))**2)

R_s = np.abs( (n1*a - n2*b)/(n1*a + n2*b) )**2
R_p = np.abs( (n1*b - n2*a)/(n1*b + n2*a) )**2
R = 0.5*(R_s + R_p)

T_s = 1 - R_s
T_p = 1 - R_p
T = 0.5*(T_s + T_p)

ratio = R/T
ratio_masked = np.ma.masked_where(n1 >= n2,ratio)

fig0,ax0 = plt.subplots(1)
ax0.imshow(ratio_masked,cmap='viridis',origin='lower',extent=[1,n_max,1,n_max])
plt.show()

fig1,ax1 = plt.subplots(1)
ax1.imshow(R,cmap='viridis',origin='lower',extent=[1,n_max,1,n_max])
plt.show()
