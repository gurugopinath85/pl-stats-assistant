from flask import Flask, request, jsonify
from openai import OpenAI
import pandas as pd
import os


app = Flask(__name__)
# Load OpenAI API key
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
print("Welcome to PL Stats! Ask questions about player stats, prizepicks player props, or other trends. Type 'exit', 'quit', or 'q' to quit.\n")

while True:
    user_question = input("Your question: ").strip()
    if user_question.lower() in ["exit", "quit", "q"]:
        print("Thank you for using the application! Goodbye!")
        break

    
    context = f"""
STANDARD PLAYER STATS (latest):
{df_standard.head(40).to_string(index=False)}

HISTORICAL STATS (older or match-level):
{df_historical.head(40).to_string(index=False)}

Question: {user_question}
"""

    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": context}
            ]
        )
        reply = response.choices[0].message.content
        print("\nHere's what I found:\n")
        print(reply)
        print("\n" + "-"*60 + "\n")

    except Exception as e:
        print(f"\nGPT API Error: {e}")
