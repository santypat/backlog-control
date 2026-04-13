import streamlit as st

def load_styles():

    st.markdown("""
    <style>

    .main-header{
        font-size:2.5rem;
        font-weight:700;
        color:#1f77b4;
    }

    .task-card{
        background:white;
        padding:1rem;
        border-radius:8px;
        border-left:4px solid #667eea;
    }

    </style>
    """, unsafe_allow_html=True)