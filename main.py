from fastapi import FastAPI
from database import engine
import models
import uvicorn
from routes import router

models.Base.metadata.create_all(bind=engine)

app = FastAPI(title='Backstract Generated APIs - studentcollection-coll-6b8d1cf9b558499b83618bc4e8b7646e',debug=False,docs_url='/wizardly-galois-530ff3b6ca9611efbd990242ac12000482/docs',openapi_url='/wizardly-galois-530ff3b6ca9611efbd990242ac12000482/openapi.json')

app.include_router(router, prefix='/wizardly-galois-530ff3b6ca9611efbd990242ac12000482/api', tags=['APIs v1'])

def main():
    uvicorn.run('main:app', host='127.0.0.1', port=8008, reload=True)

if __name__ == '__main__':
    main()