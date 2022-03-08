import numpy as np
import pandas as pd

traitsQuestions = 35
n = 100
traits_data = pd.DataFrame(np.random.randint(4, size=(n, traitsQuestions)) + 1)
traits_importance_data = pd.DataFrame(np.random.randint(4, size=(n, traitsQuestions)) + 1)

difference_keys = [10, 5, 2.5, 1]
importance_keys = [0.5, 1, 1.5, 2]

def get_score(p1, p2):
  differences = abs(traits_data.iloc[p1] - traits_data.iloc[p2])
  differences = [difference_keys[i] for i in differences]
  importance = [importance_keys[i-1] for i in traits_importance_data.iloc[p1]]
  return sum([a*b for a, b in zip(differences, importance)])

def get_average_score(p1, p2):
  differences = abs(traits_data.iloc[p1] - traits_data.iloc[p2])
  differences = [difference_keys[i] for i in differences]
  importance_p1 = [importance_keys[i-1] for i in traits_importance_data.iloc[p1]]
  importance_p2 = [importance_keys[i-1] for i in traits_importance_data.iloc[p2]]
  p1_to_p2_score = sum([a*b for a, b in zip(differences, importance_p1)])
  p2_to_p1_score = sum([a*b for a, b in zip(differences, importance_p2)])
  return (p1_to_p2_score + p2_to_p1_score) / 2

def get_matches(p1, exclude=[-1]):
  p1_scores = {}
  for i in range(n):
    if i == p1 or i in exclude: continue
    p1_scores[i] = get_score(p1, i)
  return sorted(p1_scores, key=p1_scores.get, reverse=True)

final_matches = []
taken = set()

counter = 0
while (len(taken) != n):
  counter += 1

  all_matches = dict()
  for i in range(n):
    if not i in taken:
      all_matches[i] = get_matches(i, taken)

  # Gets where user placed in their matches' lists
  all_matches_places = dict()
  for i in range(n):
    if not i in taken:
      all_matches_places[i] = [all_matches[match].index(i) for match in all_matches[i]]

  # Add "perfect" matches first
  place = 0
  added = 0
  while (added == 0):
    for i in range(n):
      if not i in taken and not all_matches[i][0] in taken and all_matches_places[i][0] == place:
        final_matches.append((i, all_matches[i][0]))
        taken.add(i)
        taken.add(all_matches[i][0])
        added += 1
    place += 1

  print(f'Round: {counter}')
  print(f'Matches added: {added}')
  print(f'Went to place: {place}')
  print()

for match in final_matches:
  print(match, get_average_score(match[0], match[1]))