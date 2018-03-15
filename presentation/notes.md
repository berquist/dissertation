# Comments/notes from defense practice talk

http://wps.prenhall.com/wps/media/objects/724/741576/Instructor_Resources/Chapter_05/Text_Images/FG05_02.JPG

## Shiv

Slide 8
- Title? "Ionic liquids" for CO2 capture
- Togo question - Why these? Water tolerant, fairly good CO2 capture already

Slide 11
- My question - how does this modeling help make better ionic liquids?

Slide 12
- Some labels?

Slide 13
- Pauli repulsion
- signs of terms

Slide 14
- <mu(0),mu(t)> autocorrelation function
- information about MD
- citation

Slide 15
- its unclear that you are getting intermediate wavefunctions and thus properties instead of just energy

Slide 20
- ALMO definition -> MO of only 1 fragment

Slide 23
- get rid of derivative table
- move other table forward?

## Dan

- Didn't understand Dan's question about "building up"

## Tom

- major spectroscopic challenge -- inhomogeneous environments
- **suggestion: assertion-evidence style**
- **give me more explanation on method**
- "not excited states, just looking at polarizability" -- this statement did not make sense to me
- What is an IL? What makes it useful?
- Why these ILs?
- "Screening" -- how long does it take to run your calculation?
- Suggest reordering slides to put some more method background first
- slide 16: method? basis? very unclear
- How did you do this? (ALMO EDA decomp) [you later went through this to some degree]
- What's a COVP?
- Did you ever define an ALMO?
- Do people know what a Linear Response is? 
- **What's the usefulness of being able to calculate any arbitrary linear response and decompose it like this?**

## Notebook

- green CO2 spectrum color is too light
- why these ILs? experimentally studied/validated
- switch from water dimer in ALMO-EDA example introduction with eqn/sums
- Pauli repulsion antisymmetry
- dipole-dipole ACS
- key statements on AIMD slide
- mention earlier this will be turned into frequency decomp
- overview slide
- How is the frequen decom done <- separate slide
- get rid of derivative table and move LR table earlier
- separate ALMO + canonical result
- plots on same scale
- long tail convergence slides <- move to main
- overlap of wavefunctions ALMO tails
- differentiation b/w model systems -> choice of model
- potential application _second_
- single message for each slide + orientation text
- building up to total understanding - CT in wfn, response
- table into bar graph
- is the formulation of LR(MI)
- group labels by value they converged to + split
- molecular understanding (?)

## Regular meeting

- quantum chemistry connects frequencies to structure
- can help those _who use_ screening
- desirable properties of ionic liquids -> solvation energy, reversible
- point out nomenclature...these are the example ILs studied
- put cluster on nu3 trend slide
- **Driving forces**
- Define ALMO
- Is within an SCF procedure
- _bar graph from water dimer_
- Differences b/w spectra due to CT, not electrostatics
    - importance for CT-dependent properties such as electrocatalysis
    - (dis)prove importance of electrostatics such as in Start spectroscopy
- E -> w -> <<P;Q>> after tables
- Empirical map for response property, determine importance of incorporating gd, pol, CT, disp, ...
- ~~Example: Static polarizability~~ Numerical benchmarks, mention _why_ static pol
    - **well, why static pol?**
    - _can compare to finite difference numerical derivatives_
    - static helps provide the connection between analytic derivatives and response theory
1. Confirm correctness before scientific results
   **branding** <- outcomes
2. r -> infty
3. Physics _introduced_ by model
- bar graph at equil. rather than table
- Epol, CT vs. basis set size
- **def2-SVPD only** not SVP, bar graph first then chart/plot
- start w/ abs of free, plus delta, plus delta, ...
- not trying to approach/approximate canonical result: trying to 
- "although written as a sum, not trying to..."

- use vibrational frequency calculations to help understand CO2 solvation by ionic liquids
- a key part of this analysis was energy decomposition analysis
- outcomes: what to do in the future

# Overlap of basis functions/AOs/MOs with comparison to SAPT

## Ramos-Cordoba/Lambrecht 2011

> By imposing the condition that the molecular orbitals on fragment A have contributions only from the atomic orbitals on fragment A, the physical effect of charge transfer between the fragments is prohibited, as is the unphysical artifact of basis set superposition error.

> The principal limitation to bear in mind about the ALMO approximation is that it depends on the basis functions being well-localized to the fragments to which they belong. Accordingly, the ALMO approximation is ill-defined when the AO basis set is linearly dependent in the sense that (basis) functions on one fragment can represent those on another.

How to determine linear dependence? A set of vectors is linearly dependent if its determinant is zero. Since the determinant is non-zero only if a matrix is invertible, which requires all non-zero eigenvalues, a set of vectors is linearly dependent if one or more eigenvalues are nearly zero.

# Pauli repulsion

