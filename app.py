from flask import Flask, render_template, request, jsonify
import traceback
import random

app = Flask(__name__)

# Global model cache
models = {}
USE_MOCK = False  # Set to True if models can't be loaded

def get_model(task_type, model_name=None):
    """Get or create a model pipeline for the specified task."""
    global USE_MOCK
    
    if USE_MOCK:
        return None  # Return None for mock mode
    
    key = f"{task_type}:{model_name if model_name else 'default'}"
    
    if key not in models:
        try:
            from transformers import pipeline, set_seed
            print(f"Loading model for {key}...")
            if task_type == "text-generation":
                model_name = model_name or "gpt2"
                models[key] = pipeline(task_type, model=model_name)
            elif task_type == "sentiment-analysis":
                models[key] = pipeline(task_type)
            else:
                raise ValueError(f"Unsupported task type: {task_type}")
            print(f"Model {key} loaded successfully")
        except Exception as e:
            print(f"Failed to load model: {str(e)}")
            print("Switching to MOCK mode for demonstration")
            USE_MOCK = True
            return None
    
    return models.get(key)

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
        
        # Get the appropriate model
        model = get_model(task_type)
        
        # Use mock responses if model is not available
        if USE_MOCK or model is None:
            print(f"Using MOCK mode for {task_type}")
            
            # Generate mock responses
            if task_type == "text-generation":
                # Simulate text generation with some variety based on seed
                if seed:
                    random.seed(int(seed))
                
                continuations = [
                    " transforming every aspect of our lives, from healthcare to transportation.",
                    " increasingly integrated into our daily workflows and decision-making processes.",
                    " becoming more accessible and democratized across industries.",
                    " advancing at an exponential rate, with breakthrough discoveries happening regularly.",
                    " reshaping how we interact with technology and each other."
                ]
                continuation = random.choice(continuations)
                response_text = prompt + continuation
                
            elif task_type == "sentiment-analysis":
                # Simple mock sentiment analysis
                positive_keywords = ['love', 'great', 'excellent', 'amazing', 'wonderful', 'fantastic', 'good', 'best']
                negative_keywords = ['hate', 'terrible', 'awful', 'bad', 'worst', 'horrible', 'poor', 'nightmare']
                
                prompt_lower = prompt.lower()
                pos_count = sum(1 for word in positive_keywords if word in prompt_lower)
                neg_count = sum(1 for word in negative_keywords if word in prompt_lower)
                
                if pos_count > neg_count:
                    label = "POSITIVE"
                    score = 0.85 + random.random() * 0.1
                elif neg_count > pos_count:
                    label = "NEGATIVE"
                    score = 0.85 + random.random() * 0.1
                else:
                    label = "NEUTRAL"
                    score = 0.55 + random.random() * 0.1
                
                response_text = f"Sentiment: {label} (Confidence: {score:.4f})"
            
            else:
                return jsonify({'error': f'Unsupported task type: {task_type}'}), 400
        
        else:
            # Use real models
            from transformers import set_seed
            
            # Set seed if provided
            if seed is not None:
                set_seed(int(seed))
            
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
            'seed': seed,
            'mock_mode': USE_MOCK or model is None
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
