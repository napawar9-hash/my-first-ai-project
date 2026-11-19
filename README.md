# AI Chatbot Starter

A beginner-friendly Python project that sends a prompt to the OpenAI API and prints the response.

## Features
- Simple command-line chat prompt
- Reads the API key from an environment file
- Keeps secrets out of GitHub using `.gitignore`

## Setup

1. Install Python 3.10 or newer.
2. Create and activate a virtual environment (recommended).
3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Copy `.env.example` to `.env` and add your own API key.
5. Run:

   ```bash
   python app.py
   ```

## API key safety

Never upload your real API key, `.env` file, passwords, or private credentials to GitHub.
The `.env` file is excluded by `.gitignore`.

## Project structure

```text
ai-github-starter/
├── app.py
├── requirements.txt
├── .env.example
├── .gitignore
└── README.md
```

## About

This is a starter project for learning how to build and publish an AI-powered application.
