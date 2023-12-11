import re
from flask import Flask, request, jsonify
import g4f

app = Flask(__name__)

def read_documents_from_file(file_path):
    with open(file_path, 'r') as file:
        documents = file.read()
    return documents

def create_prompt(user_input, documents):
    prompt = f"""
        Here is some general idea about my company documents:

        {documents}
        
        I want you to pretend to be a helpful chatbot and guide my employees on the questions they have with my documents.
        The question they have is as follows: {user_input}

        Reply to this in a JSON format resembling this:
        {{"redirect": , "response": {{"recommended_document": "", "steps": ["", "", "", "", ""], "additional_advice": ""}}}} 
        
        If the question asks for a redirect to a URL, set the "redirect" to true, else set it to false
        
        """
    return prompt

def get_g4f_response(user_input):
    model = g4f.models.gpt_35_turbo
    provider = g4f.Provider.Bing

    user_message = {"role": "user", "content": user_input}

    response = g4f.ChatCompletion.create(
        model=model,
        provider=provider,
        messages=[user_message],
    )

    if isinstance(response, list):
        return response[-1].get("content", "")
    elif isinstance(response, str):
        return response
    else:
        return response.get("choices", [])[0].get("message", {}).get("content", "")


def extract_information(g4f_response):
    pattern = r'"redirect": (true|false), "response": {"recommended_document": "(.*?)", "steps": \[(.*?)\], "additional_advice": "(.*?)"'
    match = re.search(pattern, g4f_response)

    if match:
        redirect_value = match.group(1).lower() == 'true'
        recommended_document = match.group(2)
        steps = [step.strip('"') for step in match.group(3).split(',')]
        additional_advice = match.group(4)

        return {"redirect": redirect_value, "response": {"recommended_document": recommended_document, "steps": steps, "additional_advice": additional_advice}}
    else:
        return None

@app.route('/response', methods=['POST', 'OPTIONS'])
def response():
    documents_file_path = 'documents.txt'
    documents_content = read_documents_from_file(documents_file_path)

    # Handling the preflight request 
    if request.method == 'OPTIONS':
        response = app.make_default_options_response()
    elif request.method == 'POST':
        try:
            data = request.get_json(force=True)
            user_input = data.get('user_input', '') 

            prompt = create_prompt(user_input, documents_content)
            g4f_response = get_g4f_response(prompt)

            extracted_json = extract_information(g4f_response)

            if extracted_json:
                response = jsonify(extracted_json)
            else:
                response = jsonify({"error": "Failed to extract information from the response"})
        except Exception as e:
            response = jsonify({"error": str(e)})
        
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type')
    response.headers.add('Access-Control-Allow-Methods', 'POST, OPTIONS')
    return response


if __name__ == '__main__':
    app.run(debug=True)