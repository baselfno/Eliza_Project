# 🤖 Eliza Project — Al Hilal Chatbot (Streamlit)

## Brief Introduction
The Eliza Task is inspired by one of the first natural language processing (NLP) programs, **ELIZA**, developed by **Joseph Weizenbaum** at MIT in the 1960s. ELIZA uses pattern matching and substitution to simulate human-like conversations. The most famous script, **"DOCTOR,"** emulates a Rogerian psychotherapist. This task challenges you to build a web-based version of ELIZA that can interact with users by simulating a conversation.

---

## 📝 Overview
This project is a **Streamlit-based**, domain-focused conversational agent about **Al Hilal** club.  
It implements a modular pipeline for:
- Parsing user input (language/type detection)
- Mapping it to topics (players, achievements, club info, other sports, greetings, etc.)
- Normalizing tokens via synonyms
- Returning structured, consistent answers from curated data modules

The app provides a **multi-page** UI (Home, Chat, About Us) and reuses ELIZA-like ideas (lightweight rules, pattern keywords, controlled responses) tailored to a specific domain.

---

## 🚀 Features
- **Multi-Page Streamlit App**: `Home`, `Chat`, `About Us` via `st.navigation` / `st.Page`
- **Intent/Type Detection**: Routes questions to **thing / time / location / person / how / quantity / yes/no / question**
- **Topic Classifiers**: Detects **players**, **achievements**, **club info**, **other sports**, **greetings**, and **off-topic**
- **Synonym Normalization**: Unifies spelling variants for robust matching
- **Domain Knowledge**: Curated data for players, achievements, stadium, dates, rivalries, etc.
- **Rotating “Escapes”**: Graceful replies to off-topic teams, injuries, or Arabic-only input (with counters)
- **Extensible Modules**: Add new topics by dropping a file under `pages/quesions/` and mapping keywords

---

## 🗂 Project Structure
pages/
├─ about_us.py # About page UI (Streamlit)
├─ abu_rakan.png # Image asset used in UI
├─ chat.py # Chat interface (input/output)
├─ home.py # Landing page
├─ quesions/ # Topic/answer modules (note the spelling)
│ ├─ achievements_answers.py # Achievements/titles/cups responses
│ ├─ escape_answers.py # “Escape” responses for off-topic/undesired queries
│ ├─ hilal_info_answers.py # Core club info (founded, stadium, nicknames)
│ ├─ other_sports_answers.py # Other sports (volleyball, basketball, etc.)
│ ├─ player_answers.py # Player-centric answers (positions, numbers)
│ └─ welcome_answers.py # Greetings / welcoming replies

.gitignore
README.md
app.py # Streamlit entry point (navigation)
condition_map.py # Intent/type & topic routing (keywords/heuristics)
escaper.py # Rotating escape replies + club fact cyclers
hilal_data.py # Domain data: players, former players, achievements...
requirements.txt # Python dependencies
synonym.py # Token normalization via synonym dictionary


▶️ Setup & Run
1) Clone
bash
git clone https://github.com/baselfno/Eliza_Project.git
cd Eliza_Project

3) Install Dependencies
bash
pip install -r requirements.txt

4) Run the App
bash
streamlit run app.py
Open the URL from the terminal (typically http://localhost:8501).

🧪 Example Queries
“Who wears number 29 at Al Hilal?”

“When was Al Hilal founded?”

“Tell me about Al Hilal achievements.”

“Which defenders play for Al Hilal?”

“What other sports does Al Hilal have?”






📝 Future Enhancements
NLP Upgrade: Transformer-based intent/entity extraction

Persistence: Store conversation history & analytics

Admin Console: No-code content editing for answers and facts

Multilingual: Curated Arabic responses with controlled coverage


📚 Learning Outcomes
Designing a modular, ELIZA-inspired rule-based conversational agent
Structuring a multi-page Streamlit app with clean navigation and separation of concerns
Managing domain knowledge via Python data modules
Improving robustness using synonym normalization and keyword heuristics


📄 License
This project is provided for educational purposes. Please add a license file if you intend to distribute or modify it.


👤 Author
Developed by: Basel Felemban
