import fitz
import streamlit as st
import os

result = fitz.open()
pages_count =[]

def save_uploadedfile(uploadedfile, save_path):
    try:
        with open(os.path.join(save_path,uploadedfile.name),"wb") as f:
            f.write(uploadedfile.getbuffer())
        #return st.success("Saved File:{} to Downloads".format(uploadedfile.name))
        return st.success(f"Saved File: {uploadedfile.name} to {save_path}")
    except PermissionError as e:
        return st.error(f"Permission denied: {e}")

uploaded_pdf = st.file_uploader("Upload pdf ", type=['pdf'], accept_multiple_files=True)
save_path = st.text_input("Enter the directory to save files", "C:/Users/john.tan/Downloads/")

for pdf in uploaded_pdf:
      
    if pdf is not None:
        doc = fitz.open(stream=pdf.read(), filetype="pdf")
        text = ""
        for page in doc:
            text += page.get_text()
        st.write("Number of pages: ", doc.page_count)
        #st.write(text)
        result.insert_pdf(doc)
        pages_count.append(doc.page_count)
        doc.close()

if st.button("Save Merged PDF"):
    result.save(os.path.join(save_path, "merge-result.pdf"))
    #save_uploadedfile(result, save_path)
#result.save("C:/Users/john.tan/Downloads/merge-result.pdf")

st.write("Total number of pages: ", sum(pages_count))
#https://discuss.streamlit.io/t/how-to-use-pymupdf-to-read-a-pdf-after-uploading-that-via-st-file-uploader/7268/4
