"""                                                                                                                                 
  eBay Marketplace Account Deletion Notification endpoint.        
  Required for eBay production API access (GDPR/CCPA compliance).                                                                     
  This app stores no user data, so deletion requests are no-ops.                                                                      
  """                                                                                                                                 
                                                                                                                                      
  import hashlib                                                  
  import os
  from flask import Flask, request, jsonify

  app = Flask(__name__)

  VERIFICATION_TOKEN = "f7k2mX9pQr4nBv8wLc3tYj6sHe5dAu1z"
  ENDPOINT_URL       = "https://ebay-deletion-endpoint-2-0o10.onrender.com/ebay/deletion"


  @app.route("/ebay/deletion", methods=["GET"])
  def ebay_challenge():
      challenge_code = request.args.get("challenge_code", "")
      if not challenge_code:
          return jsonify({"error": "missing challenge_code"}), 400

      hash_input = challenge_code + VERIFICATION_TOKEN + ENDPOINT_URL
      digest     = hashlib.sha256(hash_input.encode("utf-8")).hexdigest()

      print(f"[challenge] code={challenge_code}")
      print(f"[challenge] token={VERIFICATION_TOKEN}")
      print(f"[challenge] endpoint={ENDPOINT_URL}")
      print(f"[challenge] response={digest}")

      return jsonify({"challengeResponse": digest}), 200


  @app.route("/ebay/deletion", methods=["POST"])
  def ebay_deletion():
      return "", 200


  @app.route("/health")
  def health():
      return "OK", 200


  if __name__ == "__main__":
      app.run(host="0.0.0.0", port=int(os.getenv("PORT", 8080)))
