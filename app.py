"""
Python file for webpage deployment for DSC Ensign College

"""


from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles


app = FastAPI(
    title='DSC Ensign College',
    description='DSC Ensign College Website',
    version='1.0'
)
app.mount('/assets', StaticFiles(directory='assets'), name='static')
templates = Jinja2Templates(directory='assets')


@app.get('/')
def index(request: Request):
    """Main page"""
    return templates.TemplateResponse('index.html', {
        'request': request
    })

@app.get('/join')
def join(request: Request):
    """Join page"""
    return templates.TemplateResponse('join.html', {
        'request': request
    })
