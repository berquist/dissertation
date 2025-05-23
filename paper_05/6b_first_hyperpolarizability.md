

```python
"""Tutorial: SCF first hyperpolarizability"""

__author__    = "Eric J. Berquist"
__credit__    = ["Eric J. Berquist"]

__copyright__ = "(c) 2014-2017, The Psi4NumPy Developers"
__license__   = "BSD-3-Clause"
__date__      = "2017-12-19"
```

# SCF First Hyperpolarizability

## Introduction

In Tutorial 6a, the calculation of linear response properties from analytic derivative theory is presented, the foundation of which are the coupled-perturbed Hartree-Fock (CPHF) or coupled-perturbed self-consistent field (CPSCF) equations. Starting from analytic derivative theory provides a convenient physical picture: how does the total energy of a system change under the influence of one or more internal or external perturbations? Continuing the case of an external electric field, the total energy of a system can be represented with a series expansion:

$$
E(\mathbf{E}) = \sum_{n=0}^{\infty} \frac{1}{n!}E^{(n)}(\mathbf{a})\cdot(\mathbf{E}-\mathbf{a})^{n},
$$

where the electric field is $\mathbf{E} = \vec{E} = (E_x,E_y,E_z)$ and $\mathbf{a}$ is the expansion point. In practice, we always expand around $\mathbf{a} = \mathbf{0}$, so it is a Maclaurin series:

$$
E(\mathbf{E}) = \sum_{n=0}^{\infty} \frac{1}{n!}\mathbf{E}^{(n)}(\mathbf{0})\cdot\mathbf{E}^{n}.
$$

Expanding the above to the first 4 explicit terms gives

$$
E(\mathbf{E}) \approx E^{(0)}(\mathbf{0}) + \mathbf{E}^{(1)}(\mathbf{0})\cdot\mathbf{E} + \frac{1}{2}\mathbf{E}^{(2)}(\mathbf{0})\cdot\mathbf{E}^{2} + \frac{1}{6}\mathbf{E}^{(3)}(\mathbf{0})\cdot\mathbf{E}^{3},
$$

where we identify

\begin{align}
E^{(0)} &\rightarrow \textrm{the unperturbed ground-state energy} \\
E_{a}^{(1)} &\rightarrow -\mu_{a},\textrm{the dipole moment} \\
E_{ab}^{(2)} &\rightarrow -\alpha_{ab},\textrm{the polarizability} \\
E_{abc}^{(3)} &\rightarrow -\beta_{abc},\textrm{the first hyperpolarizability}
\end{align}

The first hyperpolarizability is the leading-order term that describes the _nonlinear_ response of a system to an external electric field. Each term in the series expansion increases the rank of the coefficient by one: the ground-state energy is a scalar, the dipole is a length 3 vector, the polarizability is a 3-by-3 matrix, and the first hyperpolarizability is a 3-by-3-by-3 tensor.

Translated into the language of analytic derivative theory, is it represented as $\beta_{abc} = \left.\frac{\partial^{3} E}{\partial E_a \partial E_b \partial E_c}\right|_{\mathbf{E}=\mathbf{0}}$, though it is not yet clear how to take derivatives of the energy beyond what is presented in tutorial 6a. Additionally, nothing has been stated about time dependence; everything to this point has been the static case, where the strength of fields do not vary with time. We will first incorporate time dependence, and equations for derivative theory will result.

### Notation

Before going further, some notational conventions should be mentioned. When used as field indices, $a,b,c,\dots \in \{x,y,z\}$, the three Cartesian directions.

For matrix indices, $\mu,\nu,\lambda,\sigma,\dots$ label atomic orbitals (AOs)/basis functions, $i,j,k,l,\dots$ label occupied molecular orbitals (MOs), $a,b,c,d,\dots$ label unoccupied/virtual MOs, and $p,q,r,s,\dots$ label all MOs. Einstein summation is used, so repeated indices are contracted over.

## Derivation

Again, write the total Hamiltonian as the sum of unperturbed and perturbed components

