# Analysis Plan: Classifying Elevated Depression from Sleep, Mood, and Personality

## Research Question

Can we classify participants as having elevated depression (PHQ-9 >= 5) or minimal symptoms (< 5) using sleep, mood, personality, and demographic features? Which classifier performs best, and which features are most important?

## Dataset

- **Source:** Boston College COVID-19 Sleep and Well-Being Study (Cunningham, Fields, & Kensinger, 2021)
- **Files:** Three CSVs that need merging:
  - `daily_survey.csv` — ~52K daily diary entries from ~1,484 participants
  - `demographics.csv` — age, sex for ~1,662 participants
  - `round1_assessment.csv` — Big Five personality (BFI-2) + GAD-7 anxiety for ~914 participants

## Step 1: Data Loading and Merging

1. Load all three CSV files
2. Aggregate daily survey per participant (groupby sub_id, take the mean)
3. Score Big Five personality from BFI-2 items (30 items, 6 per trait, some reverse-scored)
4. Compute GAD-7 total anxiety score (sum of 7 items)
5. Deduplicate round1_assessment (some participants have duplicate entries)
6. Merge all three on sub_id (inner join)
7. Check final N and class balance

## Step 2: Create Binary Target

- PHQ-9 >= 5 → elevated depression (1)
- PHQ-9 < 5 → minimal symptoms (0)
- The PHQ-9 here is averaged from daily entries, so it's a continuous measure — threshold at 5

## Step 3: Feature Selection

**21 features:**
- Daily mood: PANAS positive affect, PANAS negative affect, sadness, happiness
- Sleep: total sleep time, sleep efficiency, sleep latency, awakenings
- Lifestyle: exercise, alcohol, isolation, stress coping, COVID worry, social contact
- Demographics: age, biological sex
- Personality: Big Five (Extraversion, Agreeableness, Conscientiousness, Neuroticism, Openness)
- Anxiety: GAD-7 total

**Don't include:** PHQ-9 itself (that's the target), individual DASS items (circular)

## Step 4: Train/Test Split

- 80% training, 20% test
- Stratified split (keeps class proportions equal in both sets)
- Use `random_state=42` for reproducibility

## Step 5: Models

1. **Baseline:** Majority-class classifier (DummyClassifier) — always predicts elevated
2. **Logistic Regression:** With StandardScaler (LR is sensitive to feature scales)
3. **Decision Tree:** `max_depth=5` to prevent overfitting
4. **Random Forest:** 100 trees, `max_depth=10`

## Step 6: Evaluation

For each model, report:
- Accuracy
- F1 score (important because classes are slightly imbalanced)
- AUC (area under the ROC curve)
- Confusion matrix

Then compare all models in a bar chart.

## Step 7: Feature Importance

- Random Forest feature importances (built-in)
- Logistic regression coefficient magnitudes (for comparison)
- Plot top 10 features

## Step 8: Threshold Analysis

- Default threshold is 0.5, but try alternatives (0.3, 0.4, 0.5, 0.6, 0.7)
- For a depression screener, lower threshold = catch more cases (higher recall) but more false positives
- Report how precision, recall, and F1 change with threshold

## Step 9: Ethical Consideration

- Think about: Who might be harmed by false negatives (missed cases)?
- Think about: What happens if the model works differently for different groups?
- Think about: Should a model like this be used to make decisions about people?

## Expected Outcome

Based on the feature set (mood, sleep, personality, anxiety), we expect decent classification performance (AUC > 0.85). PANAS negative affect and GAD-7 should be strong predictors, since they directly measure emotional distress which overlaps with depression.
