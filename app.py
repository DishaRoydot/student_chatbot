import streamlit as st
import os
# =========================================================
# GNIOT × AKTU STUDENT SUPPORT SYSTEM
# =========================================================

st.set_page_config(
    page_title="GNIOT × AKTU Student Support",
    page_icon="🎓",
    layout="wide"
)

# =========================================================
# HEADER
# =========================================================

st.title("🎓 GNIOT × AKTU Student Support")
st.subheader("B.Tech CSE Student Portal")

st.write(
    "Your student assistant for academics, syllabus, exams, "
    "attendance, notes, placements and college enquiries."
)

st.divider()

# =========================================================
# SIDEBAR
# =========================================================

st.sidebar.title("📚 GNIOT Student Portal")

section = st.sidebar.selectbox(
    "Select Section",
    [
        "🤖 Student Chatbot",
        "📚 AKTU Syllabus",
        "📖 Notes",
        "📝 Previous Year Questions",
        "📅 Exam Information",
        "📊 Attendance",
        "🏫 GNIOT Enquiry",
        "💰 Fees & Scholarship",
        "🏠 Hostel",
        "📚 Library",
        "💼 Placements",
        "🚀 Internships",
        "📈 SGPA Calculator",
        "🎯 CGPA Calculator",
        "📢 Important Notices"
    ]
)

# =========================================================
# SEMESTERS
# =========================================================

semesters = [
    "1st Semester",
    "2nd Semester",
    "3rd Semester",
    "4th Semester",
    "5th Semester",
    "6th Semester",
    "7th Semester",
    "8th Semester"
]

# =========================================================
# CSE SUBJECTS
# =========================================================

cse_subjects = {

    "1st Semester": [
        "Engineering Mathematics",
        "Engineering Physics",
        "Engineering Chemistry",
        "Programming for Problem Solving",
        "Basic Electrical Engineering",
        "Engineering Graphics",
        "Soft Skills"
    ],

    "2nd Semester": [
        "Engineering Mathematics",
        "Engineering Physics",
        "Engineering Chemistry",
        "Programming for Problem Solving",
        "Basic Electronics",
        "Engineering Mechanics",
        "Soft Skills"
    ],

    "3rd Semester": [
        "Data Structures",
        "Discrete Mathematics",
        "Digital Logic Design",
        "Computer Organization",
        "Object Oriented Programming",
        "Technical Communication"
    ],

    "4th Semester": [
        "Design and Analysis of Algorithms",
        "Database Management Systems",
        "Operating Systems",
        "Computer Networks",
        "Theory of Computation",
        "Web Technology"
    ],

    "5th Semester": [
        "Software Engineering",
        "Compiler Design",
        "Computer Graphics",
        "Artificial Intelligence",
        "Professional Elective",
        "Open Elective"
    ],

    "6th Semester": [
        "Machine Learning",
        "Cloud Computing",
        "Information Security",
        "Professional Elective",
        "Open Elective",
        "Project / Practical Work"
    ],

    "7th Semester": [
        "Professional Elective",
        "Professional Elective",
        "Open Elective",
        "Project",
        "Seminar"
    ],

    "8th Semester": [
        "Major Project",
        "Professional Elective",
        "Open Elective",
        "Internship / Project Work"
    ]
}

# =========================================================
# CHATBOT
# =========================================================

