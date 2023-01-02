import streamlit as st
import asyncio
import httpx

async def get_response(client: httpx., url, file):
        resp = await client.post(url,file)
        pokemon = resp.json()
        return pokemon


async def main(files):

    async with httpx.AsyncClient() as client:

        tasks = []
        
        # uploaded_files = st.file_uploader("upload file",accept_multiple_files=True)
        # submit = st.button(label="submit")

        if uploaded_files is not None and submit is True:
            for uploaded_file in uploaded_files:
                url = 'http://127.0.0.1:8000/uploadfile/'
                st.write("filename:", uploaded_file.name)
                tasks.append(asyncio.ensure_future(get_response(client,url,uploaded_file)))

        responses = await asyncio.gather(*tasks)
        for response in responses:
            st.write(response)


uploaded_files = st.file_uploader("upload file",accept_multiple_files=True)
submit = st.button(label="submit")

if uploaded_files is not None and submit is True:
    asyncio.run(main(uploaded_files))
# uploaded_files = st.file_uploader("Choose a CSV file", accept_multiple_files=True)
# submit = st.button(label="submit")
# if uploaded_files is not None and submit is True:
#     for uploaded_file in uploaded_files:
#         st.write("filename:", uploaded_file.name)
#         res = rt.post("127.0.0.1:8000/uploadfile/",files=uploaded_file)
#         st.write(res.json())
