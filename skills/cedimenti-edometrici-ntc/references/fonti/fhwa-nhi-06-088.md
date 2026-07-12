# Fonte: FHWA NHI-06-088 - Soils and Foundations, Reference Manual Volume I (dicembre 2006) - paragrafi sul cedimento di consolidazione primaria

> Fonte: U.S. Department of Transportation - Federal Highway Administration,
> "Soils and Foundations - Reference Manual Volume I", Publication No. FHWA
> NHI-06-088, NHI Course No. 132012, dicembre 2006, 462 pagine.
> URL ufficiale: https://www.fhwa.dot.gov/engineering/geotech/pubs/nhi06088.pdf
> File: `not_in_repo/fhwa-nhi-06-088.pdf`, SHA256 in `references/sources.yaml`
> (riproducibile, verificato con doppio download).
> Licenza: opera del Governo federale USA; la Technical Report Documentation
> Page del documento riporta "No restrictions" alla voce distribuzione.
> Ruolo nella skill: "altro codice internazionale" ai sensi del cap. 12 delle
> NTC 2018 (vedi trascrizione in `ntc2018-dm-17-01-2018.md`), per la
> formulazione di calcolo del cedimento di consolidazione primaria che le NTC
> e la Circolare non forniscono in forma chiusa.
> Trascrizione dei paragrafi rilevanti: 7.5.2 (con 7.5.2.1, 7.5.2.2, 7.5.2.3,
> equazioni 7-2..7-7, pagg. 7-24/7-28) e 5.4.6.1 (correlazioni per Cc,
> pag. 5-33). Le equazioni sono rese in notazione piana fedele al PDF.

## Par. 7.5.2 - Computation of Primary Consolidation Settlements (pag. 7-24)

> Depending upon the magnitude of the existing effective stress relative to
> the maximum past effective stress at a given depth, in-situ soils can be
> considered normally consolidated, overconsolidated (preconsolidated), or
> underconsolidated. The behavior of in-situ soils to additional loads is
> highly dependent upon the stress history. The overconsolidation ratio,
> OCR, which is a measure of the degree of overconsolidation in a soil is
> defined as pc/po. The value of OCR provides a basis for determining the
> effective stress history of the clay at the time of the proposed loading
> as follows:
>
> - OCR = 1 - the clay is considered to be "normally consolidated" under the
>   existing load, i.e., the clay has fully consolidated under the existing
>   load (pc = po).
> - OCR > 1 - the clay is considered to be "overconsolidated" under the
>   existing load, i.e., the clay has consolidated under a load greater than
>   the load that currently exists (pc > po).
> - OCR < 1 - the clay is considered to be "underconsolidated" under the
>   existing load, i.e., consolidation under the existing load is still
>   occurring and will continue to occur under that load until primary
>   consolidation is complete, even if no additional load is applied
>   (pc < po).

## Par. 7.5.2.1 - Normally Consolidated Soils (pagg. 7-24/7-25)

> The settlement of a geotechnical feature or a structure resting on n
> layers of normally consolidated soils (pc = po) can be computed from
> Figure 7-10a where n is the number of layers into which the consolidating
> layer is divided:
>
> Sc = somma_su_n [ Cc/(1+eo) * Ho * log10(pf/po) ]   [7-2]
>
> where:
> Cc = compression index
> eo = initial void ratio
> Ho = layer thickness
> po = initial effective vertical stress at the center of layer n
> pf = po + delta_p = final effective vertical stress at the center of
>      layer n.
>
> The final effective vertical stress is computed by adding the stress
> change due to the applied load to the initial vertical effective stress.
> The total settlement will be the sum of the compressions of the n layers
> of soil.
>
> Normally the slope of the virgin portion of the e-log p curve is
> determined from the corrected one-dimensional consolidation curve measured
> on specimens taken from each relevant soil in the stratigraphic profile.
> The procedure for determining the corrected curve is presented in
> Table 7-6a. Common correlations for estimating Cc were presented in
> Section 5.4.6.1 of Chapter 5 and can be used to check laboratory results.
>
> Sometimes the consolidation data is presented in terms of vertical strain
> (epsilon_v) instead of void ratio. In this case the slope of the virgin
> portion of the modified consolidation curve is called the modified
> compression index and is denoted as Cc_eps [...]. Settlement is computed
> by using Equation 7-3 for normally consolidated soils where all of the
> other terms are defined as for Equation 7-2.
>
> Sc = somma_su_n [ Ho * Cc_eps * log10(pf/po) ]   [7-3]
>
> By comparing Equations 7-2 and 7-3, it can be seen that
> Cc_eps = Cc / (1+eo)

## Par. 7.5.2.2 - Overconsolidated (Preconsolidated) Soils (pagg. 7-26/7-27)

