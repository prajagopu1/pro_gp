import streamlit as st
import pandas as pd

name=st.text_input("Enter your name:")
fname=st.text_input("Enter your fathe name:")
adr=st.text_area("enter your adress:")
classdata=st.selectbox("enter your class:",(1,2,3,4,5))

button=st.button("done")

if button:
    st.markdown(f"""
               name: {name}\n
             fname: {fname}\n
              adres:  {adr}\n
              {classdata}""")

# def button():
    # pd(f"{name.get(),fname.get(),adr.get(),classdata.get()}")

# st.title("hello ashapuira mandir ")
# st.header("paython")
# st.subheader("java")
# st.markdown("hello python")
# st.code("""for i in range(1,5,1):
#         print("hello gopal")""")