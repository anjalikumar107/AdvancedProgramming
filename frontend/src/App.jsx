import React from "react";
import { BrowserRouter, Link, Route, Routes } from "react-router-dom";
import DashboardPage from "./pages/DashboardPage";
import ComparePage from "./pages/ComparePage";
import DetailPage from "./pages/DetailPage";

// handles navigation between the dashboard pages
export default function App() {
  return (
    <BrowserRouter>
      <nav style={{ background: "#0f172a", padding: "1rem" }}>
        <Link style={{ color: "white", marginRight: "1rem" }} to="/">
          Dashboard
        </Link>
        <Link style={{ color: "white" }} to="/compare">
          Compare
        </Link>
      </nav>
      <Routes>
        <Route path="/" element={<DashboardPage />} />
        <Route path="/compare" element={<ComparePage />} />
        <Route path="/project/:projectName" element={<DetailPage />} />
      </Routes>
    </BrowserRouter>
  );
}