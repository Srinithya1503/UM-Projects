# Drug Side Effects to Medical Condition Prediction

## Project Overview

This project builds an end-to-end Natural Language Processing (NLP) pipeline to predict the **medical condition** associated with a drug based solely on its reported **side effects text**. Using structured exploratory data analysis, careful text preprocessing, TF-IDF vectorization, and classical machine learning models, the system provides **interpretable and confidence-aware predictions** suitable for clinical decision support scenarios.

The final system goes beyond simple classification by incorporating **prediction confidence analysis and Top-K outputs**, ensuring safer and more realistic deployment in healthcare-related contexts.

---

## Business and Clinical Motivation

* Side effects are often documented as unstructured free text
* Many medical conditions share overlapping symptom descriptions
* For clinical analytics and pharmacovigilance, **uncertainty awareness is critical**

This project demonstrates how to:

* Extract signal from noisy medical text
* Handle imbalanced multi-class clinical data
* Produce predictions that communicate **both outcome and confidence**

---

## Dataset Description

* **Source**: Drugs.com
* **Records**: 2,931 drugs
* **Target**: Medical condition (multi-class)
* **Input Feature**: Side effects (free-text)

### Key Columns Used

* `drug_name`
* `medical_condition`
* `side_effects`

### Class Distribution Insight

The dataset is moderately imbalanced, with conditions such as *Pain*, *Colds & Flu*, and *Acne* dominating the distribution, while several conditions have limited samples. This strongly influenced model selection and evaluation strategy.

---

## Repository Structure

```
drug-side-effects-condition-prediction/
│
├── data/
│   ├── raw/
│   │   └── drugs_side_effects_drugs_com.csv
│   └── processed/
│       └── final_confidence_aware_predictions.csv
│
├── notebooks/
│   ├── 01_eda.ipynb
│   ├── 02_preprocessing_and_vectorization.ipynb
│   ├── 03_model_training_and_evaluation.ipynb
│   ├── 04_prediction_analysis.ipynb
│
│
├── requirements.txt
├── .gitignore
└── README.md
```

---

## Exploratory Data Analysis (EDA)

Key findings from EDA:

### 1. Medical Condition Distribution

* A small number of conditions account for a large proportion of drugs
* Many rare conditions require careful evaluation using **Macro F1**, not accuracy alone

### 2. Side Effects Text Length

* Highly right-skewed distribution
* Majority of entries are short, but extreme outliers exceed 30,000 characters
* Mean length significantly higher than median due to outliers

### EDA-Driven Decision

Side effects text was **truncated at the 99th percentile (4,692 characters)** to:

* Reduce noise
* Prevent model dominance by extreme outliers
* Preserve nearly all clinically relevant information

---

## Data Preprocessing and Feature Engineering

### Text Cleaning

* Lowercasing
* Removal of special characters and excessive whitespace
* Preservation of medical terminology

### Text Length Handling

* Truncation at the 99th percentile based on EDA
* Ensures consistent and stable feature extraction

### Vectorization

* **TF-IDF Vectorization**
* Fixed vocabulary size (10,000 features)
* Sparse representation suitable for classical ML models

This approach balances interpretability, performance, and computational efficiency.

---

## Model Development

Two models were trained and evaluated:

### Baseline Model

* Logistic Regression
* Class-weighted to address imbalance
* Strong linear baseline for sparse TF-IDF features

### Final Model

* Random Forest Classifier
* Better captures non-linear interactions between symptom terms
* Improved performance on minority classes

---

## Model Evaluation

### Evaluation Metrics

* Accuracy
* Macro F1 Score
* Weighted F1 Score
* Per-class precision and recall
* Confusion matrix analysis

### Final Performance Comparison

| Model               | Macro F1 | Weighted F1 |
| ------------------- | -------- | ----------- |
| Logistic Regression | 0.75     | 0.73        |
| Random Forest       | 0.80     | 0.79        |

**Random Forest** was selected as the final model due to superior overall and minority-class performance.

---

## Prediction Confidence Analysis

Rather than treating all predictions equally, this project explicitly analyzes **prediction confidence** using model probabilities.

### Observed Confidence Zones

* **Low confidence (< 0.35)**: Ambiguous or generic symptom descriptions
* **Medium confidence (0.35–0.70)**: Overlapping symptom profiles
* **High confidence (> 0.70)**: Strong, condition-specific signals

This analysis revealed that forcing single-label predictions in low-confidence cases would be unsafe in real-world clinical settings.

---

## Advanced Prediction Strategy

The final prediction system is **confidence-aware**:

| Confidence Level | Prediction Strategy                |
| ---------------- | ---------------------------------- |
| < 0.35           | Assign "Other" and flag for review |
| 0.35 – 0.70      | Return Top-3 predicted conditions  |
| > 0.70           | Return single predicted condition  |

This transforms the model from a simple classifier into a **decision-support system**.

---

## Final Outputs

The prediction pipeline produces:

* Predicted medical condition
* Prediction confidence score
* Decision note (high / medium / low confidence)
* Optional Top-3 condition suggestions

All results are saved as:

```
data/processed/final_confidence_aware_predictions.csv
```

---

## Key Takeaways

* TF-IDF combined with Random Forest performs strongly for clinical text classification
* Confidence analysis is essential for responsible ML in healthcare
* Top-K predictions improve interpretability for ambiguous cases
* The system is robust, reproducible, and artifact-driven

---

## Future Improvements

* Contextual embeddings (BioBERT, ClinicalBERT)
* Per-class confidence thresholds
* SHAP-based interpretability for text features
* Multi-label classification for comorbid conditions
* API deployment using FastAPI or Flask

---

## License

This project is released under the MIT License.

---

## Final Note

This project demonstrates not only technical modeling skills, but also an understanding of **clinical uncertainty, model limitations, and responsible deployment practices**. 
---

