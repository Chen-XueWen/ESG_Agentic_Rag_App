from llama_cpp import Llama
from retriever import get_relevant_context

llm = Llama(model_path="path/to/llama-3.2-3b.Q4_K_M.gguf", n_ctx=2048)

def call_llama(prompt):
    output = llm(prompt, max_tokens=512, stop=["</s>"])
    return output["choices"][0]["text"].strip()

class EnvironmentAgent:
    def run(self, company):
        context = get_relevant_context(f"{company} environmental performance OR sustainability")
        prompt = f"""
Evaluate the *Environmental* performance of {company} using the context below.

Context:
{context}

Score out of 10, and explain briefly.
"""
        return call_llama(prompt)

class SocialAgent:
    def run(self, company):
        context = get_relevant_context(f"{company} social responsibility OR labor OR diversity")
        prompt = f"""
Evaluate the *Social* responsibility of {company} using the context below.

Context:
{context}

Score out of 10, and explain briefly.
"""
        return call_llama(prompt)

class GovernanceAgent:
    def run(self, company):
        context = get_relevant_context(f"{company} corporate governance OR board OR ethics")
        prompt = f"""
Evaluate the *Governance* of {company} using the context below.

Context:
{context}

Score out of 10, and explain briefly.
"""
        return call_llama(prompt)

class AggregatorAgent:
    def run(self, results):
        prompt = f"""
You're an ESG aggregator. Given the evaluations:

Environment:
{results['env']}

Social:
{results['soc']}

Governance:
{results['gov']}

1. Extract the scores.
2. Compute a weighted average ESG score.
3. Output a formatted summary like:

🌿 Environment (x/10): ...
🤝 Social (x/10): ...
🏛️ Governance (x/10): ...
🧠 Final ESG Score: x.x/10
"""
        return call_llama(prompt)
