from flask import Flask, request, jsonify, send_from_directory
from flask_mail import Mail, Message
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

app = Flask(__name__)

# Email configuration
app.config['MAIL_SERVER'] = os.getenv('SMTP_HOST', 'smtp.gmail.com')
app.config['MAIL_PORT'] = int(os.getenv('SMTP_PORT', '587'))
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False
app.config['MAIL_USERNAME'] = os.getenv('SMTP_USER')
app.config['MAIL_PASSWORD'] = os.getenv('SMTP_PASS')
app.config['MAIL_DEFAULT_SENDER'] = os.getenv('SMTP_USER')

# Initialize Mail
mail = Mail(app)

@app.route('/')
def index():
    return send_from_directory('.', 'index.html')

@app.route('/<path:filename>')
def serve_static(filename):
    return send_from_directory('.', filename)

@app.route('/submit-contact', methods=['POST'])
def submit_contact():
    try:
        # Get form data
        data = request.get_json() if request.is_json else request.form.to_dict()
        
        first_name = data.get('first-name', '')
        last_name = data.get('last-name', '')
        email = data.get('email', '')
        phone = data.get('phone', '')
        company = data.get('company', '')
        subject_type = data.get('subject', '')
        message_content = data.get('message', '')
        
        # Validate required fields
        if not all([first_name, last_name, email, subject_type, message_content]):
            return jsonify({'error': 'Missing required fields'}), 400
        
        # Create email message
        subject = f"New Contact Form Submission - {subject_type}"
        
        # Format the email body
        email_body = f"""
New contact form submission from Liwa Labs website:

Name: {first_name} {last_name}
Email: {email}
Phone: {phone if phone else 'Not provided'}
Company: {company if company else 'Not provided'}
Service Interest: {subject_type}

Message:
{message_content}

---
This message was sent from the Liwa Labs contact form.
        """
        
        # Create and send email
        msg = Message(
            subject=subject,
            recipients=[os.getenv('RECIPIENT_EMAIL')],
            body=email_body,
            reply_to=email
        )
        
        mail.send(msg)
        
        return jsonify({
            'success': True, 
            'message': 'Thank you for your message! We will get back to you within 24 hours.'
        })
        
    except Exception as e:
        print(f"Error sending email: {str(e)}")
        return jsonify({
            'error': 'Failed to send message. Please try again or contact us directly.',
            'details': str(e)
        }), 500

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)