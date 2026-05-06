# Android Gerrit Team Health Dashboard

A web application that provides a quick, read-only overview of Android Gerrit project health. The dashboard displays key information such as open changes, merged changes, abandoned changes, and overall health score for the multiple projects.

The application supports developers and team leads who need fast insight into project activity without manually checking each Gerrit repository.

## Features

- View multiple Android Gerrit projects in one dashboard
- Display key metrics:
  - Open changes
  - Merged changes (90 days)
  - Abandoned changes (90 days)
  - Health score and label
- Compare projects side-by-side
- Navigate between dashboard, comparison, and detail pages
- Direct links to Gerrit repositories
- Simple caching to reduce repeated API calls

## Technology Stack

- Backend: Python (FastAPI)
- Frontend: React (Vite)
- API Requests: httpx
- Testing: pytest
- Platform: Web (desktop-focused)

## Running the Application (GitHub Codespaces)

### Backend
cd backend
pip install -r requirements.txt
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000

### Frontend
cd frontend
npm install
npm run dev -- --host 0.0.0.0

Then open the forwarded port 5173 in the Codespaces Ports tab.

### Usage
1. Open the dashboard page
2. View project health cards for each Android team
3. Navigate to the comparison page to compare metrics
4. Click "View details" to inspect a specific project
5. Use "Open repo" to view the project in Gerrit

### Security Notes
- Only predefined Android Gerrit projects are accessed
- Input validation is applied to project requests
- The application uses public, read-only Gerrit data
- Backend API includes error handling and safe responses

### Testing
cd backend
python -m pytest