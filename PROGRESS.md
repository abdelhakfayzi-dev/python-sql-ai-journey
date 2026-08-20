# Learning Log — Python / SQL / AI Journey

##  Python

### Day 1-3 — 21/06/2026
- Covered: Beazley sections 0-1 (setup, intro to Python)
- Built: first.py, mortgage.c exercise, titanic_io.py, basic file I/O practice
- Struggled with: lost detailed tracking these days, starting fresh from today
- Could I rebuild this from memory tomorrow? Partially — need to revisit
  
### Day 4 — 22/06/2026
- Time: 2h
- Covered: 2.1 Datatypes and Data Structures
- Built: Portfolio Report Script , Missing Stocks Script
- Struggled with: Git merge conflicts (resolved)
- Could I rebuild this from memory tomorrow? 70% of it

### Day 5 — 23/06/2026
- Time: 2h
- Covered: Containers (lists, tuples, sets, dicts), formatting exercise, portfolio table
- Built: Portfolio table report with formatted columns, converted list of tuples to dictionary,+ some exercises on containers.
- Struggled with: Nothing major
- Could I rebuild this from memory tomorrow?  90% of it

### Day 6 — 24/06/2026
- Time: 30min
- Covered: sequences and collections
- Built: nothing.
- Struggled with:nothing.
- Could I rebuild this from memory tomorrow?

### Day 7 — 25/06/2026
- Time: 2h
- Covered: List comprehensions, sequences (slicing, concatenation, repetition, membership, enumerate, zip), collections (Counter, defaultdict, deque)
- Built: `practice_sequences.py` (10 exercises), `list_comprehensions.py` (10 exercises)
- Struggled with:nothing.
- Could I rebuild this from memory tomorrow? Yes

### Day 8 — 26/06/2026
- Time: 4h
- Covered: 
  - Section 2.7 (Object model, mutability, identity, deepcopy)
  - Section 3.1 (Functions, script writing, main guard)
  - Built complete portfolio_report program with:
    - read_portfolio, read_prices, make_report, print_report, portfolio_report
    - Exception handling with csv.reader and csv.DictReader
    - Flexible function 
- Built: 
  - object_model_practice.py
  - portfolio_report.py (fully structured program)
  - warmup.py (list comprehension review)
- Struggled with: 
  - read_prices using csv.reader vs csv.DictReader (fixed)
  - Floating-point artifacts in output (normal)
  - Git contributions not showing (email mismatch)
- Could I rebuild this from memory tomorrow? 
  Yes  – I understand the full structure: read → process → report, with functions separated by responsibility.

 ### Day 9 — 27/06/2026
  - Time: 1h
- Covered: 
  - Read Section 3.2 (More on functions) – default arguments
  - Wrote fileparse.py with parse_csv function
  - Added column selector (select parameter) – still working on it
- Built: fileparse.py (parse_csv with select parameter)
- Struggled with: 
  - Understanding how `select` works 
  - Column selection logic (still not fully clear)
- Could I rebuild this from memory tomorrow? 
  Not yet – need to review the column selector logic and practice it.
  
### Day 10 — 28/06/2026
  - Time: 2h30
- Covered: 
  - Built complete analyzer.py from scratch
  - read_portfolio, read_prices, build_report, print_report
  - Formatted table with alignment and summary
  - Tracked best and worst performing stocks
  - Git merge conflict resolution (merge --abort, pull, push)
- Built: analyzer.py (full working program)
- Struggled with:
  - read csv files
  - dict list confusion while looping
  - Tracking best/worst logic
- Could I rebuild this from memory tomorrow? Yes – I understand the full data flow now

---

## SQL Fundamentals
### Day 11 — 01/07/2026
- Time: 1.5 hours
- Covered: 
  - SQLBolt Lessons 1-4 (SELECT, WHERE, ORDER BY, LIMIT, OFFSET)
  - Built value_checker.py 
  - Reviewed best/worst tracking logic
- Built: value_checker.py
- Struggled with: 
  - Aggregating duplicate stock entries in Python (fixed by removing break and summing totals)
  - SQL syntax for ORDER BY and LIMIT (getting used to it)
- Could I rebuild this from memory tomorrow? 
  Yes – Python aggregation logic is clear, SQL basics are making sense.
- Notes: 
  - Missed June 29-30 (took a break / personal time).
  - Back on track July 1.
    
