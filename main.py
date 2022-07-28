import numpy as np
import pandas as pd

from score import *

counter = 0
while (len(taken) < n-1):
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

mycursor = mydb.cursor()

mycursor.execute('truncate table friendMatches')

for match in final_matches:
  print(backgroundInfo['first_name'][match[0]], backgroundInfo['last_name'][match[0]], '+', backgroundInfo['first_name'][match[1]], backgroundInfo['last_name'][match[1]], get_score(match[0], match[1]), get_score(match[1], match[0]))

  mycursor.execute(f"INSERT INTO friendMatches (uuid_person1, uuid_person2) VALUES ('{backgroundInfo['uuid'][match[0]]}', '{backgroundInfo['uuid'][match[1]]}')")

# with pd.option_context('display.max_rows', None, 'display.max_columns', None): 
#   m1 = final_matches[0][0]
#   m2 = final_matches[0][1]
#   differences = abs(questions.iloc[m1] - questions.iloc[m2])
#   print(differences)

#   print(interestQuestions.iloc[m1] == interestQuestions.iloc[m2])

# friendMatches = pd.read_sql('SELECT * FROM friendMatches', con=mydb)
# with pd.option_context('display.max_rows', None, 'display.max_columns', None): 
#   print(friendMatches)

# for i in range(n):
#   for j in range(n):
#     print(f"{backgroundInfo['first_name'][i]} {backgroundInfo['first_name'][j]}, {get_score(i, j)}")

mydb.close()