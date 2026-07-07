from datetime import date
import re
from bs4 import BeautifulSoup

BLOG_POSTS = [
    {
        "slug": "class-10-board-exam-preparation-guide-cbse",

        "title": "How to Prepare for Class 10 Board Exam: The Complete CBSE Guide for 2026–27",

        "meta_title": "Class 10 Board Exam Prep 2026–27: Study Plan, Notes & AI-Powered Learning | Genelis",

        "meta_description": (
            "CBSE Class 10 board exam preparation guide with chapter weightage charts, "
            "subject-wise strategy, an 8-week study plan, and how Genelis helps students study smarter."
        ),

        "focus_keyword": "how to prepare for class 10 board exam",

        "secondary_keywords": [
            "CBSE class 10 study plan",
            "class 10 notes CBSE NCERT",
            "AI study coach class 10",
            "mock tests class 10 CBSE",
            "important questions class 10",
            "smart revision class 10"
        ],

        "class": "10",
        "subject": "Board Exam Preparation",
        "category": "Exam Preparation",

        "author": "Genelis Team",

        "published_date": "2026-07-03",
        "updated_date": "2026-07-05",

        "featured_image": "",
        "reading_time": "11 min",

        "excerpt": (
            "A complete CBSE Class 10 board exam preparation guide with weightage, "
            "subject-wise strategy, an 8-week study plan, and AI-powered revision guidance."
        ),

        "content": """
        <section>
        <p>
            Most Class 10 students don't fall short because they don't study. They fall short because they
            study the <em>wrong things</em>. They revise the chapters they're already comfortable with,
            score 68% on a mock test, note the number, and move on. The specific topics where they lost
            those 32 marks go unaddressed. The same gaps surface in February.
        </p>

        <p>
            This guide is built around that gap — between effort and outcome — and how to close it.
            You'll find the CBSE chapter weightage, subject-wise strategy, an 8-week preparation plan,
            and where AI-powered personalised learning changes the equation.
        </p>

        <div class="gdl-callout">
            <div class="gdl-callout-icon">💡</div>
            <div class="gdl-callout-content">
            <h4>Key Takeaway</h4>
            <p>
                Studying harder is not enough. Class 10 preparation improves when students know
                what to revise, why they lost marks, and how to close those gaps before the board exam.
            </p>
            </div>
        </div>
        </section>

        <section>
        <h2>Class 10 Is a Different Beast. Here's Why.</h2>

        <p>
            Class 10 is the first time many students sit for a national-level board exam. It tests
            conceptual application under time pressure, not just syllabus completion.
        </p>

        <p>
            The content also builds on Class 9, especially in Maths and Science. That means unresolved
            gaps from the previous year often appear as weak areas right when board preparation becomes
            serious.
        </p>

        <p>
            Students who score 90%+ are not always the ones who study the most. They are usually the ones
            who prepare strategically — knowing which units carry more marks, which question types repeat,
            and which weak areas need attention before February.
        </p>
        </section>

        <section>
        <h2>Stop Guessing. Here's Exactly Where CBSE Hides Your Marks.</h2>

        <p>
            Smart exam preparation starts with knowing where marks actually come from. Each major subject
            carries 80 marks in theory and 20 marks through internal assessment.
        </p>

        <h3>Mathematics — 80 marks</h3>

        <div class="vis-wrap">
            <div class="vis-title">Maths marks distribution — where 80 marks come from</div>

            <div class="bar-row">
            <div class="bar-label">Algebra</div>
            <div class="bar-track"><div class="bar-fill" style="width:25%">25%</div></div>
            <div class="bar-marks">20 marks</div>
            </div>

            <div class="bar-row">
            <div class="bar-label">Geometry</div>
            <div class="bar-track"><div class="bar-fill" style="width:18.75%">19%</div></div>
            <div class="bar-marks">15 marks</div>
            </div>

            <div class="bar-row">
            <div class="bar-label">Trigonometry</div>
            <div class="bar-track"><div class="bar-fill" style="width:15%">15%</div></div>
            <div class="bar-marks">12 marks</div>
            </div>

            <div class="bar-row">
            <div class="bar-label">Statistics &amp; Probability</div>
            <div class="bar-track"><div class="bar-fill" style="width:13.75%">14%</div></div>
            <div class="bar-marks">11 marks</div>
            </div>

            <div class="bar-row">
            <div class="bar-label">Mensuration</div>
            <div class="bar-track"><div class="bar-fill" style="width:12.5%">12.5%</div></div>
            <div class="bar-marks">10 marks</div>
            </div>

            <div class="bar-row">
            <div class="bar-label">Coordinate Geometry</div>
            <div class="bar-track"><div class="bar-fill" style="width:7.5%">7.5%</div></div>
            <div class="bar-marks">6 marks</div>
            </div>

            <div class="bar-row">
            <div class="bar-label">Number Systems</div>
            <div class="bar-track"><div class="bar-fill" style="width:7.5%">7.5%</div></div>
            <div class="bar-marks">6 marks</div>
            </div>
        </div>

        <p>
            <strong>The takeaway:</strong> Algebra, Geometry, and Trigonometry together account for nearly
            60% of the Maths paper. If your weak areas sit in these units, they deserve priority.
        </p>

        <h3>Science — 80 marks</h3>

        <div class="vis-wrap">
            <div class="vis-title">Science marks distribution — three subjects, one paper</div>

            <div class="bar-row">
            <div class="bar-label">Chemical Substances</div>
            <div class="bar-track"><div class="bar-fill" style="width:31.25%">31%</div></div>
            <div class="bar-marks">25 marks</div>
            </div>

            <div class="bar-row">
            <div class="bar-label">World of Living</div>
            <div class="bar-track"><div class="bar-fill" style="width:31.25%">31%</div></div>
            <div class="bar-marks">25 marks</div>
            </div>

            <div class="bar-row">
            <div class="bar-label">Effects of Current</div>
            <div class="bar-track"><div class="bar-fill" style="width:15%">15%</div></div>
            <div class="bar-marks">12 marks</div>
            </div>

            <div class="bar-row">
            <div class="bar-label">Light</div>
            <div class="bar-track"><div class="bar-fill" style="width:15%">15%</div></div>
            <div class="bar-marks">12 marks</div>
            </div>

            <div class="bar-row">
            <div class="bar-label">Natural Resources</div>
            <div class="bar-track"><div class="bar-fill" style="width:7.5%">7.5%</div></div>
            <div class="bar-marks">6 marks</div>
            </div>
        </div>

        <p>
            <strong>The takeaway:</strong> Chemistry and Biology together account for a large part of the
            Science paper. Students should not over-focus only on Physics numericals while ignoring Biology
            diagrams and Chemistry equations.
        </p>

        <h3>Social Science — 80 marks</h3>

        <table>
            <thead>
            <tr>
                <th>Subject</th>
                <th>Key Focus Areas</th>
                <th>Marks</th>
            </tr>
            </thead>
            <tbody>
            <tr>
                <td>History</td>
                <td>Nationalism, Industrialisation, Print Culture</td>
                <td>20</td>
            </tr>
            <tr>
                <td>Geography</td>
                <td>Resources, Agriculture, Minerals, Transport</td>
                <td>20</td>
            </tr>
            <tr>
                <td>Political Science</td>
                <td>Power Sharing, Federalism, Democracy, Political Parties</td>
                <td>20</td>
            </tr>
            <tr>
                <td>Economics</td>
                <td>Development, Sectors, Money and Credit, Globalisation</td>
                <td>20</td>
            </tr>
            </tbody>
        </table>

        <p>
            <strong>The takeaway:</strong> All four Social Science subjects carry equal importance.
            Map work is one of the most reliable scoring areas and should not be left for the last week.
        </p>

        <h3>English — 80 marks</h3>

        <table>
            <thead>
            <tr>
                <th>Section</th>
                <th>Content</th>
                <th>Marks</th>
            </tr>
            </thead>
            <tbody>
            <tr>
                <td>Reading</td>
                <td>Unseen passages and comprehension</td>
                <td>20</td>
            </tr>
            <tr>
                <td>Writing and Grammar</td>
                <td>Letters, essays, notices, grammar exercises</td>
                <td>30</td>
            </tr>
            <tr>
                <td>Literature</td>
                <td>Prose, poetry, extracts and textbook-based questions</td>
                <td>30</td>
            </tr>
            </tbody>
        </table>

        <p>
            <strong>The takeaway:</strong> Writing and Grammar is one of the highest-scoring sections,
            but it requires active practice. Reading literature alone is not enough.
        </p>
        </section>

        <section>
        <h2>3 Ways Students Study Hard and Score Badly.</h2>

        <p>
            These are the patterns that separate students who study hard but remain stuck from students
            who improve consistently before board exams.
        </p>

        <div class="mistake-grid">
            <div class="mistake-card">
            <div class="icon">😌</div>
            <div class="prob">Mistake 1</div>
            <p>
                <strong>Revising comfortable chapters</strong> instead of the ones that are actually weak.
            </p>
            <div class="sol">The fix</div>
            <p>
                Use topic-wise accuracy to decide what to revise next, not comfort or habit.
            </p>
            </div>

            <div class="mistake-card">
            <div class="icon">📊</div>
            <div class="prob">Mistake 2</div>
            <p>
                <strong>Using mock tests only for practice</strong> instead of diagnosis.
            </p>
            <div class="sol">The fix</div>
            <p>
                Treat every wrong answer as a signal. Log it, revise it, and reattempt it.
            </p>
            </div>

            <div class="mistake-card">
            <div class="icon">🌫️</div>
            <div class="prob">Mistake 3</div>
            <p>
                <strong>Guessing where you stand</strong> without topic-wise performance data.
            </p>
            <div class="sol">The fix</div>
            <p>
                Use study analytics to understand exact weak areas instead of relying on feelings.
            </p>
            </div>
        </div>
        </section>

        <section>
        <h2>What CBSE Actually Rewards in Each Subject</h2>

        <h3>Mathematics — practise application, not recognition</h3>

        <p>
            Maths is where targeted practice creates the biggest difference. CBSE tests application,
            not only recall. Build formula sheets, practise word problems, and give special attention
            to Algebra, Geometry, Trigonometry and Statistics.
        </p>

        <h3>Science — three subjects, three different strategies</h3>

        <p>
            Treat Science as Physics, Chemistry and Biology combined into one paper. Chemistry needs
            equation accuracy, Biology needs diagram practice, and Physics needs numerical clarity,
            derivations and formula application.
        </p>

        <h3>Social Science — structure beats knowledge</h3>

        <p>
            Social Science rewards structured answers. Use headings, bullet points, keywords and maps.
            The same knowledge presented clearly usually scores better than long unstructured paragraphs.
        </p>

        <h3>English — the 30-mark section students ignore</h3>

        <p>
            Writing and Grammar require regular practice. Students should practise formal letters,
            articles, notices and grammar exercises instead of relying only on literature revision.
        </p>

        <div class="gdl-callout">
            <div class="gdl-callout-icon">📌</div>
            <div class="gdl-callout-content">
            <h4>Strategy Reminder</h4>
            <p>
                The best Class 10 preparation plan is not equal time for every chapter. It is smart time
                based on weightage, weakness and repeated question patterns.
            </p>
            </div>
        </div>
        </section>

        <section>
            <h2>8 Weeks. One Plan. Here's How to Actually Use Them.</h2>

            <p>
                This plan assumes boards start in mid-February. Count back 8 weeks from your first paper
                and start there. The goal is not to study everything again. The goal is to diagnose,
                repair, practise, and consolidate.
            </p>

            <div class="week-grid">
                <div class="week-card">
                <div class="wk">Week 1</div>
                <div class="wk-title">Diagnose, don't study</div>
                <p>Take one full mock test without over-preparing. Use the result to map your baseline accuracy by unit.</p>
                </div>

                <div class="week-card">
                <div class="wk">Week 2</div>
                <div class="wk-title">Attack your two weakest units</div>
                <p>Spend more time on the lowest-accuracy units. Revise the concepts behind your wrong answers.</p>
                </div>

                <div class="week-card">
                <div class="wk">Week 3</div>
                <div class="wk-title">Prioritise high-mark units</div>
                <p>Focus on Algebra, Chemical Substances, Biology diagrams, writing practice, and map work.</p>
                </div>

                <div class="week-card peak">
                <div class="wk">Week 4</div>
                <div class="wk-title">Second mock and reattempt</div>
                <p>Take another mock. Compare repeated mistakes with Week 1 and reattempt every wrong answer.</p>
                </div>

                <div class="week-card">
                <div class="wk">Week 5</div>
                <div class="wk-title">Social Science structure week</div>
                <p>Practise answer writing, headings, bullet points, keywords and daily map work.</p>
                </div>

                <div class="week-card">
                <div class="wk">Week 6</div>
                <div class="wk-title">English and formula sheets</div>
                <p>Practise writing tasks three times a week and revise formula sheets daily from memory.</p>
                </div>

                <div class="week-card peak">
                <div class="wk">Week 7</div>
                <div class="wk-title">Wrong-question notebook sweep</div>
                <p>Reattempt every wrong question logged since Week 1. Flag anything still weak for final revision.</p>
                </div>

                <div class="week-card close">
                <div class="wk">Week 8</div>
                <div class="wk-title">Consolidate, don't panic</div>
                <p>No new chapters. Timed practice, quick revision, formula recall, sleep and confidence.</p>
                </div>
            </div>
            </section>

            <section>
            <h2>Studying More Isn't the Answer. This Is.</h2>

            <p>
                Most preparation problems come from one root issue: study sessions are disconnected. A student
                takes a mock test, sees a score, and moves on. A chapter is revised once and forgotten. Nothing
                adapts based on performance.
            </p>

            <div class="signal-box">
                <div class="signal-card noise">
                <div class="label">❌ Noise</div>
                <div class="val">62%</div>
                <p>Your Maths mock score tells you that something is wrong, but not exactly where to study next.</p>
                </div>

                <div class="signal-card signal">
                <div class="label">✅ Signal</div>
                <div class="val">Topic Map</div>
                <p>Quadratic Equations: 43% · Trigonometry: 58% · Statistics: 89% — now your next step is clear.</p>
                </div>
            </div>

            <h3>Meet Genelis: AI-Powered Personalized Learning for Class 10</h3>

            <p>
                Genelis is built on Adaptive Personalized Intelligence — a system that does not deliver the
                same content to every student. It learns from your performance, identifies specific learning
                gaps, generates customised study material, and guides revision based on actual progress.
            </p>

            <div class="accuracy-demo">
                <h4>What your weak area map can look like after a Science mock test</h4>

                <div class="acc-row">
                <div class="acc-subject">Heredity and Evolution</div>
                <div class="acc-bar"><div class="acc-fill" style="width:43%;background:#e04848"></div></div>
                <div class="acc-pct" style="color:#e04848">43%</div>
                </div>

                <div class="acc-row">
                <div class="acc-subject">Light — Refraction</div>
                <div class="acc-bar"><div class="acc-fill" style="width:58%;background:#eda100"></div></div>
                <div class="acc-pct" style="color:#eda100">58%</div>
                </div>

                <div class="acc-row">
                <div class="acc-subject">Acids and Bases</div>
                <div class="acc-bar"><div class="acc-fill" style="width:71%;background:#4a90d9"></div></div>
                <div class="acc-pct" style="color:#4a90d9">71%</div>
                </div>

                <div class="acc-row">
                <div class="acc-subject">Life Processes</div>
                <div class="acc-bar"><div class="acc-fill" style="width:88%;background:#1baf7a"></div></div>
                <div class="acc-pct" style="color:#1baf7a">88%</div>
                </div>
            </div>

            <h3>The Genelis Learning Loop™</h3>

            <p>
                Every feature is part of one connected system. The loop turns performance into the next
                learning action instead of leaving students to guess what to do.
            </p>

            <div class="loop-steps">
                <div class="loop-step"><span class="step-num">Step 1</span>Attempt mock test</div>
                <div class="loop-arrow">→</div>
                <div class="loop-step"><span class="step-num">Step 2</span>AI detects weak topics</div>
                <div class="loop-arrow">→</div>
                <div class="loop-step"><span class="step-num">Step 3</span>Wrong answers are logged</div>
                <div class="loop-arrow">→</div>
                <div class="loop-step"><span class="step-num">Step 4</span>Targeted notes appear</div>
                <div class="loop-arrow">→</div>
                <div class="loop-step"><span class="step-num">Step 5</span>Reattempt mistakes</div>
                <div class="loop-arrow">→</div>
                <div class="loop-step"><span class="step-num">Step 6</span>Gap verified closed</div>
            </div>

            <p>
                This is learning that compounds. Every session makes the next session more precise.
            </p>

            <p>
                <a href="https://app.genelis.in/?utm_source=blog&utm_medium=article&utm_campaign=class10-board-prep&utm_content=cta-inline">
                Start your personalised Class 10 study plan on Genelis — free →
                </a>
            </p>
            </section>
        """,

        "faq": [
            {
                "question": "How to prepare for Class 10 board exam effectively?",
                "answer": "Start with unit-wise weightage, focus on high-weightage chapters, take mock tests regularly, track mistakes, and revise weak areas instead of only revising comfortable chapters."
            },
            {
                "question": "Is Class 10 harder than Class 9?",
                "answer": "Yes. Class 10 introduces board-style preparation, timed exams, and greater pressure, so students need a more strategic study plan."
            },
            {
                "question": "How many hours should a Class 10 student study per day?",
                "answer": "In the final months, 4 to 6 focused hours can work well for many students, provided the time is spent on weak areas, mock tests, revision, and answer practice."
            },
            {
                "question": "Does Genelis help with Class 10 board exam preparation?",
                "answer": "Yes. Genelis helps Class 10 students with AI-powered notes, mock tests, weak-area tracking, personalised revision, and performance-based learning guidance."
            }
        ],

        "related_articles": [
            "class-10-maths-notes-important-questions",
            "class-10-science-high-yield-topics-cbse",
            "class-10-social-science-preparation",
            "smart-revision-ai-study-coach-cbse"
        ]
    }
]
def get_all_posts():
    return [prepare_blog_post(post) for post in BLOG_POSTS]


