import streamlit as st
import replicate


input = {
    "prompt": "Give me a class of classic physics",
    "temperature": 0.95,
    "max_new_tokens": 500
}

for event in replicate.stream(
    "meta/llama-2-7b",
    input=input
):

    st.write(event)
    print(event, end="")
#=> ", he orders a martini. everyone in the place stops and s...
