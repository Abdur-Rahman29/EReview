def get_styles():
    return """
    <style>
    /* Main background color */
    .main {
        background-color: #e8f0f2; /* Softer light blue */
        color: #333333; /* Darker text color for contrast */
        font-family: 'Arial', sans-serif;
        display: flex;
        flex-direction: column;
        align-items: center; /* Center align items */
        padding: 10px; /* Padding around the main container */
        width: 200%; /* Set a specific width, adjust as needed */
        margin: 0 auto; /* Center the container */
    }

    /* Title styling */
    h1 {
        text-align: center;
        color: rgb(0, 70, 150); /* Brighter soft blue */
        margin-bottom: 20px; /* Space below the title */
        font-size: 2.5em; /* Increased font size */
        text-shadow: 4px 4px 8px rgba(0, 0, 0, 0.4); /* Subtle shadow for depth */
    }

    /* Button styling */
    .button-container {
        display: flex;
        justify-content: space-between; /* Space buttons to ends */
        width: 100%; /* Full width for buttons */
        margin-top: 20px; /* Space above buttons */
    }

    .stButton > button {
        background-color: rgb(0, 70, 150); /* Soft blue button */
        color: white;
        border: none;
        padding: 12px 24px; /* Increased padding */
        border-radius: 8px; /* More rounded corners */
        cursor: pointer;
        transition: background-color 0.3s, transform 0.2s; /* Smooth transition */
        font-size: 1.1em; /* Slightly larger font */
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1); /* Shadow for depth */
        margin: 10px 0; /* Space between buttons */
    }

    .stButton > button:hover {
        background-color: #005bb5; /* Darker shade on hover */
        transform: translateY(-3px); /* Lift effect on hover */
        box-shadow: 0 4px 10px rgba(0, 0, 0, 0.3); /* Deeper shadow on hover */
    }

    /* Radio button styling */
    .stRadio > div {
        margin: 10px 0; /* Space between radio buttons */
    }

    .stRadio > div > label {
        display: flex;
        align-items: center; /* Center align label and radio */
        cursor: pointer;
        padding: 12px; /* Increased padding for better touch area */
        border-radius: 5px; /* Rounded corners for the label */
        transition: background-color 0.3s, transform 0.2s; /* Smooth background change */
    }

    .stRadio > div > label:hover {
        background-color: rgba(0, 123, 255, 0.1); /* Light hover effect */
    }

    .stRadio > div > input[type="radio"] {
        margin-right: 10px; /* Space between radio button and label */
        cursor: pointer; /* Pointer cursor for better UX */
    }

    /* Focus effect */
    .stRadio > div:focus-within {
        outline: 2px solid rgb(0, 70, 150); /* Outline when focused */
        box-shadow: 0 0 5px rgba(0, 123, 255, 0.5); /* Subtle glow effect */
    }

    /* Dropdown styling */
    .stExpander {
        transition: background-color 0.3s; /* Smooth transition for hover effect */
        width: 100%; /* Full width for expander */
    }

    .stExpander:hover {
        background-color: #e9e9e9; /* Slightly darker on hover */
    }

    /* Tab content styling */
    .tab-content {
        display: flex;
        flex-wrap: wrap; /* Allow wrapping of tab content */
        justify-content: flex-start; /* Align content to the start */
        margin-top: 10px; /* Space above tab content */
        padding: 10px; /* Padding inside tab content */
        width: 100%; /* Full width */
        box-sizing: border-box; /* Include padding in width */
    }

    .tab-item {
        margin: 5px; /* Space between items */
        padding: 10px; /* Padding for each item */
        background-color: #f0f0f0; /* Light background for items */
        border-radius: 5px; /* Rounded corners */
        flex: 1 1 auto; /* Allow items to grow and shrink */
        max-width: calc(100% - 10px); /* Prevent overflow */
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1); /* Light shadow */
    }

    /* Response box styling */
    .response-box {
        background-color: #ffffff; /* White background for response box */
        color: #333333; /* Text color for readability */
        border-radius: 8px;
        padding: 15px; /* Increased padding */
        margin: 10px 0; /* Space between response boxes */
        border-left: 6px solid rgb(0, 70, 150); /* Accent color */
        width: 100%;
        box-shadow: 0 2px 8px rgba(0, 0, 0, 0.15); /* More pronounced shadow */
    }

    /* Footer styling */
    footer {
        text-align: center;
        padding: 20px;
        color: rgb(0, 70, 150); /* Brighter soft blue */
        font-size: 1.1em; /* Slightly larger footer text */
        margin-top: 20px; /* Space above the footer */
    }
    </style>
    """
