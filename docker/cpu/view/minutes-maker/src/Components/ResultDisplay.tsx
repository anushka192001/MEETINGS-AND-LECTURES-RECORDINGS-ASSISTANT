import React, { useContext, useRef, useEffect } from "react";
import { AppContext } from "./AppContext";
import ReactMarkdown from "react-markdown";
import { Box, Paper, Typography } from "@mui/material";
import PacmanLoader from "react-spinners/PacmanLoader";
import { ChatBox } from "./ChatBox";

const ResultDisplay: React.FC = () => {
  const { apiResponse, isLoading } = useContext(AppContext);
  // 1. Add a ref for the summary/timeline section
  const summaryRef = useRef<HTMLDivElement>(null);

  // 2. Scroll into view when apiResponse appears
  useEffect(() => {
    if (apiResponse && summaryRef.current) {
      summaryRef.current.scrollIntoView({ behavior: "smooth" });
    }
  }, [apiResponse]);



  if (!isLoading) return null;
  if (!apiResponse) {
    return (
    <Box sx={{
      display: "flex",
      justifyContent: "center",
      mt: 0.1               // margin-top to separate from submit
    }}>
      <PacmanLoader color="#5c6bc0" loading size={24} />
    </Box>
  );   
  } 
  return (
    <Box sx={{ mx: "auto", width: "98%", mt: 2 }} ref={summaryRef}>
      <Box sx={{
        display: "flex",
        flexWrap: "wrap",
        justifyContent: "space-between",
        gap: 2
      }}>
        <Paper sx={{
          flex: "1 1 45%",
          padding: 3,
          margin: 1,
          textAlign: "left",
          backgroundColor: "#f6f6f6",
          boxShadow: "0px 0px 8px rgba(0,0,0,0.12)",
          "&:hover": { boxShadow: "0px 0px 8px 2px rgba(9,67,68,0.23)" },
        }}>
          <Typography variant="h4" sx={{ fontWeight: "bold", color: "primary.main", fontFamily: "Ubuntu" }}>
            Timeline
          </Typography>
          <ReactMarkdown>{apiResponse.timeline}</ReactMarkdown>
        </Paper>

        <Paper sx={{
          flex: "1 1 45%",
          padding: 3,
          margin: 1,
          textAlign: "left",
          backgroundColor: "#f6f6f6",
          boxShadow: "0px 0px 8px rgba(0,0,0,0.12)",
          "&:hover": { boxShadow: "0px 0px 8px 2px rgba(9,67,68,0.23)" },
        }}>
          <Typography variant="h4" sx={{ fontWeight: "bold", color: "primary.main", fontFamily: "Ubuntu" }}>
            Summary
          </Typography>
          <ReactMarkdown>{apiResponse.summary}</ReactMarkdown>
        </Paper>
      </Box>

      <Box sx={{ mt: 4 }}>
        <ChatBox />
      </Box>
    </Box>
  );
};

export { ResultDisplay };
