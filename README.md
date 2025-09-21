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

🧠 Conversation Pipeline
1) Preprocessing & Language Check
is_it_in_arabic(question: list[str]) checks for Arabic characters.

If Arabic-only is detected, escaper['arabic_escape'] rotates polite prompts to use English.

check_question_mark(question: str) and minimal-length checks route to:

escaper['not_question'] (non-question inputs),

escaper['very_short'] (too-short inputs).

2) Question Type (ELIZA-like)
question_is_about(tokens) classifies into:

thing, time, location, person, how, quantity, yesno, question, or not a question.

3) Topic Detection (Domain Routing)
Helpers in condition_map.py:

is_it_about_welcoming, is_it_about_general_health

is_it_about_players (uses synonym.search and get_player_in_question)

is_it_about_achievements

is_it_about_club

is_it_about_other_sports_answers (uses sport_exists_in_list)

is_it_about_escape / is_it_about_other_teams / is_it_other_matches

4) Synonym Normalization
synonym.search(word) maps spelling variants to a base token
(e.g., "AL-HILAL" → "hilal", "kolibaly" → "koulibaly", "gk" → "goalkeeper").

5) Domain Answers
hilal_data.py provides structured data:

Hilal_info (name, founding year, stadium),

current_players, former_players,

achievements (counts/titles/years),

alhilal_other_sports_info (descriptions + achievements).

Topic modules in pages/quesions/ format responses using this data.

6) Rotating Escapes & Fact Cyclers
escaper.py:

escapers[...] cycles canned responses (e.g., for injuries, other teams, Arabic-only).

escaper_forClup[...] rotates club facts like founded, stadium, nickname, etc.

update_counter(...) and get_unexpected_response(topic) handle cycling.

▶️ Setup & Run
1) Clone
bash
نسخ
تحرير
git clone https://github.com/baselfno/Eliza_Project.git
cd Eliza_Project
2) Install Dependencies
bash
نسخ
تحرير
pip install -r requirements.txt
3) Run the App
bash
نسخ
تحرير
streamlit run app.py
Open the URL from the terminal (typically http://localhost:8501).

🧪 Example Queries
“Who wears number 29 at Al Hilal?”

“When was Al Hilal founded?”

“Tell me about Al Hilal achievements.”

“Which defenders play for Al Hilal?”

“What other sports does Al Hilal have?”



🛠️ Extending the Bot
Add a new topic: create pages/quesions/<topic>_answers.py and expose a handler function.

Map keywords: add a detector in condition_map.py (possibly using synonyms).

Expand synonyms: edit synonym.py to normalize more misspellings/aliases.

New facts: append to hilal_data.py (players, cups, events, etc.).

Customize escapes: tweak escaper.py lists and cycling behavior.


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
