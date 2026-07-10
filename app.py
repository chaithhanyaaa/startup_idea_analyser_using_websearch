import streamlit as st
from chain import analyze_startup


st.set_page_config(
    page_title="Startup Analyst",
    page_icon="🚀",
    layout="wide"
)

st.title("Startup Analyst")
st.caption("AI-powered startup idea analysis with market research")

idea = st.text_area(
    "Describe your startup idea",
    height=120,
    placeholder="e.g. AI interview preparation platform for college students"
)

if st.button("Analyze", type="primary"):
    if not idea.strip():
        st.warning("Please enter a startup idea.")
    else:
        with st.spinner("Researching and analyzing..."):
            result = analyze_startup(idea)

        if result.get("error"):
            st.error(f"Research failed: {result['error']}")
        else:
            analysis = result.get("analysis") or {}

            st.markdown("---")
            st.subheader("Analysis")

            if isinstance(analysis, dict):
                col1, col2 = st.columns(2)
                with col1:
                    st.markdown("**Summary**")
                    st.write(analysis.get("summary", ""))

                    st.markdown("**Market Opportunity**")
                    st.write(analysis.get("market_opportunity", ""))

                    st.markdown("**Strengths**")
                    for item in analysis.get("strengths", []):
                        st.markdown(f"- {item}")

                    st.markdown("**Weaknesses**")
                    for item in analysis.get("weaknesses", []):
                        st.markdown(f"- {item}")

                    st.markdown("**Risks**")
                    for item in analysis.get("risks", []):
                        st.markdown(f"- {item}")

                with col2:
                    st.markdown("**Competitors**")
                    for item in analysis.get("competitors", []):
                        st.markdown(f"- {item}")

                    st.markdown("**Monetization**")
                    for item in analysis.get("monetization", []):
                        st.markdown(f"- {item}")

                    st.markdown("**MVP Features**")
                    for item in analysis.get("mvp_features", []):
                        st.markdown(f"- {item}")
            else:
                st.markdown(str(analysis))

            sources = result.get("sources", [])
            if sources:
                st.markdown("---")
                st.subheader("Sources")
                for url in sources:
                    st.markdown(f"- {url}")
