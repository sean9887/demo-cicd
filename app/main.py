from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse

app = FastAPI()
app.mount("/image", StaticFiles(directory="image"), name="image")

@app.get("/", response_class=HTMLResponse)
async def root():
    return """
    <html>
        <head><title>ArgoCD CI/CD Demo</title></head>
        <body>
            <h1>Hello from CI/CD!</h1>
            <img src="/image/dog1.png" width="300px" />
        </body>
    </html>
    """
