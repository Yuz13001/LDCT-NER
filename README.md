# LDCT NER
This is an open source NER model for lung cancer screening LDCT reports. 

To use this NER model, you need to install Stanza in Python first. Please find the installation guide at [stanfordnlp/stanza: Official Stanford NLP Python Library for Many Human Languages (github.com)](https://github.com/stanfordnlp/stanza)



To load and use the NER model, simply following the steps below:

```python
#Load stanza 
import stanza

#Load the NER model
nlp = stanza.Pipeline(lang='en', processors={'ner': 'tokenize'}, ner_model_path='Model/en_final_nertagger.pt')

#A sample free text
text = "the left lung shows a tiny ground-glass nodule left apex image 111. calcified granuloma left upper lobe image 222."

#Information extraction using NER
doc = nlp(text)
print(*[f'entity: {ent.text}\ttype: {ent.type}' for sent in doc.sentences for ent in sent.ents], sep='\n')

```



