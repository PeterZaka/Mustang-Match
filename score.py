import numpy as np
import pandas as pd

from data import *

def get_score(p1, p2):
  differences = abs(questions.iloc[p1] - questions.iloc[p2])
  differences = [difference_keys[i] for i in differences]
  importance = [importance_keys[i-1] for i in weights.iloc[p1]]

  differences.extend(interestQuestions.iloc[p1] == interestQuestions.iloc[p2])
  importance.extend([interests_importance_keys[i-1] for i in interestQuestionsWeights.iloc[p1]])
  
  return sum([a*b for a, b in zip(differences, importance)])

def get_average_score(p1, p2):
  differences = abs(questions.iloc[p1] - questions.iloc[p2])
  differences = [difference_keys[i] for i in differences]
  importance_p1 = [importance_keys[i-1] for i in weights.iloc[p1]]
  importance_p2 = [importance_keys[i-1] for i in weights.iloc[p2]]

  differences.extend(interestQuestions.iloc[p1] == interestQuestions.iloc[p2])
  importance_p1.extend([interests_importance_keys[i-1] for i in interestQuestionsWeights.iloc[p1]])
  importance_p2.extend([interests_importance_keys[i-1] for i in interestQuestionsWeights.iloc[p2]])
  
  p1_to_p2_score = sum([a*b for a, b in zip(differences, importance_p1)])
  p2_to_p1_score = sum([a*b for a, b in zip(differences, importance_p2)])
  return (p1_to_p2_score + p2_to_p1_score) / 2

def get_matches(p1, exclude=[-1]):
  p1_scores = {}
  for i in range(n):
    if i == p1 or i in exclude: continue
    p1_scores[i] = get_score(p1, i)
  return sorted(p1_scores, key=p1_scores.get, reverse=True)