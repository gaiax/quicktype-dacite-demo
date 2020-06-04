# quicktype-dacite-demo

## requirements

- pyenv
- pipenv

## usage

### setup dependencies

```shell
pipenv install
```

### try converting local json file

```shell
pipenv run python main.py
```

### try converting with `__post_init__()`

```shell
pipenv run python post_init_example.py
```

### try running server

```shell
pipenv run python server.py

# try request
curl http://127.0.0.1:5042/connpass/titles

# try request with search query
curl http://127.0.0.1:5042/connpass/titles\?series_id\=3109
```

[APIリファレンス - connpass](https://connpass.com/about/api/)
