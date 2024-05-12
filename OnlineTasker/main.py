from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
import uvicorn
from number_of_tasks import *

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
    array_words = number.split(' ')
    print(array_words)
    if (array_words[0] == 'Matan'):
        if (array_words[3][0] == 'T'):
            img = f'../static/Online-tasking-pages/calculus-tasking/out{dict_of_number_T_calculus[int(array_words[1])][array_words[3]]}.png'
            source = f'../static/Online-tasking-pages/calculus-tasking/'
        else:
            img = f'../static/Online-tasking-pages/calculus-tasks/out{dict_of_number_of_tasks_calculus[int(array_words[2])][array_words[3]]}.png'
            source = f'../static/Online-tasking-pages/calculus-tasks/'
    elif (array_words[0] == 'Angem'):
        if (array_words[2][0] == 'Т'):
            img = f'../static/Online-tasking-pages/analytic-geometry-tasking/out{dict_of_number_T_geometry[int(array_words[1])][array_words[2]]}.png'
            source = f'../static/Online-tasking-pages/analytic-geometry-tasking/'
        else:
            img = f'../static/Online-tasking-pages/analytic-geometry-tasks/out{dict_of_number_of_tasks_geometry[array_words[2]]}.png'
            source = f'../static/Online-tasking-pages/analytic-geometry-tasks/'
    elif (array_words[0] == 'Discr'):
        img = f'../static/Online-tasking-pages/Discrete-math-tasks/out{dict_of_number_of_tasks_discret[array_words[1]]}.png'
        source = f'../static/Online-tasking-pages/Discrete-math-tasks/'
    return templates.TemplateResponse('third_page.html', context={'request': request, 'image': img, 'source':source})


if __name__ == "__main__":
    uvicorn.run("main:app", host='127.0.0.1', port=8013, reload=True)
