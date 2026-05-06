import axios from "axios";

const api = axios.create({
  baseURL: "https://upgraded-happiness-gxqqvg6vvg7ph95jg-8000.app.github.dev/api",
});

export async function fetchProjects() {
  const response = await api.get("/projects");
  console.log("API DATA:", response.data);
  return response.data;
}