def chatbot(question):

    q = question.lower()

    if any(x in q for x in ["hello", "hi", "hey"]):
        return """
👋 Hello!

I am the GNIOT × AKTU Student Support Assistant.

You can ask me about:

📚 Syllabus
📝 Exams
📖 Notes
📊 Attendance
🏫 GNIOT enquiry
💰 Fees
🏠 Hostel
💼 Placements
🚀 Internships
📈 SGPA / CGPA
💻 CSE subjects
"""

    if "syllabus" in q:
        return """
📚 AKTU B.Tech CSE Syllabus

Select your semester from the sidebar's AKTU Syllabus section.

For exact current syllabus details, always verify the latest
official AKTU syllabus document.
"""

    if "attendance" in q:
        return """
📊 Attendance

You can calculate your attendance using the Attendance section.

Formula:

Attendance % =
(Classes Attended / Total Classes) × 100

⚠️ College/University attendance requirements should always
be verified from the current official rules.
"""

    if "exam" in q or "datesheet" in q or "date sheet" in q:
        return """
📝 AKTU Examination

For examination information, check:

• Semester examination
• Practical examination
• Internal examination
• Admit card
• Examination centre
• Paper code

⚠️ Examination dates can change. Always verify the latest
official AKTU examination notice.
"""

    if "dsa" in q or "data structure" in q:
        return """
💻 Data Structures Roadmap

Start with:

1. Arrays
2. Strings
3. Linked Lists
4. Stacks
5. Queues
6. Recursion
7. Trees
8. Graphs
9. Sorting
10. Searching
11. Dynamic Programming
"""

    if "python" in q:
        return """
🐍 Python Roadmap

Start with:

• Variables
• Data Types
• Conditions
• Loops
• Functions
• Lists
• Tuples
• Dictionaries
• OOP
• File Handling
• Libraries
"""

    if "placement" in q:
        return """
💼 GNIOT Placement Preparation

For B.Tech CSE placements, focus on:

1. Programming
2. DSA
3. Aptitude
4. Communication
5. Projects
6. Git & GitHub
7. Resume
8. Technical Interviews
9. HR Interviews
"""

    if "internship" in q:
        return """
🚀 Internship Preparation

Start with:

• Programming fundamentals
• DSA
• Projects
• GitHub
• Resume
• LinkedIn
• Interview preparation

Try to build projects that demonstrate your actual skills.
"""

    if "sgpa" in q:
        return """
📈 SGPA

SGPA depends on:

• Subject credits
• Grade obtained in each subject

Use the SGPA Calculator section to calculate it.
"""

    if "cgpa" in q:
        return """
🎯 CGPA

CGPA represents your cumulative academic performance
across semesters.

Use the CGPA Calculator section to calculate an estimate.
"""

    if "fee" in q or "fees" in q:
        return """
💰 Fees & Scholarship

For exact current GNIOT fee amounts, always verify the
latest official college fee notice.

This section can be used for:

• Tuition fees
• Examination fees
• Hostel fees
• Scholarship
• Reimbursement
"""

    if "hostel" in q:
        return """
🏠 GNIOT Hostel

Common hostel-related enquiries include:

• Room allocation
• Hostel rules
• Mess
• Leave
• Maintenance
• Warden
• Hostel fees

For current rules, contact the college hostel administration.
"""

    if "library" in q:
        return """
📚 Library

The library section can provide information about:

• Books
• Reference material
• Study resources
• Library membership
• Book issue/return

Check the current GNIOT library rules for exact timings.
"""

    if "college" in q or "enquiry" in q:
        return """
🏫 GNIOT College Enquiry

Possible departments:

• Academic Department
• Examination Cell
• Accounts
• Admission
• Training & Placement
• Hostel
• Library
• Student Section
• Scholarship

For official contact details, use the latest GNIOT
college information.
"""

    return """
🤖 I don't have a specific answer for that yet.

Try asking:

• What is the CSE syllabus?
• What is DSA?
• How can I prepare for placements?
• How do I calculate SGPA?
• How do I calculate attendance?
• Tell me about internships.
• Tell me about GNIOT hostel.
• Tell me about AKTU exams.
"""
# =========================================================
# STUDENT CHATBOT UI
# =========================================================

