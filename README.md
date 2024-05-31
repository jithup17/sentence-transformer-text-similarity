# Sentence Similarity Scoring and Weighted Evaluation

This project provides a Python-based solution for calculating similarity scores between sentences and generating weighted evaluation scores using the Sentence Transformers library. It can be used to evaluate the accuracy of LLMs (Large Language Models) by comparing their responses to a reference text or human-generated answers. In this specific example, the project compares the responses of a custom-built LLM with those of PDF AI.

## Overview

This script performs the following tasks:

Similarity Calculation: Utilizes the 'stsb-roberta-large' model from Sentence Transformers to compute cosine similarity scores between pairs of sentences in an Excel file. The sentences are extracted from columns named 'Dottie' (custom LLM), 'Material' (reference text), and 'PDF_AI'.

Weighted Evaluation: Applies a weighted scoring mechanism based on question type ('Direct' or 'Indirect') and evaluation type ('Internal' or 'SME') to generate weighted scores using both human and model scores. The weights can be adjusted to customize the evaluation process.

Output: Appends the similarity scores and weighted evaluation scores to the original Excel file.

## Requirements

Python 3.x

Sentence Transformers library (pip install sentence-transformers)

Pandas library (pip install pandas)

## Usage

Prepare your data: Ensure your Excel file has columns named 'Dottie', 'Material', 'PDF_AI', 'Q_type', 'eval_type', 'Human_Score', and 'human_score_pdf_ai'.

Install dependencies: Run pip install sentence-transformers pandas

Modify file paths: Replace the placeholders ('') in the code with the actual paths to your input and output Excel files.

Execute the script: Run the Python script. It will read the Excel file, compute similarity scores, calculate weighted evaluation scores, and save the updated results back to the Excel file.

## File descriptions:

[Your script file].py: The main Python script containing the code.

[Your input file].xlsx: The input Excel file containing the sentences and other relevant data.

[Your output file].xlsx: The output Excel file with appended similarity and weighted evaluation scores.

### Additional Notes

The script includes error handling for missing values (NaN) in the input data.

The weighted scoring mechanism can be easily customized by adjusting the weights in the score_weighted and score_weighted_PDF_AI functions.

Consider exploring different Sentence Transformers models to find the one that best suits your specific task and dataset.

#### Disclaimer

This code is provided as a starting point. You may need to modify it to adapt to your specific use case or data format.
