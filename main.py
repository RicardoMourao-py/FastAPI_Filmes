from fastapi import FastAPI
from sql_app.routes import routeAvaliacao, routeFilme

app = FastAPI(
    title="Cadastre Filmes e os Avalie !!!",
    description="API para gerenciar filmes e avaliações",
    version="1.0.0",
)

# Adiciona as rotas para as classes Movie e Rating
app.include_router(routeFilme.router, tags=["Filmes"])
app.include_router(routeAvaliacao.router, tags=["Avaliações"])