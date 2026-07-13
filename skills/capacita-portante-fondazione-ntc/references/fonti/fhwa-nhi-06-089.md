# Fonte: FHWA NHI-06-089 - Soils and Foundations, Reference Manual Volume II (dicembre 2006) - capacita' portante delle fondazioni superficiali

> Fonte: U.S. Department of Transportation - Federal Highway Administration,
> "Soils and Foundations - Reference Manual Volume II", Publication No. FHWA
> NHI-06-089, NHI Course No. 132012, dicembre 2006.
> URL ufficiale: https://www.fhwa.dot.gov/engineering/geotech/pubs/nhi06089.pdf
> File: `not_in_repo/fhwa-nhi-06-089.pdf`, SHA256 in `references/sources.yaml`
> (riproducibile, verificato con doppio download).
> Licenza: opera del Governo federale USA (pubblico dominio), come il Volume I
> della stessa pubblicazione.
> Ruolo nella skill: "altro codice internazionale" ai sensi del cap. 12 delle
> NTC 2018 (vedi trascrizione in `ntc2018-dm-17-01-2018.md`), per la
> formulazione del carico limite che le NTC e la Circolare non forniscono in
> forma chiusa.
> Trascrizione dei paragrafi rilevanti: 8.4.2 (equazione di capacita'
> portante, eq. 8-1..8-5, pagg. 8-18/8-19), 8.4.3 (forma generale con fattori
> correttivi, eq. 8-6, pag. 8-23), 8.4.3.1 (forma/eccentricita', eq. 8-7..8-9
> e Table 8-4, pagg. 8-24/8-27), 8.4.3.2 (falda, Table 8-5, pag. 8-27),
> 8.4.3.3 (approfondimento, Table 8-6, pag. 8-28). Equazioni rese in
> notazione piana fedele al PDF.

## Par. 8.4.2 - Bearing Capacity Equation Formulation (pagg. 8-18/8-19)

> For a concentrically loaded rigid strip footing with a rough base on a
> level homogeneous foundation material without the presence of water, the
> gross ultimate bearing capacity, qult, is expressed as follows (after
> Terzaghi, 1943):
>
> qult = c(Nc) + q(Nq) + 0.5 (gamma)(Bf)(Ngamma)   [8-1]
>
> ("Cohesion" term + "Surcharge" term + Foundation soil "Weight" term)
>
> where:
> c = cohesion of the soil (ksf) (kPa)
> q = total surcharge at the base of the footing = qappl + gamma_a*Df
>     (qappl = applied surcharge; gamma_a = unit weight of the overburden
>     material above the base of the footing causing the surcharge pressure)
> Df = depth of embedment
> gamma = unit weight of the soil under the footing
> Bf = footing width, i.e., least lateral dimension of the footing
>
> Nq = bearing capacity factor for the "surcharge" term (dimensionless)
>    = e^(pi*tan(phi)) * tan^2(45 deg + phi/2)   [8-2]
>
> Nc = bearing capacity factor for the "cohesion" term (dimensionless)
>    = (Nq - 1) * cot(phi)   for phi > 0 deg   [8-3]
>    = 2 + pi = 5.14         for phi = 0 deg   [8-4]
>
> Ngamma = bearing capacity factor for the "weight" term (dimensionless)
>        = 2 (Nq + 1) tan(phi)   [8-5]
>
> Many researchers proposed different expressions for the bearing capacity
> factors, Nc, Nq, and Ngamma. The expressions presented above are those
> used by AASHTO (2004 with 2006 Interims). These expressions are a function
> of the friction angle, phi. Table 8-1 can be used to estimate friction
> angle, phi, from corrected SPT N-value, N160, for cohesionless soils.
> Otherwise, the friction angle can be measured directly by laboratory tests
> or in situ testing. The values of Nc, Nq, and Ngamma as computed for
> various friction angles by Equations 8-3/8-4, 8-2, and 8-5, respectively
> are included in Table 8-1 and in Figure 8-15.

Cross-check con Table 8-2 (Bearing Capacity Factors, AASHTO 2004 with 2006
Interims), prime righe trascritte per verifica dei valori calcolati:

> phi = 0: Nc = 5.14, Nq = 1.0, Ngamma = 0.0
> phi = 1: Nc = 5.4, Nq = 1.1
> phi = 2: Nc = 5.6, Nq = 1.2
> [la tabella prosegue nel PDF fino a phi = 45+]

## Par. 8.4.3 - Bearing Capacity Correction Factors (pag. 8-23)

> Note that Equation 8-1 assumes a rigid strip footing with a rough base,
> loaded through its centroid, that is bearing on a level surface of
> homogeneous soil. Various correction factors have been proposed by
> numerous investigators to account for footing shape adjusted for
> eccentricity, location of the ground water table, embedment depth, sloping
> ground surface, an inclined base, the mode of shear, local or punching
> shear, and inclined loading. [...]
>
> The general form of the ultimate bearing capacity equation, including
> correction terms, is:
>
> qult = c*Nc*sc*bc + q*Nq*Cwq*sq*bq*dq + 0.5*gamma*Bf*Ngamma*Cwgamma*sgamma*bgamma   [8-6]
>
> where: sc, sgamma and sq are shape correction factors
> bc, bgamma and bq are base inclination correction factors
> Cwgamma and Cwq are groundwater correction factors
> dq is an embedment depth correction factor to account for the shearing
> resistance along the failure surface passing through cohesionless material
> above the bearing elevation. [...] Therefore, theoretically the "q" in the
> surcharge term should be replaced with (qa + gamma*Df*dq) where qa is
> defined as an applied surcharge for cases where applied surcharge is
> considered in the analysis;
> Nc, Nq and Ngamma are bearing capacity factors that are a function of the
> friction angle of the soil. [...]

