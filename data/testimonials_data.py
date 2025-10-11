def get_testimonials():
    """Returns structured testimonials and recommendations data"""
    testimonials = [
        {
            "id": 1,
            "name": "Dr. Rajesh Kumar",
            "role": "Professor, Mewa Vanguard College",
            "company": "Mewa Vanguard College",
            "image_url": None,
            "rating": 5,
            "text": "Sai Varun has consistently demonstrated exceptional skills in data analytics and web development. His DataInsightHub project showcases his ability to combine technical expertise with practical business solutions. He's a dedicated student who goes above and beyond in his projects.",
            "date": "2024-09-01"
        },
        {
            "id": 2,
            "name": "Priya Sharma",
            "role": "Senior Developer",
            "company": "NICT Computer Education",
            "image_url": None,
            "rating": 5,
            "text": "During his internship, Sai Varun proved to be a quick learner and an excellent team player. He successfully built a full-stack blog application using Flask and demonstrated strong problem-solving skills. His attention to detail and commitment to code quality were impressive.",
            "date": "2024-08-15"
        },
        {
            "id": 3,
            "name": "Amit Patel",
            "role": "Data Analyst",
            "company": "Tech Solutions Inc.",
            "image_url": None,
            "rating": 5,
            "text": "I collaborated with Sai Varun on a data visualization project. His proficiency in Excel, Power BI, and Python was remarkable. He has a unique ability to translate complex data into meaningful insights that drive business decisions.",
            "date": "2024-07-20"
        },
        {
            "id": 4,
            "name": "Sarah Johnson",
            "role": "Project Manager",
            "company": "Digital Innovations",
            "image_url": None,
            "rating": 5,
            "text": "Sai Varun's work on the Vayu Vihar helicopter booking system demonstrated his full-stack development capabilities. He handled both frontend and backend with ease, and his real-time features implementation was particularly impressive. A talented developer with great potential.",
            "date": "2024-06-10"
        },
        {
            "id": 5,
            "name": "Mohammed Ali",
            "role": "Cybersecurity Consultant",
            "company": "SecureNet Solutions",
            "image_url": None,
            "rating": 4,
            "text": "CyberScan-Pro shows Sai Varun's understanding of network security fundamentals. His implementation of vulnerability scanning and OSINT integration demonstrates both technical skills and ethical awareness in cybersecurity.",
            "date": "2024-05-25"
        },
        {
            "id": 6,
            "name": "Lisa Chen",
            "role": "ML Engineer",
            "company": "AI Innovations Lab",
            "image_url": None,
            "rating": 5,
            "text": "The LoanGuardian-AI project showcases Sai Varun's machine learning expertise. His approach to feature engineering and model selection was methodical and well-reasoned. He's definitely someone to watch in the AI/ML space.",
            "date": "2024-04-15"
        }
    ]
    
    return testimonials

def get_testimonial_by_id(testimonial_id):
    """Get a specific testimonial by ID"""
    testimonials = get_testimonials()
    for testimonial in testimonials:
        if testimonial['id'] == testimonial_id:
            return testimonial
    return None

def get_featured_testimonials(limit=3):
    """Get featured testimonials for display"""
    testimonials = get_testimonials()
    # Return top-rated testimonials with 5-star ratings
    featured = [t for t in testimonials if t['rating'] == 5]
    return featured[:limit]

def get_average_rating():
    """Calculate average rating from all testimonials"""
    testimonials = get_testimonials()
    if not testimonials:
        return 0
    total_rating = sum(t['rating'] for t in testimonials)
    return round(total_rating / len(testimonials), 1)

def get_testimonials_count():
    """Get total count of testimonials"""
    return len(get_testimonials())
