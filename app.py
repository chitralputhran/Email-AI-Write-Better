import streamlit as st 
from langchain_openai import ChatOpenAI

from langchain.prompts import (
    ChatPromptTemplate,
    SystemMessagePromptTemplate,
    HumanMessagePromptTemplate
)

from prompts import system_prompt, user_prompt

# Constants
PAGE_TITLE = "Email AI"
PAGE_ICON = "📧"
OPENAI_MODEL_NAME = "gpt-4"
OPENAI_API_KEY_PROMPT = 'OpenAI API Key'



# Set page config
st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON, initial_sidebar_state="collapsed")
st.header("",divider='blue')
st.title(f"📧 :blue[_{PAGE_TITLE}_] | Write better emails")
st.header("",divider='blue')

# Get OpenAI API key
openai_api_key = st.sidebar.text_input(OPENAI_API_KEY_PROMPT, type='password')

if not openai_api_key.startswith('sk-'):
    st.info("Please add your OpenAI API key in the sidebar to continue.")
    st.stop()

with st.sidebar:
        
    st.divider()
    
    st.write('*Your email generation flow begins with giving us the sender and reciever names along with the style of the email.*')
    st.caption('''**That's it! 
               Once we have it, we'll understand it and start exploring our options.
                Then, we'll work together to and come up with the best possible email.**
    ''')

    st.divider()


# Form inputs
with st.form("email_info"):

    email_topic = st.text_input(
            "Give us an overview of this email",
            placeholder= "Development update on a project",
        )

    email_tone = st.selectbox(
            "Lets set the tone for the email",
            ('Professional', 'Casual', 'Persuasive', 'Friendly', 'Instructive')
        )
    
    num_of_lines = st.slider('How many line?', 2, 50, 10)
    
    sender_name = st.text_input(
            "Name of the Sender",
            placeholder= "You can add your name here.",
        )
    
    receiver_name = st.text_input(
            "Name of the Receiver",
            placeholder= "To whom you are sending this email.",
        )
    
    submitted = st.form_submit_button("Give me that email!")



if submitted: 
    system_message_prompt = SystemMessagePromptTemplate.from_template(system_prompt)
    human_message_prompt = HumanMessagePromptTemplate.from_template(user_prompt)
    chat_prompt = ChatPromptTemplate.from_messages([system_message_prompt, human_message_prompt])
    
    request = chat_prompt.format_prompt(
        email_topic=email_topic, 
        email_tone=email_tone, 
        num_of_lines = num_of_lines, 
        sender_name =  sender_name, 
        receiver_name = receiver_name
        ).to_messages()

    st.divider()
    
    st.subheader("Email: ")
    with st.spinner('Please wait...'):
        chat = ChatOpenAI(model_name=OPENAI_MODEL_NAME, temperature=0.2, openai_api_key=openai_api_key)

        result = chat(request)

        st.write(result.content)
        st.divider()