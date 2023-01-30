from fastapi import FastAPI
from pydantic import BaseModel
from generator import assesment
#from pre_parse import parseWords
import time # input datetime


from fastapi.openapi.utils import get_openapi
from fastapi.openapi.docs import (
    get_redoc_html,
    get_swagger_ui_html,
    get_swagger_ui_oauth2_redirect_html,
)

from fastapi import applications

from fastapi.staticfiles import StaticFiles

app = FastAPI(docs_url=None, redoc_url=None)

app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get("/docs", include_in_schema=False)
async def custom_swagger_ui_html():
    return get_swagger_ui_html(
        openapi_url=app.openapi_url,
        title=app.title + " - Swagger UI",
        oauth2_redirect_url=app.swagger_ui_oauth2_redirect_url,
        swagger_js_url="/static/swagger-ui-bundle.js",
        swagger_css_url="/static/swagger-ui.css",
    )


@app.get(app.swagger_ui_oauth2_redirect_url, include_in_schema=False)
async def swagger_ui_redirect():
    return get_swagger_ui_oauth2_redirect_html()


@app.get("/redoc", include_in_schema=False)
async def redoc_html():
    return get_redoc_html(
        openapi_url=app.openapi_url,
        title=app.title + " - ReDoc",
        redoc_js_url="/static/redoc.standalone.js",
    )

def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema
    openapi_schema = get_openapi(
        title="RELEN Smart Assessment API documentation",
        version="0.0.2",
        description="This API and Documentation was developed by processor",
        routes=app.routes,
    )
    openapi_schema["info"]["x-logo"] = {
        "url": "/static/logo-teal.png"
    }
    app.openapi_schema = openapi_schema
    return app.openapi_schema


app.openapi = custom_openapi



class Item(BaseModel):
    link: str
    item_id: str
   

@app.get("/")
async def root():
    print("wait")
    return {"message": "Welcome Processor, its a good day."}

# p = multiprocessing.Process(target=assesment)



@app.post("/items/")
async def create_item(item: Item):
    print(item)
  
    link = item.link
    unique_id = item.item_id
    # mylist = [1,2,3,4]
  
    # creating new process
    # starting process
    # wait until process is finished
    # p = multiprocessing.Process(target=assesment)
     # starting process 1
    # p.start()
    # p.join()
    # return p
    first = time.localtime().tm_min
    sec = time.localtime().tm_sec
    print ("begin------",first, sec)
    result = assesment(link, unique_id)

    first = time.localtime().tm_min
    sec = time.localtime().tm_sec
    print ("begin------",first, sec)
    #total = assesment(link,unique_id)
    #print(" total type  Below")
    #print(type(total)) 1.18
    #print(" total   Below")
    #print(total)

    #item["resource_link"] = resource_link.resource_link

    return result
