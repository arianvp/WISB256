from scipy.integrate import odeint
import scipy
import numpy


class Lorenz:
    def __init__(self,state,sigma=10,rho=28,beta=(8/3)):
        self.state = state
        self.sigma = sigma
        self.rho = rho
        self.beta = beta

    def f(self, state, t):
        x,y,z = state

        return [self.sigma * (y-x), x * (self.rho-z)-y, x*y-self.beta*z]


    def solve(self,T,dt):
        return odeint(self.f, self.state, scipy.arange(0,T,dt))
