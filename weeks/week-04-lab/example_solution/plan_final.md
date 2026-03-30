# Final Plan: What Actually Happened

> This is the updated plan reflecting what we actually built. Compare with the original `plan.md` to see what changed and why.

## What We Set Out to Do

Build regression models (baseline, linear, Ridge, Lasso) to predict DASS Depression from Big Five personality and demographics. Compare models using cross-validated MAE and R², interpret the coefficients.

## What Changed

### 1. Data cleaning was straightforward

The age filter only removed 7 rows (ages > 100). The VCL filter removed ~1,148 rows (2.9% of the sample). After cleaning, we had **38,620 rows** — more than enough for stable modelling.

### 2. All DASS and TIPI items were complete

Surprisingly, there were zero missing values in the DASS-42 items and TIPI items. This made the scoring step much easier than expected — no need to handle missing items.

### 3. Emotional Stability dominated as expected

The correlation between Emotional Stability and DASS Depression was r = −0.52, far stronger than any other predictor. This confirmed our hypothesis from the plan — neuroticism (the inverse of Emotional Stability) is the single best personality predictor of depression.

### 4. Regularisation barely mattered

With 38,620 rows and only 11 features, the dataset is very "wide" relative to "tall" — there's no risk of overfitting, so Ridge and Lasso performed almost identically to ordinary least squares:

| Model | CV MAE | CV R² |
|-------|--------|-------|
| Baseline (mean) | 10.59 | ~0.00 |
| Linear Regression | 8.19 | 0.339 |
| Ridge (alpha=1.0) | 8.19 | 0.339 |
| Lasso (alpha=0.1) | 8.20 | 0.339 |

This is actually a useful pedagogical finding: regularisation matters most when you have many features relative to observations. With 38K rows and 11 features, there's little to regularise.

### 5. Lasso feature selection was informative at higher alphas

At the default alpha=0.1, Lasso only zeroed out gender and married. But increasing alpha revealed an interpretable feature importance ranking:
- alpha=0.5: Lasso kept all Big Five traits but dropped all demographics
- alpha=1.0: Lasso also dropped Agreeableness
- alpha=5.0: Only Emotional Stability and age survived

This Lasso path tells a clear story: personality matters more than demographics for predicting depression, and Emotional Stability matters most of all.

### 6. Two scripts worked well for the pipeline

We split the work into two scripts:
1. `explore_data.py` — data loading, cleaning, summary statistics, and initial exploration
2. `model_and_predict.py` — scoring, feature selection, modelling, evaluation, and visualisations

This separation keeps exploration and modelling distinct, which is cleaner than having everything in one script.

## Key Findings

1. **R² ≈ 0.34** — personality and demographics explain about a third of the variance in depression scores. This is quite good for individual-level prediction from survey data.

2. **Emotional Stability is the strongest predictor** (coefficient ≈ −3.4) — a 1-point increase in Emotional Stability is associated with a 3.4-point decrease in DASS Depression. This makes sense: Emotional Stability is the inverse of neuroticism, which has been consistently linked to depression in personality research.

3. **Extraversion (−1.4) and Conscientiousness (−1.1) are moderate predictors** — more extraverted and more conscientious people tend to report lower depression scores.

4. **Demographics add very little** beyond personality — this is consistent with the personality psychology literature, which finds that broad traits like the Big Five capture much of the demographic variation in mental health outcomes.

5. **No overfitting** — training R² (0.339) and cross-validated R² (0.339) were virtually identical, and test R² (0.334) was very close. With this much data and few features, overfitting is not a concern.

## What We'd Do Differently

- Try adding **interaction terms** (e.g., Extraversion × Emotional Stability) — maybe the combination of traits matters more than each one alone
- Try **non-linear models** (polynomial features, decision trees) — the relationship between personality and depression may not be perfectly linear
- Consider **separate models by country/region** — given that 54% of the sample is from Malaysia, country-level differences might be important
