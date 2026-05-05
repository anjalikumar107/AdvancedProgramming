import React from "react";
import HealthBar from "./HealthBar";

export default function ProjectCard({ project }) {
  return (
    <div
      style={{
        background: "#0f172a",
        color: "white",
        padding: "1rem",
        borderRadius: "12px",
      }}
    >
      <h2>{project.team}</h2>
      <p>{project.project}</p>

      <strong>
        {project.health_label} — {project.overall_health_score}/100
      </strong>

      <HealthBar score={project.overall_health_score} />
    </div>
  );
}