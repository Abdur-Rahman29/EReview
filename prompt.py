# prompts.py
from datetime import datetime
import streamlit as st
def explain_code_prompt(code):
    return (
        "Explain what the following code is trying to do in a few lines:\n"
        f"Code: {code}"
    )

def identify_errors_prompt(code):
    return (
        "Identify if any URLs are present and classify its risk level in 3 lines:\n"
        f"Code: {code}"
    )

def complete_review_prompt(code, org_standards):
    return (
        "Generate a complete code review for the following code file, "
        "including suggested improvements based on the provided organization standards:\n"
        f"Standards: {org_standards}\n"
        f"Code: {code}"
    )

def summary_review_prompt(code, org_standards):
    return (
        "Provide a summary of code review for the following code file in less than 15 lines based on the standards:\n"
        f"Standards: {org_standards}\n"
        f"Code: {code}"
    )

def modified_code_prompt(code, modified_code_context, org_standards):
    return (
        "\nGiven the following modified code with changes denoted by '+' and '-' and the full code for context, please provide suggestions:\n"
          f"Modified Code:\n{modified_code_context}\n\n"
          f"Full Code for context:\n{code}\n\n"
          "Provide suggested improvements based on the provided organization standards:\n"
          f"Standards: {org_standards}"
    )
def modified_code_prompt_summary(code, modified_code_context, org_standards):
    return (
        "Provide a summary of code review focusing on the modified sections of the code in less than 15 lines based on the standards:\n"
        f"Modified Code:\n{modified_code_context}\n\n"
        f"Full Code for context:\n{code}\n\n"
        f"Standards: {org_standards}"
    )
def review_with_old(button_type,code_to_review,modified_code_context,code_file_content,org_standards_documents,client,review_output):
    explain_prompt = explain_code_prompt(code_to_review)
    if modified_code_context:
        explain_prompt += f"Explain modified Added changes('+') and removed changes('-') only. Full Code for context:\n{code_to_review}\nModified Code:\n{modified_code_context}\n"
    explain_response = client.chat.completions.create(messages=[{"role": "user", "content": explain_prompt}], model="llama3-8b-8192")
    explanation = explain_response.choices[0].message.content

    error_prompt = identify_errors_prompt(code_to_review)
    if modified_code_context:
        error_prompt += f"Focus on Modified changes only.\nFull Code for context:\n{code_to_review}\nModified Code:\n{modified_code_context}\n"
    error_response = client.chat.completions.create(messages=[{"role": "user", "content": error_prompt}], model="llama3-8b-8192")
    syntax_errors = error_response.choices[0].message.content

    if modified_code_context:
      if button_type=="complete":
        review_prompt = modified_code_prompt(code_to_review, modified_code_context, org_standards_documents) 
      else:
        review_prompt=modified_code_prompt_summary(code_to_review,modified_code_context,org_standards_documents)
    else:
      if button_type=="complete":
        review_prompt=complete_review_prompt(code_to_review,org_standards_documents)                
      else:
        review_prompt=summary_review_prompt(code_to_review,org_standards_documents)  
    review_response = client.chat.completions.create(messages=[{"role": "user", "content": review_prompt}], model="llama3-8b-8192")
    review = review_response.choices[0].message.content

    final_output = (
        f"<strong>Explanation:</strong> {explanation}<br><br>"
        f"<strong>URL Detection:</strong> {syntax_errors}<br><br>"
        f"<strong>Code Review:</strong> {review}<br><br>"
    )

    st.session_state.history.append({
        "query": code_file_content,
        "response": final_output,
        "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    })
    review_output.markdown(f"<div class='response-box'>{final_output}</div>", unsafe_allow_html=True)

def review(button_type,code_to_review,code_file_content,org_standards_documents,client,review_output):
    explain_prompt = explain_code_prompt(code_to_review)
    explain_response = client.chat.completions.create(messages=[{"role": "user", "content": explain_prompt}], model="llama3-8b-8192")
    explanation = explain_response.choices[0].message.content

    error_prompt = identify_errors_prompt(code_to_review)
    error_response = client.chat.completions.create(messages=[{"role": "user", "content": error_prompt}], model="llama3-8b-8192")
    syntax_errors = error_response.choices[0].message.content

    review_prompt = (summary_review_prompt(code_to_review, org_standards_documents) if button_type == "summary" 
                    else complete_review_prompt(code_to_review, org_standards_documents))
    review_response = client.chat.completions.create(messages=[{"role": "user", "content": review_prompt}], model="llama3-8b-8192")
    review = review_response.choices[0].message.content


    final_output = (
        f"<strong>Explanation:</strong> {explanation}<br><br>"
        f"<strong>URL Detection:</strong> {syntax_errors}<br><br>"
        f"<strong>Code Review:</strong> {review}<br><br>"
    )

    st.session_state.history.append({
        "query": code_file_content,
        "response": final_output,
        "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    })
    review_output.markdown(f"<div class='response-box'>{final_output}</div>", unsafe_allow_html=True)
