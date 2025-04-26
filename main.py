
from flask import Flask, render_template, request, jsonify, session, redirect, url_for
import openai
import os
from functools import wraps

app = Flask(__name__)
app.secret_key = os.environ.get('FLASK_SECRET_KEY', 'your-secret-key-here')

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'logged_in' not in session:
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated_function

# Initialize OpenAI (will need API key in environment variables)
PROMPT_TEMPLATE = """Create a prompt template for chatting with AI models based on this scenario: {scenario}

Consider what information and structure would make the AI response most effective. Provide a template that users can copy, fill in the [bracketed sections], and paste into their AI chat conversations.

Remember to:
- Keep the template clear and focused
- Include placeholders for key details
- Structure it for optimal AI response

Return only the template itself, no explanations."""

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        if request.form['password'] == os.environ.get('APP_PASSWORD', 'admin'):
            session['logged_in'] = True
            return redirect(url_for('home'))
        return 'Invalid password'
    return render_template('login.html')

@app.route('/')
@login_required
def home():
    return render_template('index.html')

@app.route('/sectors')
@login_required
def sectors():
    return render_template('sectors.html')

@app.route('/ai-tools')
@login_required
def ai_tools():
    return render_template('ai_tools.html')

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
