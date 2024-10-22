import os
import streamlit as st
from groq import Groq
from datetime import datetime
import pandas as pd
from functions import load_documents_from_files,extract_changed_code,parse_diff,compare_code,display_error_tabs,calculate_score,calculate_severity,determine_severity_from_score,detect_vulnerabilities,severity
from prompt import review_with_old,review
from styles import get_styles  # Import your styles
import re

groq_api_key = "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"

st.markdown(get_styles(), unsafe_allow_html=True)

image_path = "/content/Picture1.png"  # Adjust this path if needed
if os.path.exists(image_path):
    st.image(image_path, width=700,)
else:
    st.warning("Image not found at the specified path.")

st.title("EReview Bot")

client = Groq(api_key=groq_api_key)

class Document:
    def __init__(self, content, metadata={}):
        self.page_content = content
        self.metadata = metadata

if "history" not in st.session_state:
    st.session_state.history = []

org_standards_file = st.file_uploader("Upload Org Standards File (starts with 'EStandards'):", 
                                       type=["txt", "docx", "pdf","pptx"])
if org_standards_file:
  code_file = st.file_uploader("Upload New Code File :", 
                                type=["py", "js", "java", "html", "css","cpp",])
  old_code_file = st.file_uploader("Upload Old Code File :", 
                                    type=["py", "js", "java", "html", "css","cpp"])

if org_standards_file and not org_standards_file.name.startswith("EStandards"):
    st.warning("The Org standards file must start with 'EStandards'.")

if org_standards_file and code_file and org_standards_file.name.startswith("EStandards"):
    org_standards_documents = load_documents_from_files([org_standards_file])
    
    if code_file:
        code_file_content = code_file.getvalue().decode("utf-8")
        st.success("New code uploaded successfully. Ready for further processing.")
       
        error_count=display_error_tabs(code_file_content, client,org_standards_documents)
        
        old_code_content = ""
        if old_code_file:
            old_code_content = old_code_file.getvalue().decode("utf-8")

        if old_code_content:
          
            changes = extract_changed_code(old_code_content, code_file_content)

            if len(changes) > 2:  # If there's more than just the header
                st.info("The new code is classified as 'Modified'.")

                parsed_changes = parse_diff(old_code_content,code_file_content,changes)
                df_changes = pd.DataFrame(parsed_changes)
                with st.expander("Changes", expanded=False):
                  st.dataframe(df_changes)
                st.markdown(f"**Code Classification:** The new code is classified as: **{'Modified'}**")

                review_type = st.radio("Select Review Type:", options=["Modified Code", "Entire New Code"])

                col1, col2 = st.columns(2)
                with col1:
                    complete_button = st.button("Complete Code Review")

                with col2:
                    summary_button = st.button("Summary")

                review_output = st.empty()

                code_to_review = code_file_content
                modified_code_context = '\n'.join(changes) if review_type == "Modified Code" else None

                
                if complete_button:
                    review_with_old("complete",code_to_review,modified_code_context,code_file_content,org_standards_documents,client,review_output)
                    score=calculate_score(org_standards_documents,code_to_review,client)
                    with st.expander("Score Explanation"):
                        st.write(f"Explanation: {score}")
                    total_score=calculate_severity(error_count)
                    determine_severity_from_score(total_score)
                    severity(error_count,total_score,code_to_review)

                if summary_button:
                    review_with_old("summary",code_to_review,modified_code_context,code_file_content,org_standards_documents,client,review_output)
                    score=calculate_score(org_standards_documents,code_to_review,client)
                    total_score=calculate_severity(error_count)
                    determine_severity_from_score(total_score)
                    severity(error_count,total_score,code_to_review)
        else:
            col1, col2 = st.columns(2)
            with col1:
                complete_button = st.button("Complete Code Review")


            with col2:
                summary_button = st.button("Summary")

            # Define the output area below the buttons
            review_output = st.empty()

            code_to_review = code_file_content

            
            if complete_button:
                review("complete",code_to_review,code_file_content,org_standards_documents,client,review_output)
                score=calculate_score(org_standards_documents,code_to_review,client)
                with st.expander("Score Explanation"):
                    st.write(f"Explanation: {score}")
                total_score=calculate_severity(error_count)
                determine_severity_from_score(total_score)
                severity(error_count,total_score,code_to_review)
            if summary_button:
                review("summary",code_to_review,code_file_content,org_standards_documents,client,review_output)
                score=calculate_score(org_standards_documents,code_to_review,client)
                total_score=calculate_severity(error_count)
                determine_severity_from_score(total_score)
                severity(error_count,total_score,code_to_review)
             
# Footer
st.markdown("<footer>&copy; 2024 Everi Holdings. All rights reserved.</footer>", unsafe_allow_html=True)
