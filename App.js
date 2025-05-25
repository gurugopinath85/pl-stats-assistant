// frontend/src/App.js

import React, { useState } from "react";

function App() {
  const [question, setQuestion] = useState("");
  const [response, setResponse] = useState("");

  const askQuestion = async () => {
    const res = await fetch("http://localhost:5000/ask", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ question }),
    });
    const data = await res.json();
    setResponse(data.answer);
  };

  return (
    <div style={{ padding: "2rem" }}>
      <h1>Premier League Chatbot</h1>
      <input
        type="text"
        value={question}
        onChange={(e) => setQuestion(e.target.value)}
        placeholder="Ask about Haaland or Arsenal"
        style={{ width: "400px", marginRight: "10px" }}
      />
      <button onClick={askQuestion}>Ask</button>

      <div style={{ marginTop: "2rem" }}>
        <strong>Answer:</strong>
        <p>{response}</p>
      </div>
    </div>
  );
}

export default App;
