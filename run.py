import streamlit as st
import plotly.graph_objects as go

if __name__ == "__main__":

    '''# Easy Sankey maker'''

    sankey = [
        "Hello 100 World", 
        "Hello 10 C",
        "Hello 50 D",
        "D 10 Hello"
    ]

    inputs = st.text_area(value="\n".join(sankey), label="Enter connections, one per line") 

    if inputs:
        sankey = [i.strip() for i in inputs.split("\n") if i]
    

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

    fig.update_layout(title_text=st.text_input(label="Title", value="An easy sankey diagram"), font_size=10)
    st.write(fig)


    st.info("This tool is based on plotly and streamlit and is available for free at https://github.com/simonvc/easysankey")