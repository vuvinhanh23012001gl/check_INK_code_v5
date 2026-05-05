
import uvicorn
import socketio
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from routers import router_home,sio

def create_app():
    app = FastAPI(title="Width Line Detection")
    app.mount(
        "/static",
        StaticFiles(directory="static"),
        name="static"
    )
    app.include_router(router_home)
    socket_app = socketio.ASGIApp(
        sio,
        app
    )
    return socket_app

app = create_app()

def main():
    uvicorn.run(
        "run:app",          # file:object
        host="127.0.0.1",
        port=8000,
        reload=True,
        ws_ping_interval=None
    )
if __name__ == "__main__":
    import pipeline.one_product
    # main()



# import services.vision.detect.egde.unet_plus.mask_and_polygon
# import pipeline.one_product
