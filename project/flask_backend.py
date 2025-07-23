from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

steps = [
    "Kya aap Nursing College mein admission lena chahte ho?",
    "Apne 12th class mein Biology opt kiya tha?",
    "Aap eligible hain. Yeh ek 4-year ka program hai.",
    "Fee structure:\n- Tuition: ₹60,000\n- Bus: ₹10,000\n- Total: ₹70,000",
    "Hostel & Training:\n- Separate hostels\n- Real hospital training",
    "Location: Delhi, easily reachable by metro/public transport",
    "Approved by INC, Delhi. Nationally valid degree.",
    "Training Centres:\n- District & Regional Hospitals\n- Ranchi Neurosurgery",
    "Scholarships:\n- Post-Matric ₹18k–₹23k\n- Labour ₹40k–₹48k",
    "Only 60 seats. Apply early to be safe.",
    "Eligibility:\n- Biology in 12th\n- PNT entrance\n- Age 17–35",
    "Great! Registration link will be shared soon."
]

@app.route('/chat', methods=['POST'])
def chat():
    data = request.json
    user_input = data.get("user_input", "").lower()
    step = data.get("step", 0)

    if user_input in ["no", "nahi", "na"]:
        return jsonify({
            "bot_response": "Koi baat nahi. Agar future mein admission lena ho toh zarur batana.",
            "step": 0
        })

    if step < len(steps):
        response = steps[step]
        step += 1
    else:
        response = "Thank you for chatting! Best of luck."
        step = 0

    return jsonify({"bot_response": response, "step": step})

if __name__ == '__main__':
    app.run(debug=True, port=5001)