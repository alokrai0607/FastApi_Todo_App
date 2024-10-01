Instructions for your FastAPI Todo App:

---

# FastAPI Todo App

A fully-functional Todo application built using **Python** 🐍, **FastAPI** ⚡, and **MySQL** 🗄️.

## How to Run the Application:

### Step-by-Step Guide

1. **Open PowerShell** 💻:
   - Navigate to your desktop and open PowerShell.

2. **Clone the Repository** 📥:
   - Run the following command to download the repository:
     ```bash
     git clone https://github.com/alokrai0607/FastApi_Todo_App.git
     ```
   - The repository will be cloned to your desktop.

3. **Open the Project in VS Code** 📝:
   - Navigate to the downloaded `FastApi_Todo_App` folder.
   - Open the folder using **Visual Studio Code**.

4. **Open the Terminal in VS Code** 💡:
   - In the VS Code menu, go to `Terminal` → `New Terminal`.
   - Make sure you’re in the `fastapi_todo_app` directory in the terminal.

5. **Activate the Virtual Environment** 🔄:
   - Run the following command to activate the virtual environment:
     ```bash
     .\venv\Scripts\Activate
     ```

6. **Run the Application** 🚀:
   - Start the FastAPI server by executing:
     ```bash
     .\venv\Scripts\uvicorn app.main:app --reload
     ```

7. **Visit the App** 🌐:
   - Open your web browser and go to [http://127.0.0.1:8000](http://127.0.0.1:8000) to see your Todo App in action!

### Important Notes:

1. **Create the Database** 🛠️:
   - Make sure to manually create the database in MySQL. The database name should match the one specified in the configuration file (`config.py`).

2. **Update Database Credentials** 🔐:
   - Open the `config.py` file and update your MySQL database credentials (username, password, host, port, and database name) according to your local MySQL setup.

---

Let me know if you need any further modifications or additional instructions!