if section == "🤖 Student Chatbot":

    st.header("🤖 GNIOT × AKTU Free Student Assistant")

    st.caption(
        "🆓 No OpenAI • No paid API • No API key • "
        "Local PDF search • English + Hinglish"
    )

    # -----------------------------------------------------
    # SESSION STATE
    # -----------------------------------------------------

    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []

    if "pending_question" not in st.session_state:
        st.session_state.pending_question = ""

    if "quiz_questions" not in st.session_state:
        st.session_state.quiz_questions = []

    if "quiz_subject" not in st.session_state:
        st.session_state.quiz_subject = "Subject"

    # -----------------------------------------------------
    # QUICK ACTIONS
    # -----------------------------------------------------

    st.markdown("### ⚡ Quick Actions")

    qa_cols = st.columns(3)

    quick_actions = [
        ("📚 3rd Sem Syllabus", "3rd semester syllabus"),
        ("🧠 DSA Quiz", "DSA quiz"),
        ("📖 Search PDFs", "PPS notes me important topics batao"),
        ("📝 Study Plan", "DBMS 7 day study plan"),
        ("📊 Attendance", "68 out of 100 attendance hai"),
        ("💼 Placement", "CSE placement roadmap"),
    ]

    for col, (label, text) in zip(qa_cols * 2, quick_actions):

        if col.button(
            label,
            use_container_width=True
        ):
            st.session_state.pending_question = text

    st.divider()

    # -----------------------------------------------------
    # CHAT HISTORY
    # -----------------------------------------------------

    for msg in st.session_state.chat_history[-12:]:

        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])

    # -----------------------------------------------------
    # USER INPUT
    # -----------------------------------------------------

    question = st.chat_input(
        "💬 English ya Hinglish mein kuch bhi pucho..."
    )

    # Quick action se question aaya ho
    if st.session_state.pending_question:

        question = st.session_state.pending_question

        st.session_state.pending_question = ""

    # -----------------------------------------------------
    # PROCESS QUESTION
    # -----------------------------------------------------

    if question and question.strip():

        question = question.strip()

        # User message save
        st.session_state.chat_history.append(
            {
                "role": "user",
                "content": question
            }
        )

        # Show user message
        with st.chat_message("user"):
            st.markdown(question)

        # Assistant response
        with st.chat_message("assistant"):

            with st.spinner(
                "🧠 Understanding your question..."
            ):

                try:

                    result = chatbot(question)

                    # -------------------------------------------------
                    # IMPORTANT FIX
                    # chatbot() string return kare to dictionary
                    # mein convert kar do
                    # -------------------------------------------------

                    if isinstance(result, str):

                        result = {
                            "answer": result,
                            "sources": [],
                            "intent": "general"
                        }

                    # Agar chatbot None return kare
                    if result is None:

                        result = {
                            "answer": (
                                "Sorry, mujhe is question ka answer "
                                "generate nahi ho paya."
                            ),
                            "sources": [],
                            "intent": "general"
                        }

                    # Safety check
                    if not isinstance(result, dict):

                        result = {
                            "answer": str(result),
                            "sources": [],
                            "intent": "general"
                        }

                    answer = result.get(
                        "answer",
                        "Sorry, answer generate nahi ho paya."
                    )

                    sources = result.get(
                        "sources",
                        []
                    )

                    # -------------------------------------------------
                    # ANSWER
                    # -------------------------------------------------

                    st.markdown(answer)

                    # -------------------------------------------------
                    # SOURCES
                    # -------------------------------------------------

                    if sources:

                        with st.expander(
                            "📚 Sources used"
                        ):

                            for source in sources:

                                if isinstance(
                                    source,
                                    dict
                                ):

                                    title = source.get(
                                        "title",
                                        "Document"
                                    )

                                    link = source.get(
                                        "link",
                                        ""
                                    )

                                    if link:
                                        st.markdown(
                                            f"📄 [{title}]({link})"
                                        )
                                    else:
                                        st.write(
                                            f"📄 {title}"
                                        )

                                else:
                                    st.write(
                                        f"📄 {source}"
                                    )

                    # -------------------------------------------------
                    # SAVE ASSISTANT RESPONSE
                    # -------------------------------------------------

                    st.session_state.chat_history.append(
                        {
                            "role": "assistant",
                            "content": answer
                        }
                    )

                except Exception as e:

                    st.error(
                        "⚠️ Chatbot mein error aa gaya."
                    )

                    st.code(
                        str(e)
                    )

                    st.info(
                        "Tip: Agar PDF search use karna hai, "
                        "PyMuPDF install karo: "
                        "pip install PyMuPDF"
                    )

    # -----------------------------------------------------
    # QUIZ
    # -----------------------------------------------------

    quiz_questions = st.session_state.get(
        "quiz_questions",
        []
    )

    if quiz_questions:

        st.divider()

        st.subheader(
            f"🧠 {st.session_state.get('quiz_subject', 'Subject')} Quiz"
        )

        score = 0

        for i, item in enumerate(
            quiz_questions
        ):

            # Expected format:
            # (question, options, correct_answer)

            try:

                qtext, options, correct_answer = item

            except Exception:

                continue

            selected = st.radio(
                f"Q{i + 1}. {qtext}",
                options,
                key=f"quiz_answer_{i}"
            )

            if selected == correct_answer:

                score += 1

        if st.button(
            "🏆 Check Quiz Score",
            type="primary"
        ):

            total = len(
                quiz_questions
            )

            st.success(
                f"🎯 Your Score: {score}/{total}"
            )

            if score == total:

                st.balloons()

                st.success(
                    "🔥 Excellent! Perfect score!"
                )

            elif score >= total * 0.7:

                st.info(
                    "👏 Good job! Thoda aur revision karo."
                )

            else:

                st.warning(
                    "📖 Kuch topics revise karke "
                    "quiz dobara try karo."
                )

    # -----------------------------------------------------
    # CLEAR CHAT
    # -----------------------------------------------------

    st.divider()

    clear_col, info_col = st.columns(
        [1, 3]
    )

    with clear_col:

        if st.button(
            "🗑️ Clear Chat",
            use_container_width=True
        ):

            st.session_state.chat_history = []

            st.rerun()

    with info_col:

        with st.expander(
            "ℹ️ How this free chatbot works"
        ):

            st.write(
                """
                🤖 This chatbot uses your project's local
                Python logic and searchable PDF content.

                📚 It can work with PDFs inside:

                • notes/
                • pyq/

                🆓 No OpenAI API is required.

                🔑 No paid API key is required.

                💬 You can ask questions in English,
                Hindi or Hinglish.
                """
            )

            # PyMuPDF status
            if "fitz" in globals():

                st.success(
                    "📚 PDF reader: PyMuPDF available"
                )

            else:

                st.warning(
                    "📚 PDF reader: PyMuPDF not detected. "
                    "Install it using: pip install PyMuPDF"
                )


