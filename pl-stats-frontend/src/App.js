import React, { useState } from "react";
import './App.css';

function App() {
  const [question, setQuestion] = useState("");
  const [messages, setMessages] = useState([]);
  const [loading, setLoading] = useState(false);

  const askGPT = async () => {
    if (!question.trim()) return;

    const userMessage = { text: question, from: "user" };
    setMessages([...messages, userMessage]);
    setLoading(true);
    setQuestion("");

    try {
      const res = await fetch("http://localhost:5000/ask", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ question })
      });

      const data = await res.json();
      const gptMessage = { text: data.answer || "Error: no answer", from: "bot" };
      setMessages(prev => [...prev, gptMessage]);
    } catch (err) {
      setMessages(prev => [...prev, { text: "Something went wrong.", from: "bot" }]);
    }

    setLoading(false);
  };

  const handleKeyPress = (e) => {
    if (e.key === "Enter") askGPT();
  };

  return (
    <div className="chatbot-container">
      <div id="chatbot">
        <div id="header">Premier League Stats Assistant</div>
        <div id="conversation">
          {messages.map((msg, idx) => (
            <div
              key={idx}
              className={`chatbot-message ${msg.from === "user" ? "user-message" : ""}`}
            >
              <p className="chatbot-text" sentTime={new Date().toLocaleTimeString()}>
                {msg.text}
              </p>
            </div>
          ))}
          {loading && (
            <div className="chatbot-message">
              <p className="chatbot-text">Thinking...</p>
            </div>
          )}
        </div>

        <div id="input-form">
          <input
            id="input-field"
            type="text"
            placeholder="Ask about goals, xG, team trends..."
            value={question}
            onChange={(e) => setQuestion(e.target.value)}
            onKeyDown={handleKeyPress}
          />
          <button id="submit-button" onClick={askGPT} className="send-icon">
            ➤
          </button>
        </div>
      </div>
    </div>
  );
}

export default App;
