def get_skills_data():
    """Returns structured skills data for visualization"""
    skills_data = [
        # Data Tools
        {"skill": "MS Excel", "percentage": 90, "category": "Data Tools"},
        {"skill": "Power BI", "percentage": 88, "category": "Data Tools"},
        {"skill": "Pandas", "percentage": 85, "category": "Data Tools"},
        {"skill": "Tableau", "percentage": 80, "category": "Data Tools"},
        
        # Programming Languages
        {"skill": "Python", "percentage": 87, "category": "Programming"},
        {"skill": "JavaScript", "percentage": 85, "category": "Programming"},
        {"skill": "Java", "percentage": 80, "category": "Programming"},
        {"skill": "SQL", "percentage": 87, "category": "Programming"},
        
        # Web Development
        {"skill": "HTML5", "percentage": 90, "category": "Web Development"},
        {"skill": "CSS3", "percentage": 88, "category": "Web Development"},
        {"skill": "React", "percentage": 80, "category": "Web Development"},
        {"skill": "Node.js", "percentage": 80, "category": "Web Development"},
        {"skill": "MongoDB", "percentage": 80, "category": "Web Development"},
        {"skill": "Flask", "percentage": 85, "category": "Web Development"},
        
        # AI/ML
        {"skill": "Scikit-learn", "percentage": 75, "category": "AI/ML"},
        {"skill": "TensorFlow", "percentage": 70, "category": "AI/ML"},
        {"skill": "OpenCV", "percentage": 72, "category": "AI/ML"},
        {"skill": "NLP", "percentage": 68, "category": "AI/ML"},
    ]
    
    return skills_data

def get_skills_by_category():
    """Returns skills grouped by category"""
    skills_data = get_skills_data()
    categories = {}
    
    for skill in skills_data:
        category = skill['category']
        if category not in categories:
            categories[category] = []
        categories[category].append(skill)
    
    return categories
