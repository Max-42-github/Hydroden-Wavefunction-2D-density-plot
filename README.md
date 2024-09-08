#### Hydrogen Wavefunction and electron 2D density plots using Python

Solving the Schrödinger Equation for Hydrogen Atom Wavefunctions for spherical coordinate.

We get the following expression for the wavefunction $\psi$ :

$$\psi_{nlm}(r,\theta,\phi) = \sqrt{\left(\frac{2}{na}\right)^3 \frac{(n-l-1)!}{2n(n+l)!}} e^{-r/na}\left(\frac{2r}{na}\right)^3 [L_{n-l-1}^{2l+1}(2r/na)] Y_{l}^{m}(\theta,\phi)$$

where $n,l,m$ are the Quantum numbers.

Here we have plotted the above expression as a density plot.

Example : ![hydrogen_subplot (1)](https://github.com/user-attachments/assets/6080cd24-512e-4174-b3ef-caa4bfd8484d)


In the file "hydrogen_wavefunction.py" the wavefunction is calculated part by part. The evaluation is broken down as : 

* Radial component
* Angular component

Further the above parts are combined to get the *wavefunction* and then the *probability* is calculated from it.

Later, in the code there is section for setting the parameters where we can set the quantum numbers $n,m$ and Bohr Radius $a_0$ .