\begin{align}
\hat{H}(\mathbf{E},t) &= \hat{H}^{(0)} + \hat{V}(\mathbf{E},t) \\
\hat{V}(\mathbf{E},t) &= -\mathbf{\mu} \cdot \mathbf{E}(e^{\pm i \omega t} + 1)
\end{align}

where part of the external field now oscillates with some characteristic frequency $\omega$. This can be incorporated into the time-dependent Schrodinger equation, which for a stationary state obeys

\begin{align}
\left[ \hat{H}^{(0)} + \hat{V}(\mathbf{E},t) - i\frac{\partial}{\partial t} \right] \psi(t) &= 0, \\
FC - i \frac{\partial}{\partial t} SC &= SC\epsilon, \\
\frac{\partial}{\partial t} C^{\dagger} S C &= 0,
\end{align}

where the full definition of the Fock matrix is

$$
F_{\mu\nu} = h_{\mu\nu} + D_{\lambda\sigma}[2J_{\mu\nu\lambda\sigma} - K_{\mu\nu\lambda\sigma}]
$$

and the density matrix is defined as

$$
D_{\mu\nu} = C_{\mu p}n_{pq}C_{\nu q}^{\dagger},
$$

where the diagonal occupation number matrix $n_{ii} = 2$ and $n_{aa} = 0$ for RHF.

In general, the MO coeffients are perturbation- and time-dependent, but the basis functions themselves are not. This means that when the series expansion for the perturbation above is performed on other quantities, only $F$, $C$, $\epsilon$, and $D$ are affected. For example, the Lagrangian multiplier matrix $\epsilon$ can be expanded as

$$
\epsilon(\mathbf{E}) = \epsilon^0 + E_a\epsilon^a + \frac{1}{2!}E_aE_b\epsilon^{ab} + \frac{1}{3!}E_aE_bE_c\epsilon^{abc} + \cdots
$$

where $a,b,c,...\in\{x,y,z\}$, and

\begin{align}
\epsilon^{a} &= e^{\pm i \omega t} \epsilon^{a}(\pm\omega) + \epsilon^{a}(0), \\
\epsilon^{ab} &= e^{\pm 2 i \omega t} \epsilon^{ab}(\pm\omega,\pm\omega) + e^{\pm i \omega t} \{ \epsilon^{ab}(0,\pm\omega) + \epsilon^{ab}(\pm\omega,0)\} + \epsilon^{ab}(\pm\omega,\mp\omega) + \epsilon^{ab}(0,0), \\
\epsilon^{abc} &= e^{\pm 3 i \omega t} \epsilon^{abc}(\pm\omega,\pm\omega,\pm\omega) + e^{\pm 2 i \omega t} \{\epsilon^{abc}(0,\pm\omega,\pm\omega) + \epsilon^{abc}(\pm\omega,0,\pm\omega) + \epsilon^{abc}(\pm\omega,\pm\omega,0)\} + e^{\pm i \omega t} \{\epsilon^{abc}(\pm\omega,\pm\omega,\mp\omega) + \epsilon^{abc}(\pm\omega,\mp\omega,\pm\omega) + \epsilon^{abc}(\mp\omega,\pm\omega,\pm\omega)\} + e^{\pm i \omega t} \{\epsilon^{abc}(0,0,\pm\omega) + \epsilon^{abc}(0,\pm\omega,0) + \epsilon^{abc}(\pm\omega,0,0)\} + \{\epsilon^{abc}(0,\pm\omega,\mp\omega) + \epsilon^{abc}(\pm\omega,0,\mp\omega) + \epsilon^{abc}(\pm\omega,\mp\omega,0)\} + \epsilon^{abc}(0,0,0),
\end{align}

showing that each order of the expansion consists of all possible phase combinations. For the first hyperpolarizability, only quantities with at most two field indices are required. Each permutationally unique subterm of the expansion corresponds to a different physical observable:

* $(0) \rightarrow$ static polarizability $\rightarrow \alpha(0;0) = -Tr[H^{a} D^{b}(0)]$
* $(\pm\omega) \rightarrow$ dynamic polarizability $\rightarrow \alpha(\mp\omega;\pm\omega) = -Tr[H^{a} D^{b}(\pm\omega)]$

