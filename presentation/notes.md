# Comments/notes from defense practice talk

http://wps.prenhall.com/wps/media/objects/724/741576/Instructor_Resources/Chapter_05/Text_Images/FG05_02.JPG

## Shiv

Slide 8
- [x] Title? "Ionic liquids" for CO2 capture
- [x] Togo question - Why these? Water tolerant, fairly good CO2 capture already

Slide 11
- [x] My question - how does this modeling help make better ionic liquids?

Slide 12
- [x] Some labels?

Slide 13
- [x] Pauli repulsion
- [x] signs of terms

Slide 14 (not going to include this at all)
- [x] <mu(0),mu(t)> autocorrelation function
- [x] information about MD
- [x] citation

Slide 15
- [x] its unclear that you are getting intermediate wavefunctions and thus properties instead of just energy

Slide 20
- [x] ALMO definition -> MO of only 1 fragment

Slide 23
- [x] get rid of derivative table
- [x] move other table forward?

## Dan

- [x] Didn't understand Dan's question about "building up"

## Tom

- [x] major spectroscopic challenge -- inhomogeneous environments
- [x] **suggestion: assertion-evidence style**
- [x] **give me more explanation on method**
- [x] "not excited states, just looking at polarizability" -- this statement did not make sense to me
- [x] What is an IL? What makes it useful?
- [x] Why these ILs?
- [x] "Screening" -- how long does it take to run your calculation?
- [x] Suggest reordering slides to put some more method background first
- [x] slide 16: method? basis? very unclear
- [x] How did you do this? (ALMO EDA decomp) [you later went through this to some degree]
- [x] What's a COVP?
- [x] Did you ever define an ALMO?
- [x] Do people know what a Linear Response is?
- [x] **What's the usefulness of being able to calculate any arbitrary linear response and decompose it like this?**

## Notebook

- [x] green CO2 spectrum color is too light
- [x] why these ILs? experimentally studied/validated
- [x] switch from water dimer in ALMO-EDA example introduction with eqn/sums
- [x] Pauli repulsion antisymmetry
- [x] dipole-dipole ACF
- [x] key statements on AIMD slide
- [x] mention earlier this will be turned into frequency decomp
- [x] overview slide
- [x] How is the frequen decom done <- separate slide
- [x] get rid of derivative table and move LR table earlier
- [x] separate ALMO + canonical result
- [ ] plots on same scale
- [x] long tail convergence slides <- move to main
- [x] overlap of wavefunctions ALMO tails
- [ ] differentiation b/w model systems -> choice of model
- [ ] potential application _second_
- [ ] single message for each slide + orientation text
- [ ] building up to total understanding - CT in wfn, response
- [ ] table into bar graph
- [ ] is the formulation of LR(MI)
- [ ] group labels by value they converged to + split
- [ ] molecular understanding (?)

## Regular meeting

- [x] quantum chemistry connects frequencies to structure
- [ ] can help those _who use_ screening
- [x] desirable properties of ionic liquids -> solvation energy, reversible
- [x] point out nomenclature...these are the example ILs studied
- [x] put cluster on nu3 trend slide
- [ ] **Driving forces**
- [ ] Define ALMO
- [ ] Is within an SCF procedure
- [ ] _bar graph from water dimer_
- [ ] Differences b/w spectra due to CT, not electrostatics
    - [ ] importance for CT-dependent properties such as electrocatalysis
    - [ ] (dis)prove importance of electrostatics such as in Start spectroscopy
- [x] E -> w -> <<P;Q>> after tables
- [ ] Empirical map for response property, determine importance of incorporating gd, pol, CT, disp, ...
- [x] ~~Example: Static polarizability~~ Numerical benchmarks, mention _why_ static pol
    - [x] **well, why static pol?**
    - [x] _can compare to finite difference numerical derivatives_
    - [x] static helps provide the connection between analytic derivatives and response theory
