import os
import re
import uuid
import base64
import requests
import json
from datetime import datetime
from flask import Flask, request, jsonify

# ========== Configuration updated with your provided values ==========
ACCESS_TOKEN = os.getenv("WA_ACCESS_TOKEN", "EAACHWo8LZCYRwBO2jLLIiT9iVBPxM4hTxPqgYnRVQ3DZCQRVLXIZAVetYOa5dP7A8hqzID9bPvRbmBEzQzwm5ZBr0rhKdgiBdSqKXx2PTrWv5HGDR7NEGioqvSwfZC44C98649VhlAr6OvYSA2U0CEZC0qNgTp7jcPXrhMmrM4VAZBd8WaOhLsRY5QvnKFga0u8k098HKtmghln4lmpL49EtqFITkZCfK5AgHbeN5gn5tM1Mb9YtrMjoMV0S2gsuDJrBXxLxKQRvm30ctw0iNXWre4zBmPcYOHRvhARzLGAZDZD")  # Replace with your token
PHONE_NUMBER_ID = os.getenv("WA_PHONE_ID", "579796315228068")  # Replace with your phone ID
API_VER = "v18.0"  # Stable version
WA_URL = f"https://graph.facebook.com/{API_VER}/{PHONE_NUMBER_ID}/messages"
VERIFY_TOKEN = os.getenv("WA_VERIFY_TOKEN", "MYUNIQUEVERIFYTOKEN123")

APPSCRIPT_URL = os.getenv("APPSCRIPT_URL", "https://script.google.com/macros/s/AKfycbwKNLH84NpC9rzJAcJSlfy2j3pOtfSMpQz0zj8dAY7tQqMsWxIesYXuS6aUKbNVu6e/exec")
OPENROUTER_KEY = os.getenv("OPENROUTER_KEY", "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")
OPENROUTER_MODEL = "qwen/qwen3-30b-a3b:free"
OPENROUTER_API = "https://openrouter.ai/api/v1/chat/completions"

ADMIN_EMAIL = os.getenv("ADMIN_EMAIL", "solutions@nexabloom.io")
DRIVE_FOLDER_ID = os.getenv("DRIVE_FOLDER_ID", "1qobSLoixuJILlkSP-nIo4qOHzVOLMpWv")
CALENDLY_URL = os.getenv("CALENDLY_URL", "")  # optional
CAL_DEFAULT_TZ = os.getenv("CAL_TZ", "Europe/London")
MAX_MEDIA_BYTES = int(os.getenv("MAX_MEDIA_BYTES", str(12*1024*1024)))  # 12MB
GRAPH_BASE = f"https://graph.facebook.com/{API_VER}"

SHEET_ID = os.getenv("SHEET_ID", "105mrH6iAIPzUJ035iHymxIjS7FaEnPcPeb3hIdgBr-s")
SHEET_TAB = os.getenv("SHEET_TAB", "Cases")  # change if your tab name differs

# WhatsApp interactive limits to prevent silent UI drops
WA_LIM = {
    "list": {"title": 24, "desc": 72, "button": 20, "header": 60, "body": 1024, "rows": 10}
}

app = Flask(__name__)

@app.route("/", methods=["GET"])
def health():
    return "OK", 200

# ========== Webhook ==========
@app.route("/webhook", methods=["GET", "POST"])
def webhook():
    if request.method == "GET":
        if request.args.get("hub.verify_token") == VERIFY_TOKEN:
            return request.args.get("hub.challenge"), 200
        return "Forbidden", 403
    
    data = request.get_json(force=True)
    print(f"Incoming webhook: {data}")
    
    for entry in data.get("entry", []):
        for change in entry.get("changes", []):
            value = change.get("value", {})
            for msg in value.get("messages", []):
                uid = msg.get("from")
                # handle logic here
    
    return jsonify({"status": "ok"}), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.getenv("PORT", 5000)))
