from datetime import datetime

def get_blog_posts():
    """Returns structured blog posts data"""
    posts = [
        {
            "id": 1,
            "title": "Building DataInsightHub: A Journey in Data Visualization",
            "slug": "building-datainsighthub",
            "author": "KR Sai Varun",
            "date": "2024-09-15",
            "category": "Data Analytics",
            "tags": ["Excel", "Power BI", "Python", "AI"],
            "excerpt": "Learn how I built a comprehensive Excel & Power BI dashboard with automated analysis and AI-driven insights for data visualization.",
            "content": """
# Building DataInsightHub: A Journey in Data Visualization

Creating DataInsightHub was an exciting challenge that combined my passion for data analytics with practical business intelligence needs.

## The Problem

Many businesses struggle to make sense of their data. They have Excel spreadsheets full of information but lack the tools to visualize trends and gain actionable insights.

## The Solution

DataInsightHub integrates Excel's powerful data manipulation capabilities with Power BI's stunning visualizations. The addition of AI-driven insights takes it a step further by automatically detecting patterns and anomalies.

## Key Features

- **Automated Data Processing**: Python scripts that clean and transform raw data
- **Interactive Dashboards**: Power BI dashboards that update in real-time
- **AI Insights**: Machine learning models that identify trends and predict outcomes
- **User-Friendly Interface**: Designed for non-technical users

## Technologies Used

- **Excel**: Data storage and initial processing
- **Power BI**: Visualization and reporting
- **Python**: Automation and AI/ML algorithms
- **Pandas**: Data manipulation

## Lessons Learned

1. **Start with the user**: Understanding user needs is crucial
2. **Iterate quickly**: Build MVPs and get feedback early
3. **Document everything**: Good documentation saves time later

Check out the project on [GitHub](https://github.com/KRSaiVarun/DatainsightHub)!
            """,
            "image_url": None
        },
        {
            "id": 2,
            "title": "Full Stack Development: Lessons from Building Vayu Vihar",
            "slug": "fullstack-lessons-vayu-vihar",
            "author": "KR Sai Varun",
            "date": "2024-08-20",
            "category": "Web Development",
            "tags": ["React", "Node.js", "MongoDB", "Full Stack"],
            "excerpt": "Discover the challenges and solutions in building a real-time helicopter booking web application with modern tech stack.",
            "content": """
# Full Stack Development: Lessons from Building Vayu Vihar

Vayu Vihar is a real-time helicopter booking platform that taught me invaluable lessons about full stack development.

## Architecture Overview

The application follows a modern MERN stack architecture:
- **Frontend**: React with responsive design
- **Backend**: Node.js and Express for API
- **Database**: MongoDB for flexible data storage
- **Real-time**: WebSocket integration for live updates

## Key Challenges

### 1. Real-Time Booking System
Managing concurrent bookings required careful state management and race condition handling.

### 2. Payment Integration
Implementing secure payment processing while maintaining a smooth user experience.

### 3. Flight Tracking
Integrating real-time location tracking with map visualization.

## Technical Decisions

- **Why React?**: Component reusability and efficient re-rendering
- **Why MongoDB?**: Flexible schema for evolving booking requirements
- **Why Node.js?**: Non-blocking I/O perfect for real-time applications

## Code Quality

Maintaining code quality through:
- ESLint and Prettier for consistent code style
- Jest for unit testing
- Git hooks for pre-commit validation

## Results

The application successfully handles multiple concurrent bookings with real-time updates and secure payment processing.

View the code on [GitHub](https://github.com/krsaivarun/vayu-vihar)!
            """,
            "image_url": None
        },
        {
            "id": 3,
            "title": "Machine Learning in Finance: LoanGuardian-AI Case Study",
            "slug": "ml-finance-loanguardian",
            "author": "KR Sai Varun",
            "date": "2024-07-10",
            "category": "AI/ML",
            "tags": ["Python", "Machine Learning", "Streamlit", "Finance"],
            "excerpt": "How I built a machine learning model to predict loan defaults with 89% accuracy using Python and Scikit-learn.",
            "content": """
# Machine Learning in Finance: LoanGuardian-AI Case Study

LoanGuardian-AI is a machine learning application that predicts loan default risk, helping financial institutions make better lending decisions.

## The Challenge

Financial institutions need to assess loan default risk accurately to minimize losses while maximizing approved loans.

## Data Science Approach

### 1. Data Collection
- Historical loan data
- Applicant demographics
- Credit history
- Employment information

### 2. Feature Engineering
Created meaningful features:
- Debt-to-income ratio
- Payment history score
- Employment stability index
- Credit utilization rate

### 3. Model Selection
Tested multiple algorithms:
- Logistic Regression: 82% accuracy
- Random Forest: 87% accuracy
- XGBoost: **89% accuracy** ✓

### 4. Model Validation
- Cross-validation to prevent overfitting
- ROC-AUC score: 0.92
- Precision-Recall analysis

## Implementation with Streamlit

Built an interactive web app where users can:
- Input applicant information
- Get instant risk assessment
- View feature importance
- Explore model explanations

## Key Learnings

1. **Feature Quality > Quantity**: Focus on meaningful features
2. **Balance Your Dataset**: Handle class imbalance carefully
3. **Explainability Matters**: Model interpretability is crucial in finance
4. **Continuous Monitoring**: Models need regular retraining

## Tech Stack

- **Python**: Core language
- **Scikit-learn**: ML algorithms
- **Pandas**: Data manipulation
- **Streamlit**: Web interface
- **Plotly**: Interactive visualizations

Explore the project on [GitHub](https://github.com/krsaivarun/loanguardian-ai)!
            """,
            "image_url": None
        },
        {
            "id": 4,
            "title": "Cybersecurity Basics: Building CyberScan-Pro",
            "slug": "cybersecurity-basics-cyberscan",
            "author": "KR Sai Varun",
            "date": "2024-06-05",
            "category": "Security",
            "tags": ["Python", "Security", "Nmap", "OSINT"],
            "excerpt": "A beginner's guide to network security assessment through building a Python-based vulnerability scanner.",
            "content": """
# Cybersecurity Basics: Building CyberScan-Pro

CyberScan-Pro is a vulnerability scanner that helped me understand network security fundamentals.

## What is Vulnerability Scanning?

Vulnerability scanning is the process of identifying security weaknesses in networks, systems, and applications before attackers can exploit them.

## Building CyberScan-Pro

### Core Features

1. **Port Scanning**: Identify open ports using Nmap
2. **Service Detection**: Determine running services and versions
3. **OSINT Integration**: Gather public information
4. **Vulnerability Database**: Check against known CVEs
5. **Report Generation**: Create detailed security reports

### Technical Implementation

```python
# Example: Port scanning with Nmap
import nmap

nm = nmap.PortScanner()
nm.scan(hosts='192.168.1.1', arguments='-sV -sC')

for host in nm.all_hosts():
    print(f'Host: {host} ({nm[host].hostname()})')
    print(f'State: {nm[host].state()}')
    
    for proto in nm[host].all_protocols():
        ports = nm[host][proto].keys()
        for port in ports:
            print(f'Port: {port}\\tState: {nm[host][proto][port]["state"]}')
```

## Security Best Practices

1. **Always Get Permission**: Never scan networks without authorization
2. **Rate Limiting**: Avoid overwhelming target systems
3. **Responsible Disclosure**: Report vulnerabilities ethically
4. **Continuous Learning**: Stay updated with latest threats

## Tools & Technologies

- **Nmap**: Network scanning
- **Python**: Automation and scripting
- **OSINT APIs**: Information gathering
- **CVE Database**: Vulnerability tracking

## Ethical Considerations

Security tools are powerful. Always:
- Use them legally and ethically
- Get proper authorization
- Report findings responsibly
- Respect privacy and data protection laws

Check it out on [GitHub](https://github.com/krsaivarun/cyberscan-pro)!
            """,
            "image_url": None
        }
    ]
    
    return posts

def get_blog_post_by_id(post_id):
    """Get a specific blog post by ID"""
    posts = get_blog_posts()
    for post in posts:
        if post['id'] == post_id:
            return post
    return None

def get_blog_post_by_slug(slug):
    """Get a specific blog post by slug"""
    posts = get_blog_posts()
    for post in posts:
        if post['slug'] == slug:
            return post
    return None

def get_blog_categories():
    """Get all unique blog categories"""
    posts = get_blog_posts()
    categories = set(post['category'] for post in posts)
    return sorted(list(categories))

def get_posts_by_category(category):
    """Get all posts in a specific category"""
    posts = get_blog_posts()
    return [post for post in posts if post['category'] == category]

def get_recent_posts(limit=3):
    """Get most recent blog posts"""
    posts = get_blog_posts()
    sorted_posts = sorted(posts, key=lambda x: x['date'], reverse=True)
    return sorted_posts[:limit]
