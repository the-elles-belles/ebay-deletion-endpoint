"""
eBay Marketplace Account Deletion Notification endpoint.
Required for eBay production API access (GDPR/CCPA compliance).
This app stores no user data, so deletion requests are no-ops.
"""

import hashlib
import hmac
import base64
import os
from flask import Flask, request, jsonify

app = Flask(__name__)

VERIFICATION_TOKEN = os.getenv("EBAY_VERIFICATION_TOKEN", "grading-arbitrage-ebay-verify")
ENDPOINT_URL       = os.getenv("ENDPOINT_URL", "")


@app.route("/ebay/deletion", methods=["GET"])
def ebay_challenge():
    """
    eBay sends a GET with challenge_code to verify the endpoint.
    Must respond with SHA-256 hash of (challenge_code + verificationToken + endpoint_url).
    """
    challenge_code = request.args.get("challenge_code", "")
    if not challenge_code:
        return jsonify({"error": "missing challenge_code"}), 400

    # Hash: SHA-256(challengeCode + verificationToken + endpointUrl)
    hash_input  = challenge_code + VERIFICATION_TOKEN + ENDPOINT_URL
    digest      = hashlib.sha256(hash_input.encode("utf-8")).hexdigest()

    return jsonify({"challengeResponse": digest}), 200


@app.route("/ebay/deletion", methods=["POST"])
def ebay_deletion():
    """
    eBay POSTs deletion requests here. We store no user data so nothing to delete.
    Must return 200 to acknowledge receipt.
    """
    return "", 200


@app.route("/health")
def health():
    return "OK", 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.getenv("PORT", 8080)))