### Day 12 — 02/07/2026
  - Time: 2 hours
- Covered: SQLBolt Lessons 1-8 (SELECT, WHERE, JOINs, NULLs)
- Built: SQL query skills – filtering, joining, handling missing data
- Struggled with: OUTER JOINs at first – understood after working through examples
- Could I rebuild this from memory tomorrow? Yes – basic SQL syntax is clear
  
### Day 13 — 07/07/2026
- Time: 30min
- Covered: SQLBolt Lesson 9 
- Built: SQL query skills – arithmetic, aliases, string concatenation
- Struggled with: Nothing major 
- Next: Lesson 10 (Aggregates)
- Notes: Took a break June 29–30 and July 3–6. Back on track.

### Day 14 — 08/07/2026
- Time: 1 hour 
- Covered: SQLBolt Lessons 10–13 (Aggregates, GROUP BY, HAVING, Order of Execution, INSERT)
- Built: Queries with aggregation, grouping, filtering, and inserting rows
- Struggled with: HAVING vs WHERE
- Next: Lessons 14–18

### Day 15 — 09/07/2026
- Time: ~1.5 hours
- Covered: SQLBolt Lessons 14–18 
- Built: Completed all 18 SQLBolt lessons
- Struggled with: Nothing major.
- Next: Connect Python to SQLite and run queries from Python

### Day 16 — 01/08/2026

- Time: 1.5 hours
- Covered: Built skill matcher with SQLite – students and internships tables, insert data, skill matching logic with split/loop
- Built: internships.py
- Struggled with: Understanding execute vs executemany – now clear; re-learned split/strip logic
- Could I rebuild this from memory tomorrow? Partially – I understand the structure but need to review the matching loop and SQLite setup

### Day 17 — 02/08/2026
- Time: 2 hours
- Covered: GitHub profile setup — banner, bio, visitor counter, stats, snake animation, progress table
- Built: Profile README 
- Struggled with: Snake workflow (fixed), stats cards rate‑limit (switched to text)
- Could I rebuild this from memory tomorrow? Yes

### Day 18 — 04/08/2026
- Time: 2 hours
- Covered: File I/O, API requests, JSON parsing, dictionary and list operations, CV matching logic
- Built: city_weather.py, CV scoring script
- Struggled with: Sorting results, API response structure
- Could I rebuild this from memory tomorrow? Yes – I understand the flow now

### Day 19 — 05/08/2026
- Time: 2 hours
- Covered: ChatGPT Prompt Engineering for Developers (DeepLearning.AI short course)
- Built: Prompt engineering skills — system/user prompts, iterative prompt development, summarization, inferring, transforming, expanding
- Struggled with: Nothing major — course was well-structured
- Could I rebuild this from memory tomorrow? Yes — core prompt engineering principles are clear now

### Day 20 — 06/08/2026
- Time: 2 hours
- Covered: Integrating LLM APIs into Python scripts, handling API errors, and adapting to SDK differences.
- Built: Upgraded `cv_scorer.py` with Groq API analysis. Built and deployed a local Streamlit web interface (`app.py`) to make the tool usable via browser.
- Struggled with: Git push protection (secret scanning) and environment variables. Overcame by debugging terminal outputs instead of reinstalling everything.
- Could I rebuild this from memory tomorrow? Yes

### Day 21 — 07/08/2026
- Time: 2 hours
- Covered: Streamlit Cloud deployment (requirements.txt, TOML secrets, redeploy cycle), README as a product storefront, public build-log writing, recruiter-perspective resume analysis, first freelance lead hunting on Reddit
- Built: CV/Internship Fit Scorer live at cv-scorer-first.streamlit.app — professional README with live link + stack badges — first LinkedIn build log published — LaTeX gig hunt playbook with Reddit search operators
- Struggled with: ModuleNotFoundError caused by PowerShell UTF-16 requirements.txt; the urge to quit when deploys kept failing; heavy resistance to posting publicly ("cringe") — shipped the post anyway
- Could I rebuild this from memory tomorrow? Yes
  
### Day 22 — 08/08/2026
- Time: 3 hours
- Covered: RAG fundamentals, vector embeddings as meaning coordinates, pypdf for PDF text extraction, LLM temperature control, context window limits
- Built: Level 1 RAG in the CV Scorer — PDF upload → text extraction → Groq skill extraction → case-insensitive matching → recruiter analysis. Shipped live on Streamlit Cloud
- Struggled with: LLM hallucination (model flipped the gap and claimed ML was missing) fixed by tightening the prompt.
- Could I rebuild this from memory tomorrow? Yes

