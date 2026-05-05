import React, { useEffect, useState } from "react";
import { fetchProjects } from "./parts/api";
import ProjectCard from "./parts/ProjectCard";

export default function App() {
  const [projects, setProjects] = useState([]);

  // fetch project data once when the page loads
  useEffect(() => {
    fetchProjects().then(setProjects);
  }, []);

  return (
    <main
      style={{
        padding: "1rem",
        background: "#e5e7eb", // light grey background
        minHeight: "100vh",
      }}
    >
      <section
        style={{
          background: "#0f172a", // navy header
          color: "white",
          padding: "1.5rem",
          borderRadius: "12px",
          marginBottom: "1rem",
        }}
      >
        <h1>Android Gerrit Software Team Health Dashboard</h1>
        <p>Compare Android Gerrit projects using 90-day review activity.</p>
      </section>

      {/* display a card for each project */}
      {projects.map((project) => (
        <ProjectCard key={project.project} project={project} />
      ))}
    </main>
  );
}