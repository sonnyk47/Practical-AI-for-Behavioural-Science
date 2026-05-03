# Final Plan: What Actually Happened

> This is the updated plan reflecting what we actually built. Compare with the original `plan.md` to see what changed and why.

## What We Set Out to Do

Build classification models (baseline, logistic regression, decision tree, random forest) to predict elevated depression (PHQ-9 >= 5) from sleep, mood, personality, and demographic features. Compare models using accuracy, F1, and AUC, analyse feature importance, explore decision thresholds, and consider ethical implications.

## What Changed

### 1. Merging yielded fewer participants than expected

The three datasets have different participant counts (daily: 1,484; demographics: 1,662; round 1: 839 unique). After inner joins, we ended up with **836 participants** — fewer than the ~911 we initially estimated. This is because inner joins only keep participants present in *all three* datasets.

### 2. Round 1 had duplicate entries

75 participants had duplicate entries in `round1_assessment.csv`. We kept the first entry for each (`drop_duplicates(subset='sub_id', keep='first')`). This wasn't in the original plan but was necessary for clean merging.

### 3. Class balance was nearly even

The binary target split 54.5% elevated / 45.5% minimal — much more balanced than typical clinical datasets. This means accuracy is a reasonable metric (unlike in heavily imbalanced datasets), and the majority-class baseline is only ~54.5%.

### 4. Logistic Regression and Random Forest performed similarly

| Model | Accuracy | F1 | AUC |
|-------|----------|-----|-----|
| Baseline (majority class) | 0.545 | — | — |
| Logistic Regression | 0.815 | 0.827 | 0.911 |
| Decision Tree (depth=5) | 0.804 | 0.811 | 0.871 |
| Random Forest (100 trees) | 0.815 | 0.821 | 0.920 |

Both logistic regression and random forest achieved ~81.5% accuracy — a substantial improvement over the 54.5% baseline. The random forest had the highest AUC (0.920), suggesting better probability calibration, but logistic regression had a slightly higher F1 (0.827 vs 0.821). The decision tree lagged behind both on all metrics.

### 5. PANAS negative affect and GAD-7 dominated

The top predictors were:
- **PANAS negative affect** (RF importance: 0.140) — daily negative mood strongly predicts depression classification
- **GAD-7 total** (RF importance: 0.127) — anxiety and depression are highly comorbid
- **Stress coping** (RF importance: 0.080) — lower coping ability predicts elevated depression
- **Sadness** (RF importance: 0.073) — direct mood measure
- **Isolation** (RF importance: 0.072) — less social contact predicts depression

This makes clinical sense — these features all measure emotional distress or social withdrawal, which are core features of depression. The personality traits and demographics contributed less but still added signal.

### 6. Threshold choice has real consequences

At the default threshold of 0.5:
- Recall ≈ 0.87 — catches 87% of elevated cases
- Precision ≈ 0.78 — 78% of flagged participants actually have elevated depression

Lowering the threshold to 0.3:
- Recall ≈ 0.95 — catches 95% of elevated cases
- Precision ≈ 0.67 — more false positives

For a screening tool where missing a depressed person is worse than a false alarm, the lower threshold is arguably better. But this is a values judgement, not a statistical one.

### 7. Refactoring improved code quality

The initial notebook had repeated metric-computation code for each model. We refactored to create an `evaluate_model()` function that takes any fitted model and returns a dictionary of metrics. This eliminated ~40 lines of duplicated code and made it trivial to add new models.

### 8. Two scripts worked well for the pipeline

We split the work into two scripts:
1. `explore_data.py` — data loading, aggregation, merging, summary statistics, and class balance
2. `classify_depression.py` — feature selection, splitting, modelling, evaluation, and all visualisations

This separation keeps exploration and modelling distinct, which is cleaner than one monolithic script.

## Key Findings

1. **AUC ≈ 0.92** — the random forest achieved strong discrimination between elevated and minimal depression. This is quite good for a classification model using survey-level features.

2. **PANAS negative affect is the strongest predictor** — daily negative mood captured by the PANAS is more predictive than any single personality trait or sleep variable. This aligns with the affect-based models of depression in clinical psychology.

3. **GAD-7 anxiety is the second-strongest predictor** — consistent with the well-established comorbidity between anxiety and depression. People who are anxious are more likely to also be depressed.

4. **The decision tree underperformed** — with max_depth=5, the tree couldn't capture the complexity of the relationships. The random forest's ensemble approach (averaging 100 trees) reduced this variance substantially.

5. **Threshold choice is a values judgement** — for a screening context (catch everyone, follow up later), threshold 0.3 is better. For a diagnostic context (fewer false alarms), threshold 0.5 or higher is better. There's no objectively "right" answer.

## What We'd Do Differently

- Try **cross-validation** for model selection (we used it for evaluation but not hyperparameter tuning)
- Try **XGBoost** as a fifth model to see if gradient boosting improves on random forest
- Check whether the model works **equally well for males and females** (subgroup fairness analysis)
- Try **SMOTE** or `class_weight='balanced'` to see if addressing the slight class imbalance changes results
- Consider whether **daily-level prediction** (not aggregated per participant) would work differently
