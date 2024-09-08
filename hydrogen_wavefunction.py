'''

 Plotting Schrodinger Equation Solution for Hydrogen Atom. 

'''

import numpy as np 
import matplotlib.pyplot as plt 
import scipy.special as sp


def radial(n, l, r, a0):

	x_argument = ((2*r)/(n*a0))

	# Constant term

	const_term = (((2/(n * a0)) ** 3) * ((sp.factorial(n-l-1))/(2*n * (sp.factorial(n+l))))) ** (1/2)

	# Exponential term

	exp_term = np.exp((-r)/(n*a0))

	# laguerre term

	n_arg = n-l-1
	k_arg = (2*l) - 1 

	laguerre_term = (x_argument ** l) * (sp.assoc_laguerre(x_argument, n_arg, k_arg))


	radial_part = const_term * exp_term * laguerre_term

	return radial_part



def angular(m,l,theta,phi):

	# constant term

	const_term = (-1 ** m) * (((((2*l) + 1)/(4*np.pi)) * ((sp.factorial(l-m))/(sp.factorial(l+m)))) ** (1/2))

	# Legendre polynomial 

	cos_theta = np.cos(theta)

	legendre = sp.lpmv(m, l, cos_theta)

	# exponatial term


	'''
			 EXP PART IS MADE 1 CONSIDERING phi = 0, HERE BUT FOR OTHER VALUE IT NEED TO BE CONSIDERD.

	'''

	exp_term = 1

	angular_part = const_term * legendre * exp_term

	return angular_part


def wave_function(n,l,m,a0):

	# Evaluation grid

	grid_lim = 40
	grid_res = 1000

	X = np.linspace(-grid_lim,grid_lim,grid_res)
	Y = np.linspace(-grid_lim,grid_lim,grid_res)

	x,y = np.meshgrid(X,Y)
	#eps = 1 * (10**(-7))


	r = np.sqrt((x ** 2) + (y ** 2))
	theta = np.arctan(y/x)

	phi = 0

	radial_part = radial(n, l, r, a0)
	angular_part = angular(m, l ,theta, phi)

	psi = radial_part * angular_part

	return psi


def probablity(psi):

	probablity = abs(psi ** 2)

	return probablity



# Setting parameters

n = 4

fig = plt.figure(figsize = (7,7))

for l in range(0,n):
	

	m = 1
	a0 = 1


	psi = wave_function(n,l,m,a0) 
	sqrt_prob = np.sqrt(probablity(psi))
	prob = probablity(psi)


	# Ploting the results

	plt.style.use("dark_background")

	plt.rcParams['font.family'] = 'STIXGeneral'
	plt.rcParams['mathtext.fontset'] = 'stix'

	plt.subplot(1,3,l+1)
	plt.title(f'({n},{l},{m})')

	# Good color map = 'magma' , 'mako'

	image = plt.imshow(sqrt_prob.T, cmap = 'magma')


plt.colorbar()

plt.suptitle(f'Hydrogen Atom - Wave Function Probablity Density', size = 16)

plt.show()











