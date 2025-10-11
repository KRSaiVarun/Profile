import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
import base64
import os
from PIL import Image
from data.skills_data import get_skills_data
from data.projects_data import get_projects_data
from data.blog_data import get_blog_posts, get_blog_post_by_id, get_blog_categories, get_recent_posts
from data.testimonials_data import get_testimonials, get_featured_testimonials, get_average_rating
from utils.email_handler import send_email
from utils.analytics import (
    load_analytics, get_total_views, get_page_view_trends, 
    get_popular_pages, get_popular_projects, get_engagement_stats, get_recent_activity
)

# Page configuration
st.set_page_config(
    page_title="KR Sai Varun - Portfolio",
    page_icon="👨‍💻",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for dark theme
st.markdown("""
<style>
    .main-header {
        background: linear-gradient(90deg, #339af0 0%, #845ef7 25%, #ff6b6b 55%, #ffd43b 85%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        font-size: 3rem;
        font-weight: bold;
        text-align: center;
        margin-bottom: 20px;
    }
    .section-header {
        color: #e6eef8;
        font-size: 2rem;
        font-weight: bold;
        margin-bottom: 15px;
        border-bottom: 2px solid #4A90E2;
        padding-bottom: 10px;
    }
    .skill-card {
        background-color: #12141a;
        padding: 20px;
        border-radius: 10px;
        border: 1px solid rgba(255,255,255,0.1);
        margin: 10px 0;
    }
    .project-card {
        background-color: #12141a;
        padding: 20px;
        border-radius: 10px;
        border: 1px solid rgba(255,255,255,0.1);
        margin: 15px 0;
    }
    .social-links {
        display: flex;
        gap: 20px;
        justify-content: center;
        margin: 20px 0;
    }
    .contact-form {
        background-color: #12141a;
        padding: 25px;
        border-radius: 10px;
        border: 1px solid rgba(255,255,255,0.1);
    }
    .blog-card {
        background-color: #12141a;
        padding: 20px;
        border-radius: 10px;
        border: 1px solid rgba(255,255,255,0.1);
        margin: 15px 0;
        transition: transform 0.2s;
    }
    .blog-card:hover {
        transform: translateY(-2px);
        border-color: #4A90E2;
    }
    .blog-meta {
        color: #a9b3c3;
        font-size: 0.9rem;
        margin: 10px 0;
    }
    .blog-tag {
        background-color: rgba(74, 144, 226, 0.2);
        color: #4A90E2;
        padding: 4px 12px;
        border-radius: 12px;
        font-size: 0.85rem;
        margin-right: 8px;
        display: inline-block;
    }
    .testimonial-card {
        background-color: #12141a;
        padding: 25px;
        border-radius: 10px;
        border: 1px solid rgba(255,255,255,0.1);
        margin: 15px 0;
        position: relative;
    }
    .testimonial-quote {
        font-style: italic;
        color: #e6eef8;
        margin: 15px 0;
        line-height: 1.6;
    }
    .testimonial-author {
        font-weight: 600;
        color: #4A90E2;
        margin-top: 15px;
    }
    .testimonial-role {
        color: #a9b3c3;
        font-size: 0.9rem;
    }
    .star-rating {
        color: #ffd43b;
        font-size: 1.2rem;
    }
</style>
""", unsafe_allow_html=True)

def load_profile_image():
    """Load and display profile image"""
    try:
        image = Image.open("assets/profile.jpg")
        return image
    except FileNotFoundError:
        st.warning("Profile image not found. Using placeholder.")
        return None

def create_skills_chart(skills_data, chart_type="bar"):
    """Create interactive skills visualization"""
    df = pd.DataFrame(skills_data)
    
    if chart_type == "bar":
        fig = px.bar(
            df, 
            x='skill', 
            y='percentage',
            color='category',
            title="Skills Proficiency",
            color_discrete_sequence=['#4A90E2', '#845ef7', '#ff6b6b', '#51cf66']
        )
    elif chart_type == "radar":
        categories = df['category'].unique()
        fig = go.Figure()
        
        for category in categories:
            category_data = df[df['category'] == category]
            fig.add_trace(go.Scatterpolar(
                r=category_data['percentage'],
                theta=category_data['skill'],
                fill='toself',
                name=category
            ))
        
        fig.update_layout(
            polar=dict(
                radialaxis=dict(
                    visible=True,
                    range=[0, 100]
                )),
            showlegend=True,
            title="Skills Radar Chart"
        )
    
    fig.update_layout(
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        font_color='#e6eef8'
    )
    
    return fig

def download_resume():
    """Create download button for resume"""
    try:
        with open("assets/resume.pdf", "rb") as file:
            btn = st.download_button(
                label="📄 Download Resume",
                data=file,
                file_name="KR_Sai_Varun_Resume.pdf",
                mime="application/pdf",
                use_container_width=True
            )
        return btn
    except FileNotFoundError:
        st.error("Resume file not found.")
        return False

def main():
    # Sidebar navigation
    st.sidebar.title("🚀 Navigation")
    page = st.sidebar.selectbox(
        "Go to section:",
        ["🏠 Home", "👨‍💻 About", "🔧 Skills", "💼 Projects", "📝 Blog", "⭐ Testimonials", "📊 Analytics", "📧 Contact"]
    )
    
    # Main content based on selected page
    if page == "🏠 Home":
        show_home()
    elif page == "👨‍💻 About":
        show_about()
    elif page == "🔧 Skills":
        show_skills()
    elif page == "💼 Projects":
        show_projects()
    elif page == "📝 Blog":
        show_blog()
    elif page == "⭐ Testimonials":
        show_testimonials()
    elif page == "📊 Analytics":
        show_analytics()
    elif page == "📧 Contact":
        show_contact()

def show_home():
    """Homepage with introduction"""
    col1, col2, col3 = st.columns([1, 2, 1])
    
    with col2:
        st.markdown('<h1 class="main-header">Hi, I\'m Sai Varun</h1>', unsafe_allow_html=True)
        st.markdown("### Full Stack Developer & Data Analyst")
        
        # Profile image
        image = load_profile_image()
        if image:
            st.image(image, width=300, use_column_width=False)
        
        st.markdown("""
        **Motivated BCA student** with expertise in Excel, Power BI, and full stack development. 
        Skilled in data visualization, reporting, and dashboards, alongside strong web development experience.
        """)
        
        # Social links
        st.markdown("""
        <div class="social-links">
            <a href="https://github.com/krsaivarun" target="_blank">
                <img src="https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white" alt="GitHub">
            </a>
            <a href="https://www.linkedin.com/in/kr-r-sai-varun-891788262" target="_blank">
                <img src="https://img.shields.io/badge/LinkedIn-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white" alt="LinkedIn">
            </a>
        </div>
        """, unsafe_allow_html=True)
        
        # Download resume button
        download_resume()

def show_about():
    """About section with education and experience"""
    st.markdown('<h2 class="section-header">About Me</h2>', unsafe_allow_html=True)
    
    col1, col2 = st.columns([1, 2])
    
    with col1:
        image = load_profile_image()
        if image:
            st.image(image, use_column_width=True)
    
    with col2:
        st.markdown("### I'm KR Sai Varun")
        st.markdown("""
        Motivated BCA student (2022–2025, 80% aggregate) with expertise in Excel, Power BI, and full stack development. 
        Skilled in data visualization, reporting, and dashboards, alongside strong web development experience. 
        Effective communicator with proven teamwork, problem-solving, and presentation skills, seeking to contribute 
        in data analysis and full stack roles.
        """)
    
    # Education section
    st.markdown('<h3 class="section-header">🎓 Education</h3>', unsafe_allow_html=True)
    education_data = [
        {"Degree": "BCA", "Institution": "Mewa Vanguard College, Bangalore", "Period": "2022–2025", "Grade": "80%"},
        {"Degree": "Pre-University", "Institution": "Sri Krishna Degree College", "Period": "2022", "Grade": "55%"},
        {"Degree": "Secondary", "Institution": "VET School VV Puram", "Period": "2020", "Grade": "60%"}
    ]
    
    for edu in education_data:
        st.markdown(f"""
        **{edu['Degree']}** - {edu['Institution']} ({edu['Period']}) | **{edu['Grade']}**
        """)
    
    # Experience section
    st.markdown('<h3 class="section-header">💼 Experience</h3>', unsafe_allow_html=True)
    st.markdown("""
    **Full Stack Web Development Intern** - NICT Computer Education  
    *May 2024 – Sep 2025*
    
    • Built a CRUD blog platform using Flask & SQLite  
    • Designed responsive UIs with HTML, CSS, JavaScript  
    • Managed SQL operations for dynamic content  
    • Used Excel for task tracking and reporting  
    • Collaborated with team members to deliver project milestones
    """)

def show_skills():
    """Skills section with interactive visualizations"""
    st.markdown('<h2 class="section-header">🔧 Technical Skills</h2>', unsafe_allow_html=True)
    
    skills_data = get_skills_data()
    
    # Chart type selector
    col1, col2 = st.columns([3, 1])
    with col2:
        chart_type = st.selectbox("Chart Type:", ["bar", "radar"])
    
    # Create and display chart
    fig = create_skills_chart(skills_data, chart_type)
    st.plotly_chart(fig, use_container_width=True)
    
    # Skills breakdown by category
    st.markdown("### Skills Breakdown")
    
    df = pd.DataFrame(skills_data)
    categories = df['category'].unique()
    
    for category in categories:
        st.markdown(f"#### {category}")
        category_skills = df[df['category'] == category]
        
        cols = st.columns(2)
        for i, (_, skill) in enumerate(category_skills.iterrows()):
            with cols[i % 2]:
                progress_value = skill['percentage'] / 100
                st.metric(
                    label=skill['skill'],
                    value=f"{skill['percentage']}%"
                )
                st.progress(progress_value)

def show_projects():
    """Projects showcase section"""
    st.markdown('<h2 class="section-header">💼 Projects</h2>', unsafe_allow_html=True)
    
    projects = get_projects_data()
    
    # Get all unique technologies and categories
    all_technologies = set()
    all_categories = set()
    for project in projects:
        all_technologies.update(project['technologies'])
        all_categories.add(project['category'])
    all_technologies = sorted(list(all_technologies))
    all_categories = sorted(list(all_categories))
    
    # Initialize session state for filters if not exists
    if 'selected_techs' not in st.session_state:
        st.session_state.selected_techs = []
    if 'selected_category' not in st.session_state:
        st.session_state.selected_category = "All"
    
    # Filtering controls
    col1, col2, col3 = st.columns([2, 2, 1])
    
    with col1:
        selected_techs = st.multiselect(
            "Filter by Technology:",
            all_technologies,
            default=st.session_state.selected_techs,
            key="tech_filter",
            placeholder="Select technologies..."
        )
        st.session_state.selected_techs = selected_techs
    
    with col2:
        category_options = ["All"] + all_categories
        selected_category = st.selectbox(
            "Filter by Category:",
            category_options,
            index=category_options.index(st.session_state.selected_category),
            key="category_filter"
        )
        st.session_state.selected_category = selected_category
    
    with col3:
        st.markdown("<br>", unsafe_allow_html=True)
        if st.button("Clear Filters", use_container_width=True):
            # Clear both custom state and widget keys
            st.session_state.selected_techs = []
            st.session_state.selected_category = "All"
            if 'tech_filter' in st.session_state:
                del st.session_state['tech_filter']
            if 'category_filter' in st.session_state:
                del st.session_state['category_filter']
            st.rerun()
    
    # Filter projects
    filtered_projects = projects
    
    # Filter by category
    if selected_category != "All":
        filtered_projects = [p for p in filtered_projects if p['category'] == selected_category]
    
    # Filter by technology
    if selected_techs:
        filtered_projects = [
            p for p in filtered_projects 
            if any(tech in p['technologies'] for tech in selected_techs)
        ]
    
    # Show project count
    st.markdown(f"**Showing {len(filtered_projects)} of {len(projects)} projects**")
    st.markdown("---")
    
    # Create project cards
    if filtered_projects:
        for project in filtered_projects:
            with st.container():
                st.markdown(f'<div class="project-card">', unsafe_allow_html=True)
                
                col1, col2 = st.columns([3, 1])
                
                with col1:
                    st.markdown(f"### {project['title']}")
                    st.markdown(f"**Category:** {project['category']}")
                    st.markdown(project['description'])
                    
                    # Technologies used
                    if project['technologies']:
                        tech_badges = " ".join([f"`{tech}`" for tech in project['technologies']])
                        st.markdown(f"**Technologies:** {tech_badges}")
                
                with col2:
                    if project['github_link']:
                        st.link_button("View on GitHub", project['github_link'])
                    if project['live_link']:
                        st.link_button("Live Demo", project['live_link'])
                
                st.markdown('</div>', unsafe_allow_html=True)
                st.markdown("---")
    else:
        st.info("No projects match the selected filters. Try selecting different options.")

def show_blog():
    """Blog section with posts listing and detail view"""
    st.markdown('<h2 class="section-header">📝 Blog</h2>', unsafe_allow_html=True)
    
    # Initialize session state for blog navigation
    if 'selected_post_id' not in st.session_state:
        st.session_state.selected_post_id = None
    
    # If a post is selected, show the post detail
    if st.session_state.selected_post_id:
        show_blog_post(st.session_state.selected_post_id)
        return
    
    # Get blog posts
    posts = get_blog_posts()
    categories = get_blog_categories()
    
    # Category filter
    col1, col2 = st.columns([3, 1])
    with col1:
        selected_category = st.selectbox(
            "Filter by Category:",
            ["All"] + categories,
            key="blog_category_filter"
        )
    
    # Filter posts by category
    filtered_posts = posts
    if selected_category != "All":
        filtered_posts = [p for p in posts if p['category'] == selected_category]
    
    with col2:
        st.markdown("<br>", unsafe_allow_html=True)
        if selected_category == "All":
            st.markdown(f"**{len(filtered_posts)} Posts**")
        else:
            st.markdown(f"**{len(filtered_posts)} of {len(posts)} Posts**")
    
    st.markdown("---")
    
    # Display blog posts as cards
    for post in filtered_posts:
        with st.container():
            st.markdown('<div class="blog-card">', unsafe_allow_html=True)
            
            # Post title
            st.markdown(f"### {post['title']}")
            
            # Post metadata
            st.markdown(f'<div class="blog-meta">📅 {post["date"]} | 👤 {post["author"]} | 📂 {post["category"]}</div>', unsafe_allow_html=True)
            
            # Post excerpt
            st.markdown(post['excerpt'])
            
            # Tags
            if post['tags']:
                tags_html = "".join([f'<span class="blog-tag">{tag}</span>' for tag in post['tags']])
                st.markdown(tags_html, unsafe_allow_html=True)
            
            # Read more button
            col1, col2, col3 = st.columns([1, 1, 3])
            with col1:
                if st.button("Read More →", key=f"read_{post['id']}", use_container_width=True):
                    st.session_state.selected_post_id = post['id']
                    st.rerun()
            
            st.markdown('</div>', unsafe_allow_html=True)
            st.markdown("---")

def show_blog_post(post_id):
    """Display a single blog post"""
    post = get_blog_post_by_id(post_id)
    
    if not post:
        st.error("Post not found!")
        if st.button("← Back to Blog"):
            st.session_state.selected_post_id = None
            st.rerun()
        return
    
    # Back button
    if st.button("← Back to Blog"):
        st.session_state.selected_post_id = None
        st.rerun()
    
    # Post header
    st.markdown(f"# {post['title']}")
    st.markdown(f'<div class="blog-meta">📅 {post["date"]} | 👤 {post["author"]} | 📂 {post["category"]}</div>', unsafe_allow_html=True)
    
    # Tags
    if post['tags']:
        tags_html = "".join([f'<span class="blog-tag">{tag}</span>' for tag in post['tags']])
        st.markdown(tags_html, unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Post content (markdown)
    st.markdown(post['content'])
    
    st.markdown("---")
    
    # Back button at the bottom
    if st.button("← Back to Blog", key="back_bottom"):
        st.session_state.selected_post_id = None
        st.rerun()

def show_testimonials():
    """Testimonials and recommendations section"""
    st.markdown('<h2 class="section-header">⭐ Testimonials & Recommendations</h2>', unsafe_allow_html=True)
    
    testimonials = get_testimonials()
    avg_rating = get_average_rating()
    
    # Display stats
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Total Reviews", len(testimonials))
    with col2:
        st.metric("Average Rating", f"{avg_rating}/5")
    with col3:
        five_star = sum(1 for t in testimonials if t['rating'] == 5)
        st.metric("5-Star Reviews", five_star)
    
    st.markdown("---")
    
    # Display testimonials in a grid
    for i in range(0, len(testimonials), 2):
        cols = st.columns(2)
        
        for j, col in enumerate(cols):
            if i + j < len(testimonials):
                testimonial = testimonials[i + j]
                with col:
                    st.markdown('<div class="testimonial-card">', unsafe_allow_html=True)
                    
                    # Star rating
                    stars = "⭐" * testimonial['rating']
                    st.markdown(f'<div class="star-rating">{stars}</div>', unsafe_allow_html=True)
                    
                    # Quote
                    st.markdown(f'<div class="testimonial-quote">"{testimonial["text"]}"</div>', unsafe_allow_html=True)
                    
                    # Author info
                    st.markdown(f'<div class="testimonial-author">{testimonial["name"]}</div>', unsafe_allow_html=True)
                    st.markdown(f'<div class="testimonial-role">{testimonial["role"]}, {testimonial["company"]}</div>', unsafe_allow_html=True)
                    
                    st.markdown('</div>', unsafe_allow_html=True)

def show_analytics():
    """Analytics dashboard section"""
    st.markdown('<h2 class="section-header">📊 Analytics Dashboard</h2>', unsafe_allow_html=True)
    
    st.info("📈 This dashboard shows simulated portfolio analytics for demonstration purposes.")
    
    # Get analytics data
    engagement = get_engagement_stats()
    recent = get_recent_activity(7)
    
    # Key metrics
    st.markdown("### 📈 Key Metrics")
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("Total Views", f"{engagement['total_views']:,}")
    with col2:
        st.metric("Contact Submissions", engagement['contact_submissions'])
    with col3:
        st.metric("Resume Downloads", engagement['resume_downloads'])
    with col4:
        st.metric("Last 7 Days", f"{recent['total']:,}")
    
    st.markdown("---")
    
    # Page views over time
    st.markdown("### 📅 Page Views Over Time (Last 30 Days)")
    
    trends = get_page_view_trends()
    df_trends = pd.DataFrame(trends)
    
    # Create line chart
    fig_trends = px.line(
        df_trends,
        x='date',
        y=['home', 'about', 'skills', 'projects', 'blog', 'testimonials', 'contact'],
        title="Daily Page Views",
        labels={'value': 'Views', 'variable': 'Page', 'date': 'Date'}
    )
    fig_trends.update_layout(
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        font_color='#e6eef8',
        hovermode='x unified'
    )
    st.plotly_chart(fig_trends, use_container_width=True)
    
    st.markdown("---")
    
    # Popular pages and projects
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("### 🏆 Most Popular Pages")
        popular_pages = get_popular_pages()
        
        for page, views in popular_pages[:5]:
            st.markdown(f"**{page.title()}**: {views:,} views")
            progress = views / popular_pages[0][1] if popular_pages else 0
            st.progress(progress)
    
    with col2:
        st.markdown("### 💼 Most Popular Projects")
        popular_projects = get_popular_projects()
        
        for project, views in popular_projects[:5]:
            st.markdown(f"**{project}**: {views:,} views")
            progress = views / popular_projects[0][1] if popular_projects else 0
            st.progress(progress)
    
    st.markdown("---")
    
    # Engagement breakdown
    st.markdown("### 🎯 Engagement Breakdown")
    
    # Create pie chart for page distribution
    page_data = get_popular_pages()
    df_pages = pd.DataFrame(page_data, columns=['Page', 'Views'])
    
    fig_pie = px.pie(
        df_pages,
        values='Views',
        names='Page',
        title='Page View Distribution',
        color_discrete_sequence=px.colors.sequential.Blues_r
    )
    fig_pie.update_layout(
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        font_color='#e6eef8'
    )
    st.plotly_chart(fig_pie, use_container_width=True)

def show_contact():
    """Contact form section"""
    st.markdown('<h2 class="section-header">📧 Contact Me</h2>', unsafe_allow_html=True)
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown('<div class="contact-form">', unsafe_allow_html=True)
        
        with st.form("contact_form", clear_on_submit=True):
            name = st.text_input("Your Name *", placeholder="Enter your full name")
            email = st.text_input("Your Email *", placeholder="Enter your email address")
            subject = st.text_input("Subject", placeholder="What's this about?")
            message = st.text_area("Message *", placeholder="Your message here...", height=150)
            
            submitted = st.form_submit_button("Send Message", use_container_width=True)
            
            if submitted:
                if name and email and message:
                    success = send_email(name, email, subject, message)
                    if success:
                        st.success("Message sent successfully! I'll get back to you soon.")
                    else:
                        st.error("Failed to send message. Please try again or contact me directly.")
                else:
                    st.error("Please fill in all required fields (marked with *).")
        
        st.markdown('</div>', unsafe_allow_html=True)
    
    with col2:
        st.markdown("### Get in Touch")
        st.markdown("""
        **📧 Email:** krsaivarun@gmail.com  
        **📱 Phone:** +91 8618266736  
        **📍 Location:** Bangalore, India
        
        **Connect with me:**
        """)
        
        st.markdown("""
        <div style="display: flex; flex-direction: column; gap: 10px;">
            <a href="https://github.com/krsaivarun" target="_blank" style="text-decoration: none;">
                <img src="https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white" alt="GitHub">
            </a>
            <a href="https://www.linkedin.com/in/kr-r-sai-varun-891788262" target="_blank" style="text-decoration: none;">
                <img src="https://img.shields.io/badge/LinkedIn-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white" alt="LinkedIn">
            </a>
        </div>
        """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
