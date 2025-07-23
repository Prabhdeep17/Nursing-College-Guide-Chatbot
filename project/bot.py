import streamlit as st

st.set_page_config(page_title="Nursing College Admission Bot", layout="centered")

st.title("👩‍⚕️ Nursing College Admission Assistant")
st.write("Namaste! I'm your AI Assistant to help with Nursing College Admissions.")

# Session state to keep track of progress
if 'step' not in st.session_state:
    st.session_state.step = 0

def next_step():
    st.session_state.step += 1

def restart():
    st.session_state.step = 0

step = st.session_state.step

# Chat Flow
if step == 0:
    st.write("Bot: Kya aap Nursing College mein admission lena chahte ho?")
    if st.button("Yes"):
        next_step()
    if st.button("No"):
        st.info("Bot: Koi baat nahi. Agar kabhi admission lena ho toh pooch lena!")
        restart()

elif step == 1:
    st.write("Bot: Apne 12th class mein Biology opt kiya tha?")
    if st.button("Haan (Yes)"):
        next_step()
    if st.button("Nahi (No)"):
        st.warning("Bot: B.Sc Nursing ke liye Biology zaroori hai.")
        restart()

elif step == 2:
    st.success("Bot: Wonderful! Aap eligible hain. Yeh ek 4-year ka program hai jo aapko hospitals aur public health field ke liye train karta hai.")
    if st.button("Aur details chahiye"):
        next_step()
    if st.button("Nahi, bas itna hi"):
        st.info("Bot: Thik hai, kabhi bhi info chahiye ho toh poochna.")
        restart()

elif step == 3:
    st.write("### 📋 Fee Structure")
    st.markdown("""
    - Tuition Fee: ₹60,000  
    - Bus Fee: ₹10,000  
    - Total Yearly Fee: ₹70,000  
    - Installments:  
      • ₹30,000 at admission  
      • ₹20,000 after 1st semester  
      • ₹20,000 after 2nd semester
    """)
    if st.button("Hostel aur Training info chahiye"):
        next_step()
    if st.button("Skip"):
        next_step()

elif step == 4:
    st.write("### 🏨 Hostel & Training")
    st.markdown("""
    **Hostel Facilities:**
    - 24x7 Water & Electricity  
    - CCTV Surveillance  
    - Full-time Warden

    **Training:**
    - Hospital mein real patients ke saath training  
    - Experts ki guidance mein  
    """)
    if st.button("Location ke baare mein batao"):
        next_step()
    if st.button("Skip Location Info"):
        next_step()

elif step == 5:
    st.write("📍 College Location:")
    st.info("College Delhi mein hai. Public transport and metro available hai.")
    if st.button("Reputation ke baare mein?"):
        next_step()
    if st.button("Aage badho"):
        next_step()

elif step == 6:
    st.write("🏅 Reputation:")
    st.success("College INC Delhi se approved hai — degree nationally valid hai.")
    if st.button("Training centres ki info chahiye"):
        next_step()
    if st.button("Skip"):
        next_step()

elif step == 7:
    st.write("🏥 Training Centres:")
    st.markdown("""
    - District Hospital, Backundpur  
    - Regional Hospital, Chartha  
    - Community Health Centres  
    - Ranchi Neurosurgery & Allied Sciences Hospital  
    """)
    if st.button("Scholarship info?"):
        next_step()
    if st.button("Skip"):
        next_step()

elif step == 8:
    st.write("🎓 Scholarships Available:")
    st.markdown("""
    - Post-Matric Scholarship: ₹18,000–₹23,000  
    - Labour Ministry Scholarship: ₹40,000–₹48,000 (if registered)  
    """)
    st.info("Application simple hai. Humari team help karti hai.")
    if st.button("Seat info?"):
        next_step()
    if st.button("Next"):
        next_step()

elif step == 9:
    st.write("📊 Total Seats:")
    st.warning("60 seats hi available hain. Admission competitive hai, apply early!")
    if st.button("Age Limit aur Eligibility"):
        next_step()
    if st.button("Skip"):
        next_step()

elif step == 10:
    st.write("✅ Eligibility & Age Limit")
    st.markdown("""
    - 12th mein Biology hona chahiye  
    - PNT Entrance Test clear karna  
    - Age between 17 to 35 years  
    """)
    if st.button("Mujhe admission lena hai"):
        next_step()
    if st.button("Main eligible nahi hoon"):
        st.warning("Koi baat nahi. Kisi ko recommend karna ho toh pooch lena!")
        restart()

elif step == 11:
    st.success("🎉 Great! Registration link and further steps will be shared with you. Best of luck!")
    if st.button("Start Over"):
        restart()