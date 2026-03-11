import streamlit as st

from agents.research_agent import research_agent
from agents.report_agent import report_agent
from memory.memory_manager import save_history, get_history
from exports.pdf_export import generate_pdf


# ----------------------------
# PAGE SETTINGS
# ----------------------------

st.set_page_config(
    page_title="AI Deep Research Agent",
    page_icon="🔎",
    layout="wide"
)

st.title("🔎 AI Deep Research Agent")

st.write("Search any topic and generate an AI research report.")


# ----------------------------
# USER INPUT
# ----------------------------

user_query = st.text_input(
    "Enter research topic",
    key="research_query"
)

search_button = st.button("Start Research")


# ----------------------------
# RUN RESEARCH
# ----------------------------

if search_button and user_query:

    with st.spinner("🔎 Searching the internet..."):

        text, sources = research_agent(user_query)

        report = report_agent(user_query, text)


    st.success("Research Completed")


    # ----------------------------
    # LAYOUT (Perplexity Style)
    # ----------------------------

    col1, col2 = st.columns([3,1])

    # REPORT
    with col1:

        st.subheader("📄 Research Report")

        st.write(report)


    # SOURCES
    with col2:

        st.subheader("🔗 Sources")

        if len(sources) == 0:
            st.write("No sources found")

        else:
            for i, src in enumerate(sources):
                st.markdown(f"[{i+1}] {src}")


    # ----------------------------
    # CONFIDENCE SCORE
    # ----------------------------

    confidence = min(len(sources) * 20, 95)

    st.progress(confidence/100)

    st.write(f"Research Confidence: {confidence}%")


    # ----------------------------
    # SAVE HISTORY
    # ----------------------------

    save_history(user_query, confidence)


    # ----------------------------
    # PDF EXPORT
    # ----------------------------

    pdf_file = generate_pdf(report)

    with open(pdf_file, "rb") as f:

        st.download_button(
            "Download Research Report",
            f,
            file_name="research_report.pdf"
        )


# ----------------------------
# SIDEBAR HISTORY
# ----------------------------

st.sidebar.title("Research History")

history = get_history()

for item in history:
    st.sidebar.write(f"{item['topic']} ({round(item['confidence'])}%)")