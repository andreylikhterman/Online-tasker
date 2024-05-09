from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
import uvicorn

app = FastAPI()
app.mount("/static", StaticFiles(directory="static", html=True), name="static")
templates = Jinja2Templates(directory='templates')


@app.get('/', response_class=HTMLResponse)
async def static(request: Request):
    return templates.TemplateResponse('first_page.html', context={'request': request})

@app.post('/tasks')
def form(request: Request, school: str = Form(...), semester: str = Form(...), subject: str = Form(...), number_task: str = Form(...)):
    return templates.TemplateResponse('second_page.html', context={'request': request, 'school' : school, 'semester' : semester, 'subject' : subject, 'number_task' : number_task})

@app.post('/tasks/image')
def form(request: Request, number: str = Form(...)):
    return templates.TemplateResponse('third_page.html', context={'request': request, 'number' : number})


if __name__ == "__main__":
    uvicorn.run("main:app", host='127.0.0.1', port=8010, reload=True)