## Par. 8.4.3.1 - Footing Shape (Eccentricity and Effective Dimensions) (pagg. 8-24/8-27)

> The general bearing capacity equation is applicable to strip footings,
> i.e., footings with Lf/Bf >= 10. Therefore, footing shape factors should
> be included in the equation for the ultimate bearing capacity for
> rectangular footings with Lf/Bf ratios less than 10.
>
> [...] Eccentricity is accounted for by distributing the non-uniform
> pressure distribution due to the eccentric load as an equivalent uniform
> pressure over an "effective area" that is smaller than the actual area of
> the original footing such that the point of application of the eccentric
> load passes through the centroid of the "effective area." The eccentricity
> correction is usually applied by reducing the width (Bf) and length (Lf)
> such that:
>
> B'f = Bf - 2 eB   [8-7]
> L'f = Lf - 2 eL   [8-8]
>
> where [...] eB and eL are the eccentricities in the Bf and Lf directions,
> respectively. These eccentricities are computed by dividing the applied
> moment in each direction by the applied vertical load. [...] When
> eccentric load occurs in both directions, the equivalent uniform bearing
> pressure is assumed to act over an effective fictitious area, A', where
> (AASHTO, 2004 with 2006 Interims):
>
> A' = B'f * L'f   [8-9]
>
> [...] The concept of equivalent footing and Meyerhof pressure is used for
> geotechnical analysis during sizing of the footing, i.e., bearing capacity
> and settlement analyses. However, the structural design of a footing
> should be performed using the actual trapezoidal or triangular pressure
> distributions [...]
>
> Limiting eccentricities are defined to ensure that zero contact pressure
> does not occur at any point beneath the footing. These limiting
> eccentricities vary for soil and rock. Footings founded on soil should be
> designed such that the eccentricity in any direction (eB or eL) is less
> than one-sixth (1/6) of the actual footing dimension in the same
> direction. For footings founded on rock, the eccentricity should be less
> than one-fourth (1/4) of the actual footing dimension. If the eccentricity
> does not exceed these limits, a separate calculation for stability with
> respect to overturning need not be performed. If eccentricity does exceed
> these limits, the footing should be resized.
>
> The shape correction factors are summarized in Table 8-4. For
> eccentrically loaded footings, AASHTO (2004 with 2006 Interims) recommends
> use of the effective footing dimensions, B'f and L'f, to compute the shape
> correction factors. [...]

Table 8-4 - Shape correction factors (AASHTO, 2004 with 2006 Interims):

> phi = 0:  sc = 1 + (Bf / (5*Lf));  sgamma = 1.0;  sq = 1.0
> phi > 0:  sc = 1 + (Bf/Lf)*(Nq/Nc);
>           sgamma = 1 - 0.4*(Bf/Lf);
>           sq = 1 + (Bf/Lf)*tan(phi)
> Note: Shape factors, s, should not be applied simultaneously with inclined
> loading factors, i. See Section 8.4.3.5.

## Par. 8.4.3.2 - Location of the Ground Water Table (pag. 8-27)

> If the ground water table is located within the potential failure zone
> above or below the base of a footing, buoyant (effective) unit weight
> should be used to compute the overburden pressure. A simplified method for
> accounting for the reduction in shearing resistance is to apply factors to
> the two terms in the bearing capacity equation that include a unit weight
> term. Recall that the cohesion term is neither a function of soil unit
> weight nor effective stress. The ground water factors may be computed by
> interpolating values between those provided in Table 8-5 (DW = depth to
> water from ground surface).

Table 8-5 - Correction factor for location of ground water table (AASHTO,
2004 with 2006 Interims):

> DW = 0:              Cwgamma = 0.5;  Cwq = 0.5
> DW = Df:             Cwgamma = 0.5;  Cwq = 1.0
> DW >= 1.5*Bf + Df:   Cwgamma = 1.0;  Cwq = 1.0
> Note: For intermediate positions of the ground water table, interpolate
> between the values shown above.

## Par. 8.4.3.3 - Embedment Depth (pag. 8-28)

> If the backfill or cover over the footing is known to be a high-quality,
> compacted granular material that can be assumed to remain in place over
> the life of the footing, additional shearing resistance due to the
> backfill can be accounted for by including in the surcharge term the
> embedment depth correction factor, dq, shown in Table 8-6. Otherwise, the
> depth correction factor can be conservatively omitted.

Table 8-6 - Depth correction factors (Hansen and Inan, 1970; AASHTO, 2004
with 2006 Interims); valori tabulati solo per phi = 32, 37, 42 gradi e
Df/Bf = 1, 2, 4, 8:

> phi = 32: dq = 1.20 (Df/Bf=1); 1.30 (2); 1.35 (4); 1.40 (8)
> phi = 37: dq = 1.20 (1); 1.25 (2); 1.30 (4); 1.35 (8)
> phi = 42: dq = 1.15 (1); 1.20 (2); 1.25 (4); 1.30 (8)
> Note: The depth correction factor should be used only when the soils above
> the footing bearing elevation are as competent as the soils beneath the
> footing level; otherwise, the depth correction factor should be taken
> as 1.0.

## Ambiti trattati nel manuale ma NON trascritti (fuori ambito della skill)

Par. 8.4.3.4 (base inclinata), 8.4.3.5 (carico inclinato), 8.4.3.6 (piano
campagna in pendenza, fattori Ncq/Ngamma_q), 8.4.3.7 (terreni stratificati),
8.4.5 (rottura locale/punzonamento), 8.4.8 (capacita' presuntive): la skill
li dichiara fuori ambito e rinvia al PDF ufficiale.
