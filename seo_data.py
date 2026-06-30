SEO_DATA = {
    "home": {
        "title": "Genelis | AI Learning Platform for CBSE & NCERT Students",
        "description": "Genelis is an AI learning platform for CBSE Classes 9–12 with AI Notes, Mock Tests, Question Bank, Study Analytics, and Personalized Learning.",
        "path": "/",
        "keywords": [
            "AI Learning Platform",
            "CBSE",
            "NCERT",
            "AI Notes",
            "Mock Tests",
            "Question Bank",
            "Personalized Learning",
            "AI Study Coach"
        ]
    },

    "about": {
        "title": "About Genelis | Connected Learning for CBSE Students",
        "description": "Learn why Genelis is building one connected learning experience for CBSE and NCERT students with AI-powered notes, practice, mocks, and guidance.",
        "path": "/about",
        "keywords": [
            "Genelis",
            "Connected Learning",
            "AI Education Platform",
            "CBSE",
            "NCERT",
            "Personalized Learning"
        ]
    },

    "learning_system": {
        "title": "Genelis Learning Loop™ | Connected AI Learning System",
        "description": "Discover the Genelis Learning Loop: Learn, Practice, Test, Analyse, Improve, Reinforce, and Excel through one connected AI learning system.",
        "path": "/learning-system",
        "keywords": [
            "The Genelis Learning Loop",
            "Connected Learning",
            "AI Learning Platform",
            "Personalized Learning",
            "Study Analytics",
            "AI Study Coach"
        ]
    },

    "classes": {
        "title": "CBSE Classes 9–12 | AI Notes, Mock Tests & Question Bank",
        "description": "Explore AI-powered learning for CBSE Classes 9, 10, 11, and 12 with NCERT-based AI Notes, Mock Tests, Question Bank, and Study Analytics.",
        "path": "/classes",
        "keywords": [
            "CBSE",
            "NCERT",
            "Class 9 Notes",
            "Class 10 Notes",
            "Class 11 Notes",
            "Class 12 Notes",
            "AI Notes",
            "Mock Tests"
        ]
    },

    "pricing": {
        "title": "Pricing | Genelis AI Notes, Mock Tests & Study Coach",
        "description": "View Genelis pricing plans for AI Notes, Mock Tests, Question Bank, AI Study Coach, Study Analytics, and Personalized Learning.",
        "path": "/pricing",
        "keywords": [
            "AI Notes",
            "Mock Tests",
            "Question Bank",
            "AI Study Coach",
            "Personalized Learning",
            "Study Analytics"
        ]
    },

    "blog": {
        "title": "Genelis Blog | CBSE Study Tips, Notes & Exam Preparation",
        "description": "Read Genelis insights on CBSE exam preparation, NCERT study strategies, Important Questions, Formula Sheets, AI Notes, and smarter revision.",
        "path": "/blog",
        "keywords": [
            "Exam Preparation",
            "Important Questions",
            "Formula Sheet",
            "Mathematics Notes",
            "Physics Notes",
            "Chemistry Notes",
            "Biology Notes"
        ]
    },

    "contact": {
        "title": "Contact Genelis | Support, Feedback & Partnerships",
        "description": "Contact Genelis for support, feedback, partnerships, school collaborations, and enquiries about AI-powered CBSE learning.",
        "path": "/contact",
        "keywords": [
            "Genelis",
            "AI Education Platform",
            "CBSE",
            "AI Learning Platform"
        ]
    },
        "terms": {
        "title": "Terms of Use | Genelis",
        "description": "Read the Genelis Terms of Use for using the website, platform, subscriptions, AI-powered learning features, and student services.",
        "path": "/terms",
        "keywords": ["Genelis Terms", "Terms of Use", "AI Learning Platform"]
    },

    "privacy": {
        "title": "Privacy Policy | Genelis",
        "description": "Read how Genelis collects, uses, protects, and manages user data for its AI-powered learning platform.",
        "path": "/privacy",
        "keywords": ["Genelis Privacy Policy", "Privacy Policy", "Student Data Protection"]
    },

    "cookies": {
        "title": "Cookie Policy | Genelis",
        "description": "Read the Genelis Cookie Policy to understand how cookies and similar technologies may be used on the website.",
        "path": "/cookies",
        "keywords": ["Cookie Policy", "Genelis Cookies", "Website Cookies"]
    },

    "refund": {
        "title": "Refund Policy | Genelis",
        "description": "Read the Genelis Refund Policy for subscriptions, billing, cancellations, and payment-related terms.",
        "path": "/refund",
        "keywords": ["Refund Policy", "Subscription Policy", "Genelis Pricing"]
    },

    "grievance": {
        "title": "Grievance Redressal | Genelis",
        "description": "Contact Genelis for grievance redressal, complaints, support issues, and platform-related concerns.",
        "path": "/grievance",
        "keywords": ["Grievance Redressal", "Genelis Support", "Student Support"]
    },

    "copyright": {
        "title": "Copyright Policy | Genelis",
        "description": "Read the Genelis Copyright Policy covering intellectual property, content ownership, and permitted platform usage.",
        "path": "/copyright",
        "keywords": ["Copyright Policy", "Intellectual Property", "Genelis Content"]
    },

    "childsafety": {
        "title": "Child & Student Safety Policy | Genelis",
        "description": "Read the Genelis Child and Student Safety Policy for safe, responsible, and age-appropriate learning experiences.",
        "path": "/childsafety",
        "keywords": ["Child Safety Policy", "Student Safety", "EdTech Safety"]
    },

    "responsibleAI": {
        "title": "Responsible AI Policy | Genelis",
        "description": "Read the Genelis Responsible AI Policy explaining safe, supportive, and transparent use of AI in learning.",
        "path": "/responsibleAI",
        "keywords": ["Responsible AI Policy", "AI in Education", "AI Learning Platform"]
    }
}


def get_class_seo(class_id, class_info):
    class_label = f"Class {class_id}"

    return {
        "title": f"CBSE {class_label} | AI Notes, Mock Tests & Question Bank | Genelis",
        "description": f"Prepare for CBSE {class_label} with Genelis using AI Notes, NCERT-based practice questions, mock tests, study analytics, and personalized learning guidance.",
        "path": f"/classes/{class_id}",
        "keywords": [
            "CBSE",
            "NCERT",
            f"{class_label} Notes",
            "AI Notes",
            "Mock Tests",
            "Question Bank",
            "Practice Questions",
            "Exam Preparation"
        ]
    }