1. [x] Confirm correctness before scientific results
2. [x] r -> infty
3. [ ] Physics _introduced_ by model
- [ ] **branding** <- outcomes
- [ ] bar graph at equil. rather than table
- [ ] Epol, CT vs. basis set size
- [ ] **def2-SVPD only** not SVP, bar graph first then chart/plot
- [ ] start w/ abs of free, plus delta, plus delta, ...
- [ ] not trying to approach/approximate canonical result: trying to
- [ ] "although written as a sum, not trying to..."

- [ ] use vibrational frequency calculations to help understand CO2 solvation by ionic liquids
- [ ] a key part of this analysis was energy decomposition analysis
- [ ] outcomes: what to do in the future

# OneNote

## Context: CO2 solvation by ionic liquids

outline approach

spectra <-> MD <-> quantum
            ^
            |
            v
            molecular picture (Eint, rai, diff)

"Example of power of computational sim of spectra and more specifically decomposition"

## Lewis structures

_screening?_ for "optimal" ionic liquid
-> define figure(s) of merit
understanding, molecular picture

## expt. solvatochromic shift

define c4c1im again

## expt. vs calc.

encouraging initial results

1. box(spectrum) <-> box(MD traj.
                         RDF, vib, PES)
2. Now go deeper and learn about molecular interactions

## slide with electrocatalysis fig

_explain_

3-4 slides about CO2
punchlines
summary

# Comments/notes from defense practice talk 2

## Tom

Hi Eric,

By slide #

2. [x] "Goal_s_." [You listed multiple] Also, why do we generally care about decomposing spectra? Maybe a sentence or two (spoken) about the bigger picture could serve as motivation for your methods development.

3. [x] Watch the title of your spectroscopy slide. You're a little under-general with your definition.

5. [x] IL definition - include the "room temperature" part. NaCl is liquid at high enough temps. Some more motivation on why it is experimentally interesting to change the anion [I can send you refs if you want]

6. [x] related to (5). Why is the \nu_3 shift a metric of interest?

7. [x] Careful with your description of TFA. I don't know of any experimental evidence of chemisorption of CO2 by [bmim][TFA]. If you describe "chemisorption" -- know what reaction is thought to occur.

8. [x] "bottom up" [versus "top down"?] I wasn't entirely sure what you meant by this. Do you have an example of the comparison and why it's relevant?

9. [x] What do these COVP pictures mean? [we discussed] Frequencies don't match those on slide 7.

10. [ ] "Spectroscopic map" ... We miss some context here on the story.

16. [x] Able to apply to piezo systems [we discussed]? Be careful with description of Hessian. You said it was the curvature of the electronic surface of the molecule. You could get some confusion there.

17. [x] Did you attempt to reanalyze CO2 with this new method? [we discussed]

20. [x] Hard to tell colors apart. Be clear about the distinction between your two asymptotes.

24. [x] "Is available online" -- **you** put these online, right? The way you described it makes it sound like someone else already had them up. Use the active voice (even if it's 1st person plural "we placed these online ...")

Potential questions could come up about peer review of open source, and the validity of contributions from randos. For example, could Tom Brinzer go and make a bunch of contributions, polluting the repo with his dirty experimentalist's code?

Seems to be coming together, though what do I know. I'll be there on Friday. I'm going to have to leave immediately after your talk though, to drive cross state. Hopefully we can catch up sometime next week, and celebrate your successful defense.

Best,

Tom

### Response



# Overlap of basis functions/AOs/MOs with comparison to SAPT

## Ramos-Cordoba/Lambrecht 2011

> By imposing the condition that the molecular orbitals on fragment A have contributions only from the atomic orbitals on fragment A, the physical effect of charge transfer between the fragments is prohibited, as is the unphysical artifact of basis set superposition error.

> The principal limitation to bear in mind about the ALMO approximation is that it depends on the basis functions being well-localized to the fragments to which they belong. Accordingly, the ALMO approximation is ill-defined when the AO basis set is linearly dependent in the sense that (basis) functions on one fragment can represent those on another.

How to determine linear dependence? A set of vectors is linearly dependent if its determinant is zero. Since the determinant is non-zero only if a matrix is invertible, which requires all non-zero eigenvalues, a set of vectors is linearly dependent if one or more eigenvalues are nearly zero.

# Pauli repulsion