def get_post_by_slug(slug):
    post = next((post for post in BLOG_POSTS if post["slug"] == slug), None)

    if post is None:
        return None

    return prepare_blog_post(post)

def get_posts_by_category(category):
    return [
        post for post in BLOG_POSTS
        if post["category"].lower() == category.lower()
    ]


def get_posts_by_subject(subject):
    return [
        post for post in BLOG_POSTS
        if post["subject"].lower() == subject.lower()
    ]


def get_posts_by_class(student_class):
    return [
        post for post in BLOG_POSTS
        if post["class"] == student_class
    ]


def strip_html_tags(html):
    clean = re.sub(r"<.*?>", "", html)
    return " ".join(clean.split())


def estimate_reading_time(content):
    text = strip_html_tags(content)
    words = len(text.split())
    minutes = max(1, round(words / 200))
    return f"{minutes} min read"


def generate_excerpt(content, length=155):
    text = strip_html_tags(content)
    if len(text) <= length:
        return text
    return text[:length].rsplit(" ", 1)[0] + "..."


def prepare_blog_post(post):
    post = post.copy()

    post["meta_title"] = post.get("meta_title") or f"{post['title']} | Genelis"
    post["excerpt"] = post.get("excerpt") or generate_excerpt(post.get("content", ""))
    post["meta_description"] = post.get("meta_description") or post["excerpt"]
    post["reading_time"] = post.get("reading_time") or estimate_reading_time(post.get("content", ""))
    post["author"] = post.get("author") or "Genelis Team"
    post["featured_image"] = post.get("featured_image") or ""
    content_with_ids, toc = generate_toc(post.get("content", ""))

    post["content"] = content_with_ids
    post["toc"] = toc

    return post

