def get_projects_data():
    """Returns structured projects data"""
    projects = [
        {
            "title": "DataInsightHub",
            "description": "Excel & Power BI Dashboard with automated analysis & AI-driven insights for comprehensive data visualization and business intelligence.",
            "technologies": ["Excel", "Power BI", "Python", "AI/ML"],
            "github_link": "https://github.com/KRSaiVarun/DatainsightHub",
            "live_link": None
        },
        {
            "title": "Vayu Vihar",
            "description": "Real-time helicopter booking web application with interactive booking system, payment integration, and flight tracking.",
            "technologies": ["React", "Node.js", "MongoDB", "Express"],
            "github_link": "https://github.com/krsaivarun/vayu-vihar",
            "live_link": None
        },
        {
            "title": "FlaskBlog",
            "description": "CRUD blog application built with Flask and SQLite, featuring user authentication, post management, and responsive design.",
            "technologies": ["Flask", "SQLite", "HTML", "CSS", "JavaScript"],
            "github_link": "https://github.com/krsaivarun/flaskblog",
            "live_link": None
        },
        {
            "title": "CyberScan-Pro",
            "description": "Python-based vulnerability scanner using Nmap & OSINT APIs for comprehensive network security assessment.",
            "technologies": ["Python", "Nmap", "APIs", "Cybersecurity"],
            "github_link": "https://github.com/krsaivarun/cyberscan-pro",
            "live_link": None
        },
        {
            "title": "LoanGuardian-AI",
            "description": "Machine learning-powered loan default prediction application built with Streamlit for financial risk assessment.",
            "technologies": ["Python", "Streamlit", "Scikit-learn", "Pandas"],
            "github_link": "https://github.com/krsaivarun/loanguardian-ai",
            "live_link": None
        },
        {
            "title": "DataInsight Hub Pro",
            "description": "Advanced React dashboard with Chart.js integration and smooth animations for enhanced data visualization experience.",
            "technologies": ["React", "Chart.js", "JavaScript", "CSS"],
            "github_link": "https://github.com/krsaivarun/datainsight-hub-pro",
            "live_link": None
        },
        {
            "title": "QR Code Generator",
            "description": "Simple and efficient QR code generator with customization options and bulk generation capabilities.",
            "technologies": ["Python", "QR Library", "Tkinter"],
            "github_link": "https://github.com/krsaivarun/qr-generator",
            "live_link": None
        },
        {
            "title": "Weather App",
            "description": "Real-time weather application with location-based forecasting and interactive weather maps.",
            "technologies": ["JavaScript", "Weather API", "HTML", "CSS"],
            "github_link": "https://github.com/krsaivarun/weather-app",
            "live_link": None
        },
        {
            "title": "Travel Manager",
            "description": "Comprehensive travel planning and management application with itinerary creation and expense tracking.",
            "technologies": ["Python", "Flask", "SQLite", "Bootstrap"],
            "github_link": "https://github.com/krsaivarun/travel-manager",
            "live_link": None
        }
    ]
    
    return projects

def get_featured_projects():
    """Returns featured projects for highlight display"""
    all_projects = get_projects_data()
    featured = ["DataInsightHub", "Vayu Vihar", "LoanGuardian-AI", "CyberScan-Pro"]
    
    return [project for project in all_projects if project["title"] in featured]

def get_projects_by_technology(tech):
    """Returns projects filtered by technology"""
    all_projects = get_projects_data()
    return [project for project in all_projects if tech in project["technologies"]]
