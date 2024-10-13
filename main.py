# pip install --upgrade langchain langchain-google-genai streamlit
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
import os
os.environ["GOOGLE_API_KEY"] = "AIzaSyDLdtIPpcHvLjLeXpmiPlGqut-4VdUx82Q"

tweet_template = "Give me {number} tweets about {topic}"
tweet_prompt = PromptTemplate(template=tweet_template, input_variables=["number", "topic"])
gemini_model = ChatGoogleGenerativeAI(model="gemini-1.5-flash-latest")
tweet_chain = tweet_prompt | gemini_model

#response= tweet_chain.invoke({"number": 5, "topic": "AI"})

import streamlit as st

st.header("Tweet Generator-RAJA")
st.subheader("Generate tweets using Generative AI")

topic= st.text_input("Topic")
number= st.number_input("Number of tweets", min_value=1, max_value=10, value=1, step=1)
if st.button("Generate"):
    tweets= tweet_chain.invoke({"number": number, "topic": topic})
    st.write(tweets.content)



