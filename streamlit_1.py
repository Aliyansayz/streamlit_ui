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
        "Drinking water can help improve your skin's health. 💧",
        "Exercise can boost your mood and reduce symptoms of depression. 🏃‍♂️",
        "A healthy diet can improve your overall well-being. 🥗",
        "Regular physical activity can help you maintain a healthy weight. ⚖️",
        "Getting enough sleep is crucial for good health. 🛌",
        "Mental health is just as important as physical health. 🧠",
        "Spending time in nature can reduce stress levels. 🌳",
        "Staying hydrated can improve brain function and energy levels. 🚰",
        "Eating a variety of fruits and vegetables can reduce the risk of chronic diseases. 🍇🥦",
        "Laughter can boost your immune system. 😂"
    ]
}
df = pd.DataFrame(data)

# Set the title and description
st.title("Health Trivia Facts 🌿")
st.markdown("""
Welcome to the Health Trivia Facts page! Here, you'll find interesting and surprising facts about health and wellness. Explore the trivia, learn something new, and stay healthy! 💪🧘‍♀️🍎
""")

# Function to add new fact
def add_fact(category, fact):
    global df
    new_data = {'Category': category, 'Fact': fact}
    df = df.append(new_data, ignore_index=True)
    st.success("New fact added successfully! ✨")

# Show all categories and facts
def show_categories_and_facts():
    categories = df['Category'].unique()
    st.subheader("Available Categories 📚")
    for category in categories:
        st.markdown(f"### {category} 🌟")
        facts = df[df['Category'] == category]['Fact'].tolist()
        for fact in facts:
            st.markdown(f"- {fact}")

# Randomly display 3 facts from each category
def show_random_facts():
    categories = df['Category'].unique()
    st.subheader("Random Health Facts 🎲")
    for category in categories:
        st.markdown(f"### {category} 🌟")
        facts = df[df['Category'] == category]['Fact'].tolist()
        random_facts = random.sample(facts, min(3, len(facts)))
        for fact in random_facts:
            st.markdown(f"- {fact}")

# Buttons to show all categories and random facts
if st.button('Show All Categories'):
    show_categories_and_facts()

if st.button('Show Random Facts'):
    show_random_facts()

# Form to add a new fact
st.subheader("Add a New Health Fact ✍️")
with st.form("Add Fact"):
    category = st.selectbox("Select Category", df['Category'].unique())
    new_fact = st.text_input("Enter the new fact")
    submit_button = st.form_submit_button(label="Add Fact")
    if submit_button:
        add_fact(category, new_fact)

# Add a footer
st.markdown("""
---
Stay informed and take care of your health! 🌟🌿🍃
""")
