from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import uvicorn
from infrastructure.config.database import criar_bd
from routes import produto_route, cliente_route,  venda_route, fornecedor_route

criar_bd()
app = FastAPI()
templates = Jinja2Templates(directory="templates")
app.mount(path="/static", app=StaticFiles(directory="static"), name="static")

app.include_router(produto_route.router)
app.include_router(cliente_route.router)
app.include_router(venda_route.router)
app.include_router(fornecedor_route.router)

@app.get("/", response_class=HTMLResponse)
async def get_farmacia(request: Request):
    return templates.TemplateResponse("index.html", {"request":request})

if __name__ == "__main__":
    uvicorn.run("main:app", port=8000, reload=True)
