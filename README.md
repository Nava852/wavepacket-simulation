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

**Let's solve first for our space function $\psi$**

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

We have all solutions for our wave function, the thing is, all of the solutions describe the state of the particle, not just one, so we have to write the complete general solution for the wave function.
since all our solutions 'eigenstates'depend of k, we can write the general solution as a combination of all posible k values,
giving this, also A, would depend of k, since it would be the corresponding coeficient for a k solution.

$\psi(x,t)=A(k)e^{i(kx-w(k)t)}dk$*

$\psi(x,t)=\frac{1}{\sqrt{2\pi}}\int_{\Re }^{}A(k)e^{i(kx-w(k)t)}dk$

Notice that we would have to give and infinite amount of numbers for A(k), we look for a more realistic way to determine our solution, and this is making use of the Fourier Transform

Basically, we are asking our state $\psi(x,0)$ how much of each wave determined by its frecuency has.

$A(k) =\frac{1}{\sqrt{2\pi}}\int_{\Re}^{}\psi(x,0)e^{-ikx}dx$


Look that we just use t=0 as our initial condition for the solution, since it would be our begin of the experiment, if we build it just taking this 'initial photo of the particle' this would be enough to determine the solution for the particle.

So, we need a starting poing to the solution, it is often choosed as a normal distribution either of the value k or the position.


Here, is when the problems comes 'hard' to handle, since we have that our solution to this, are complex integrals under Fourier Transforms,

**Which solution fits best to this case?**

We generally have two options, the first one being taking a finite number of possible Ks, and then using FFT, so we would basically discretize our solution. And then we have an analytical way to solve it, which is often harder to get and calculate, but more precise. This also implies that, computationally, it is more expensive. In this case, we can adventure ourselves building it the analytical way, as we do not have a potential for the particle, and taking advantage of the fact that Gaussian forms under Fourier Transformations give us another Gaussian distribution.

So, out initial condition would be

$\psi(x,0)=Be^{-\frac{x^{2}}{4\sigma^{2}}}e^{ik_{0}x}$

where

$B =(2\pi\sigma^{2})^{-1/4}$


Putting in into $A(k)$, we end up with

$A(k) =\frac{1}{\sqrt{2\pi}}\int_{\Re}^{}Be^{-\frac{x^{2}}{4\sigma^{2}}}e^{ik_{0}x}e^{-ikx}dx$

$A(k) =\frac{B}{\sqrt{2\pi}}\int_{\Re}^{}e^{-\frac{x^{2}}{4\sigma^{2}}+i(k_{0}-k)x}dx$

This type of integrals can be solved with

$\int_{\Re}^{}e^{-(ax^{2}+bx)}dx=\sqrt{\frac{\pi}{a}}e^{\frac{b^{2}}{4a}}$

So,


$A(k) =\frac{B}{\sqrt{2\pi}}(2\sigma\sqrt{\pi})e^{-\sigma^{2}(k-k_{0})^{2}}$


Now, replacing in our wave equation

$\psi(x,t)=\frac{1}{\sqrt{2\pi}}\int_{\Re }^{}\frac{B}{\sqrt{2\pi}}(2\sigma\sqrt{\pi})e^{-\sigma^{2}(k-k_{0})^{2}}e^{i(kx-w(k)t)}dk$

$\psi(x,t)=\frac{B\sigma}{\sqrt{\pi}}\int_{\Re }^{}e^{-\sigma^{2}(k-k_{0})^{2}+i(kx-w(k)t)}dk$

Now we have to transform our integral to solve it as we did above.

$\int_{\Re}^{}e^{-(ax^{2}+bx+c)}dx=\sqrt{\frac{\pi}{a}}e^{\frac{b^{2}}{4a}-c}$

Ending with

$\psi(x,t)=\frac{B\sigma}{\sqrt{\pi}}\int_{\Re }^{}e^{-k^{2}(\sigma^{2}+\frac{i\hslash t}{2m})+k(2\sigma^{2}k_{0}+ix)-\sigma^{2}k_{0}^{2}}dk$

Now, solving and symplifing the most to end up with one exponential, we have.

$\psi(x,t)=\frac{B\sigma}{\sqrt{\sigma^{2}+\frac{i\hslash t}{2m}}}exp[\frac{(2\sigma^{2}k_{0}-ix)^{2}}{4(\sigma^{2}+\frac{i\hslash t}{2m})}-\sigma^{2}k_{0}^{2}]$

Let's make some use of three total variable sustitutions in order to make it look cleaner

$\psi(x,t)=\frac{B\sigma}{\sqrt{\alpha}}exp[\frac{\beta^{2}}{4\alpha}-\sigma^{2}k_{0}^{2}]$

where

$\alpha=\sigma^{2}+\frac{i\hslash t}{2m}$

$\beta=2\sigma^{2}k_{0}-ix$

$B =(2\pi\sigma^{2})^{-1/4}$


**The jump to the 3d simulation**

Since we are looking to simulate the cloud probability in $\Re^{3}$, we have to make some changes to our global solution, since it only works for one dimension $\Re$

We are going to take advantage of the fact that multiply exponentials is easy, and since every dimension would be independent each from the other, we use

$\psi(x,y,z,t)=\psi(x,t)\psi(y,t)\psi(z,t)$

Making some other arrangaments, we end up with

$\psi(x,y,z,t)=\frac{B^{3}\sigma^{3}}{\alpha^{\frac{3}{2}}}exp[\frac{\beta_{x}^{2}+\beta_{y}^{2}+\beta_{z}^{2}}{4\alpha}-3\sigma^{2}k_{0}^{2}]$

where

$\alpha=\sigma^{2}+\frac{i\hslash t}{2m}$

$\beta_{j}=2\sigma^{2}k_{0j}-ij$

$j=x,y,z$

$B =(2\pi\sigma^{2})^{-1/4}$


**Finnally, the probability of the particle given its position and time**

We need
$P(x,y,z,t)=|\psi(x,y,z,t)|^{2}$


We are dealing with a complex probability function, is not just squaring the wave function
we use

$|\psi(x,y,z,t)|^{2}=\psi\psi^{*}$



**Ending with**

$P(x,y,z,t)  = \frac{1}{(2\pi \sigma^2(t))^{3/2}} \exp \left[ -\frac{(x - v_{gx}t)^2 + (y - v_{gy}t)^2 + (z - v_{gz}t)^2}{2\sigma^2(t)} \right]$

Where
$v_{gj}=\frac{\hslash k_{0j}}{m}$

$j=x,y,z$

$\sigma(t) = \sigma \sqrt{1 + \left( \frac{\hbar t}{2m\sigma^2} \right)^2}$

this is our function to simulate or free electron travelling, now, we are left with determining our values of mass, standard deviation, and initial K. The config.py script, is open to change these values in order to have fun experimenting with the simulation


https://jobgether.com/offer/69dda6e2c646310ee38d9908-ai-data-quality-analyst

https://app.terminal.io/onboarding/sign-up

