import hashlib                                                                                                                      
  from flask import Flask, request, jsonify
                                                                                                                                      
  app = Flask(__name__)                                           

  VERIFICATION_TOKEN = "f7k2mX9pQr4nBv8wLc3tYj6sHe5dAu1z"
  ENDPOINT_URL = "https://ebay-deletion-endpoint-2-0o10.onrender.com/ebay/deletion"

  @app.route("/ebay/deletion", methods=["GET"])
  def ebay_challenge():
      challenge_code = request.args.get("challenge_code", "")
      if not challenge_code:
          return {"error": "missing challenge_code"}, 400
      hash_input = challenge_code + VERIFICATION_TOKEN + ENDPOINT_URL
      digest = hashlib.sha256(hash_input.encode("utf-8")).hexdigest()
      return {"challengeResponse": digest}, 200

  @app.route("/ebay/deletion", methods=["POST"])
  def ebay_deletion():
      return "", 200

  @app.route("/health")
  def health():
      return "OK", 200
