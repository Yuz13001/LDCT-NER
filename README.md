# LDCT NER
An open source NER model for lung cancer screening LDCT reports.

To use this NER model, you need to install Stanza in Python first. 

To load the model, please find the demo below:

```python
import stanza
nlp = stanza.Pipeline(lang='en', processors={'ner': 'tokenize'}, ner_model_path='Model/en_final_nertagger.pt')

text = "the left lung shows a tiny ground-glass nodule left apex image 111. calcified granuloma left upper lobe image 222."

doc = nlp(text)
print(*[f'entity: {ent.text}\ttype: {ent.type}' for sent in doc.sentences for ent in sent.ents], sep='\n')

```



