import streamlit as st
import requests
# import httpx

uploaded_file = st.file_uploader("uploadfile")
submit = st.button(label="submit")

url = "http://localhost:8000/uploadfile/"

if uploaded_file is not None and submit is True:
    st.write(f"uploading {uploaded_file.name}")
    file = {"file": (uploaded_file.name, uploaded_file.getvalue())}
    res = requests.post(url,files=file)
    content = res.json()
    st.write(f"res = {res}")
    st.write(f"content = {content}")
    st.write("done")

# elif uploaded_file is None and submit is True:
#     st.write("NO files choosen")

# files = {'upload-file': open('report.xls', 'rb')}
# r = httpx.post("https://httpbin.org/post", files=files)
# url = "http://localhost:8000/uploadfile/"

# uploaded_files = st.file_uploader("uploadfiles", accept_multiple_files=True)
# submit = st.button(label="submit")
# if uploaded_files is not None and submit is True:
#     with httpx.Client() as client:
#         for uploaded_file in uploaded_files:
#             st.write("filename:", uploaded_file.name)
#             file = {'upload-file': uploaded_file.getvalue()}
#             res = client.post(url, files=file)
#             st.write(res.json())