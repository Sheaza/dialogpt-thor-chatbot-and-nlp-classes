import streamlit as st
import torch
import transformers
from streamlit_chat import message
from transformers import AutoTokenizer, AutoModelForCausalLM

st.set_page_config(
    page_title="Thor kinda bot demo",
    page_icon=":robot:"
)


@st.cache(hash_funcs={transformers.AutoTokenizer: hash}, suppress_st_warning=True, allow_output_mutation = True)
def load_data():
    tokenizer = AutoTokenizer.from_pretrained('microsoft/DialoGPT-small', padding_side="right")
    model = AutoModelForCausalLM.from_pretrained('thor-small')
    return tokenizer, model


tokenizer, model = load_data()
st.header("Thor kinda bot - Demo")

if 'generated' not in st.session_state:
    st.session_state['generated'] = []
    st.session_state["chat_history_ids"] = None

if 'past' not in st.session_state:
    st.session_state['past'] = []


def query(input):
    new_user_input_ids = tokenizer.encode(input + tokenizer.eos_token, return_tensors='pt')
    bot_input_ids = torch.cat([st.session_state.chat_history_ids, new_user_input_ids], dim=-1) if len(st.session_state.past) > 0 else new_user_input_ids
    st.session_state.chat_history_ids = model.generate(
        bot_input_ids, max_length=2000,
        pad_token_id=tokenizer.eos_token_id,
        no_repeat_ngram_size=3,
        do_sample=True,
        top_k=100,
        top_p=0.92,
        temperature=0.8,
    )
    return tokenizer.decode(st.session_state.chat_history_ids[:, bot_input_ids.shape[-1]:][0], skip_special_tokens=True)


def get_text():
    input_text = st.text_input("You: ", key="input")
    return input_text


user_input = get_text()

if user_input:
    output = query(user_input)

    st.session_state.past.append(user_input)
    st.session_state.generated.append(output)

if st.session_state['generated']:

    for i in range(len(st.session_state['generated'])-1, -1, -1):
        message(st.session_state["generated"][i], key=str(i))
        message(st.session_state['past'][i], is_user=True, key=str(i) + '_user')
