import axios from "axios";

// backend API connection
const api = axios.create({
  baseURL: "http://localhost:8000/api",
});

// get all project summaries
export async function fetchProjects() {
  const response = await api.get("/projects");
  return response.data;
}