# Premier League Stats Assistant

This is a personal project built to combine my interest in football statistics with my growing experience in AI and web development. I was inspired by sports betting platforms like PrizePicks and the growing availability of detailed player data. I wanted to create a tool that helps make more informed picks using actual player and team performance stats.

The core idea is simple: allow users to ask natural-language questions like:

- "Should I take over 0.5 goals for Haaland vs Brighton?"
- "How many assists did Bukayo Saka have last season?"
- "Which team has the highest expected goals?"

The assistant uses OpenAI's GPT-3.5 to interpret the question and respond using two CSV-based datasets:
- Standard player stats (season-level)
- Historical or match-level stats

Currently, I am updating it so that it can be accessed through a 
Flask backend API and connected to a React or Streamlit frontend.
More development to follow.

## Features

- Accepts natural-language football stat questions
- Uses real CSV datasets as the basis for analysis
- Offers betting-style insights (e.g., over/under suggestions)
- GPT-powered response engine
- Flask API for easy frontend integration

## How It Works

1. Two CSV files are loaded using Pandas:
   - One with current player stats
   - One with older or match-based stats

2. The app sends a preview of the data and the user's question to the OpenAI API.

3. GPT responds with an explanation, insight, or suggested pick based on the available data.

## Setup Instructions

### Prerequisites

- Python 3.8 or newer
- pip
- OpenAI API key

### Clone the Project

```bash
git clone https://github.com/your-username/pl-stats-assistant.git
cd pl-stats-assistant
