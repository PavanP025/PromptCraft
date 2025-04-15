
from flask import Flask, render_template, request, jsonify
import openai
import os

app = Flask(__name__)

# Initialize OpenAI (will need API key in environment variables)
PROMPT_TEMPLATE = """You are an expert prompt engineer. Your task is to generate a highly specific and structured prompt for the given scenario.

Scenario: {scenario}

Transform this scenario into a well-crafted prompt that:
1. Clearly states the specific task or challenge
2. Defines the expected format and structure
3. Includes relevant constraints or requirements
4. Specifies the depth or scope of the response

Example format:
"Generate [specific number] of [type of content] that [specific action/goal] using [technique/approach]. Each [output unit] must [specific requirement] related to [topic/theme]."

Return only the transformed prompt, formatted as a single paragraph without any additional explanation."""

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
