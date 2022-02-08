# FASTAPI_Async_Python
This repository is exclusive to my studies In FAST API using Asyncio

### RESOURCES

- https://www.youtube.com/watch?v=IZUjJ3rPY1E
- https://fastapi.tiangolo.com/pt/async/
- https://www.lobdata.com.br/2021/04/03/
- criando-uma-api-pronta-para-produ%C3%A7%C3%A3o-com-fastapi-pt.2/
https://docs.python.org/pt-br/3/library/asyncio.html


### PARA QUE SERVE?
Lib para escrever codigo simultaneo usando sintaxe async/await.
Asyncio fornece um conjunto de APIs de alto nível para:

- executar corrotinas do Python simultaneamente e ter controle total sobre sua execução;
- realizar IPC e E/S de rede;
- controlar subprocessos;
- distribuir tarefas por meio de filas;
- sincronizar código simultâneo;

### CÓDIGO ASSINCRONO

Código assíncrono apenas significa que a linguagem 💬 tem um jeito de dizer para o computador / programa 🤖 que em certo ponto, ele 🤖 terá que esperar por algo para finalizar em outro lugar. Vamos dizer que esse algo seja chamado "arquivo lento" 📝.

## CONCORRÊNCIA E ASYNC/AWAIT

Para chamar as funções use `await`:

`results = await some_library()`

Desta forma, tem que declarar a função com async def: 

```
@app.get('/')
async def read_results():
    results = await some_library()
    return results
```
Você somente pode usar await dentro de funções ASYNC DEF.

