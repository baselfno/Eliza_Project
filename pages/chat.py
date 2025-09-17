import time
from quesions.escape_answers import *
from quesions.hilal_info_answers import *
from quesions.player_answers import *
from quesions.achievements_answers import *
from quesions.other_sports_answers import *
from quesions.welcome_answers import *
import streamlit as st
from hilal_data import *
from escaper import *
from condition_map import *
import string



# Function to analyze text and respond to questions
def analyze_question(question):
    # check if there is question mark in question
    had_question_mark = check_question_mark(question)
    
    # remove punctuation
    question = question.translate(str.maketrans('', '', string.punctuation))
    
    # str -> list
    question = question.lower().strip().split()

    # restore question mark if existed
    if had_question_mark:
        question.append('?')
    print(question)


    # check if question is in arabic
    if is_it_in_arabic(question):
        return update_counter("arabic_escape")

    
    # Hi, How are You
    if is_it_about_welcoming(question) and is_it_about_general_health(question):
        return get_welcome(question) + ", " + get_general_health_questions()

    # Hi, Hello, ...
    if is_it_about_welcoming(question):
        return get_welcome(question)
    
    # How are You
    if is_it_about_general_health(question):
        return get_general_health_questions()
    
    # Bye
    if is_it_about_farewell(question):
        return 'Bye'
    
    # if just 2 words. ex: "I like"
    if len(question) < 3 :
            return "what?"
    
    # If it include escape topics. ex [nassr, injuries]
    if is_it_about_escape(question):
        return get_escape_answers(question)

    # Not a question, Does not have [what, when, ...]
    if question_is_about(question) == 'not a question':        
        return update_counter("not_question")
    
    if is_it_other_matches(question):
        return get_other_matches_answers(question)

    # Check if the question is about players
    if is_it_about_players(question): 
        return get_player_questions(question)
    

    # Check if the question is about achievements
    if is_it_about_achievements(question):
        answer = get_achievements_info(question)

        # since achievements keywords are too common answer may be empty string
        if answer:
            return answer

    # Check if the question is about hilal other sports
    if is_it_about_other_sports_answers(question):
        return get_other_sports_answers(question)


    # Check if the question about hilal generally
    if is_it_about_club(question):
        return get_club_answers(question)
    
    # if question is yes/no question, return general answer
    if question_is_about(question) == 'yesno':
        return get_yesno_answers(question)
    
    # Default response if no known conditions were met
    return update_counter("last_escape")


# holds the page elements
def show():
    st.title("Abu Rakan")
    st.write("I am Abu Rakan, Ask me anything about Al-Hilal and I will tell you how Al-Hilal is a great team.")

    # Initialize or persist chat history
    if 'questions' not in st.session_state:
        st.session_state['questions'] = []
    if 'responses' not in st.session_state:
        st.session_state['responses'] = []

    # Display previous messages
    for question, response in zip(st.session_state['questions'], st.session_state['responses']):
        # Display user messages
        with st.chat_message("YOU"):
            st.write(question)
        # Display assistant messages
        with st.chat_message("Abu Rakan"):
            st.write(response)

    # Capture new user input
    question = st.chat_input("chat with Abu Rakan")
    if question:
        # Add the question to session state
        st.session_state['questions'].append(question)
        
        # Display the new messages
        with st.chat_message("YOU"):
            st.write(question)

        time.sleep(2)
        
        with st.chat_message("Abu Rakan"):
            placeholder = st.empty()
            placeholder.write(". ")
            time.sleep(1)
            placeholder.write(". . ")
            time.sleep(1)
            placeholder.write(". . .")
            response = analyze_question(question)
            time.sleep(1)
            placeholder.write(". ")
            time.sleep(1)
            placeholder.write(". .")
            time.sleep(1)
            
            st.session_state['responses'].append(response)
            
            placeholder.write(response)

show()