* $(0,0) \rightarrow$ static (first) hyperpolarizability $\rightarrow \beta(0;0,0) = -Tr[H^{a} D^{bc}(0,0)]$
* $(0,\pm\omega) \rightarrow$ electrooptic Pockels effect (EOPE) $\rightarrow \beta(\mp \omega;0,\pm\omega) = -Tr[H^{a} D^{bc}(0,\pm\omega)]$
* $(\pm\omega,\pm\omega) \rightarrow$ second harmonic generation (SHG) $\rightarrow \beta(\mp 2\omega;\pm\omega,\pm\omega) = -Tr[H^{a} D^{bc}(\pm\omega,\pm\omega)]$
* $(\pm\omega,\mp\omega) \rightarrow$ optical rectification $\rightarrow \beta(0;\pm\omega,\mp\omega) = -Tr[H^{a} D^{bc}(\pm\omega,\mp\omega)]$

where each property is calculated as the trace over the AO-basis dipole matrices $H^{a}$ with the appropriate perturbed density. The task now comes down to calculating the necessary perturbed density for the phenomenon of interest. The second-order densities required for the four different first hyperpolarizabilities are (Karna eqs. III-2a to III-2d)

\begin{align}
D^{ab}(\pm\omega,\pm\omega) &= C^{ab}(\pm\omega,\pm\omega) n C^{0\dagger} + C^{a}(\pm\omega) n C^{b\dagger}(\mp\omega) + C^{b}(\pm\omega) n C^{a\dagger}(\mp\omega) + C^{0} n C^{ab\dagger}(\mp\omega,\mp\omega), \\
D^{ab}(0,\pm\omega) &= C^{ab}(0,\pm\omega) n C^{0\dagger} + C^{a}(0) n C^{b\dagger}(\mp\omega) + C^{b}(\pm\omega) n C^{a\dagger}(0) + C^{0} n C^{ab\dagger}(0,\mp\omega), \\
D^{ab}(\pm\omega,\mp\omega) &= C^{ab}(\pm\omega,\mp\omega) n C^{0\dagger} + C^{a}(\pm\omega) n C^{b\dagger}(\pm\omega) + C^{b}(\mp\omega) n C^{a\dagger}(\mp\omega) + C^{0} n C^{ab\dagger}(\mp\omega,\pm\omega), \\
D^{ab}(0,0) &= C^{ab}(0,0) n C^{0\dagger} + C^{a}(0) n C^{b\dagger}(0) + C^{b}(0) n C^{a\dagger}(0) + C^{0} n C^{ab\dagger}(0,0).
\end{align}

Already a few important insights about the equations are revealed: Each perturbation index always carries its respective frequency, and the positive and negative frequencies are related by the Hermitian adjoint (except for $C(-\omega) = -C^{0} U^{\dagger}(+\omega)$, Karna eq. 40). We also see the appearance of terms like $C^{ab}$, which will require $U^{ab}$ originating from the second-order CPHF. Computationally, this is undesirable due to the increased number of iterative calculations that must be performed, so we borrow a trick that most prominently appears in perturbation theory.

### Wigner's $2n + 1$ rule

From Schaefer, page 25:

> When the wavefunction is determined up to the $n$th order, the expectation value (electronic energy) of the the system is resolved, according to the results of perturbation theory, up to the $(2n+1)$st order. This principle is called Wigner's $2n+1$ theorem [29-31].

$$
\begin{array}{cccc}
\hline
 & \text{CI: MO/CI space} & \text{MCSCF: MO/CI space} & \text{RHF: MO space} \\
