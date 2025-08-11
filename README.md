# 📅 Sriram's MCP Calendar & Email Server 🤖  
A powerful MCP (Model Context Protocol) server that connects to Google Calendar & Gmail APIs to let you:  
- 📬 Read Emails  
- 📅 Create, Delete, and List Meetings  
- 📖 Fetch all meetings on a specific day  
- ⚡ Integrate directly with Cloud Desktop

---

## 🛠 Tech Stack 👨‍💻
- **Backend:** Python (FastAPI + MCP)
- **Google API:** Calendar API, Gmail API
- **Auth:** OAuth 2.0 with JSON credentials
- **Environment Management:** [UV](https://docs.astral.sh/uv/)

---

## 📂 Folder Structure
MCP_Server/
│
├── tools/
│ ├── calendar_tool.py # Meeting creation, deletion, fetching logic
│ ├── email_tool.py # Email reading logic
│
├── requirements.txt # Python dependencies
├── .gitignore # Ignored files (credentials, tokens)
├── main.py # MCP server entry point
├── credential.json # Google OAuth credentials (DO NOT PUSH)
├── token.json # Google OAuth token (DO NOT PUSH)


---

## 🚀 Getting Started

### 1️⃣ Clone the Project
```bash
git clone https://github.com/YOUR_USERNAME/mcp-server.git
cd mcp-server



# Install UV if not already installed
pip install uv

# Create a new virtual environment
uv venv .venv

# Activate it
# On Windows:
.venv\Scripts\activate
# On Mac/Linux:
source .venv/bin/activate


uv pip install -r requirements.txt


##4️⃣ Set up Google API Credentials
Go to Google Cloud Console

Enable Gmail API and Google Calendar API

Create OAuth 2.0 credentials and download the JSON file

Save it as:
