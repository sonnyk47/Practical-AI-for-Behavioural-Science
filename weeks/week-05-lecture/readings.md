# Week 5 Readings: Classification, Decision Trees, and Fairness

> These readings support the Week 5 lecture on classification. Start with the suggested readings — the optional ones go deeper on specific topics.

---

## Suggested Readings

### 1. Steyerberg et al. (2010) — A framework for evaluating prediction models

Steyerberg, E. W., Vickers, A. J., Cook, N. R., Gerds, T., Gonen, M., Obuchowski, N., Pencina, M. J., & Kattan, M. W. (2010). Assessing the performance of prediction models: A framework for traditional and novel measures. *Epidemiology*, *21*(1), 128–138. https://doi.org/10.1097/EDE.0b013e3181c30fb2

**Why read this:** A clear overview of how to evaluate prediction models in health research, covering calibration, discrimination (AUC), and reclassification. Written for a clinical audience, so the examples are directly relevant to behavioural science. Covers the metrics we discuss in lecture — accuracy, sensitivity, specificity, AUC — in a practical framework.

**Access:** Free via PubMed Central — [full text](https://pmc.ncbi.nlm.nih.gov/articles/PMC3575184/).

---

### 2. James et al. (2023) — ISLP Chapter 4: Classification

James, G., Witten, D., Hastie, T., Tibshirani, R., & Taylor, J. (2023). *An introduction to statistical learning: With applications in Python*. Springer. https://doi.org/10.1007/978-3-031-38747-0

**Why read this:** Chapter 4 covers logistic regression, linear discriminant analysis, and K-nearest neighbours for classification. The explanations are accessible and build from the regression concepts in earlier chapters. This is the textbook companion to what we do in the labs.

**Access:** Free PDF from the authors — [statlearning.com](https://www.statlearning.com/).

---

### 3. Obermeyer et al. (2019) — Racial bias in healthcare algorithms

Obermeyer, Z., Powers, B., Vogeli, C., & Mullainathan, S. (2019). Dissecting racial bias in an algorithm used to manage the health of populations. *Science*, *366*(6464), 447–453. https://doi.org/10.1126/science.aax2342

**Why read this:** The landmark paper showing how a widely-used healthcare algorithm systematically under-identified Black patients who needed extra care, because it used healthcare *costs* as a proxy for health *needs*. Essential reading for understanding how bias enters classification systems — not through malicious intent, but through the choice of training labels.

**Access:** Paywalled at Science, but accessible via Macquarie University library. A free copy is available via the [FTC](https://www.ftc.gov/system/files/documents/public_events/1548288/privacycon-2020-ziad_obermeyer.pdf).

---

## Optional / Deeper Readings

### 4. Chekroud et al. (2016) — Machine learning for depression treatment prediction

Chekroud, A. M., Zotti, R. J., Shehzad, Z., Gueorguieva, R., Johnson, M. K., Trivedi, M. H., Cannon, T. D., Krystal, J. H., & Corlett, P. R. (2016). Cross-trial prediction of treatment outcome in depression: A machine learning approach. *The Lancet Psychiatry*, *3*(3), 243–250. https://doi.org/10.1016/S2215-0366(15)00471-X

**Why read this:** Uses machine learning to predict which patients with depression will respond to a specific antidepressant (citalopram). Demonstrates classification in a clinical context — the target is "remission" vs "no remission." Shows how ML can inform personalised treatment decisions.

**Access:** Paywalled (Elsevier). Accessible via Macquarie University library.

---

### 5. Breiman (2001) — Random Forests

Breiman, L. (2001). Random forests. *Machine Learning*, *45*(1), 5–32. https://doi.org/10.1023/A:1010933404324

**Why read this:** The original paper introducing Random Forests. Surprisingly readable for a technical paper — Breiman explains the intuition behind bagging, random feature selection, and out-of-bag error estimation clearly. If you want to understand *why* random forests work, this is the source.

**Access:** Free PDF from the author's Berkeley website — [randomforest2001.pdf](https://www.stat.berkeley.edu/~breiman/randomforest2001.pdf).

---

### 6. Chouldechova (2017) — The impossibility of fair prediction

Chouldechova, A. (2017). Fair prediction with disparate impact: A study of bias in recidivism prediction instruments. *Big Data*, *5*(2), 153–163. https://doi.org/10.1089/big.2016.0047

**Why read this:** Proves mathematically that when base rates differ between groups, you cannot simultaneously satisfy multiple common definitions of fairness. This is the "impossibility theorem" discussed in lecture — a foundational result for anyone thinking about algorithmic fairness.

**Access:** Paywalled at publisher. Free preprint on arXiv — [arxiv.org/abs/1703.00056](https://arxiv.org/abs/1703.00056).

---

### 7. Dwyer, Falkai, & Koutsouleris (2018) — ML in clinical psychology and psychiatry

Dwyer, D. B., Falkai, P., & Koutsouleris, N. (2018). Machine learning approaches for clinical psychology and psychiatry. *Annual Review of Clinical Psychology*, *14*, 91–118. https://doi.org/10.1146/annurev-clinpsy-032816-045037

**Why read this:** A comprehensive review of how machine learning has been applied in clinical psychology and psychiatry — from diagnosis and prognosis to treatment selection. Covers classification and regression applications across multiple disorders. Good for seeing the big picture of where the field is heading.

**Access:** Paywalled (Annual Reviews). Accessible via Macquarie University library.

---

### 8. Cunningham, Fields, & Kensinger (2021) — BC COVID Sleep & Well-Being dataset

Cunningham, T. J., Fields, E. C., & Kensinger, E. A. (2021). Boston College daily sleep and well-being survey data during early phase of the COVID-19 pandemic. *Scientific Data*, *8*, Article 110. https://doi.org/10.1038/s41597-021-00886-y

**Why read this:** The data descriptor for the dataset you'll use in Week 6. Describes the survey design, variables, and data collection procedures. Useful background for understanding what the variables mean and how the data was gathered.

**Access:** Open access — [full text at Nature](https://www.nature.com/articles/s41597-021-00886-y).

---

### 9. Kroenke, Spitzer, & Williams (2001) — The PHQ-9

Kroenke, K., Spitzer, R. L., & Williams, J. B. W. (2001). The PHQ-9: Validity of a brief depression severity measure. *Journal of General Internal Medicine*, *16*(9), 606–613. https://doi.org/10.1046/j.1525-1497.2001.016009606.x

**Why read this:** The validation paper for the PHQ-9, the depression measure used in the Week 6 dataset. Understanding the measure helps you interpret what the classification target actually means — what does "elevated depression" (score ≥ 5) represent clinically?

**Access:** Free via PubMed Central — [full text](https://pmc.ncbi.nlm.nih.gov/articles/PMC1495268/).

---

### 10. Jacobucci, Grimm, & Zhang (2023) — ML for social and behavioural research

Jacobucci, R., Grimm, K. J., & Zhang, Z. (2023). *Machine learning for social and behavioral research*. Guilford Press.

**Why read this:** A textbook written specifically for behavioural science researchers, covering classification, regression, trees, and ensembles with psychology-relevant examples throughout. The classification chapters complement our lecture material well. Consider this if you want a more thorough treatment than ISLP Chapter 4.

**Access:** Paywalled (purchase from Guilford Press). Check Macquarie University library for access.

---

## Readings by Week Topic

| Week | Topic | Key readings |
|------|-------|-------------|
| 1 | AI + Problem Solving | See Week 1 readings |
| 2 | First ML Lab | See Week 2 challenge brief |
| 3 | Generalisation & Overfitting | See Week 3 readings |
| 4 | Regression Lab | See Week 4 challenge brief |
| **5** | **Classification & Trees** | **Steyerberg et al. (2010), ISLP Ch 4, Obermeyer et al. (2019)** |
| **6** | **Classification Lab** | **Cunningham et al. (2021), Kroenke et al. (2001)** |

---

*[Back to companion reading](README.md) · [Back to course overview](../../README.md)*
