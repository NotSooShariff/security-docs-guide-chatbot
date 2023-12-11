<<<<<<< HEAD
# Security Documentation Chatbot 🤖📃
=======
<h1 align="center">Security Documentation Chatbot</h1> 
>>>>>>> 59c2d43e89f96b1a115477359ec6d84969846cdb

This chatbot is designed to assist users within your organization in navigating the vast landscape of cybersecurity guidelines, frameworks, and compliance documents.

<img width="1280" alt="image" src="https://github.com/NotSooShariff/security-docs-guide-chatbot/assets/93514938/2582e7a3-f272-4cf8-af95-e44369fc562b">

## Purpose

In the dynamic realm of cybersecurity, staying compliant with standards and regulations is crucial. However, with a plethora of documents to sift through, finding the right information can be a daunting task. This Project aims to streamline this process by providing users with personalized guidance on which documents to follow for specific purposes, as well as where to locate these documents within your organizational repository.

## Key Features

- **Document Discovery:** Effortlessly find the right documents for your specific cybersecurity needs.
- **Compliance Guidance:** Receive guidance on adhering to industry standards and frameworks.
- **User-Friendly Interface:** A chat-based interface for intuitive and accessible interaction.

## Prerequisities

Have Git & Python installed on your system and added to PATH Environment Variables. Optionally, ensure you have a list of Documents that you want the Chatbot to be trained on. 

## Getting Started

To use this chatbot for your own organization, follow the installation and setup instructions below.

1. Clone this repository by running the following command in your terminal: 

```
git clone https://github.com/NotSooShariff/security-docs-guide-chatbot.git
```

2. Activate the virtual environment

```
venv\Scripts\activate
```

3. Install the dependencies 

```
pip install requirements.txt
```

4. Currently, the Chatbot can be queried on the following documents:

- **Acceptable Use Policy (AUP)**
- **Information Security Policy**
- **Data Breach Response Plan**
- **Security Awareness Training Materials**
- **Incident Response Plan**
- **Remote Work Security Guidelines**
- **Security Incident Log**
- **Security Patching Policy**
- **Bring Your Own Device (BYOD) Policy**
- **Physical Security Policy**
- **Vendor Security Assessment Checklist**
- **Compliance Audit Checklist**
- **Data Retention and Destruction Policy**
- **NIST Cybersecurity Framework Implementation Guide**
- **ISO 27001 Information Security Management System (ISMS)**
- **CIS Critical Security Controls**
- **GDPR Compliance Checklist**
- **HIPAA Security Rule Compliance Guide**
- **PCI DSS Compliance Checklist**
- **SOC 2 Compliance Framework**
- **Cybersecurity Maturity Model Certification (CMMC) Guidelines**
- **ITIL (Information Technology Infrastructure Library) Security Management**
- **Cloud Security Alliance (CSA) Security Guidance**
- **OWASP Application Security Verification Standard**
- **National Cyber Security Centre (NCSC) Cyber Essentials**
- **Federal Risk and Authorization Management Program (FedRAMP) Compliance Checklist**
- **Acceptable Encryption Policy**
- **Disaster Recovery Plan**
- **Business Continuity Plan (BCP)**
- **Change Management Policy**
- **Mobile Device Management (MDM) Policy**
- **Password Policy**
- **Network Security Policy**
- **Social Media Usage Policy**
- **Employee Code of Conduct**
- **IT Asset Management Policy**
- **Remote Access Policy**
- **Physical Access Control Policy**
- **User Account Management Policy**
- **IT Incident Reporting Procedures**

If you would like to modify these and/or add your own, run the `setup.py` with the following command:
```
python setup.py
```

You can also just choose to paste the documents in the `documents.txt` file if you want to add them in bulk

5. Finally, run the server

```
python server.py
```

6. Test that the server is running by running the `requests.py` file in the tests directory using one of the questions in the `questions.md` file. 

7. Create a User Interface (UI) Website to Interact with the server or use the example `index.html` provided.


## License

This project is licensed under the MIT License - see the [LICENSE](https://github.com/NotSooShariff/security-docs-guide-chatbot/blob/main/LICENSE.md) file for details.

## Contributions

Contributions are welcome! Feel free to fork the repo and issue a pull request to improve this project.