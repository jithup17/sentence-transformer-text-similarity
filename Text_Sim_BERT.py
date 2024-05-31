from sentence_transformers import SentenceTransformer, util
import pandas as pd
import numpy as np
import time
from time import sleep

model = SentenceTransformer('stsb-roberta-large')

df = pd.read_excel('') #file path
print("File Read")
# Initialize an empty list to store similarity scores
similarity_scores = []
similarity_scores_PDF_AI = []
# Loop through all rows in the DataFrame
for index, row in df.iterrows():
    sentence1 = row['Custom_LLM'] ## Custom LLM Response
    sentence2 = row['Material'] ## Extract or paragraph containing the answer
    sentence3 = row['PDF_AI'] ## PDF AI Response

    # Check for NaN values and handle them
    if pd.isna(sentence1) or pd.isna(sentence2) or pd.isna(sentence3):
        print(f"Skipping row {index + 1} due to NaN values")
        continue

    # Encode sentences to get their embeddings
    embedding1 = model.encode(sentence1, convert_to_tensor=True)
    embedding2 = model.encode(sentence2, convert_to_tensor=True)
    embedding3 = model.encode(sentence3, convert_to_tensor=True)
    print("Embedding Finished")
    # Compute similarity scores of two embeddings
    cosine_score = util.pytorch_cos_sim(embedding1, embedding2).item() * 100
    cosine_score_PDF_AI = util.pytorch_cos_sim(embedding2, embedding3).item() * 100
    print("Similarity Score Calculated!")
    similarity_scores.append(cosine_score)
    similarity_scores_PDF_AI.append(cosine_score_PDF_AI)

    print(f"Row {index + 1}:")
    #print("Sentence 1:", sentence1)
    #print("Sentence 2:", sentence2)
    print(f"Similarity Score : {cosine_score:.2f}%\n")
    print(f"Similarity Score : {cosine_score_PDF_AI:.2f}%\n")

# Add similarity scores to the DataFrame
df['Similarity_Score'] = similarity_scores
df['Similarity_Score_PDF_AI'] = similarity_scores_PDF_AI
# Save the updated DataFrame
df.to_excel('', index=False) #file path

sleep(5)

df = pd.read_excel('') #file path

def score_weighted(row):
        model_score = row['Similarity_Score']
        human_score = row['Human_Score']

        if row['Q_type'] == 'Direct':
            if row['eval_type'] == 'Internal':
                return ((model_score / 100) * 0.7 + human_score * 0.3)
            elif row['eval_type'] == 'SME':
                return ((model_score / 100) * 0.25 + human_score * 0.75)
        elif row['Q_type'] == 'Indirect':
            if row['eval_type'] == 'Internal':
                return ((model_score / 100) * 0.3 + human_score * 0.7)
            elif row['eval_type'] == 'SME':
                return ((model_score / 100) * 0.2 + human_score * 0.8)


def score_weighted_PDF_AI(row):
    model_score_PDF_AI = row['Similarity_Score_PDF_AI']
    human_score_PDF_AI = row['human_score_pdf_ai']

    if row['Q_type'] == 'Direct':
        if row['eval_type'] == 'Internal':
            return ((model_score_PDF_AI / 100) * 0.7 + human_score_PDF_AI * 0.3)
        elif row['eval_type'] == 'SME':
            return ((model_score_PDF_AI / 100) * 0.25 + human_score_PDF_AI * 0.75)
    elif row['Q_type'] == 'Indirect':
        if row['eval_type'] == 'Internal':
            return ((model_score_PDF_AI / 100) * 0.3 + human_score_PDF_AI * 0.7)
        elif row['eval_type'] == 'SME':
            return ((model_score_PDF_AI / 100) * 0.2 + human_score_PDF_AI * 0.8)

result_list = []
result_list_PDF_AI = []
for index, row in df.iterrows():
    weighted_score = score_weighted(row)
    weighted_score_PDF_AI = score_weighted_PDF_AI(row)
    result_list.append(weighted_score)
    result_list_PDF_AI.append(weighted_score_PDF_AI)

df['Weighted_Score'] = result_list
df['Weighted_Score_PDF_AI'] = result_list_PDF_AI

# Save the updated DataFrame
df.to_excel('', index=False) #file path
