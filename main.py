from openai import OpenAI
import os
from dotenv import load_dotenv
load_dotenv()
import streamlit as st


st.title("shyari generator")
user_input=st.text_input("enter keyword")
button=st.button("submit")
if button and user_input:
    
    client = OpenAI(
      api_key=os.environ.get("api_key"),
    )
    completion = client.chat.completions.create(
      model="gpt-4o-mini",
      messages=[
        {"role": "system", "content": "You are good at hindi Shayari "},
        {"role": "user", "content": f"compose a shyari inhindi language first and then in english based on keyword: {user_input}"}
      ]
    )

    print(completion.choices[0].message.content)
    st.text_area("shyeri",completion.choices[0].message.content,height=800)
