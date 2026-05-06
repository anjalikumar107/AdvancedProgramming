import React, { useEffect, useState } from "react";
import { fetchProjects } from "../services/api";

// page for comparing project health scores
export default function ComparePage() {
  const [projects, setProjects] = useState([]);

  useEffect(() => {
    fetchProjects().then(setProjects);
  }, []);

  return (
    <main style={{ padding: "1rem", background: "#e5e7eb", minHeight: "100vh" }}>
      <section
        style={{
          background: "#0f172a",
          color: "white",
          padding: "1.5rem",
          borderRadius: "12px",
          marginBottom: "1rem",
        }}
      >
        <h1>Project Comparison</h1>
        <p>Compare project health scores side by side.</p>
      </section>
      <table style={{ width: "100%", borderCollapse: "collapse", background: "white" }}>
        <thead style={{ background: "#0f172a", color: "white" }}>
          <tr>
            <th style={{ padding: "0.75rem", textAlign: "left" }}>Team</th>
            <th style={{ padding: "0.75rem", textAlign: "left" }}>Project</th>
            <th style={{ padding: "0.75rem", textAlign: "left" }}>Health</th>
            <th style={{ padding: "0.75rem", textAlign: "left" }}>Merged 90d</th>
          </tr>
        </thead>
        <tbody>
          {projects.map((project) => (
            <tr key={project.project}>
              <td style={{ padding: "0.75rem" }}>{project.team}</td>
              <td style={{ padding: "0.75rem" }}>{project.project}</td>
              <td style={{ padding: "0.75rem" }}>{project.overall_health_score}/100</td>
              <td style={{ padding: "0.75rem" }}>{project.merged_changes_90d}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </main>
  );
}