\hline
\text{Energy}, E & C_{\mu}^{i} , C_{I} & C_{\mu}^{i}, C_{I} & C_{\mu}^{i} \\
\text{First Derivative}, \frac{\partial E}{\partial a} & U^{a} , C_{I} & C_{\mu}^{i}, C_{I} & C_{\mu}^{i}\\
\text{Second Derivative}, \frac{\partial^{2} E}{\partial a \partial b} & U^{ab} , \frac{\partial C_{I}}{\partial a} & U^{a}, \frac{\partial C_{I}}{\partial a} & U^{a} \\
\text{Third Derivative}, \frac{\partial^{3} E}{\partial a \partial b \partial c} & U^{abc} , \frac{\partial C_{I}}{\partial a} & U^{a}, \frac{\partial C_{I}}{\partial a} & U^{a} \\
\text{Fourth Derivative}, \frac{\partial^{4} E}{\partial a \partial b \partial c \partial d} & U^{abcd} , \frac{\partial^{2} C_{I}}{\partial a \partial b} & U^{ab}, \frac{\partial^{2} C_{I}}{\partial a \partial b} & U^{ab} \\
\text{Fifth Derivative}, \frac{\partial^{5} E}{\partial a \partial b \partial c \partial d \partial e} & U^{abcde} , \frac{\partial^{2} C_{I}}{\partial a \partial b} & U^{ab}, \frac{\partial^{2} C_{I}}{\partial a \partial b} & U^{ab} \\
\hline
\end{array}
$$

Since the first hyperpolarizability is calculated as a third derivative of the energy, perturbed coefficients with only one field index should be required. From the above table, we can also see why SCF gradients ($\frac{\partial E}{\partial R_A}$, where $R_A$ is the $A$-th Cartesian component of nucleus $R$) avoid the need to solve for $U$ matrices.

## Final expressions

To this point, most work has been in the AO basis, but it is conceptually easier to work in the MO basis, in particular due to the use of the $\epsilon$ equations (Karna eq. 34)

$$
\epsilon^{a}(\pm\omega) = G^{a}(\pm\omega) + \epsilon^{0} U^{a}(\pm\omega) - U^{a}(\pm\omega) \epsilon^{0} \pm \omega U^{a}(\pm\omega),
$$

where the $G$ matrices are the MO-basis Fock matrices

$$
G^{ab\dots} = C^{0\dagger} F^{ab\dots} C^{0},
$$

and the $U$ matrices are the MO-basis perturbation parameters

$$
C^{ab\dots} = C^{0} U^{ab\dots},
$$

which will be discussed in the implementation. The final expression for the static hyperpolarizability is (Karna eq. VII-4)

$$
\beta_{abc}(0; 0, 0) = Tr[n \{  U^{a}(0) G^{b}(0) U^{c}(0) + U^{c}(0) G^{b}(0) U^{a}(0) + U^{b}(0) G^{c}(0) U^{a}(0) + U^{a}(0) G^{c}(0) U^{b}(0) + U^{c}(0) G^{a}(0) U^{b}(0) + U^{b}(0) G^{a}(0) U^{c}(0)\} ] - Tr[n \{ U^{a}(0) U^{c}(0) \epsilon^{b}(0) + U^{c}(0) U^{a}(0) \epsilon^{b}(0) + U^{b}(0) U^{a}(0) \epsilon^{c}(0) + U^{a}(0) U^{b}(0) \epsilon^{c}(0) + U^{c}(0) U^{b}(0) \epsilon^{a}(0) + U^{b}(0) U^{c}(0) \epsilon^{a}(0) \} ].
$$

By noticing that each term corresponds to a unique permutation of the field indices, it can be rewritten as

$$
\beta_{abc} = Tr\left[ n \sum \mathcal{P}(d,e,f) U^{d} G^{e} U^{f} \right] - Tr\left[ n \sum \mathcal{P}(d,e,f) U^{d} U^{e} \epsilon^{f} \right],
$$

where the permutation indices are initially assigned as $d = a, e = b, f = c$. The frequency notation has also been dropped, since each $abc$ (and therefore each $def$) will always carry the appropriate field index, making this the most general form of the first hyperpolarizability. If the indices $abc$ are also permuted, then all 27 components of the first hyperpolarizability tensor will be computed.

## Computational Procedure

