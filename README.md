**Wavepacket for an electron with no potential**

In this case, having a free electron with no potential energy, just it's kinetic energy, we define the energy the classic way.

$E=\frac{p^{2}}{2m}$

Now, using the quantum operators for momentum and energy:

$\hat{p}=-i\hslash\frac{}{}\frac{\partial }{\partial x}$

$\hat{E}=i\hslash\frac{}{}\frac{\partial }{\partial t}$

and knowing that
$E\psi=H\psi$

So we have that, replacing the operators and putting in the last equation:

$H\psi=-\frac{\hslash^{2}}{2m}\frac{\partial^{2} }{\partial x^{2}}\psi$

$E\psi=i\hslash\frac{\partial }{\partial t}\psi$

$i\hslash\frac{\partial }{\partial t}\psi=-\frac{\hslash^{2}}{2m}\frac{\partial^{2} }{\partial x^{2}}\psi$

This $\psi$ is our wave function that describes our particle, we have to solve for this DE, the trick is to assume that the solution is a product between two other functions, one depending on time, and the other depending on space.

$\psi(x,t)=\psi(x)\phi(t)$

Ending up with the same expresions as above, but solving for just one variable and either $\psi$ or $\phi$

$E\psi=-\frac{\hslash^{2}}{2m}\frac{d^{2} }{d x^{2}}\psi$

$E\phi=i\hslash\frac{d}{dt}\phi$

**Let's solve first for our space funcion $\psi$**

Arranging, normalizing and making a change of variable

$\frac{\hslash^{2}}{2m}\frac{d^{2} }{d x^{2}}\psi + E\psi=0$

$\frac{d^{2} }{d x^{2}}\psi + \frac{2mE}{\hslash^{2}}\psi=0$

$k^{2}=\frac{2mE}{\hslash^{2}}$

And finally
$\frac{d^{2} }{d x^{2}}\psi + k^{2}\psi=0$

Solving for $\psi$ is easy, we end up with

$\psi(x)=Ae^{ikx}+Be^{-ikx}$

for $k>0$

We can just take,
$\psi(x)=Ae^{ikx}$

$k\in \Re$
This works since we will get the same functions just assuming that k can be any real number, and since our definition of k above is squared, we are not violating any physical restriction.

**For the time function we have**

$i\hslash\frac{d}{dt}\phi- E\phi=0$

$\frac{d}{dt}\phi- \frac{E}{i\hslash}\phi=0$

and solving, we have

$\phi(t)=\phi(0)e^{-i\frac{E}{\hslash}t}$

performing another sustitution, we end up with

$\phi(t)=\phi(0)e^{-iwt}$

$w=\frac{E}{\hslash}$

**Final Solution**

$\psi(x,t)=\psi(x)\phi(t)$

$\psi(x,t))=Ae^{ikx}e^{-iwt}$

We take the $\phi(0)$ out since we take A as the coeficient for the whole solution

$\psi(x,t)=Ae^{i(kx-wt)}$

note also that w can be written as a function of k, since

$E=\frac{\hslash^{2}k^{2}}{2m}$

$w=\frac{\hslash k^{2}}{2m}$

**$\psi(x,t)=Ae^{i(kx-w(k)t)}$**

**$k \in \Re$**

So we have an infinite amount of solutions for this, that depends on every k value, the coeficient A, will depend on the initial conditions of the particle.

**Wavepacket**

We have all solutions for our wave function, the thing is, all of the solutions describe the state of the particle, not just one, so we have to write the complete general solucion for the wave function.
since all our solutions 'eigenstates'depend of k, we can write the general solution as a combination of all posible k values,
giving this, also A, would depend of k, since it would be the corresponding coeficient for a k solution.

$\psi(x,t)=A(k)e^{i(kx-w(k)t)}dk$*

$\psi(x,t)=\frac{1}{\sqrt{2\pi}}\int_{\Re }^{}A(k)e^{i(kx-w(k)t)}dk$

Notice that we would have to give and infinite amount of numbers for A(k), we look for a more realistic way to determine our solution, and this is making use of the Fourier Transform

Basically, we are asking our state %\psi(x,0)% how much of each wave determined by its frecuency has.

$A(k) =\frac{1}{\sqrt{2\pi}}\int_{\Re}^{}\psi(x,0)e^{-ikx}dx$


Look that we just use t=0 as our initial condition for the solution, since it would be our begin of the experiment, if we build it just taking this 'initial photo of the particle' this would be enough to determine the solution for the particle.

So, we need a starting poing to the solution, it is often choosed as a normal distribution either of the value k or the position.




