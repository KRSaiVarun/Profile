import os
import json
import smtplib
from datetime import datetime
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import streamlit as st

def save_contact_message(sender_name, sender_email, subject, message):
    """Save contact message to JSON file as fallback"""
    try:
        contact_file = "data/contact_messages.json"
        
        # Create data directory if it doesn't exist
        os.makedirs("data", exist_ok=True)
        
        # Load existing messages
        messages = []
        if os.path.exists(contact_file):
            with open(contact_file, 'r') as f:
                messages = json.load(f)
        
        # Add new message
        new_message = {
            "name": sender_name,
            "email": sender_email,
            "subject": subject,
            "message": message,
            "timestamp": datetime.now().isoformat()
        }
        messages.append(new_message)
        
        # Save updated messages
        with open(contact_file, 'w') as f:
            json.dump(messages, f, indent=2)
        
        return True
    except Exception as e:
        st.error(f"Failed to save message: {str(e)}")
        return False

def send_email(sender_name, sender_email, subject, message):
    """
    Send email using SMTP configuration
    Falls back to saving message locally if email not configured
    Returns True if successful, False otherwise
    """
    try:
        # Email configuration
        SMTP_SERVER = "smtp.gmail.com"
        SMTP_PORT = 587
        
        # Get email credentials from environment variables or Streamlit secrets
        try:
            EMAIL_ADDRESS = st.secrets.get("EMAIL_ADDRESS", "")
            EMAIL_PASSWORD = st.secrets.get("EMAIL_PASSWORD", "")
            TO_EMAIL = st.secrets.get("TO_EMAIL", "krsaivarun@gmail.com")
        except:
            # Fallback to environment variables
            EMAIL_ADDRESS = os.getenv("EMAIL_ADDRESS", "")
            EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD", "")
            TO_EMAIL = os.getenv("TO_EMAIL", "krsaivarun@gmail.com")
        
        if not EMAIL_ADDRESS or not EMAIL_PASSWORD:
            # Save message locally as fallback
            saved = save_contact_message(sender_name, sender_email, subject, message)
            if saved:
                st.info("Message saved! Email configuration not set up yet. Your message has been saved and can be reviewed at krsaivarun@gmail.com")
                return True
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
        # Save message as fallback even on email error
        saved = save_contact_message(sender_name, sender_email, subject, message)
        if saved:
            st.warning(f"Email could not be sent, but your message was saved. Please contact directly at krsaivarun@gmail.com")
            return True
        st.error(f"Failed to send or save message. Please email directly at krsaivarun@gmail.com")
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
        "timestamp": datetime.now().isoformat()
    }

def get_contact_messages():
    """Retrieve all saved contact messages"""
    try:
        contact_file = "data/contact_messages.json"
        if os.path.exists(contact_file):
            with open(contact_file, 'r') as f:
                return json.load(f)
        return []
    except Exception as e:
        st.error(f"Failed to load messages: {str(e)}")
        return []