The basic quantities we need are the matrices $C, \mu, F, \epsilon$, and $U$. The MO coefficients $C$ are already obtained from the ground-state calculation, along with $\epsilon^{0}$ (the MO energies) and $F^{0}$ (the AO-basis Fock matrix). The dipole matrices $\mu$ are needed for the linear response (polarizability) calculation, which results in response vectors that compose the off-diagonal blocks of the $U^{a}$ matrix. $G^{a}$ is obtained from $F^{a}$, which comes from performing a single Fock build with the perturbed density $D^{a}$. Finally, $\epsilon^{a}$ can be constructed.

Although the expressions so far are general for any frequency and first-order non-linear optical response, the tutorial implementation will cover the static case. For second-harmonic generation, see the reference implementation.


```python
import numpy as np
np.set_printoptions(3, linewidth=100, suppress=True)    # when we inspect the vectors/matrices,
                                                        # use a prettier format for printing
import psi4
```

The energy and density convergence criteria are tightened from defaults, as response properties are sensitive to the quality of the ground-state wavefunction.


```python
mol = psi4.geometry('''
    O
    H  1  0.9435
    H  1  0.9435  2  105.9443
    symmetry c1
''')
psi4.set_options({
    "basis": "aug-cc-pVDZ",
    "scf_type": "direct",
    "df_scf_guess": False,
    "e_convergence": 1e-9,
    "d_convergence": 1e-9,
})
```


```python
# This is to enable testing outside of the notebook environment.
import sys
try:
    get_ipython()
    sys.path.append('../../Response-Theory/Self-Consistent-Field')
except NameError:
    import os.path
    dirname = os.path.dirname(os.path.abspath(__file__))
    sys.path.append(os.path.join(dirname, '../../Response-Theory/Self-Consistent-Field'))

from helper_CPHF import helper_CPHF
```

The helper encapsulates the solution of the ground-state wavefunction followed by the frequency-(in)dependent linear response equations,

$$
\left[
\begin{pmatrix}
\mathbf{A} & \mathbf{B} \\
\mathbf{B}^{*} & \mathbf{A}^{*}
\end{pmatrix}
- \omega_{f}
\begin{pmatrix}
\mathbf{\Sigma} & \mathbf{\Delta} \\
-\mathbf{\Delta}^{*} & -\mathbf{\Sigma}^{*}
\end{pmatrix}
\right]
\begin{pmatrix}
\mathbf{X} \\
\mathbf{Y}
\end{pmatrix}
=
\begin{pmatrix}
\mathbf{V} \\
-\mathbf{V}^{*}
\end{pmatrix}
,
$$

either directly (via matrix inversion in the MO basis) or iteratively (via repeated matrix-vector products using Fock builds). For a HF/DFT reference with canonical orbitals, the above equations reduce to

$$
\left[
\begin{pmatrix}
\mathbf{A} & \mathbf{B} \\
\mathbf{B} & \mathbf{A}
\end{pmatrix}
- \omega_{f}
\begin{pmatrix}
\mathbf{1} & \mathbf{0} \\
\mathbf{0} & -\mathbf{1}
\end{pmatrix}
\right]
\begin{pmatrix}
\mathbf{X} \\
\mathbf{Y}
\end{pmatrix}
=
\begin{pmatrix}
\mathbf{V} \\
-\mathbf{V}
\end{pmatrix}
.
$$

In the static limit $(\omega_f = 0)$, the whole superoverlap matrix vanishes, and the CPHF equations can be reduced to those used in tutorial 6a.


```python
solver = helper_CPHF(mol)
solver.run()
```


    Number of occupied orbitals: 5
    Number of basis functions: 41

    Tensor sizes:
    ERI tensor           0.02 GB.
    oNNN MO tensor       0.00 GB.
    ovov Hessian tensor  0.00 GB.

    Forming Hessian...
    ...formed Hessian in 0.473 seconds.

    Inverting Hessian...
    ...inverted Hessian in 0.007 seconds.


Because the calculation of $\beta$ requires $U^{a}$, we also obtain linear response properties from a quadratic response calculation. This holds for any order of response, where lower-order response functions are automatically obtained from higher-order response calculations.


