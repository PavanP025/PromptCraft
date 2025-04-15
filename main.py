
from flask import Flask, render_template, request, jsonify
import openai
import os

app = Flask(__name__)

# Initialize OpenAI (will need API key in environment variables)
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
        client = openai.OpenAI(api_key=os.getenv('OPENAI_API_KEY'))
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful prompt engineering assistant."},
                {"role": "user", "content": PROMPT_TEMPLATE.format(scenario=scenario)}
            ]
        )
        
        return jsonify({
            'success': True,
            'result': response.choices[0].message.content
        })
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
