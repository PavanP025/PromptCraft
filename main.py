
from flask import Flask, render_template, request, jsonify
import openai
import os

app = Flask(__name__)

# Initialize OpenAI (will need API key in environment variables)
PROMPT_TEMPLATE = """You are an expert prompt engineer. Create a clear, focused prompt for the following scenario that will get the best possible response from an AI system.

Scenario: {scenario}

Format your response as a single, well-structured prompt that:
1. Uses clear, precise language
2. Includes necessary context
3. Specifies the desired output format
4. Avoids ambiguity

Return only the prompt template, with no additional explanation or commentary."""

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
