from flask import Flask, request, jsonify, send_from_directory, abort
from flask_mail import Mail, Message
import os
import re
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

PUBLIC_PAGES = {'index.html', 'about.html', 'contact.html', 'services.html', 'projects.html'}


@app.route('/')
def index():
    return send_from_directory('.', 'index.html')


@app.route('/assets/<path:filename>')
def assets(filename):
    return send_from_directory('assets', filename)


@app.route('/projects/<page>')
def project_page(page):
    # Only generated project pages: lowercase slug + .html, and the file must exist
    if not re.fullmatch(r'[a-z0-9-]+\.html', page) or not os.path.isfile(os.path.join('projects', page)):
        abort(404)
    return send_from_directory('projects', page)


@app.route('/<page>')
def page(page):
    # Serve only the public pages; never the app source or .env
    if page not in PUBLIC_PAGES:
        abort(404)
    return send_from_directory('.', page)


@app.route('/submit-contact', methods=['POST'])
def submit_contact():
    try:
        # Get form data
        data = request.get_json() if request.is_json else request.form.to_dict()
        
        name = data.get('name', '').strip()
        organisation = data.get('organisation', '').strip()
        email = data.get('email', '').strip()
        phone = data.get('phone', '').strip()
        interest = data.get('interest', '').strip() or 'Not specified'
        message_content = data.get('message', '').strip()

        # Validate required fields
        if not all([name, email, message_content]):
            return jsonify({'error': 'Missing required fields'}), 400

        subject = f"Website enquiry: {interest} ({name})"

        email_body = f"""
New enquiry from the Liwa Labs website:

Name: {name}
Organisation: {organisation or 'Not provided'}
Email: {email}
Phone: {phone if phone else 'Not provided'}
Interested in: {interest}

Message:
{message_content}
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
            'error': 'Failed to send message. Please try again or contact us directly.'
        }), 500

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=os.environ.get('FLASK_DEBUG') == '1')