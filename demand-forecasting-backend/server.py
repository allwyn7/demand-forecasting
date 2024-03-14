from flask import Flask, request, jsonify
from transformers import GPT2LMHeadModel, GPT2Tokenizer
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Load pre-trained model and tokenizer
tokenizer = GPT2Tokenizer.from_pretrained("gpt2")
model = GPT2LMHeadModel.from_pretrained("gpt2")

@app.route('/interpret', methods=['POST'])
def interpret():
    try:
        data = request.json
        prompt = data['prompt']
        generated_text = generate_text(prompt)
        return jsonify({'interpretation': generated_text})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

def generate_text(prompt, max_length=50):
    # Tokenize prompt
    input_ids = tokenizer.encode(prompt, return_tensors="pt")
    
    # Generate text based on prompt
    output = model.generate(input_ids, max_length=max_length, num_return_sequences=1)
    
    # Decode generated text
    generated_text = tokenizer.decode(output[0], skip_special_tokens=True)
    
    return generated_text

if __name__ == '__main__':
    app.run(debug=True, port=5000)
