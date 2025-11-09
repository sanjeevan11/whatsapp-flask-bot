# WhatsApp Immigration Bot

> A comprehensive WhatsApp bot for UK immigration services with AI-powered consultation scheduling, document management, and automated case intake.

## Features

- 🤖 **AI-Powered Responses**: Uses OpenRouter API for intelligent query handling
- 📋 **Service Categories**: Family Immigration, Work Immigration, Study, Visit, Settlement, Citizenship, Asylum, and Specialist Visas
- 📄 **Document Management**: Automated upload to Google Drive with case organization
- 📅 **Consultation Scheduling**: Integrated with Calendly and Google Calendar
- 📊 **Case Management**: Google Sheets integration for tracking all intakes
- ✅ **Smart Checklists**: Dynamic document requirements based on user responses
- 🔐 **Secure**: Environment-based configuration for all sensitive credentials

## Architecture

- **Backend**: Python Flask
- **Messaging**: WhatsApp Business API
- **AI**: OpenRouter (Qwen 3-30B)
- **Storage**: Google Drive API via Apps Script
- **Database**: Google Sheets
- **Hosting**: Cyclic.sh (serverless)

## Prerequisites

1. **Facebook Developer Account** with WhatsApp Business API access
2. **Google Cloud Project** with Drive and Sheets API enabled
3. **Google Apps Script** deployed as web app
4. **OpenRouter API Key**
5. **Cyclic.sh Account** (free tier)

## Environment Variables

Create a `.env` file with the following variables (see `.env.example`):

```bash
# WhatsApp Configuration
WA_ACCESS_TOKEN=your_whatsapp_access_token
WA_PHONE_ID=your_phone_number_id
WA_VERIFY_TOKEN=your_custom_verify_token

# Apps Script
APPSCRIPT_URL=your_deployed_apps_script_url

# OpenRouter AI
OPENROUTER_KEY=your_openrouter_api_key
OPENROUTER_MODEL=qwen/qwen3-30b-a3b:free

# Google Services
DRIVE_FOLDER_ID=your_drive_folder_id
SHEET_ID=your_google_sheet_id
SHEET_TAB=Cases

# Admin
ADMIN_EMAIL=your_email@example.com

# Optional
CALENDLY_URL=your_calendly_link
PORT=8080
```

## Installation & Local Development

```bash
# Clone the repository
git clone https://github.com/sanjeevan11/whatsapp-flask-bot.git
cd whatsapp-flask-bot

# Install dependencies
pip install -r requirements.txt

# Create .env file with your credentials
cp .env.example .env
# Edit .env with your actual values

# Run locally
python main.py
```

## Deployment to Cyclic.sh

### Step 1: Connect Repository

1. Go to [Cyclic.sh](https://cyclic.sh)
2. Sign in with GitHub
3. Click "Deploy" and select this repository
4. Choose **Python** runtime

### Step 2: Configure Environment Variables

In Cyclic dashboard, add all environment variables from `.env.example`:

- Go to **Variables** tab
- Add each variable one by one
- Save and redeploy

### Step 3: Deploy

- Cyclic auto-deploys on push to `main` branch
- Your webhook URL will be: `https://your-app.cyclic.app/webhook`

### Step 4: Configure WhatsApp Webhook

1. Go to Facebook Developer Console
2. Navigate to WhatsApp > Configuration
3. Add webhook URL: `https://your-app.cyclic.app/webhook`
4. Add Verify Token (same as `WA_VERIFY_TOKEN` in .env)
5. Subscribe to messages webhook

## Usage

Users interact with the bot via WhatsApp by:

1. Sending initial message (e.g., "hi" or "menu")
2. Selecting visa category
3. Answering eligibility questions
4. Uploading documents
5. Booking consultation
6. Receiving case confirmation

## Project Structure

```
├── main.py              # Main Flask application
├── requirements.txt     # Python dependencies
├── runtime.txt          # Python version
├── .env.example         # Environment variables template
├── .gitignore          # Git ignore rules
└── README.md           # This file
```

## API Endpoints

### `GET /webhook`
Webhook verification endpoint for WhatsApp.

### `POST /webhook`
Receives incoming WhatsApp messages and processes them.

### `GET /`
Health check endpoint.

## Keep-Alive (Optional)

If your app sleeps due to inactivity, use **UptimeRobot** (free):

1. Sign up at [UptimeRobot.com](https://uptimerobot.com)
2. Add new monitor (HTTP)
3. URL: `https://your-app.cyclic.app/`
4. Interval: 5 minutes

This keeps your app awake 24/7.

## Troubleshooting

### Webhook Verification Failed
- Ensure `WA_VERIFY_TOKEN` matches in both Cyclic and Facebook Console
- Check webhook URL format

### Messages Not Received
- Verify WhatsApp webhook subscriptions
- Check Cyclic logs for errors
- Ensure `WA_ACCESS_TOKEN` is valid

### File Upload Errors
- Confirm `DRIVE_FOLDER_ID` is correct
- Check Apps Script permissions
- Verify Apps Script is deployed as "Anyone"

## Updates & Redeployment

To update the bot:

```bash
# Make changes locally
git add .
git commit -m "Your update message"
git push origin main
```

Cyclic automatically redeploys on push.

## License

MIT License - feel free to use for your projects.

## Support

For issues, open a GitHub issue or contact the admin.

---

**Built with ❤️ for streamlining UK immigration services**
