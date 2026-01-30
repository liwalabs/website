# Gmail Email Setup Instructions

To make your contact form functional, you need to provide Gmail SMTP credentials. Here's how to set it up:

## Step 1: Enable 2-Factor Authentication
1. Go to your Google Account settings
2. Security → 2-Step Verification
3. Turn on 2-Step Verification if not already enabled

## Step 2: Create App Password
1. Go to Google Account settings → Security
2. Under "2-Step Verification", find "App passwords"
3. Click "App passwords"
4. Select "Mail" and "Other (custom name)"
5. Enter "Liwa Labs Website" as the custom name
6. Click "Generate"
7. Google will show you a 16-character password - copy this!

## Step 3: Provide These Settings
When prompted, provide these values:

- **SMTP_HOST**: smtp.gmail.com
- **SMTP_PORT**: 587
- **SMTP_USER**: your-gmail@gmail.com (your Gmail address)
- **SMTP_PASS**: the 16-character app password from step 2
- **RECIPIENT_EMAIL**: where you want to receive contact form emails (can be same as SMTP_USER)

## Example:
- SMTP_HOST: smtp.gmail.com
- SMTP_PORT: 587
- SMTP_USER: info@gmail.com
- SMTP_PASS: abcd efgh ijkl mnop (16 characters with spaces)
- RECIPIENT_EMAIL: info@gmail.com

Once you provide these, your contact form will automatically send emails to your inbox!