def get_related_posts(current_slug, limit=3):
    current_post = get_post_by_slug(current_slug)

    if current_post is None:
        return []

    related = []

    for post in get_all_posts():
        if post["slug"] == current_slug:
            continue

        score = 0

        if post.get("class") == current_post.get("class"):
            score += 3

        if post.get("subject") == current_post.get("subject"):
            score += 2

        if post.get("category") == current_post.get("category"):
            score += 1

        if score > 0:
            related.append((score, post))

    related.sort(key=lambda item: item[0], reverse=True)

    return [post for score, post in related[:limit]]

def generate_toc(content):
    soup = BeautifulSoup(content, "html.parser")
    toc = []

    for heading in soup.find_all(["h2", "h3"]):
        text = heading.get_text(strip=True)
        heading_id = re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")

        heading["id"] = heading_id

        toc.append({
            "text": text,
            "id": heading_id,
            "level": heading.name
        })

    return str(soup), toc

def get_prev_next_posts(current_slug):
    posts = get_all_posts()

    current_index = next(
        (index for index, post in enumerate(posts) if post["slug"] == current_slug),
        None
    )

    if current_index is None:
        return None, None

    previous_post = posts[current_index - 1] if current_index > 0 else None
    next_post = posts[current_index + 1] if current_index < len(posts) - 1 else None

    return previous_post, next_post

def get_featured_post():
    posts = get_all_posts()

    if not posts:
        return None

    return posts[0]