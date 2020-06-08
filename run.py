import streamlit as st
import plotly.graph_objects as go

if __name__ == "__main__":

    '''# Easy Sankey maker'''
    '''Enter connections, e.g. "A 100 B; A 10 C; A 50 D; D 10 A"'''

    sankey = [
        "A 100 B", 
        "A 10 C",
        "A 50 D",
        "D 10 A"
    ]

    inputs = st.text_input("Enter connections, separated by ;") 

    if inputs:
        sankey = [i.strip() for i in inputs.split(";")]
    
    sankey


    sksource = [w.split(" ")[0].replace("_", " ") for w in sankey]
    sktarget = [w.split(" ")[2].replace("_", " ") for w in sankey]
    labels=labels=list(set(list(set(sksource)) + list(set(sktarget))))

    sksource_index = [labels.index(i) for i in sksource]
    sktarget_index = [labels.index(i) for i in sktarget]
    skvalues = [w.split(" ")[1] for w in sankey]


    links=dict(source=sksource_index,
    target=sktarget_index,
    value=skvalues)

    fig = go.Figure(data=[go.Sankey(
        node = dict(
        pad = 15,
        thickness = 20,
        line = dict(color = "black", width = 0.5),
        label = labels,
        color = "blue"
        ),
        link = links)])

    fig.update_layout(title_text=st.text_input("Title"), font_size=10)
    st.write(fig)