# app.py
import streamlit as st
import streamlit.components.v1 as components

# Read HTML file
with open("Complete Python Code.html", 'r', encoding='utf-8') as f:
    html_content = f.read()

# Ensure your HTML body is responsive (optional: inject full width style)
responsive_html = f"""
<!DOCTYPE html>
<html>
<head>
    <style>
        html, body {{
            margin: 0;
            padding: 0;
            width: 100%;
            height: 100%;
        }}
        iframe, div {{
            width: 100%;
        }}
    </style>
</head>
<body>
    {html_content}
</body>
</html>
"""

# Set Streamlit layout to wide
st.set_page_config(page_title="HTML Viewer", layout="wide")

# Embed the HTML with full width and height
components.html(responsive_html, height=st.session_state.get("height", 1000), scrolling=True)