# =========================================================
# SYLLABUS
# =========================================================

elif section == "📚 AKTU Syllabus":

    st.header("📚 AKTU B.Tech CSE Syllabus")

    semester = st.selectbox(
        "Select Semester",
        semesters
    )

    st.subheader(semester)

    for subject in cse_subjects[semester]:
        st.write("📘", subject)

    st.info(
        "⚠️ Subject lists may vary by AKTU regulation/session. "
        "Verify the latest official syllabus before using it "
        "for examination preparation."
    )

# =========================================================
# NOTES
# =========================================================

elif section == "📖 Notes":

    st.header("📖 Study Notes")

    semester = st.selectbox(
        "Select Semester",
        semesters
    )

    subject = st.selectbox(
        "Select Subject",
        cse_subjects[semester]
    )

    st.info(
        f"📚 Notes for {subject} ({semester})"
    )

    import os
   

    notes_folder = os.path.join(
        os.path.dirname(os.path.abspath(__file__)),
        "notes",
        "ist sem"
    )
    

    # Subject ke according PDF name identify karna
    subject_keywords = {
        "Programming for Problem Solving": ["PPS"],
        "Engineering Physics": ["Physics"],
        "Basic Electrical Engineering": ["electrical"],
        "Engineering Chemistry": ["Chemistry"],
        "Engineering Mathematics": ["Math", "Mathematics","maths1"],
        "Engineering Graphics": ["Graphics"],
        "Soft Skills": ["Soft", "Skill"],
    }

    keywords = subject_keywords.get(subject, [subject])

    if os.path.exists(notes_folder):

        files = os.listdir(notes_folder)

        matching_files = []

        for file in files:

            if file.lower().endswith(".pdf"):

                for keyword in keywords:

                    if keyword.lower() in file.lower():

                        matching_files.append(file)
                        break

        if matching_files:

            st.success(
                f"📚 {len(matching_files)} note(s) found!"
            )

            for pdf in matching_files:

                pdf_path = os.path.join(
                    notes_folder,
                    pdf
                )

                st.write(f"📄 {pdf}")

                with open(pdf_path, "rb") as file:

                    st.download_button(
                        label=f"⬇️ Download {pdf}",
                        data=file.read(),
                        file_name=pdf,
                        mime="application/pdf"
                    )

        else:

            st.warning(
                "📂 Notes for this subject are not available yet."
            )

    else:

        st.error(
            "❌ Notes folder not found."
        )

