import streamlit as st
from news_scraper import generate_and_index
from agents import EnvironmentAgent, SocialAgent, GovernanceAgent, AggregatorAgent

st.set_page_config(page_title="ESG Recommender - Multi-Agent")
st.title("🌱 Multi-Agent ESG Scoring")

company = st.text_input("Enter company name:")

if st.button("Analyze ESG"):
    if not company:
        st.warning("Please enter a company name.")
    else:
        with st.spinner("Scraping + indexing ESG info..."):
            generate_and_index(company)

        with st.spinner("Running ESG agents..."):
            env_agent = EnvironmentAgent()
            soc_agent = SocialAgent()
            gov_agent = GovernanceAgent()
            agg_agent = AggregatorAgent()

            env = env_agent.run(company)
            soc = soc_agent.run(company)
            gov = gov_agent.run(company)

            report = agg_agent.run({"env": env, "soc": soc, "gov": gov})

            st.success("Done!")
            st.markdown("### 📝 ESG Report")
            st.markdown(report)
