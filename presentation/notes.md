# Comments/notes from defense practice talk

http://wps.prenhall.com/wps/media/objects/724/741576/Instructor_Resources/Chapter_05/Text_Images/FG05_02.JPG

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

## Regular meeting

- use vibrational frequency calculations to help understand CO2 solvation by ionic liquids
- a key part of this analysis was energy decomposition analysis
- outcomes: what to do in the future

# Overlap of basis functions/AOs/MOs with comparison to SAPT

## Ramos-Cordoba/Lambrecht 2011

> By imposing the condition that the molecular orbitals on fragment A have contributions only from the atomic orbitals on fragment A, the physical effect of charge transfer between the fragments is prohibited, as is the unphysical artifact of basis set superposition error.

> The principal limitation to bear in mind about the ALMO approximation is that it depends on the basis functions being well-localized to the fragments to which they belong. Accordingly, the ALMO approximation is ill-defined when the AO basis set is linearly dependent in the sense that (basis) functions on one fragment can represent those on another.

How to determine linear dependence? A set of vectors is linearly dependent if its determinant is zero. Since the determinant is non-zero only if a matrix is invertible, which requires all non-zero eigenvalues, a set of vectors is linearly dependent if one or more eigenvalues are nearly zero.

# Pauli repulsion

