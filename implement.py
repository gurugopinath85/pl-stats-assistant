from flask import Flask, request, jsonify
from flask_cors import CORS
from openai import OpenAI
import pandas as pd
import os


app = Flask(__name__)
CORS(app)
# Load OpenAI API key
#Main implementation of OpenAI services to be able to create a text-based response
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY")) 

# Use Csv files available
df_standard = pd.read_csv("pl_standard_stats_2025-05-20_20-14-01.csv")
df_historical = pd.read_csv("dataset - 2020-09-24.csv")


def clean_df(df):
    df.columns = [col.strip().replace(" ", "_") for col in df.columns]
    return df

df_standard = clean_df(df_standard)
df_historical = clean_df(df_historical)

# GPT prompt
system_prompt = """
You are a football data analyst using two datasets:
1. A 'standard player stats' dataset with season-level stats like goals, assists, xG, minutes.
2. A 'historical dataset' with older or different structured player or match-level data.

You help users make PrizePicks-style over/under betting decisions, like "Should I take over 0.5 goals for Saka vs Brighton?"

Each time:
- Read the user's question
- Use stats from either dataset to reason about the player or team
- If possible, reference trends, form, or opponent performance
- If data is limited, explain what’s missing

Be cautious but helpful in making OVER/UNDER-style suggestions.
"""

# 
@app.route("/ask", methods=["POST"])
def ask():
    try:
        user_question = request.json.get("question")  # ✅ Make sure this matches

        context = f"""
STANDARD PLAYER STATS:
{df_standard.head(40).to_string(index=False)}

HISTORICAL STATS:
{df_historical.head(40).to_string(index=False)}

Question: {user_question}
"""

        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": context}
            ]
        )
        return jsonify({"answer": response.choices[0].message.content})

    except Exception as e:
        print("❌ Error in backend:", e)
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)