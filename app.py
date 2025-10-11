import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
import base64
import os
from PIL import Image
from data.skills_data import get_skills_data
from data.projects_data import get_projects_data
from utils.email_handler import send_email

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
        ["🏠 Home", "👨‍💻 About", "🔧 Skills", "💼 Projects", "📧 Contact"]
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
    
    # Create project cards
    for project in projects:
        with st.container():
            st.markdown(f'<div class="project-card">', unsafe_allow_html=True)
            
            col1, col2 = st.columns([3, 1])
            
            with col1:
                st.markdown(f"### {project['title']}")
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
