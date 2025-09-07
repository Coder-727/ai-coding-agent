# 🤖 AI Coding Agent

An AI-powered coding assistant that helps you explore, read, write, and run Python code directly from the command line.  
Built with **Google Gemini API** and Python, this agent can understand prompts and execute actions like listing files, reading file contents, writing new files, and running Python scripts.

---

## ✨ Features
- 🗂 **List files & directories** – Explore your project structure  
- 📖 **Read file contents** – Quickly view code or text files  
- ✍️ **Write & update files** – Create or modify project files  
- 🐍 **Run Python files** – Execute scripts securely in a sandboxed environment  
- 🧠 Powered by **Gemini 2.0 Flash API** for natural language understanding  

---

## 🚀 Getting Started

### 1️⃣ Clone the repository
```bash
git clone https://github.com/Coder-727/ai-coding-agent.git
cd aiagent
````

### 2️⃣ Install dependencies

It’s recommended to use a virtual environment:

```bash
python3 -m venv venv
source venv/bin/activate   # On Linux/Mac
venv\Scripts\activate      # On Windows

pip install -r requirements.txt
```

### 3️⃣ Setup environment variables

Create a `.env` file with your Google API key:

```env
GEMINI_API_KEY=your_api_key_here
```

### 4️⃣ Run the agent

```bash
python main.py "list all files in the project"
```

For verbose mode:

```bash
python main.py "run tests.py" --verbose
```

---

## 🛠 Requirements

* Python 3.9+
* `google-genai` SDK
* `python-dotenv`

Install with:

```bash
pip install -r requirements.txt
```

---

## 📖 Example Usage

```bash
$ python main.py "get the contents of lorem.txt"
wait, this isn't lorem ipsum
```

```bash
$ python main.py "create a new README.md file with the contents '# calculator'"
```

---

## 🤝 Contributing

Pull requests are welcome!
If you have suggestions for improvements, feel free to fork the repo and submit a PR.

---