> If the water content of a clay layer below the water table is closer to
> the plastic limit than the liquid limit, the soil is likely
> overconsolidated, i.e., OCR > 1. [...]
> As a result of preconsolidation, the field state of stress will reside on
> the initially flat portion of the e-log p curve. Figures 7-11a and 7-11b
> illustrate the case where a load increment, delta_p, is added so that the
> final stress, pf, is greater than the maximum past effective stress, pc.
> For this condition, the settlements for the case of n layers of
> overconsolidated soils will be computed from Equation 7-4 or Equation 7-5
> that correspond to Figure 7-11a and 7-11b, respectively.
>
> S = somma_su_n [ Ho/(1+eo) * ( Cr * log10(pc/po) + Cc * log10(pf/pc) ) ]   [7-4]
>
> S = somma_su_n [ Ho * ( Cr_eps * log10(pc/po) + Cc_eps * log10(pf/pc) ) ]   [7-5]
>
> The total settlement is computed by summing the settlements computed from
> each subdivided compressible layer within the zone of influence (ZI). The
> assumption is made that the initial and final stress calculated at the
> center of each sublayer is representative of the average stress for the
> sublayer, and the material properties are reasonably constant within the
> sublayer. The sublayers are typically 5 ft (1.5 m) to 10 ft (3 m) thick in
> highway applications. In cases where the various stratigraphic layers
> represent combinations of both normally and overconsolidated soils, the
> settlement is computed by using the appropriate combinations of Equations
> 7-2 through 7-5.

(Nota di trascrizione: nelle equazioni 7-4/7-5 il PDF usa i simboli Cr e
Cr_eps per il ramo di ricompressione e Cc/Cc_eps per il ramo vergine, con i
pedici resi qui in notazione piana. Le equazioni 7-4/7-5 sono formulate dal
manuale per il caso pf > pc; il caso pf <= pc non e' oggetto di
un'equazione numerata in questo paragrafo.)

## Par. 7.5.2.3 - Underconsolidated Soils (pagg. 7-27/7-28)

> Underconsolidation is the term used to describe the effective stress state
> of a soil that has not fully consolidated under an existing load, i.e.,
> OCR < 1. Consolidation settlement due to the existing load will continue
> to occur under that load until primary consolidation is complete, even if
> no additional load is applied. This condition is shown in Figure 7-12 by
> delta_po. Therefore, any additional load increment, delta_p, would have to
> be added to po. Consequently, if the soil is not recognized as being
> underconsolidated, the actual total primary settlement due to
> delta_po + delta_p will be greater than the primary settlement computed
> for an additional load delta_p only, i.e., the settlement may be
> under-predicted. As a result of under-consolidation, the field state of
> stress will reside entirely on the virgin portion of the consolidation
> curve as shown in Figure 7-12. The settlements for the case of n layers of
> under-consolidated soils are computed by Equation 7-6 or Equation 7-7 that
> correspond to Figure 7-12a and 7-12b, respectively.
>
> S = somma_su_n [ Ho/(1+eo) * ( Cc * log10(po/pc) + Cc * log10(pf/po) ) ]   [7-6]
>
> S = somma_su_n [ Ho * ( Cc_eps * log10(po/pc) + Cc_eps * log10(pf/po) ) ]   [7-7]

(Nota di trascrizione: nel caso sottoconsolidato pc < po; il primo termine
rappresenta la consolidazione ancora in corso sotto il carico esistente, il
secondo quella dovuta all'incremento delta_p; entrambi sul ramo vergine Cc.)

## Par. 5.4.6.1 - Compression Index, Cc (pag. 5-33)

> Over 70 different equations have been published for correlating Cc with
> the index properties of clays. Table 5-5 lists some of the more useful
> correlations. [...] Note that the coordinates in Figure 5-9 are both
> logarithmic so that values of Cc can vary by as much as a factor of 5 with
> respect to the average trend line in these empirical correlations. Values
> of Cc obtained from Table 5-5 or Figure 5-9 should not be used for final
> design.
>
> Table 5-5 - Correlations for Cc (modified after Holtz and Kovacs, 1981):
> - Cc = 0.156 eo + 0.0107  (All Clays)
> - Cc ~= 0.5 Gs (PI/100)   (Inorganic, silt, silty clay)
> - Cc = 0.30 (eo - 0.27)   (Low plasticity clays)
> - Cc = 0.009 (LL - 10)    (Clay of medium to slight sensitivity, St < 4,
>                            LL < 100)
> - Cc = 0.0115 wn          (Organic Soils, Peat)
> - Cc = 0.75 (eo - 0.50)
> (eo = initial void ratio, PI = Plasticity Index, LL = Liquid Limit,
>  St = sensitivity, wn = natural water content)

(La skill NON usa queste correlazioni per il calcolo: le riporta solo come
controllo d'ordine di grandezza dei valori di laboratorio, con l'avvertenza
del manuale "should not be used for final design".)
