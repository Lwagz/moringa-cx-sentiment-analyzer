# 📊 Moringa CX-Insight Toolkit: Sentiment Analysis

## 📖 1. Overview of Technology
This project utilizes **Python 3.13** and the **TextBlob** library to perform Natural Language Processing (NLP). 
* **TextBlob**: A Python library used for processing textual data, providing a simple API for diving into common NLP tasks like sentiment analysis.
* **CSV Module**: Used for handling the structured customer feedback data stored in `feedback.csv`.
* **Goal**: To automatically categorize customer feedback into Positive, Negative, or Neutral sentiments to improve Customer Experience (CX).

## ⚙️ 2. Set Up Instructions
Follow these steps to set up the project on your local machine:
1. **Clone the Repository**: 
   `git clone https://github.com/Lwagz/moringa-cx-sentiment-analyzer.git`
2. **Open in VS Code**: Open the project folder in Visual Studio Code.
3. **Create a Virtual Environment**: 
   - Open the Command Palette (`Ctrl+Shift+P`).
   - Select **Python: Create Environment** and choose **Venv**.
4. **Install Dependencies**: 
   Run the following in the terminal:
   ```bash
   pip install textblob
   python -m textblob.download_corpora

   WORKING EXAMPLE
   from textblob import TextBlob

# A quick test of a feedback string
feedback = "The service at Moringa was excellent!"
analysis = TextBlob(feedback)

print(f"Polarity Score: {analysis.sentiment.polarity}") 
# A score above 0 indicates a Positive sentiment.

AI PROMPTS AND LEARNING REFLECTIONS
AI Prompts Used:
1."How do I create a new text document in VS Code?".
2."How do I run python code under main.py?"
3."SyntaxError: invalid syntax for git init".
4."Which virtual environment should I create: Venv or Conda?"

Learning Reflections:

Through this project, I learned the critical difference between the Code Editor and the Terminal. I initially struggled with putting system commands (like git init) inside my Python script, which caused syntax errors. I now understand that Python files are for logic, while the Terminal is for managing the environment and version control.

Common Errors & Resolutions
A.SyntaxError: invalid syntax
Cause:Putting git or pip commands in main.py.
Solution:Move those commands to the Terminal.
B.FileNotFoundError:
Cause:CSV named incorrectly or file extension hidden.
Solution:Ensure the file is named exactly feedback.csv.
C:Resource brown not found:
Cause:TextBlob dictionary not downloaded.
Solution:Run python -m textblob.download_corpora in terminal.

Resources
1.Official TextBlob Documentation

2.Python for Beginners - VS Code Official Docs

3.Git and GitHub Basics