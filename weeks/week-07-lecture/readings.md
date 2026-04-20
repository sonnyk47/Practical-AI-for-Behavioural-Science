# Week 7 Readings: Clustering, Dimensionality Reduction, and the Structure of Psychopathology

> These readings support the Week 7 lecture on unsupervised learning. Start with the suggested readings — the optional ones go deeper on specific topics.

---

## Suggested Readings

### 1. James et al. (2023) — ISLP Chapter 12: Unsupervised Learning

James, G., Witten, D., Hastie, T., Tibshirani, R., & Taylor, J. (2023). *An introduction to statistical learning: With applications in Python*. Springer. https://doi.org/10.1007/978-3-031-38747-0

**Why read this:** Chapter 12 covers PCA, k-means clustering, and hierarchical clustering — exactly the methods we discuss in lecture. The explanations are accessible and include worked examples with Python code. This is the textbook companion to the lab material.

**Access:** Free PDF from the authors — [statlearning.com](https://www.statlearning.com/).

---

### 2. Haslam et al. (2020) — Dimensions over categories: A meta-analysis of taxometric research

Haslam, N., McGrath, M. J., Viechtbauer, W., & Kuppens, P. (2020). Dimensions over categories: A meta-analysis of taxometric research. *Psychological Medicine*, *50*(9), 1418–1432. https://doi.org/10.1017/S003329172000183X

**Why read this:** This meta-analysis of 317 taxometric findings concluded that dimensional models outnumber taxonic (categorical) models 5:1 across psychology. Directly relevant to the "types vs. dimensions" debate discussed in lecture — if most psychological constructs are dimensional, what does that mean for clustering approaches that impose categories on continuous data?

**Access:** Paywalled via Cambridge University Press. Author-hosted PDF freely available from [KU Leuven](https://ppw.kuleuven.be/okp/_pdf/Haslam2020DOCAM.pdf).

---

### 3. Jacobucci, Grimm, & Zhang (2023) — ML for social and behavioural research

Jacobucci, R., Grimm, K. J., & Zhang, Z. (2023). *Machine learning for social and behavioral research*. Guilford Press.

**Why read this:** The clustering and dimensionality reduction chapters are written specifically for behavioural science researchers, with psychology-relevant examples throughout. Bridges the gap between the technical methods and the interpretive frameworks familiar to psychology students.

**Access:** Paywalled (purchase from Guilford Press). Check Macquarie University library for access.

---

## Optional / Deeper Readings

### 4. Wattenberg, Viegas, & Johnson (2016) — How to use t-SNE effectively

Wattenberg, M., Viegas, F., & Johnson, I. (2016). How to use t-SNE effectively. *Distill*, *1*(10), e2. https://doi.org/10.23915/distill.00002

**Why read this:** An interactive, beginner-friendly guide to understanding and interpreting t-SNE (and by extension UMAP) visualisations. Covers common misreadings — over-interpreting cluster sizes, distances between groups, and shapes. The interactive figures let you experiment with different parameter settings and see how they change the output. Highly recommended before your Week 8 lab.

**Access:** Open access — [distill.pub/2016/misread-tsne](https://distill.pub/2016/misread-tsne/).

---

### 5. McInnes, Healy, & Melville (2018) — UMAP

McInnes, L., Healy, J., & Melville, J. (2018). *UMAP: Uniform Manifold Approximation and Projection for dimension reduction*. arXiv preprint arXiv:1802.03426. https://doi.org/10.48550/arXiv.1802.03426

**Why read this:** The original UMAP paper. More technical than the other readings, but the introduction and results sections are accessible. Explains why UMAP preserves local structure better than t-SNE while being much faster. Worth skimming even if you skip the mathematical details.

**Access:** Open access — [arxiv.org/abs/1802.03426](https://arxiv.org/abs/1802.03426).

---

### 6. Borsboom & Cramer (2013) — Network analysis and the structure of psychopathology

Borsboom, D., & Cramer, A. O. J. (2013). Network analysis: An integrative approach to the structure of psychopathology. *Annual Review of Clinical Psychology*, *9*, 91–121. https://doi.org/10.1146/annurev-clinpsy-050212-185608

**Why read this:** Introduces the network approach to psychopathology — the idea that symptoms cause each other rather than being caused by a latent disorder. Relevant to the lecture discussion of whether psychological constructs are categorical (types) or dimensional, and how clustering relates to these frameworks.

**Access:** Paywalled via Annual Reviews. Author-hosted PDF freely available from [psychosystems.org](https://www.psychosystems.org/files/Literature/borsboomcramerannualreview.pdf).

---

### 7. Drysdale et al. (2017) — Depression biotypes from brain connectivity

Drysdale, A. T., Grosenick, L., Downar, J., Dunlop, K., Mansouri, F., Meng, Y., Fetcho, R. N., Zebley, B., Oathes, D. J., Etkin, A., Schatzberg, A. F., Sudheimer, K., Keller, J., Mayberg, H. S., Gunning, F. M., Alexopoulos, G. S., Fox, M. D., Pascual-Leone, A., Voss, H. U., . . . Liston, C. (2017). Resting-state connectivity biomarkers define neurophysiological subtypes of depression. *Nature Medicine*, *23*(1), 28–38. https://doi.org/10.1038/nm.4246

**Why read this:** A high-profile example of using clustering (on brain connectivity data) to identify subtypes of depression. Found four "biotypes" that predicted treatment response. Demonstrates the promise and challenges of unsupervised learning in clinical neuroscience. Note: a subsequent replication attempt raised methodological concerns — a useful reminder that cluster solutions need rigorous validation.

**Access:** Free via PubMed Central — [PMC5624035](https://pmc.ncbi.nlm.nih.gov/articles/PMC5624035/).

---

### 8. Marquand et al. (2016) — Normative models for clinical heterogeneity

Marquand, A. F., Rezek, I., Buitelaar, J., & Beckmann, C. F. (2016). Understanding heterogeneity in clinical cohorts using normative models: Beyond case-control studies. *Biological Psychiatry*, *80*(7), 552–561. https://doi.org/10.1016/j.biopsych.2015.12.023

**Why read this:** Proposes normative modelling as an alternative to grouping patients into clusters. Uses the analogy of paediatric growth charts — plotting individual patients against a normative range rather than assigning them to categories. A thoughtful counterpoint to clustering-based approaches in clinical research.

**Access:** Open access (CC BY licence) — [PMC5023321](https://pmc.ncbi.nlm.nih.gov/articles/PMC5023321/).

---

### 9. Lovibond & Lovibond (1995) — DASS Manual

Lovibond, S. H., & Lovibond, P. F. (1995). *Manual for the Depression Anxiety Stress Scales* (2nd ed.). Psychology Foundation of Australia.

**Why read this:** The manual for the DASS-42, the questionnaire used in your Week 8 lab data. Understanding the scale construction — 14 items each for Depression, Anxiety, and Stress, on a 0–3 severity scale — helps you interpret PCA loadings and cluster profiles.

**Access:** The manual is not freely available, but the DASS items and scoring instructions are free from the [UNSW DASS website](https://www2.psy.unsw.edu.au/dass/).

---

### 10. Henry & Crawford (2005) — DASS-21 construct validity

Henry, J. D., & Crawford, J. R. (2005). The short-form version of the Depression Anxiety Stress Scales (DASS-21): Construct validity and normative data in a large non-clinical sample. *British Journal of Clinical Psychology*, *44*(2), 227–239. https://doi.org/10.1348/014466505X29657

**Why read this:** Examines the three-factor structure of the DASS using confirmatory factor analysis. Relevant background for Week 8's PCA analysis — you'll be exploring whether the three-factor structure emerges from the data without imposing it in advance.

**Access:** Paywalled via Wiley. Author PDF freely available from [University of Aberdeen](https://homepages.abdn.ac.uk/j.crawford/pages/dept/pdfs/BJCP_2005_DASS21.pdf).

---

## Readings by Week Topic

| Week | Topic | Key readings |
|------|-------|-------------|
| 1 | AI + Problem Solving | See Week 1 readings |
| 2 | First ML Lab | See Week 2 challenge brief |
| 3 | Generalisation & Overfitting | See Week 3 readings |
| 4 | Regression Lab | See Week 4 challenge brief |
| 5 | Classification & Trees | See Week 5 readings |
| 6 | Classification Lab | See Week 6 challenge brief |
| **7** | **Clustering & Dimensionality Reduction** | **ISLP Ch 12, Haslam et al. (2020), Wattenberg et al. (2016)** |
| **8** | **PCA/Clustering Lab** | **Lovibond & Lovibond (1995), Henry & Crawford (2005)** |

---

*[Back to companion reading](README.md) · [Back to course overview](../../README.md)*
