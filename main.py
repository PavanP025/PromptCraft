
from flask import Flask, render_template, request, jsonify
import google.generativeai as genai
import os

app = Flask(__name__)

# Initialize Gemini (will need API key in environment variables)
PROMPT_TEMPLATE = """
Given this scenario, create a well-structured prompt following these principles:
1. Be specific and clear
2. Include context and constraints
3. Break down complex requests
4. Specify desired output format

Scenario: {scenario}

Provide the improved prompt and a brief explanation of the improvements made.
"""

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/generate_prompt', methods=['POST'])
def generate_prompt():
    scenario = request.json.get('scenario', '')
    
    try:
        genai.configure(api_key=os.getenv('GEMINI_API_KEY'))
        model = genai.GenerativeModel('gemini-pro')
        response = model.generate_content(PROMPT_TEMPLATE.format(scenario=scenario))
        
        return jsonify({
            'success': True,
            'result': response.text
        })
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
