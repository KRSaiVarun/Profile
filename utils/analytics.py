import json
import os
from datetime import datetime, timedelta
import random

def get_analytics_file():
    """Get the analytics data file path"""
    return "data/analytics.json"

def initialize_analytics():
    """Initialize analytics data file if it doesn't exist"""
    analytics_file = get_analytics_file()
    
    if not os.path.exists(analytics_file):
        # Create data directory if needed
        os.makedirs("data", exist_ok=True)
        
        # Initialize with sample data for demonstration
        initial_data = generate_sample_analytics()
        
        with open(analytics_file, 'w') as f:
            json.dump(initial_data, f, indent=2)
    
    return analytics_file

def generate_sample_analytics():
    """Generate sample analytics data for demonstration"""
    end_date = datetime.now()
    start_date = end_date - timedelta(days=30)
    
    page_views = []
    current_date = start_date
    
    while current_date <= end_date:
        # Generate random views for each day
        date_str = current_date.strftime("%Y-%m-%d")
        
        # More views on weekdays, less on weekends
        is_weekend = current_date.weekday() >= 5
        base_views = random.randint(10, 30) if not is_weekend else random.randint(5, 15)
        
        page_views.append({
            "date": date_str,
            "home": max(0, random.randint(base_views - 5, base_views + 5)),
            "about": max(0, random.randint(base_views - 10, base_views)),
            "skills": max(0, random.randint(base_views - 15, base_views - 5)),
            "projects": max(0, random.randint(base_views - 8, base_views + 3)),
            "blog": max(0, random.randint(base_views - 12, base_views - 2)),
            "testimonials": max(0, random.randint(base_views - 15, base_views - 8)),
            "contact": max(0, random.randint(base_views - 10, base_views - 3))
        })
        
        current_date += timedelta(days=1)
    
    # Project views
    project_views = {
        "DataInsightHub": random.randint(150, 250),
        "Vayu Vihar": random.randint(120, 200),
        "LoanGuardian-AI": random.randint(100, 180),
        "CyberScan-Pro": random.randint(90, 150),
        "DataInsight Hub Pro": random.randint(80, 140),
        "FlaskBlog": random.randint(70, 120),
        "QR Code Generator": random.randint(50, 100),
        "Weather App": random.randint(60, 110),
        "Travel Manager": random.randint(55, 95)
    }
    
    # Blog post views
    blog_views = {
        "1": random.randint(80, 150),
        "2": random.randint(70, 130),
        "3": random.randint(60, 120),
        "4": random.randint(50, 100)
    }
    
    # Contact form submissions
    contact_submissions = random.randint(15, 35)
    
    # Resume downloads
    resume_downloads = random.randint(40, 80)
    
    return {
        "page_views": page_views,
        "project_views": project_views,
        "blog_views": blog_views,
        "contact_submissions": contact_submissions,
        "resume_downloads": resume_downloads,
        "last_updated": datetime.now().isoformat()
    }

def load_analytics():
    """Load analytics data from file"""
    analytics_file = initialize_analytics()
    
    try:
        with open(analytics_file, 'r') as f:
            return json.load(f)
    except Exception as e:
        print(f"Error loading analytics: {e}")
        return generate_sample_analytics()

def get_total_views():
    """Get total page views across all pages"""
    data = load_analytics()
    total = 0
    
    for day in data['page_views']:
        total += sum([day[page] for page in day if page != 'date'])
    
    return total

def get_page_view_trends():
    """Get page view trends over time"""
    data = load_analytics()
    return data['page_views']

def get_popular_pages():
    """Get most popular pages"""
    data = load_analytics()
    page_totals = {}
    
    for day in data['page_views']:
        for page, views in day.items():
            if page != 'date':
                page_totals[page] = page_totals.get(page, 0) + views
    
    # Sort by views
    sorted_pages = sorted(page_totals.items(), key=lambda x: x[1], reverse=True)
    return sorted_pages

def get_popular_projects():
    """Get most popular projects"""
    data = load_analytics()
    sorted_projects = sorted(data['project_views'].items(), key=lambda x: x[1], reverse=True)
    return sorted_projects

def get_popular_blog_posts():
    """Get most popular blog posts"""
    data = load_analytics()
    sorted_posts = sorted(data['blog_views'].items(), key=lambda x: x[1], reverse=True)
    return sorted_posts

def get_engagement_stats():
    """Get engagement statistics"""
    data = load_analytics()
    return {
        "contact_submissions": data['contact_submissions'],
        "resume_downloads": data['resume_downloads'],
        "total_views": get_total_views()
    }

def get_recent_activity(days=7):
    """Get recent activity data for the last N days"""
    data = load_analytics()
    recent_views = data['page_views'][-days:]
    
    total_recent_views = sum([sum([day[page] for page in day if page != 'date']) for day in recent_views])
    
    return {
        "views": recent_views,
        "total": total_recent_views
    }
