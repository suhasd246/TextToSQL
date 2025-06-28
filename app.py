from dotenv import load_dotenv
load_dotenv()

import streamlit as st
import os
import sqlite3
import google.generativeai as genai

# Configure Streamlit page
st.set_page_config(page_title="Gemini SQL Query Generator")

# Configure the API key
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

def get_gemini_response(prompt, question):
    model = genai.GenerativeModel('gemini-1.5-flash')
    response = model.generate_content([prompt[0], question])
    return response.text

def read_sql_query(sql, db):
    connection = sqlite3.connect(db)
    cursor = connection.cursor()
    cursor.execute(sql)
    data = cursor.fetchall()
    connection.commit()
    connection.close()
    return data

# Streamlit UI
st.title("Gemini SQL Query Generator")
st.header("Gemini SQL Query Generator")


prompt=[
    """
    You are an expert in converting English questions to SQL query!
    The SQL database has the name STUDENT and has the following columns - NAME, CLASS, 
    SECTION \n\nFor example,\nExample 1 - How many entries of records are present?, 
    the SQL command will be something like this SELECT COUNT(*) FROM STUDENT ;
    \nExample 2 - Tell me all the students studying in Data Science class?, 
    the SQL command will be something like this SELECT * FROM STUDENT 
    where CLASS="Data Science"; 
    also the sql code should not have ``` in beginning or end and sql word in output

    """


]

##prompt = st.text_input("Enter your prompt")
question = st.text_input("Enter your question")

submit = st.button("Submit")

if submit:
    response = get_gemini_response(prompt, question)
    print(response)
    data = read_sql_query(response, "student.db")
    st.subheader("The Response is")
    for row in data:
        print(row)
        st.write(row)
