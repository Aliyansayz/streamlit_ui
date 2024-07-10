 import streamlit as st
import pandas as pd
import random

# Initial data
data = {
    'Category': [
        'Hydration', 'Exercise', 'Diet', 'Exercise', 'Sleep',
        'Mental Health', 'Nature', 'Hydration', 'Diet', 'Mental Health'
    ],
    'Fact': [
        "Drinking water can help improve your skin's health. Staying hydrated is essential for your overall health, helping with energy levels and brain function. 💧",
        "Exercise can boost your mood and reduce symptoms of depression. Physical activity releases endorphins, which improve your mental health. 🏃‍♂️",
        "A healthy diet can improve your overall well-being. Eating a variety of fruits and vegetables reduces the risk of chronic diseases. 🥗",
        "Regular physical activity can help you maintain a healthy weight. It also strengthens your bones and muscles, and improves cardiovascular health. ⚖️",
        "Getting enough sleep is crucial for good health. Quality sleep boosts your immune system, supports growth and development, and improves cognitive function. 🛌",
        "Mental health is just as important as physical health. Practicing mindfulness and managing stress can lead to better emotional and psychological well-being. 🧠",
        "Spending time in nature can reduce stress levels. Nature exposure can improve mood, reduce anxiety, and enhance feelings of well-being. 🌳",
        "Staying hydrated can improve brain function and energy levels. Proper hydration helps maintain the balance of body fluids and supports metabolic processes. 🚰",
        "Eating a variety of fruits and vegetables can reduce the risk of chronic diseases. A balanced diet provides essential nutrients and supports overall health. 🍇🥦",
        "Laughter can boost your immune system. It can also reduce stress hormones and increase the release of endorphins, promoting an overall sense of well-being. 😂"
    ]
}
df = pd.DataFrame(data)

# Set the title and description
st.title("Health, Body, Mind & Wellness Encyclopedia 🌿")
st.markdown("""
Welcome to the Health, Body, Mind & Wellness Encyclopedia! Here, you'll find interesting and surprising facts about health and wellness. Explore the trivia, learn something new, and stay healthy! 💪🧘‍♀️🍎
""")

# Sidebar content
st.sidebar.header("Menu")
documents = ["Document 5: Wellness Wisdom", "Document 6: The Health Hub", "Document 7: Mind & Body Mastery", "Document 8: Holistic Health Handbook"]

# Search functionality
search_query = st.sidebar.text_input("Search 🔍")
if search_query:
    st.sidebar.write("### Search Results:")
    random_facts = df.sample(n=3)
    for index, row in random_facts.iterrows():
        st.sidebar.markdown(f"**{row['Category']}**: {row['Fact']}")

# Document list in sidebar
with st.sidebar.expander("Documents 📚"):
    for doc in documents:
        st.write(doc)

# Main page content
st.write("### Health Facts")
if st.sidebar.button('Process'):
    st.write("### Random Health Facts:")
    categories = df['Category'].unique()
    for category in categories:
        st.markdown(f"### {category} 🌟")
        facts = df[df['Category'] == category]['Fact'].tolist()
        random_facts = random.sample(facts, min(3, len(facts)))
        for fact in random_facts:
            st.markdown(f"- {fact}")

# Add a footer
st.markdown("""
---
Stay informed and take care of your health! 🌟🌿🍃
""")