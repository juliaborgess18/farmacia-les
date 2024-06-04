from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import uvicorn
from infrastructure.config.database import criar_bd
from routes import produto_route

app = FastAPI()
criar_bd()
templates = Jinja2Templates(directory="templates")
app.mount(path="/static", app=StaticFiles(directory="static"), name="static")

app.include_router(produto_route.router)

@app.get("/", response_class=HTMLResponse)
async def get_farmacia(request: Request):
    return templates.TemplateResponse("index.html", {"request":request})

@app.get("/cliente", response_class=HTMLResponse)
async def get_cliente(request: Request):
    return templates.TemplateResponse("cliente.html", { "request":request, "navItem": "Cliente", "urlItem": "cliente" })

@app.get("/fornecedor", response_class=HTMLResponse)
async def get_fornecedor(request: Request):
    return templates.TemplateResponse("fornecedor.html", {"request":request, "navItem": "Fornecedor", "urlItem": "fornecedor" })


@app.get("/venda", response_class=HTMLResponse)
async def get_venda(request: Request):
    return templates.TemplateResponse("venda.html", {"request":request, "navItem": "Venda", "urlItem": "venda" })

# @app.get("/cliente/cadastro", response_class=HTMLResponse)
@app.get("/cadastrar_cliente", response_class=HTMLResponse)
async def get_venda(request: Request):
    return templates.TemplateResponse("cadastrar_cliente.html", {"request":request, "navItem": "Cliente", "urlItem": "cliente" })

if __name__ == "__main__":
    uvicorn.run("main:app", port=8000, reload=True)