"""
Emotional Extraction via NRC Emotional Lexicon

This code extracts the emotional features of the Conversations Gone Awry Corpus, and outputs the results as a
CSV file for use in developing features to add to the Convokit model.
"""

import pandas as pd

from nrclex import NRCLex

from convokit import Corpus, download
corpus = Corpus(filename=download("conversations-gone-awry-corpus"))

count = 0

emotion_df = pd.DataFrame(columns=['fear', 'anger', 'anticipation', 'trust', 'surprise', 'positive', 'negative', 'sadness', 'disgust', 'joy'])

emotion_list = ['fear', 'anger', 'anticipation', 'trust', 'surprise', 'positive', 'negative', 'sadness', 'disgust', 'joy']

for utt in corpus.iter_utterances():
    emotion = NRCLex(utt.text)
    temp = []
    for k in emotion.affect_frequencies.keys():
        if k in emotion_list:
            emotion_df.loc[utt.id, k] = emotion.affect_frequencies[k]
        elif k == 'anticip':
            emotion_df.loc[utt.id, 'anticipation'] = emotion.affect_frequencies[k]

    
    '''
    # Code to test using first 10 utterances
    count += 1
    if count <= 10:
        print(utt.id)
        print('\n\n', count, ': ', emotion.affect_frequencies)
    else:
        break
    '''
    
emotion_df.to_csv('emotion_df.csv')
