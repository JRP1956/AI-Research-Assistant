# AI-Research-Assistant
AI Research Assistant — Your Personal GPT-4-Powered Research Buddy  A Python-based terminal assistant that fetches real-time web data using Tavily and delivers detailed, GPT-4 generated answers. Ask anything, build a growing knowledge base, and research smarter — all in your terminal.

Sure! Here's a **short, clear, and to-the-point** description you can include at the top of your repo or under a "Usage" section:

---

## 🔧 How to Use

1. **Install requirements** (Python 3.10+ required):
   ```bash
   pip install openai tavily
   ```

2. **Add your API keys** for Tavily and OpenAI in the script.

3. **Run the script**:
   ```bash
   python main.py
   ```

4. **Ask questions** like:
   ```
   What do you want to research on? history of AI
   ```

5. **Type `quit`** to exit the assistant.

---

## How It Works

- Takes your research question via terminal input.
- Fetches relevant web data using the **Tavily API**.
- Builds and stores a cumulative **knowledge base**.
- Uses **OpenAI GPT-4** to generate rich, structured answers based on that knowledge.
- Continues until you exit the session.

---
