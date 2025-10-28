# 📝 Project Name
This project generates short blog paragraphs using OpenAI's API.  
It was developed as part of my learning process in the **Codédex Python course**.

---

# 🚀 Description
The program allows you to enter a topic, sends it to the OpenAI API,  
and returns an AI-generated paragraph related to that topic.  
It demonstrates basic API interaction, prompt design, and environment variable handling in Python.

---

# ⚙️ Tech Stack
- Python 3
- OpenAI API
- python-dotenv
- Git & GitHub

---

# 🧩 How to Run the Project

## 1️⃣ Clone the repository
Open your terminal and run:
```bash
git clone https://github.com/your_username/your_repository_name.git
cd your_repository_name

2️⃣ Create a virtual environment (optional but recommended)
python -m venv venv
Activate the environment:
On Windows:
venv\Scripts\activate
On Mac/Linux:
source venv/bin/activate

3️⃣ Install dependencies
Install the required Python packages:
pip install openai python-dotenv
If you prefer using a requirements.txt file, create it and run:
pip install -r requirements.txt

4️⃣ Add your OpenAI API key
In the project’s root folder, create a file named .env and add the following line:
OPENAI_API_KEY=your_api_key_here

5️⃣ Run the program
Start the script:
python main.py