# =========================================================
# PYQs
# =========================================================


elif section == "📝 Previous Year Questions":

    st.header("📝 Previous Year Questions")

    semester = st.selectbox(
        "Select Semester",
        semesters,
        key="pyq_semester"
    )

    subject = st.selectbox(
        "Select Subject",
        cse_subjects[semester],
        key="pyq_subject"
    )

    PYQ_FOLDER = "pyq"

    pyq_folder_map = {
    "Engineering Mathematics": "maths1",
    "Engineering Physics": "physics",
    "Engineering Chemistry": "chemistry",
    "Programming for Problem Solving": "pps",
    "Basic Electrical Engineering": "electrical",
    "Engineering Graphics": "fme",
    "Environmental Studies": "evs"
}
       
   
    folder_name = pyq_folder_map.get(subject)

    if folder_name:

        subject_folder = os.path.join(
            PYQ_FOLDER,
            folder_name
        )

        if os.path.exists(subject_folder):

            pdf_files = [
                file
                for file in os.listdir(subject_folder)
                if file.lower().endswith(".pdf")
            ]

            if pdf_files:

                st.success(
                    f"📚 {len(pdf_files)} PYQ PDF(s) found!"
                )

                for idx, pdf_file in enumerate(
                    sorted(pdf_files)
                ):

                    pdf_path = os.path.join(
                        subject_folder,
                        pdf_file
                    )
                    st.write("PDF PATH:",pdf_path)
                    
                    st.write(
                        f"📄 **{pdf_file}**"
                    )

                    with open(
                        pdf_path,
                        "rb"
                    ) as file:

                        pdf_data = file.read()

                    st.download_button(
                        label=f"📥 Download {pdf_file}",
                        data=pdf_data,
                        file_name=pdf_file,
                        mime="application/pdf",
                        key=f"pyq_{folder_name}_{idx}"
                    )

                    # PDF Viewer
                    st.pdf(
                        pdf_data,
                        height=700
                    )

            else:

                st.warning(
                    "⚠️ No PYQ PDFs found for this subject."
                )

        else:

            st.warning(
                f"⚠️ PYQ folder for **{subject}** is not available."
            )

    else:

        st.info(
            f"📚 PYQs are not added yet for **{subject}**."
        )


# =========================================================
# EXAMS
# =========================================================

elif section == "📅 Exam Information":

    st.header("📅 AKTU Examination Information")

    st.warning(
        "⚠️ Examination dates can change. Always verify the "
        "latest official AKTU examination notice."
    )

    st.write("""
    ### Examination information

    • Semester examinations
    • Practical examinations
    • Internal examinations
    • Admit cards
    • Examination centres
    • Paper codes
    """)

# =========================================================
# ATTENDANCE
# =========================================================

elif section == "📊 Attendance":

    st.header("📊 Attendance Calculator")

    total = st.number_input(
        "Total classes",
        min_value=1,
        value=100
    )

    attended = st.number_input(
        "Classes attended",
        min_value=0,
        max_value=total,
        value=75
    )

    percentage = (attended / total) * 100

    st.metric(
        "Attendance",
        f"{percentage:.2f}%"
    )

    if percentage < 75:
        st.error("⚠️ Attendance is below 75%.")
    else:
        st.success("✅ Attendance is 75% or above.")

# =========================================================
# GNIOT ENQUIRY
# =========================================================

elif section == "🏫 GNIOT Enquiry":

    st.header("🏫 GNIOT College Enquiry")

    enquiry = st.selectbox(
        "Select Department",
        [
            "Admission",
            "Academic Department",
            "Examination Cell",
            "Accounts",
            "Training & Placement",
            "Hostel",
            "Library",
            "Scholarship",
            "Student Section"
        ]
    )

    st.info(
        f"Selected enquiry: {enquiry}"
    )

    st.write(
        "Use the latest official GNIOT contact information "
        "for the selected department."
    )

