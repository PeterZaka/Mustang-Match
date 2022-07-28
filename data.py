import numpy as np
import pandas as pd

import mysql.connector

mydb = mysql.connector.connect(

)

backgroundInfo = pd.read_sql('SELECT * FROM backgroundInfo', con=mydb)
personalityTraits = pd.read_sql('SELECT * FROM personalityTraits', con=mydb)
personalityTraitsWeights = pd.read_sql('SELECT * FROM personalityTraitsWeights', con=mydb)
interests = pd.read_sql('SELECT * FROM interests', con=mydb)
interestsWeights = pd.read_sql('SELECT * FROM interestsWeights', con=mydb)
friendMatches = pd.read_sql('SELECT * FROM friendMatches', con=mydb)


uniqueQuestions = pd.DataFrame()
uniqueQuestionsWeights = pd.DataFrame()

uniqueQuestions['feel_doing_nothing'] = personalityTraits['feel_doing_nothing'].map({'lazy': 0, 'depends': 1, 'relaxed' : 2})
uniqueQuestions['self_improvement'] = personalityTraits['self_improvement'].map({'not important': 0, 'no time': 1, 'try improve' : 2})
uniqueQuestions['introvert_extravert'] = personalityTraits['introvert_extravert'].map({'introvert': 0, 'extravert': 1})
uniqueQuestions['political_views'] = interests['political_views'].map({'infringed': 0, 'not anymore': 1, 'own safety' : 2, 'important' : 3})
uniqueQuestions['watch_play_sports'] = interests['watch_play_sports'].map({'neither': 0, 'watch': 1, 'play' : 2, 'both' : 3})

personalityTraits = personalityTraits.drop(columns=['feel_doing_nothing', 'self_improvement', 'introvert_extravert'])
interests = interests.drop(columns=['political_views', 'watch_play_sports'])

uniqueQuestionsWeights['feel_doing_nothing'] = personalityTraitsWeights.pop('feel_doing_nothing')
uniqueQuestionsWeights['self_improvement'] = personalityTraitsWeights.pop('self_improvement')
uniqueQuestionsWeights['introvert_extravert'] = personalityTraitsWeights.pop('introvert_extravert')
uniqueQuestionsWeights['political_views'] = interestsWeights.pop('political_views')
uniqueQuestionsWeights['watch_play_sports'] = interestsWeights.pop('watch_play_sports')


interestQuestions = pd.DataFrame()
interestQuestions['music_genre'] = interests.pop('music_genre')
interestQuestions['favorite_classes'] = interests.pop('favorite_classes')

interestQuestionsWeights = pd.DataFrame()
interestQuestionsWeights['music_genre'] = interestsWeights.pop('music_genre')
interestQuestionsWeights['favorite_classes'] = interestsWeights.pop('favorite_classes')

questions = pd.concat([personalityTraits, interests, uniqueQuestions], axis=1, join='inner')
weights = pd.concat([personalityTraitsWeights, interestsWeights, uniqueQuestionsWeights], axis=1, join='inner')

questions.pop('response_id')
weights.pop('response_id')

with pd.option_context('display.max_rows', None, 'display.max_columns', None): 
  # print(backgroundInfo)
  # print('-'*50)
  # print(personalityTraits)
  # print('-'*50)
  # print(personalityTraitsWeights)
  # print('-'*50)
  # print(interests)
  # print('-'*50)
  # print(interestsWeights)
  # print('-'*50)
  # print(friendMatches)

  # print('-'*50)
  # print(questions)
  # print('-'*50)
  # print(uniqueQuestionsWeights)
  
  # print(backgroundInfo.shape)
  # print('-'*50)
  # print(personalityTraits.shape)
  # print('-'*50)
  # print(personalityTraitsWeights.shape)
  # print('-'*50)
  # print(interests.shape)
  # print('-'*50)
  # print(interestsWeights.shape)
  # print('-'*50)
  # print(friendMatches.shape)
  # print('-'*25)
  # print(questions.shape)
  pass

n = questions.shape[0]

difference_keys = [10, 5, 2.5, 1]
importance_keys = [0.5, 1, 1.5, 2]
interests_importance_keys = [1, 2, 3, 4]

final_matches = []
taken = set()