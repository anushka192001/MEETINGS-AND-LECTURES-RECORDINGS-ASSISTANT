import { Typography } from "@mui/material";

const Title: React.FC = () => {
  return (
    <Typography
      variant="h4"
      gutterBottom
      component="div"
      sx={{
        fontFamily: "Ubuntu",
        marginTop: 0.5,
        marginBottom: 1,
        fontWeight: "bold",
        color: "primary.main",
      }}
    > 
      MEETINGS AND LECTURES RECORDINGS ASSISTANT
    </Typography>
  );
};

export { Title };
