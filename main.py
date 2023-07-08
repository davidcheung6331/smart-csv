from dotenv import load_dotenv
import os
import streamlit as st
import pandas as pd
from pandasai import PandasAI
from pandasai.llm.openai import OpenAI
import streamlit as st
from PIL import Image

# requirements.txt
# pandasai 
# streamlit
# OpenAI


st.set_page_config(
    page_title="CSV Analysis",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded",
)

hide_menu_style = """
        <style>
        #MainMenu {visibility: hidden;}
        </style>
        """
st.markdown(hide_menu_style, unsafe_allow_html=True)
image = Image.open("bot-human-2.jpg")
st.image(image, caption='created by MJ')


st.title("🤖  :blue[CSV Smart Analysis]")

system_openai_api_key = os.environ.get('OPENAI_API_KEY')
system_openai_api_key = st.text_input(":key: OpenAI Key :", value=system_openai_api_key)
os.environ["OPENAI_API_KEY"] = system_openai_api_key

llm = OpenAI(api_token=system_openai_api_key)
# create PandasAI object, passing the LLM
pandas_ai = PandasAI(llm)


uploaded_file = st.file_uploader("📂 upload a csv file for analysis", type=['csv'])
if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)
        st.write(df.head(10))

        prompt = st.text_area("Ask your CSV :")

        if st.button("Generate"):
            with st.spinner("Generating ...."):
                st.write("Generate your results")   
                result = pandas_ai.run(df, prompt)
                st.info(result)

 








