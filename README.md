# Natural Language Processing using spaCy library

Building aspect-based sentiment analysis system to analyze product reviews using spaCy and Keras.

This workshop was originally presented at [Warsaw IT Days 2019](https://warszawskiedniinformatyki.pl)
by [Stanisław Giziński](https://github.com/Gizzio) and [Krzysztof Kowalczyk](https://github.com/kowaalczyk) 
from our [Machine Learning Club](https://www.facebook.com/KNUM.MIMUW/).

We are also currently implementing full support for Polish language in spaCy, you can track our progress via [our GitHub organization](https://github.com/spacy-pl) and the see results on [our project website](http://spacypl.sigmoidal.io)

## Environment setup

We will be using Anaconda distribution of Python to make installation of machine learning libraries easier.
Any other distribution of `Python>=3.7` should do fine, but if you want to have exactly the same setup:

0. Clone this repository: `git clone https://github.com/knum-mimuw/spacy-workshop`
1. Download and install [Miniconda Python 3.7 installer](https://conda.io/en/latest/miniconda.html),
   make sure to add binaries to PATH variable when prompted at the end of installation
2. Open the terminal (on Windows, use newly installed Anaconda Prompt instead of CMD / Powershell)
3. Create conda environment: `conda create -n spacy-wdi python=3.7.1 spacy jupyterlab`, this may take a while
4. Activate the environment: `source activate spacy-wdi` (on Windows: `activate spacy-wdi`)
5. Download machine learning models: `python -m spacy download en`
6. Navigate to the cloned repository folder (`cd spacy-workshop`) and start jupyter lab (`jupyter lab`)
7. Download ["The Guardian Articles" dataset](http://knum.mimuw.edu.pl/spacy-workshop/) and extract it (there is only one CSV in there, place it in the cloned repository folder.
8. Download ["Semeval Aspect-Based Sentiment Analysis" dataset](http://metashare.ilsp.gr:8080/repository/download/cd28e738562f11e59e2c842b2b6a04d703f9dae461bb4816a5d4320019407d23/). Unfortunately you have to create an account there, because we are not allowed to redistribute this dataset directly due to licensing issues.


To check if the setup process was completed, go to [`localhost:8888`](http://localhost:8888/lab),
select "new console: Python 3" and type the following lines into the console:
```python
import spacy
nlp = spacy.load("en_core_web_sm")
```
If the code doesn't crash, everything was installed correctly.

## Workshop

During the workshops, we will be:
- learning about NLP from notebooks: [1-NLP-Introduction.ipynb](1-NLP-Introduction.ipynb) and [2-NLP-Glossary.ipynb](2-NLP-Glossary.ipynb)
- going through spaCy library: objects, methods, attributes, etc.
- (optional) building an aspect-based sentiment analysis pipeline on SemEval dataset (for reference implementation see [`utils/SemEval.ipynb`](utils/SemEval.ipynb))
- (optional) building a standard sentiment analysis pipeline for Guardian articles (for reference implementation see [`utils/TheGuardian.ipynb`](utils/TheGuardian.ipynb))
