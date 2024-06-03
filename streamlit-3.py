import streamlit as st
import spacy 

nlp = spacy.load("en_core_web_lg")


def extract_entities(ent_types, text):
    results = []
    doc = nlp(text)
    for ent in doc.ents:
        if ent.label_ in ent_types:
            results.append((ent.text, ent.label_))

    return results

st.title('Lesson 01.03: Forms in Streamlit')

form1 = st.sidebar.form(key='form1')
form1.header('Parameters')
ent_types = form1.multiselect('Select the entity you want to extract', ["PERSON", "ORG", "GPE"])

form1.form_submit_button('Submit')
text = st.text_area("Sample text", "John Doe is a software engineer at Google in Amman, Jordan.")


hits = extract_entities(ent_types, text)
st.write(hits)