### Day 23 — 09/08/2026
- Time: 2 hours
- Covered: Vector embeddings, semantic search, ChromaDB, idempotent seeding, cloud dependency rebuilds. Wind-down: The Illustrated Word2Vec
- Built: Level 2 RAG live — CV upload → skill extraction → ChromaDB top-3 semantic retrieval → recruiter analysis.
- Struggled with: Cloud ModuleNotFoundError for chromadb
- Could I rebuild this from memory tomorrow? Yes

### Day 24 — 10/08/2026
- Time: 0h coding
- Covered: Strategic planning. Mapped CP2 academic targets and Upwork freelance strategy.
- Built: Nothing technical today.
- Struggled with: Balancing ENSAO workload with business goals. Fixed by timeboxing.
- Rebuild from memory? N/A today.

### Day 25 — 11/08/2026
- Time: 1h
- Covered: Streamlit Cloud deployment, cloud-seeding via JSON, environment variables.
- Built: The live production app. Seeded the cloud DB with 22 internships. Added UI metadata (Title @ Company).
- Struggled with: Python indentation and setting env vars on Streamlit Cloud.
- Rebuild from memory? Yes 

### Day 26 — 12/08/2026
- Time: 30 mins
- Covered: Recovery and consistency. Reviewed the week's roadmap and rested to prevent burnout.
- Built: nothing.
- Struggled with: fatigue.
- Rebuild from memory? N/A - Rest day.

### Day 27 — 14/08/2026
- Time: ~4h
- Covered: Learned Web Scraping (freecodecamp crash course), Advanced BeautifulSoup (pagination, nested loops, data cleaning), Git remote management, and launching the agency storefronts (Upwork + Malt).
- Built: 50-page web scraper. Created a professional `portfolio` GitHub repo architecture. Set up Upwork and Malt freelancer profiles linked to the portfolio.
- Struggled with: Nested loop indentation (writing duplicate rows).
- Rebuild from memory? Yes

### Day 28 — 15/08/2026
- Time: ~6h
- Covered: Streamlit Cloud deployment, environment variable management (os.environ), n8n workflow testing & export, UPWORK + MALT.FR profiles set up and professional CV generation (LaTeX).
- Built: Verified and exported the WhatsApp Clinic Booking Bot (n8n + Twilio + Groq + Sheets). Loaded the GitHub portfolio with 3 verified projects. Completed Upwork and Malt profile (3 portfolio items).
- Struggled with: lost all the files in the first repo. Merge conflicts after web edits, hardcoded secrets in n8n JSON exports blocking pushes, and Malt's CV parsing requiring manual experience entry.
- Rebuild from memory? Yes

### Day 29 — 17/08/2026
- **Time:** 2h
- **Covered:** Web scraping, SQLite price storage, comparison logic, report formatting
- **Built:** price_tracker.py — live price monitor for French e-commerce products
- **Struggled with:** Same price status showing up every time i run the code.
- **Rebuild from memory?** Yes

### Day 30 — 18/08/2026
- **Time:** 6h
- **Covered:** B2B cold outreach, niche targeting, Selenium anti-bot scraping, lead-data cleaning/filtering
- **Built:** Lead scraper (Selenium headless), 5 cleaned lead CSVs (~300 rows), 10 personalized pitches (5 emails + 5 contact forms)
- **Struggled with:** YP IP blocks and blank addresses (solved with manual Google Maps hustle), hidden company emails (solved with bait-drop forms)
- **Could I rebuild this from memory tomorrow?** 85% of it

### Day 31 — 19/08/2026
- **Time:** 3h
- **Covered:** Prospects/leads search and 20 personalized cold emails sent
- **Built:** Nothing
- **Struggled with:** Wrong HQ assumptions, no-attachment pivot (bait-drop reply line)
- **Could I rebuild this from memory tomorrow?** yes

### Day 32 — 20/08/2026
- **Time:** 2h
- **Covered:** Niche software prospecting and 13 personalized cold emails sent
- **Built:** Nothing
- **Struggled with:** Filtering out non-US companies and verifying exact HQ locations
- **Could I rebuild this from memory tomorrow?** yes

