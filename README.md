Simple [FastAPI][fastapi] using [aioredis][aioredis] for actual app and [fakeredis][fakeredis] for testing so we are sure our actual data is disturbed by our test code.


## Depedencies

 - [Redis][redis]

## Start

```shell
git clone 

cd fastapi-aioredis

virtualenv -p python3 venv

source venv/bin/activate

pip install -r requirements.txt
```

## Run

```shell
uvicorn main:app --lifespan on
```

## Test

```shell
pytest
```

[aioredis]: https://aioredis.readthedocs.io/en/latest/
[fakeredis]: https://github.com/jamesls/fakeredis/
[fastapi]: https://fastapi.tiangolo.com
[redis]: https://redis.io/
