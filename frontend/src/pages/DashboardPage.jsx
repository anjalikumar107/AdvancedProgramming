import React, { useEffect, useState } from "react";
import { fetchProjects } from "../services/api";
import ProjectCard from "../parts/ProjectCard";

export default function DashboardPage() {
  const [projects, setProjects] = useState([]);

  useEffect(() => {
    fetchProjects()
      .then((data) => {
        console.log("PROJECT DATA:", data);
        setProjects(data);
      })
      .catch((error) => console.error("API ERROR:", error));
  }, []);

  return (
    <main style={{ padding: "1rem", background: "#e5e7eb", minHeight: "100vh" }}>
      <section style={{ background: "#0f172a", color: "white", padding: "1.5rem", borderRadius: "12px", marginBottom: "1rem" }}>
        <h1>Android Gerrit Software Team Health Dashboard</h1>
        <p>Compare Android Gerrit projects using 90-day review activity.</p>
      </section>
      {projects.length === 0 && <p>No project data loaded.</p>}
      {projects.map((project) => (
        <ProjectCard key={project.project} project={project} />
      ))}
    </main>
  );
}