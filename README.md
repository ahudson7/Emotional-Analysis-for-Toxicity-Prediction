# Preemptively Determining Toxicity of Online Communications Using Emotional Analysis

### Authors: 
Haadiya Ansari <br> 
Aaron Hudson

---
### CS 510: Adventures in NLP

Professor Ameeta Agrawal <br>
TA Steve Braich <br>
Spring 2021 <br>
Portland State University

---

## Repository Contents:

- [emotionExtraction.py](https://github.com/ahudson7/Emotional-Analysis-for-Toxicity-Prediction/blob/main/emotionExtraction.py): python script used to extract emotional features from the Conversations Gone Awry corpus

- [CGA_emotion_df.csv](https://github.com/ahudson7/Emotional-Analysis-for-Toxicity-Prediction/blob/main/CGA_emotion_df.csv): emotional features information extracted using the emotionExtraction.py script

- [ConvosGoneAwry.ipynb](https://github.com/ahudson7/Emotional-Analysis-for-Toxicity-Prediction/blob/main/ConvosGoneAwry.ipynb): Google colab notebook that contains all of the code necessary to run our model from pre-processing to the prediction phase

---

## Description:

This repository is designed to accompany our project term paper, providing our code to allow others to replicate our work and perform future research.

## References:

- Our model is built using [Convokit](https://convokit.infosci.cornell.edu/) as a foundation.<br>
Jonathan P. Chang, Caleb Chiam, Liye Fu, Andrew Wang, Justine Zhang, Cristian Danescu-Niculescu-Mizil. 2020. "ConvoKit: A Toolkit for the Analysis of Conversations". Proceedings of SIGDIAL.

- Our work is modeled after the following papers:
    - Justine Zhang, Jonathan Chang, Cristian Danescu-Niculescu-Mizil, Lucas Dixon, Yiqing Hua, Dario Taraborelli, and Nithum Thain. 2018. [Conversations gone awry: Detecting    early signs of conversational failure](https://arxiv.org/abs/1805.05345). In Proceedings of the 56th Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers), pages 1350–1361, Melbourne, Australia. Association for Computational Linguistics.
    - Éloi Brassard-Gourdeau and Richard Khoury. 2020. Using Sentiment Information for Preemptive Detection of Toxic Comments in Online Conversations. arXiv:2006.10145. Retrieved from https://arxiv.org/abs/2006.10145

- Our emotional features were extracted using the [NRC Emotional Lexicon](https://pypi.org/project/NRCLex/). <br> 
  Mark M. Bailey. 2020. NRCLex. (November 2020). Retrieved June 1, 2021 from https://pypi.org/project/NRCLex/