```python
print(np.around(solver.polar, 4))
```

    [[ 7.2587 -0.      0.    ]
     [-0.      8.7969  0.    ]
     [ 0.      0.      7.854 ]]



```python
# epsilon^{0}
moenergies = solver.epsilon
C = np.asarray(solver.C)
Co = solver.Co
Cv = solver.Cv
nbf, norb = C.shape
nocc = Co.shape[1]
nvir = norb - nocc
nov = nocc * nvir
# the response vectors X_x, X_y, X_z; Y_x, Y_y, Y_z not needed separately for static response
x = np.asarray(solver.x)
ncomp = x.shape[0]
# reuse the AO-basis dipole integrals
integrals_ao = np.asarray([np.asarray(dipole_ao_component)
                           for dipole_ao_component in solver.tmp_dipoles])
print("dimension of response vectors from linear response: {}".format(x.shape))
# for dynamic response, this will be (2 * nov)
assert x.shape[1] == nov
```

    dimension of response vectors from linear response: (3, 180)


The foundation of the CPHF equations is that the right-hand side $\mathbf{V}$ is a perturbation on the wavefunction causing single excitations from the occupied orbitals to virtual orbitals, the coefficents of which are in the response vectors $\mathbf{X}$; the vectors $\mathbf{Y}$ describe single deexcitations. Because the full (square) $\mathbf{U}$ matrices are required, all MO-based quantities must be of shape $[N_{orb}, N_{orb}]$ rather than $[N_{occ}, N_{vir}]$.


```python
# form full MO-basis dipole integrals
integrals_mo = np.empty(shape=(ncomp, norb, norb))
for i in range(ncomp):
    integrals_mo[i, ...] = (C.T).dot(integrals_ao[i, ...]).dot(C)
```

Similarly, $\mathbf{X}$ and $\mathbf{Y}$ form the off-diagonal blocks of the $\mathbf{U}$ matrices. They are usually stored as in DALTON, where each vector is of length $2N_{ov}$, with $\mathbf{X}$ on top of $\mathbf{Y}$.


```python
# repack response vectors to [norb, norb]; 1/2 is due to X + Y
U = np.zeros_like(integrals_mo)
for i in range(ncomp):
    U[i, :nocc, nocc:] = 0.5 * x[i, ...].reshape(nocc, nvir)
    U[i, nocc:, :nocc] = -0.5 * x[i, ...].reshape(nocc, nvir).T
```

A minor implementation detail: because this was not a frequency-dependent calculation, only $\mathbf{X}+\mathbf{Y}$ needs to be calculated; as they are identical, this leads to the prefactor of 1/2.


