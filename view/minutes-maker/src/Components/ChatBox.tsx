// ChatBox.tsx
import React, { useState, useEffect } from "react";
import "@chatscope/chat-ui-kit-styles/dist/default/styles.min.css";
import {
  MainContainer,
  ChatContainer,
  MessageList,
  Message,
  MessageInput,
} from "@chatscope/chat-ui-kit-react";

interface ChatMessage {
  content: string;
  sender: "user" | "bot";
}

export const ChatBox: React.FC = () => {
  const [messages, setMessages] = useState<ChatMessage[]>([]);
  const [input, setInput] = useState("");
  const [isOpen, setIsOpen] = useState(true);

  useEffect(() => {
    setMessages([{ content: "Hi! Ask me anything about the recording 😊", sender: "bot" }]);
  }, []);

  const handleSend = async (text: string) => {
    setMessages(prev => [...prev, { content: text, sender: "user" }]);
    setInput(""); 
    const res = await fetch("https://${process.env.REACT_APP_PUBLIC_IP!}/query", {
      method: "POST",
      body: new URLSearchParams({ question: text }),
    });
    if (!res.ok || !res.body) return;
    const reader = res.body.getReader();
    const decoder = new TextDecoder();
    let botText = "";
    setMessages(prev => [...prev, { content: "", sender: "bot" }]);
    while (true) {
      const { value, done } = await reader.read();
      if (done) break;
      botText += decoder.decode(value);
      setMessages(prev => {
        const copy = [...prev];
        copy[copy.length - 1] = { content: botText, sender: "bot" };
        return copy;
      });
    }
  };

  return (
    <div
      style={{
        position: "fixed",
        bottom: 20,
        right: 20,
        width: isOpen ? 320 : 60,
        height: isOpen ? 400 : 60,
        border: "1px solid #ccc",
        borderRadius: 8,
        background: "#fff",
        boxShadow: "0 2px 8px rgba(0,0,0,0.15)",
        overflow: "hidden",
        zIndex: 1000,
      }}
    >
      {isOpen ? (
        <div style={{ position: "relative", height: "100%" }}>
          {/* Close button */}
          <button
            onClick={() => setIsOpen(false)}
            style={{
              position: "absolute",
              top: 8,
              right: 8,
              width: 24,
              height: 24,
              borderRadius: "50%",
              border: "none",
              cursor: "pointer",
              background: "#eee",
              fontSize: 16,
              zIndex: 1001,
            }}
          >❌</button>

          <MainContainer>
            <ChatContainer style={{ height: "100%", display: "flex", flexDirection: "column" }}>
              <MessageList style={{ flex: 1, overflowY: "auto", padding: 8 }} scrollBehavior="auto">
                {messages.map((msg, i) => (
                  <Message key={i}
                    model={{
                      message: msg.content,
                      sender: msg.sender === "bot" ? "ChatGPT" : "You",
                      direction: msg.sender === "bot" ? "incoming" : "outgoing",
                      position: "single",
                    }}
                  />
                ))}
              </MessageList>
              <MessageInput
                placeholder="Ask a question..."
                value={input}
                onChange={setInput}
                onSend={handleSend}
                attachButton={false}
              />
            </ChatContainer>
          </MainContainer>
        </div>
      ) : (
        <button
          onClick={() => setIsOpen(true)}
          style={{
            width: "100%",
            height: "100%",
            background: "#5c6bc0",
            color: "#fff",
            border: "none",
            borderRadius: 8,
            cursor: "pointer",
            fontSize: 24,
          }}
        >
          💬
        </button>
      )}
    </div>
  );
};
