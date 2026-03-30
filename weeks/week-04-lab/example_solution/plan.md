# Analysis Plan: Predicting Depression from Personality and Demographics

## Research Question

Can we predict DASS Depression scores from Big Five personality traits and demographic variables? Which personality traits are the strongest predictors?

## Dataset

- **File:** `data/dass42_data.csv` (tab-separated)
- **Size:** 39,775 respondents × 172 columns
- **Key variables:**
  - DASS-42 items (Q1A–Q42A): coded 1–4, need recoding to 0–3
  - Big Five personality (TIPI1–TIPI10): 1–7 scale, items 2, 4, 6, 8, 10 are reverse-scored
  - Demographics: age, gender, education, urban, married, familysize

## Step 1: Data Cleaning

1. Load the data (tab-separated)
2. Filter out unreasonable ages (keep 10–100) — some entries look like birth years (e.g., 1998)
3. Check vocabulary validity: VCL6, VCL9, VCL12 are fake words. Remove respondents who endorsed 2+ fake words
4. Check for missing values in DASS items and TIPI items

## Step 2: Score the Variables

**DASS Depression subscale:**
- Items: Q3, Q5, Q10, Q13, Q16, Q17, Q21, Q24, Q26, Q31, Q34, Q37, Q38, Q42
- Recode each from 1–4 to 0–3 (subtract 1)
- Sum the 14 items → score range 0–42

**Big Five personality (TIPI):**
- Reverse-score items 2, 4, 6, 8, 10 (reverse = 8 − original)
- Extraversion = (TIPI1 + TIPI6R) / 2
- Agreeableness = (TIPI2R + TIPI7) / 2
- Conscientiousness = (TIPI3 + TIPI8R) / 2
- Emotional Stability = (TIPI4R + TIPI9) / 2
- Openness = (TIPI5 + TIPI10R) / 2

## Step 3: Choose Features

**Start with:** Big Five personality scores (5 features)
- These are the theoretically motivated predictors
- Emotional Stability should correlate strongly with depression (neuroticism is its inverse)

**Then add:** demographics (age, gender, education, urban, married, familysize)
- See if demographics improve prediction beyond personality

**Don't include:** DASS Anxiety or Stress (circular), item response times (artefactual)

## Step 4: Train/Test Split

- 80% training, 20% test
- Use `random_state=42` for reproducibility
- The test set stays locked until the very end

## Step 5: Models

1. **Baseline:** Predict the mean depression score for everyone → calculate MAE and R²
2. **Linear Regression:** Ordinary least squares → 5-fold CV
3. **Ridge (alpha=1.0):** L2 regularisation → 5-fold CV
4. **Lasso (alpha=0.1):** L1 regularisation → 5-fold CV

## Step 6: Evaluation

- Report 5-fold cross-validated MAE and R² for each model
- Compare models in a bar chart
- At the very end, evaluate the best model on the held-out test set
- Check for overfitting: is there a gap between training and CV performance?

## Step 7: Interpretation

- Examine regression coefficients — which features have the largest absolute values?
- Create a horizontal bar chart of coefficients
- Connect findings back to psychological theory:
  - Emotional Stability (inverse of neuroticism) should be the strongest predictor
  - Extraversion and Conscientiousness should also predict lower depression

## Expected Outcome

Based on previous research, personality explains roughly 30–40% of variance in depression scores (R² = 0.30–0.40). Emotional Stability (neuroticism) is consistently the strongest single predictor.
