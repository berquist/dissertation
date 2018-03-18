# 1

Hi Dan,

During my practice talk yesterday morning, you asked me a question about "building up to the canonical result" that I don't remember. If you do, can you tell me again? Thank you.

Eric

# 2

Hi Eric,

During that part of the talk there were two things going on:

1. You were explaining what the data meant, and
2. I was trying to understand what was being presented.

While you might have explained what was going on, I was more focussed on understanding what each of the curves meant and trying to determine what the take-away message was. Since I missed the fact that the canonical curve differed from the other curves through the inclusion of CT in the wave function, I mistakenly thought that as the polarization analysis used more terms in the decomposition that it should reproduce the canonical result - I understand after the questions why there is a difference now.

However, my question was really about the difference between the (Ar->All) vs. (All-All) curves. In both the small and large basis sets it was shown that the Ar contribution was more important for CT, but I am not sure if this result can be inferred from the small basis set curves because you are basically showing that you get the wrong wave function w.r.t. changes in distance (the results differed from the canonical both qualitatively and quantitatively.)

So, to clear up my misunderstanding: Can the large CT contribution from Ar be known (as opposed to coincidence or error) if you do not know about the results from with a larger basis set?

Best Regards, Dan

# 3

Thanks for the detailed email. I don't think all parts of my answer will make it into the talk, because they aren't relevant, but here goes.

> mistakenly thought that as the polarization analysis used more terms in the decomposition that it should reproduce the canonical result

I was confused as to what you meant by "more terms in the decomposition". The way I understand it now is that you're referring to the additions after `ALMO frz + pol`, specifically `+ CT(Ar -> all)` and `+ CT(all -> all) [blocked]`, and that you do not get the canonical result for the reason you mentioned: the reference wavefunction is still SCFMI, and we cannot recover all the CT effects in just the response calculation alone to make up for the fact that CT is missing in SCFMI.

Hypothetically, if all CT effects could be recovered in CT-allowed response on top of a CT-disallowed reference, then `ALMO frz + pol + CT(all -> all) [blocked]` would be identical to the canonical result. However,

1. energies are a "one-step" result, it is only a matter of doing SCFMI or SCF, but any response calculation will be a "two-step" result, where we depend on both the reference (SCFMI or SCF) _and_ the formulation of the response equations, and
2. allowing CT during response on top of a SCFMI reference is not a physical result. I think it's possible to experimentally prepare a dimer where CT is not present, but I don't think it's then possible to simultaneously measure a spectroscopic observable while allowing CT.

As you probably know from standard ALMO-EDA for energies, the sum of all terms in the decomposition _does_ equal the exact interaction energy, but only if higher-order CT effects are included in the final term. That is, the perturbative Roothaan step approximation for CT is not exact, because you are still on the SCFMI/ALMO/pol PES. The full CT correction turns off the SCFMI projection and performs canonical SCF starting from SCFMI orbitals, which then converges to the canonical result.

Although it is unphysical, I find `ALMO frz + pol + CT(all -> all) [blocked]` interesting because it is somewhat like the RS approximation, since it gives you an idea of how much of the CT in the final result is from the wavefunction, and how much is from the molecular response.

> In both the small and large basis sets it was shown that the Ar contribution was more important for CT, but I am not sure if this result can be inferred from the small basis set curves because you are basically showing that you get the wrong wave function w.r.t. changes in distance (the results differed from the canonical both qualitatively and quantitatively.)

I think that here, the appropriate comparison is between `frz + pol`, `frz + pol + CT(Ar -> all)`, and `frz + pol + CT(all -> all) [blocked]`. The main conclusion you should draw from these three curves is that most of the CT in the response calculation comes from argon to lithium, and not from lithium to argon.

Then, if you separately compare `frz + pol + CT(all -> all) [blocked]` to the canonical result, you would see that allowing CT only during response is insufficient, as it fundamentally alters the underlying PES. The goal is not to recover or approximate the canonical result, but to further understand where the CT is coming from.

As stated above, `frz + pol + CT(all -> all) [blocked]` is not really physical, and I am probably of the minority opinion that it is valuable in terms of methodology rather than some physical result.

> Can the large CT contribution from Ar be known (as opposed to coincidence or error) if you do not know about the results from with a larger basis set?

I think the three curves that all start from the SCFMI reference in the small basis set tell you this. Please let me know if you disagree.

Oddly, the `+ CT(Ar -> all)` result in the larger basis set is slightly smaller than the `frz + pol` result, and I don't know why.

---

If you're interested, I'm going to give an updated and much shorter practice talk in 655 Chevron this coming Tuesday at 2 PM.

# 4

Dear Eric,

Thank you for the response. I'll certainly be there for your next practice talk.

You mentioned the following statement:

> As stated above, frz + pol + CT(all -> all) [blocked] is not really physical, and I am probably of the minority opinion that it is valuable in terms of methodology rather than some physical result.

I completely agree with this. For myself, I would just like to hear this as it would keep me from trying to understand the physical origin of any of the relevant results. But, I understand that the talk has to focus more on the science and not so much the methodology.

Best Regards, Dan
