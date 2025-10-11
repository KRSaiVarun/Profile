import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import streamlit as st

def send_email(sender_name, sender_email, subject, message):
    """
    Send email using SMTP configuration
    Returns True if successful, False otherwise
    """
    try:
        # Email configuration
        SMTP_SERVER = "smtp.gmail.com"
        SMTP_PORT = 587
        
        # Get email credentials from environment variables or Streamlit secrets
        try:
            EMAIL_ADDRESS = st.secrets["EMAIL_ADDRESS"]
            EMAIL_PASSWORD = st.secrets["EMAIL_PASSWORD"]
            TO_EMAIL = st.secrets["TO_EMAIL"]
        except:
            # Fallback to environment variables
            EMAIL_ADDRESS = os.getenv("EMAIL_ADDRESS", "")
            EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD", "")
            TO_EMAIL = os.getenv("TO_EMAIL", "krsaivarun@gmail.com")
        
        if not EMAIL_ADDRESS or not EMAIL_PASSWORD:
            st.warning("Email configuration not found. Please contact directly at krsaivarun@gmail.com")
            return False
        
        # Create message
        msg = MIMEMultipart()
        msg['From'] = EMAIL_ADDRESS
        msg['To'] = TO_EMAIL
        msg['Subject'] = f"Portfolio Contact: {subject}" if subject else f"Portfolio Contact from {sender_name}"
        
        # Email body
        body = f"""
        New contact form submission from portfolio website:
        
        Name: {sender_name}
        Email: {sender_email}
        Subject: {subject}
        
        Message:
        {message}
        
        ---
        This message was sent from the portfolio contact form.
        Reply directly to this email to respond to {sender_name}.
        """
        
        msg.attach(MIMEText(body, 'plain'))
        
        # Send email
        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.starttls()
        server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        text = msg.as_string()
        server.sendmail(EMAIL_ADDRESS, TO_EMAIL, text)
        server.quit()
        
        return True
        
    except Exception as e:
        st.error(f"Email error: {str(e)}")
        return False

def validate_email(email):
    """Simple email validation"""
    import re
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None

def format_contact_message(name, email, subject, message):
    """Format contact message for display or storage"""
    return {
        "name": name,
        "email": email,
        "subject": subject,
        "message": message,
        "timestamp": str(pd.Timestamp.now())
    }
