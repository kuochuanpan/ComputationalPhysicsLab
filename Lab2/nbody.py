import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path
from numba import jit, njit, prange, set_num_threads

"""

This program solve 3D direct N-particles simulations 
under gravitational forces. 

This file contains two classes:

1) Particles: describes the particle properties
2) NbodySimulation: describes the simulation

Usage:

    Step 1: import necessary classes

    from nbody import Particles, NbodySimulation

    Step 2: Write your own initialization function

    
        def initialize(particles:Particles):
            ....
            ....
            particles.set_masses(mass)
            particles.set_positions(pos)
            particles.set_velocities(vel)
            particles.set_accelerations(acc)

            return particles

    Step 3: Initialize your particles.

        particles = Particles(N=100)
        initialize(particles)


    Step 4: Initial, setup and start the simulation

        simulation = Simulation(particles)
        simulation.setip(...)
        simulation.evolve(dt=0.001, tmax=10)


Author: Kuo-Chuan Pan, NTHU 2022.10.30
For the course, computational physics lab

"""

class Particles:
    """
    
    The Particles class handle all particle properties

    for the N-body simulation. 

    """
    def __init__(self,N:int=100):
        """
        Prepare memories for N particles

        :param N: number of particles.

        By default: particle properties include:
                nparticles: int. number of particles
                _masses: (N,1) mass of each particle
                _positions:  (N,3) x,y,z positions of each particle
                _velocities:  (N,3) vx, vy, vz velocities of each particle
                _accelerations:  (N,3) ax, ay, az accelerations of each partciel
                _tags:  (N)   tag of each particle
                _time: float. the simulation time 

        """
        # TODO:
        return

    def output(self,fn, time):
        """
        Write simulation data into a file named "fn"


        """
        mass = self._masses
        pos  = self._positions
        vel  = self._velocities
        acc  = self._accelerations
        tag  = self._tags
        header = """
                ----------------------------------------------------
                Data from a 3D direct N-body simulation. 

                rows are i-particle; 
                coumns are :mass, tag, x ,y, z, vx, vy, vz, ax, ay, az

                NTHU, Computational Physics Lab

                ----------------------------------------------------
                """
        header += "Time = {}".format(time)
        np.savetxt(fn,(tag[:],mass[:,0],pos[:,0],pos[:,1],pos[:,2],
                            vel[:,0],vel[:,1],vel[:,2],
                            acc[:,0],acc[:,1],acc[:,2]),header=header)

        return

class NbodySimulation:
    """
    
    The N-body Simulation class.
    
    """

    def __init__(self,particles:Particles):
        """
        Initialize the N-body simulation with given Particles.

        :param particles: A Particles class.  
        
        """

        # store the particle information
        self.nparticles = particles.nparticles
        self.particles  = particles

        # Store physical information
        self.time  = 0.0  # simulation time

        # Set the default numerical schemes and parameters
        self.setup()
        
        return

    def setup(self, G=1, 
                    rsoft=0.01, 
                    method="RK4", 
                    io_freq=10, 
                    io_title="particles",
                    io_screen=True,
                    visualized=False):
        """
        Customize the simulation enviroments.

        :param G: the graivtational constant
        :param rsoft: float, a soften length
        :param meothd: string, the numerical scheme
                       support "Euler", "RK2", and "RK4"

        :param io_freq: int, the frequency to outupt data.
                        io_freq <=0 for no output. 
        :param io_title: the output header
        :param io_screen: print message on screen or not.
        :param visualized: on the fly visualization or not. 
        
        """
        # TODO:
        return

    def evolve(self, dt:float=0.01, tmax:float=1):
        """

        Start to evolve the system

        :param dt: time step
        :param tmax: the finial time
        
        """
        # TODO:

        method = self.method
        if method=="Euler":
            _update_particles = self._update_particles_euler
        elif method=="RK2":
            _update_particles = self._update_particles_rk2
        elif method=="RK4":
            _update_particles = self._update_particles_rk4    
        else:
            print("No such update meothd", method)
            quit() 

        # prepare an output folder for lateron output
        io_folder = "data_"+self.io_title
        Path(io_folder).mkdir(parents=True, exist_ok=True)
        
        # ====================================================
        #
        # The main loop of the simulation
        #
        # =====================================================

        # TODO:

        print("Done!")
        return

    def _calculate_acceleration(self, mass, pos):
        """
        Calculate the acceleration.
        """
        # TODO:
        return acc

    def _update_particles_euler(self, dt, particles:Particles):
        # TODO:
        return particles

    def _update_particles_rk2(self, dt, particles:Particles):
        # TODO:
        return particles

    def _update_particles_rk4(self, dt, particles:Particles):
        # TODO:
        return particles


if __name__=='__main__':


    # test Particles() here
    particles = Particles(N=100)
    # test NbodySimulation(particles) here
    sim = NbodySimulation(particles=particles)
    print("Done")