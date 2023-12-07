import streamlit as st

# Initialize st.session_state.beans
st.session_state.beans = st.session_state.get("beans", 0)

st.title("Bean counter :paw_prints:")

addend = st.number_input("Beans to add", 0, 45)
if st.button("Bimbimbambam"):
    st.session_state.beans += addend
st.markdown(f"Beans counted: {st.session_state.beans}")
