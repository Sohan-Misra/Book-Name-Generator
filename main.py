import streamlit as st
import langchain_helper
st.title("Book name generator.")

genre = st.sidebar.selectbox("Pick a genre",("Science Fiction","Fantasy","Dark Fantasy","Historical Fiction","Romance","Horror","Mystery"))



if genre:
    response = langchain_helper.generate_book_name_and_chapters(genre)
    st.header(response['title'].strip('# '))
    chapters = response['chapters'].strip().split('\n')
    st.write("**Chapter Names**")
    for idx,name in enumerate(chapters,start=1):
        if name.strip():
            st.write(f"{name.strip('***')}")