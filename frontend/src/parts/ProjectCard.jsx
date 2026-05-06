import React from "react";
import { Link } from "react-router-dom";
import HealthBar from "./HealthBar";

export default function ProjectCard({ project }) {
  return (
    <div style={{ background: "#0f172a", color: "white", padding: "1rem", borderRadius: "12px", marginBottom: "1rem" }}>
      <h2>{project.team}</h2>
      <p>{project.project}</p>
      <strong>
        {project.health_label} — {project.overall_health_score}/100
      </strong>
      <div style={{ margin: "0.75rem 0" }}>
        <HealthBar score={project.overall_health_score} />
      </div>
      <ul>
        <li>Open changes: {project.open_changes}</li>
        <li>Merged 90d: {project.merged_changes_90d}</li>
        <li>Abandoned 90d: {project.abandoned_changes_90d}</li>
        <li>Merge ratio: {Math.round(project.merge_ratio * 100)}%</li>
      </ul>
      <Link style={{ color: "white", marginRight: "1rem" }} to={`/project/${encodeURIComponent(project.project)}`}>
        View details
      </Link>
      <a style={{ color: "white" }} href={project.url} target="_blank" rel="noreferrer">
        Open repo
      </a>
    </div>
  );
}