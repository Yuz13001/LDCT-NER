#Load stanza 
import stanza

#Load the NER model
nlp = stanza.Pipeline(lang='en', processors={'ner': 'tokenize'}, ner_model_path='Model/en_final_nertagger.pt')

#A sample free text
text = "the left lung shows a tiny ground-glass nodule left apex image 111. calcified granuloma left upper lobe image 222."

#Information extraction using NER
doc = nlp(text)
print(*[f'entity: {ent.text}\ttype: {ent.type}' for sent in doc.sentences for ent in sent.ents], sep='\n')
