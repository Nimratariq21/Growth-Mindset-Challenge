import streamlit as st

st.set_page_config(page_title = "growth mindset project", project_icon = "★")
st.title("Growth Mindset Project")
st.header("🚀 Welcome to your growth journey!")
st.write("Embrace challenges, learn from mistakes, and unlock your full potential.This Al powered app helps you build a growth mindset with reflection, challenges and achievements! 🌟")

# qoute section

st.header("💡 Today's Growth Mindset Qoute")
st.write("Sucess is not final, Failure is not fatal: it is a courage to continue that counts.""-Winston churchil")

st.header("🔧 what's your challenge today?")
user_input = st.text_input("Describe a challenge you're facing:") 

#conditions
if user_input:
    st.success(f"💪 you're facing {user_input}. Keep pushing forward towards your goals!")
else:
    st.warning("Tell us about your challenge to get started!")

#reflecing
st.header("Reflect on your learning")
reflection = st.text_area("Write your reflection here:")

if reflection:
    st.success(f"✨ Great Insight! Your reflection: {reflection}")
else:
    st.info("Reflecting on past experience help you grow! Share your difficulties:")


#achievements
st.header("🏆 Celebrate your  wins!")
achievements = st.text_input("Share something you've recently achieve:")

if achievements:
    st.success(f"🎊Amazing! You achieved: {achievements}")
else:
    st.info("Big or small, every achievement counts! share one now 🤩")    


#footer
st.write("- - -")
st.write("🚀 Keep believing in yourself. Growth is a journey not a destination 🌟")
st.write("**Created by Nimra Siddique!**")