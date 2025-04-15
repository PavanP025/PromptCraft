
from flask import Flask, render_template, request, jsonify
import openai
import os

app = Flask(__name__)

# Initialize OpenAI (will need API key in environment variables)
PROMPT_TEMPLATE = """
Create a clear and effective prompt template for the following scenario, focusing on the most suitable prompt engineering techniques:

Scenario: {scenario}

Return only the prompt template, formatted clearly and ready to use. The prompt should employ relevant techniques like chain-of-thought, role-playing, or step-by-step guidance as appropriate for the scenario.
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
