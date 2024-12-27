import time
import numpy as np
import pandas as pd
import streamlit as st
from MarketSize import plot_top_6_regions
from AiToolsUser import plot_AiToolsUsers
from GenAIText import plot_GenAIText
from GenAIMarketSize import map_plot_Generative_AI_MarketSize, plot_top_6_genAIMarketSize



def set_bg_color(color):
    st.markdown(
        f"""
        <style>
        .reportview-container {{
            background-color: {color};
        }}
        </style>
        """, 
        unsafe_allow_html=True
    )


set_bg_color("lightblue")


st.markdown("<h1 style='text-align: center;'>ARTIFICIAL INTELLIGENCE</h1>", unsafe_allow_html=True)

_A_I = """
Artificial intelligence (AI) is technology that enables computers and machines to simulate human learning, comprehension, problem solving, decision making, creativity and autonomy.
Applications and devices equipped with AI can see and identify objects. They can understand and respond to human language. They can learn from new information and experience. They can make detailed recommendations to users and experts. 
They can act independently, replacing the need for human intelligence or intervention (a classic example being a self-driving car). But in 2024, most AI researchers and practitioners and most AI related headlines are focused on breakthroughs in generative AI (gen AI), a technology that can create original text, images, video and other content. 
"""
st.title("What Is AI?")
def stream_data(Text):
    for word in Text.split(" "):
        yield word + " "
        time.sleep(0.05)
    data = pd.read_csv("merged_data.csv")
    yield pd.DataFrame(data)

def stream_description(Text):
    for word in Text.split(" "):
        yield word + " "
        time.sleep(0.05)

if st.button("AI Description"):
    st.write_stream(stream_data(_A_I))

with st.expander("AI Market Size", expanded=True):
    st.title("Top 5 Regions AI Market Size")
    plot_top_6_regions()  # Call the function to plot the chart
    Description = """
 
        """
    if st.button("Description"):
        st.write_stream(stream_data(Description))


with st.expander("AI Tools User", expanded=True):
    st.title("AI Tools User")
    plot_AiToolsUsers()
    Description2 = """
 
        """
    if st.button("Description 2"):
        st.write_stream(stream_description(Description2))

with st.expander("Generative AI Trend", expanded=True):
    st.title("Generative AI Trend")
    plot_GenAIText()
    Description3 = """
 
        """
    if st.button("Description 3"):
        st.write_stream(stream_description(Description3))

with st.expander("Generative AI Market Size", expanded=True):
    st.title("Generative AI Market Size")
    plot_top_6_genAIMarketSize()
    map_plot_Generative_AI_MarketSize()
    Description4 = """
 
        """
    if st.button("Description 4"):
        st.write_stream(stream_description(Description4))