# =========================================================
# FEES
# =========================================================

elif section == "💰 Fees & Scholarship":

    st.header("💰 Fees & Scholarship")

    st.write("""
    ### Available information

    • Tuition fees
    • Examination fees
    • Hostel fees
    • Scholarship
    • Fee reimbursement
    • Payment enquiries

    ⚠️ Exact amounts should be taken from the latest official
    GNIOT notice.
    """)

# =========================================================
# HOSTEL
# =========================================================

elif section == "🏠 Hostel":

    st.header("🏠 GNIOT Hostel")

    st.write("""
    ### Hostel Information

    • Room allocation
    • Hostel rules
    • Mess
    • Leave
    • Maintenance
    • Warden
    • Hostel fees

    Check the current hostel notice/rules for official details.
    """)

# =========================================================
# LIBRARY
# =========================================================

elif section == "📚 Library":

    st.header("📚 GNIOT Library")

    st.write("""
    ### Library Services

    • Textbooks
    • Reference books
    • Study material
    • Book issue/return
    • Library membership
    """)

# =========================================================
# PLACEMENTS
# =========================================================

elif section == "💼 Placements":

    st.header("💼 GNIOT CSE Placement Preparation")

    st.write("""
    ### Placement Roadmap

    1. Programming
    2. Data Structures & Algorithms
    3. Aptitude
    4. Projects
    5. Git & GitHub
    6. Resume
    7. Technical Interviews
    8. HR Interviews
    """)

# =========================================================
# INTERNSHIPS
# =========================================================

elif section == "🚀 Internships":

    st.header("🚀 Internship Preparation")

    st.write("""
    ### Build your profile

    • Learn programming
    • Learn DSA
    • Build projects
    • Use GitHub
    • Create a resume
    • Practice interviews
    • Apply regularly
    """)

# =========================================================
# SGPA CALCULATOR
# =========================================================

elif section == "📈 SGPA Calculator":

    st.header("📈 SGPA Calculator")

    number = st.number_input(
        "Number of subjects",
        min_value=1,
        max_value=15,
        value=5
    )

    total_points = 0.0
    total_credits = 0.0

    for i in range(int(number)):

        col1, col2 = st.columns(2)

        with col1:
            credit = st.number_input(
                f"Subject {i+1} Credits",
                min_value=0.0,
                value=4.0,
                key=f"credit_{i}"
            )

        with col2:
            grade = st.number_input(
                f"Subject {i+1} Grade Point",
                min_value=0.0,
                max_value=10.0,
                value=8.0,
                key=f"grade_{i}"
            )

        total_points += credit * grade
        total_credits += credit

    if total_credits > 0:

        sgpa = total_points / total_credits

        st.success(
            f"Estimated SGPA: {sgpa:.2f}"
        )

# =========================================================
# CGPA CALCULATOR
# =========================================================

elif section == "🎯 CGPA Calculator":

    st.header("🎯 CGPA Calculator")

    semesters_count = st.number_input(
        "Number of semesters completed",
        min_value=1,
        max_value=8,
        value=2
    )

    total = 0.0

    for i in range(int(semesters_count)):

        sgpa = st.number_input(
            f"Semester {i+1} SGPA",
            min_value=0.0,
            max_value=10.0,
            value=8.0,
            key=f"sgpa_{i}"
        )

        total += sgpa

    cgpa = total / semesters_count

    st.success(
        f"Estimated CGPA: {cgpa:.2f}"
    )

# =========================================================
# NOTICES
# =========================================================

elif section == "📢 Important Notices":

    st.header("📢 Important Notices")

    st.warning(
        "⚠️ Always verify important academic information "
        "from the latest official GNIOT/AKTU notice."
    )

    st.write("""
    ### Notice Categories

    📅 Examination notices

    📚 Academic notices

    📝 Internal examination notices

    🎓 Admission notices

    💼 Placement notices

    💰 Fee & scholarship notices

    🏠 Hostel notices
    """)

# =========================================================
# FOOTER
# =========================================================

st.divider()

st.caption(
    "🎓 GNIOT × AKTU Student Support | "
    "B.Tech CSE | Free local version"
)
