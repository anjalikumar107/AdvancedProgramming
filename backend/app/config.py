# base URL for Gerrit instance used for API requests
BASE_URL = "https://android.googlesource.com"
# frontend origin for CORS configuration
FRONTEND_ORIGIN = "http://localhost:5173"
# timeout (seconds) for external API requests
REQUEST_TIMEOUT = 15
# cache duration (seconds) to reduce repeated Gerrit API calls
CACHE_SECONDS = 300

# each entry represents a software team in its Android Gerrit project
PROJECTS = [
    {
        "team": "Build Systems Team",
        "project": "platform/build",
        "url": "https://android.googlesource.com/platform/build/",
    },
    {
        "team": "Core Systems Team",
        "project": "platform/system/core",
        "url": "https://android.googlesource.com/platform/system/core/",
    },
    {
        "team": "Frameworks Team",
        "project": "platform/frameworks/base",
        "url": "https://android.googlesource.com/platform/frameworks/base/",
    },
    {
        "team": "Settings Team",
        "project": "platform/packages/apps/Settings",
        "url": "https://android.googlesource.com/platform/packages/apps/Settings/",
    },
]