```python
# form G matrices from perturbation and generalized Fock matrices; do
# one more Fock build for each response vector
jk = psi4.core.JK.build(solver.scf_wfn.basisset())
jk.initialize()
G = np.empty_like(U)
R = psi4.core.Matrix(nbf, nocc)
npR = np.asarray(R)
for i in range(ncomp):
    V = integrals_mo[i, ...]

    # eqn. (III-1b)
    # Note: this simplified handling of the response vector
    # transformation for the Fock build is insufficient for
    # frequency-dependent response. 1/2 is due to X + Y
    jk.C_clear()
    L = Co
    npR[...] = x[i, ...].reshape(nocc, nvir).dot(np.asarray(Cv).T).T
    jk.C_left_add(L)
    jk.C_right_add(R)
    jk.compute()
    J = 0.5 * np.asarray(jk.J()[0])
    K = 0.5 * np.asarray(jk.K()[0])

    # eqn. (21b)
    F = (C.T).dot(4 * J - K.T - K).dot(C)
    G[i, ...] = V + F

# form epsilon matrices, eqn. (34)
E = G.copy()
omega = 0
for i in range(ncomp):
    eoU = (moenergies[..., np.newaxis] + omega) * U[i, ...]
    Ue = U[i, ...] * moenergies[np.newaxis, ...]
    E[i, ...] += (eoU - Ue)

# Assume some symmetry and calculate only part of the tensor.
# eqn. (VII-4)
hyperpolarizability = np.zeros(shape=(6, 3))
off1 = [0, 1, 2, 0, 0, 1]
off2 = [0, 1, 2, 1, 2, 2]
for r in range(6):
    b = off1[r]
    c = off2[r]
    for a in range(3):
        tl1 = 2 * np.trace(U[a, ...].dot(G[b, ...]).dot(U[c, ...])[:nocc, :nocc])
        tl2 = 2 * np.trace(U[a, ...].dot(G[c, ...]).dot(U[b, ...])[:nocc, :nocc])
        tl3 = 2 * np.trace(U[c, ...].dot(G[a, ...]).dot(U[b, ...])[:nocc, :nocc])
        tr1 = np.trace(U[c, ...].dot(U[b, ...]).dot(E[a, ...])[:nocc, :nocc])
        tr2 = np.trace(U[b, ...].dot(U[c, ...]).dot(E[a, ...])[:nocc, :nocc])
        tr3 = np.trace(U[c, ...].dot(U[a, ...]).dot(E[b, ...])[:nocc, :nocc])
        tr4 = np.trace(U[a, ...].dot(U[c, ...]).dot(E[b, ...])[:nocc, :nocc])
        tr5 = np.trace(U[b, ...].dot(U[a, ...]).dot(E[c, ...])[:nocc, :nocc])
        tr6 = np.trace(U[a, ...].dot(U[b, ...]).dot(E[c, ...])[:nocc, :nocc])
        tl = tl1 + tl2 + tl3
        tr = tr1 + tr2 + tr3 + tr4 + tr5 + tr6
        hyperpolarizability[r, a] = -2 * (tl - tr)
```


```python
ref_static = np.array([
    [ 0.00000001,   0.00000000,  -0.10826460],
    [ 0.00000000,   0.00000000, -11.22412215],
    [ 0.00000000,   0.00000000,  -4.36450397],
    [ 0.00000000,   0.00000000,  -0.00000001],
    [-0.10826460,  -0.00000001,   0.00000000],
    [-0.00000001, -11.22412215,   0.00000000]
])
assert np.allclose(ref_static, hyperpolarizability, rtol=0.0, atol=1.0e-3)
print('\nFirst dipole hyperpolarizability (static):')
print(hyperpolarizability)
```


    First dipole hyperpolarizability (static):
    [[ -0.       -0.       -0.10826]
     [ -0.       -0.      -11.22412]
     [ -0.       -0.       -4.3645 ]
     [ -0.       -0.        0.     ]
     [ -0.10826   0.       -0.     ]
     [  0.      -11.22412  -0.     ]]


## References

### Primary equations and implementation

* [Karna:1991:487][1]: Karna, Shashi P.; Dupuis, Michel. Frequency dependent nonlinear optical properties of molecules: Formulation and implementation in the HONDO program _J. Comput. Chem._ **12** 487-504 (1991)

### $2n + 1$ rule

* [Yamaguchi, Yukio; Goddard, John D.; Osamura, Yoshihiro; Schaefer III, Henry F. _A New Dimension to Quantum Chemistry: Analytic Derivative Methods in Ab Initio Molecular Electronic Structure Theory (International Series of Monographs on Chemistry);_ Oxford University Press: 1994.][2]
* [Epstein, Saul T. General Remainder Theorem _J. Chem. Phys._ **48** 4725 (1968)][3]
* [Epstein, Saul T. Constraints and the $V^{2n+1}$ theorem _Chem. Phys. Lett._ **70** 311 (1980)][4]

### Additional reading

* [Neese, Frank. Prediction of molecular properties and molecular spectroscopy with density functional theory: From fundamental theory to exchange-coupling _Coord. Chem. Rev._ **253** 526-563 (2009)][5]

  [1]: https://dx.doi.org/10.1002/jcc.540120409
  [2]: https://isbnsearch.org/isbn/9780195070286
  [3]: https://dx.doi.org/10.1063/1.1668053
  [4]: https://dx.doi.org/10.1016/0009-2614(80)85340-1
  [5]: https://dx.doi.org/10.1016/j.ccr.2008.05.014
