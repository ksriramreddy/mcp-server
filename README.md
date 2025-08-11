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
```bash
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
```

---

## 🚀 Getting Started

### 1️⃣ Clone the Project
```bash
git clone https://github.com/YOUR_USERNAME/mcp-server.git
cd mcp-server
```

##Install UV & Create Virtual Environment

```bash
# Install UV if not already installed
pip install uv

# Create a new virtual environment
uv venv .venv

# Activate it
# On Windows:
.venv\Scripts\activate
# On Mac/Linux:
source .venv/bin/activate
```

##4️⃣ Set up Google API Credentials
Go to [Google Cloud Console](https://console.cloud.google.com/)

Enable Gmail API and Google Calendar API

Create OAuth 2.0 credentials and download the JSON file

Save it as:
`credential.json`
`token.json`
⚠ DO NOT COMMIT THESE FILES TO GIT — they should be in `.gitignore`.

## 🖥 Adding to Claude AI Desktop
You can run this MCP server locally and connect it to **Claude AI Desktop**.

1. **Install Claude Desktop**  
   👉 [Download Claude for Desktop](https://claude.ai/download)

2. Clone this repo inside your local workspace:
   ```bash
   git clone https://github.com/YOUR_USERNAME/mcp-server.git
   cd mcp-server
3. Run the MCP server:

    ```bash
   python main.py
    ```
Add MCP Server to Claude's Config
Open (or create) Claude's config file:

Windows: %APPDATA%\Claude\claude_desktop_config.json

Mac: ~/Library/Application Support/Claude/claude_desktop_config.json

Add your server details under "mcpServers":

```bash
{
  "mcpServers": {
    "emailMCP": {
      "command": "uv",
      "args": [
        "--directory",
        "C:\\ABSOLUTE\\PATH\\TO\\PARENT\\FOLDER\\mcp-server",
        "run",
        "main.py"
      ]
    }
  }
}
```

##RESTAR YOU PC


---

If you want, I can now **merge this Claude Desktop section** into the **full README.md** I wrote earlier so you have a single clean file ready to push to GitHub. That way, everything — cloning, setup, Google credentials, Claude config — is in one place.

