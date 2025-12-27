from flask import Flask, render_template, request, jsonify
from transformers import pipeline, set_seed
import traceback

app = Flask(__name__)

# Global model cache
models = {}

def get_model(task_type, model_name=None):
    """Get or create a model pipeline for the specified task."""
    key = f"{task_type}:{model_name if model_name else 'default'}"
    
    if key not in models:
        print(f"Loading model for {key}...")
        if task_type == "text-generation":
            model_name = model_name or "gpt2"
            models[key] = pipeline(task_type, model=model_name)
        elif task_type == "sentiment-analysis":
            models[key] = pipeline(task_type)
        else:
            raise ValueError(f"Unsupported task type: {task_type}")
        print(f"Model {key} loaded successfully")
    
    return models[key]

@app.route('/')
def index():
    """Serve the main chat interface."""
    return render_template('index.html')

@app.route('/api/inference', methods=['POST'])
def inference():
    """Handle inference requests from the chat interface."""
    try:
        data = request.json
        prompt = data.get('prompt', '')
        task_type = data.get('task_type', 'text-generation')
        seed = data.get('seed')
        max_tokens = data.get('max_tokens', 50)
        
        if not prompt:
            return jsonify({'error': 'No prompt provided'}), 400
        
        # Set seed if provided
        if seed is not None:
            set_seed(int(seed))
        
        # Get the appropriate model
        model = get_model(task_type)
        
        # Run inference based on task type
        if task_type == "text-generation":
            result = model(prompt, max_new_tokens=max_tokens, num_return_sequences=1)
            response_text = result[0]['generated_text']
            
        elif task_type == "sentiment-analysis":
            result = model(prompt)
            label = result[0]['label']
            score = result[0]['score']
            response_text = f"Sentiment: {label} (Confidence: {score:.4f})"
        
        else:
            return jsonify({'error': f'Unsupported task type: {task_type}'}), 400
        
        return jsonify({
            'response': response_text,
            'task_type': task_type,
            'seed': seed
        })
    
    except Exception as e:
        print(f"Error during inference: {str(e)}")
        traceback.print_exc()
        return jsonify({'error': str(e)}), 500

@app.route('/api/tasks', methods=['GET'])
def get_tasks():
    """Return available task types."""
    return jsonify({
        'tasks': [
            {'id': 'text-generation', 'name': 'Text Generation (GPT-2)'},
            {'id': 'sentiment-analysis', 'name': 'Sentiment Analysis'}
        ]
    })

if __name__ == '__main__':
    print("Starting inference web server...")
    print("Navigate to http://localhost:5000 in your browser")
    app.run(debug=True, host='0.0.0.0', port=5000)
