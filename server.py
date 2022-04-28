from fastapi import FastAPI, Request, WebSocket, WebSocketDisconnect
from fastapi.templating import Jinja2Templates

app = FastAPI()

templates = Jinja2Templates(directory="templates")


@app.get("/")
async def index_page(request: Request, ):
    """Функция возращает html страницу клиенту"""
    return templates.TemplateResponse("index.html", {
        "request": request
        })

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    """Функция получает и отправляет данные через веб-сокет соединение"""
    await websocket.accept()
    try:
        while True:
            data = await websocket.receive_json()
            await websocket.send_json(data)
    except WebSocketDisconnect:
        print(f"\033[33mWARNING\033[37m:  \033[33mThe user reload or close the page")
