import re
from flask import Flask, request, jsonify
import g4f

app = Flask(__name__)

def create_prompt(user_input):
    prompt = f"""Here is some general idea about my company documents:
        ## Title: "Recent Developments in [Specific Topic]"
        Content: This document provides an overview of the most recent advancements and findings in the field of [specific topic]. It includes up-to-date information and references for further exploration.

        ## Title: "Company Safety Protocols Manual"
        Content: This comprehensive document outlines the safety protocols and guidelines that employees should adhere to while working within the company premises. It covers emergency procedures, safety equipment usage, and risk mitigation strategies.

        ## Title: "Contributions of [Employee Name]: A Compilation"
        Content: This document compiles various works authored by [employee name], showcasing their contributions to different projects, research papers, and reports within the company.

        ## Title: "Top Five Most-Accessed Documents in the Past Year"
        Content: This document contains a list of the top five most frequently accessed documents within the company's knowledge repository over the past year, along with brief summaries of each.

        ## Title: "Renewable Energy Initiatives Catalog"
        Content: A compilation of documents that mention and discuss various renewable energy initiatives undertaken by the company. It includes project reports, feasibility studies, and policy documents.

        ## Title: "EPC Division: Foundational Documents Guide"
        Content: This guide highlights the essential foundational documents for newcomers to the Engineering, Procurement, and Construction (EPC) division. It covers key processes, methodologies, and best practices.

        I want you to pretend to be a helpful chatbot and guide my employee on the questions they have with my documents.
        The question they have is as follows: {user_input}
        Reply to this in a JSON format resembling this:
        {{"redirect": , "response": {{"recommended_document": "", "steps": ["", "", "", "", ""], "additional_advice": ""}}}} If the question asks for a redirect to a URL, set the "redirect" to true, else set it to false"""
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
    # Handling the preflight request 
    if request.method == 'OPTIONS':
        response = app.make_default_options_response()
    elif request.method == 'POST':
        try:
            data = request.get_json(force=True)
            user_input = data.get('user_input', '') 

            prompt = create_prompt(user_input)
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