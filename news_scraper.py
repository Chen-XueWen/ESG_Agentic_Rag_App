import requests, os
from bs4 import BeautifulSoup
from vector_store import build_vector_db

def scrape_esg_snippets(company_name, max_snippets=5):
    query = f"{company_name} ESG OR sustainability site:reuters.com"
    url = f"https://www.google.com/search?q={query}&hl=en"
    headers = {"User-Agent": "Mozilla/5.0"}
    resp = requests.get(url, headers=headers)
    soup = BeautifulSoup(resp.text, "html.parser")

    snippets = [s.text for s in soup.select("div.BNeawe.s3v9rd.AP7Wnd")]
    return "\n\n".join(snippets[:max_snippets]) or "No ESG content found."

def generate_and_index(company_name, doc_dir="esg_docs", persist_dir="chroma_db"):
    os.makedirs(doc_dir, exist_ok=True)
    text = scrape_esg_snippets(company_name)
    path = f"{doc_dir}/{company_name.replace(' ', '_')}_esg.txt"
    with open(path, "w") as f:
        f.write(text)
    print(f"[✓] Snippet saved for {company_name}")
    build_vector_db(doc_dir, persist_dir=persist_dir)
