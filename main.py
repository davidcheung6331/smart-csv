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

CACHE_FILE_PATH = "/tmp/cache"  # Specify a different location for the cache file


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



load_dotenv()

API_KEY = os.environ['OPENAI_API_KEY']
llm = OpenAI(api_token=API_KEY)
# create PandasAI object, passing the LLM
# pandas_ai = PandasAI(llm)


st.title("🤖  :blue[CSV advanced Analysis by pandasai]")

system_openai_api_key = os.environ.get('OPENAI_API_KEY')
system_openai_api_key = st.text_input(":key: Step 1: Enter your OpenAI Key :", value=system_openai_api_key)
os.environ["OPENAI_API_KEY"] = system_openai_api_key


log = """
Calculate the Total Survival Rate for male and female ?

What are the Average Age of survived male and female ?

"""



uploaded_file = st.file_uploader("Step 2 : 📂 upload sample file - titanic.csv ", type=['csv'])
if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)
        st.caption(f"First 10 records from {uploaded_file.name}")
        st.write(df.head(10))

        with st.expander("Here is the example query, you can copy one statement"):
            st.code(log)

        prompt = st.text_area("Step 3 : Enter your prompt, it will handled by Pandas AI engine :")

        if st.button("Generate"):
            with st.spinner("Generating ...."):
                # st.write("Generate your results")
                pandas_ai = PandasAI(llm, cache_file_path=CACHE_FILE_PATH)  # Pass the cache file path
                result = pandas_ai.run(df, prompt)
                st.info(result)

 








