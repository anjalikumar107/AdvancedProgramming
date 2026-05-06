import React from "react";
import { useParams } from "react-router-dom";

// page showing selected project path
export default function DetailPage() {
  const { projectName } = useParams();
  return (
    <main style={{ padding: "1rem", background: "#e5e7eb", minHeight: "100vh" }}>
      <section
        style={{
          background: "#0f172a",
          color: "white",
          padding: "1.5rem",
          borderRadius: "12px",
        }}
      >
        <h1>Project Detail</h1>
        <p>{decodeURIComponent(projectName)}</p>
      </section>
    </main>
  );
}