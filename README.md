# star-wars-api-etl

## Getting the CSV

We can run it directly using python, i.e. using the following command

```
python3 main.py
```

Or we can use docker.

### Build docker file

```
docker build -t swae -f Dockerfile .
```

### Run docker file

This command leaves at the local data folder a CSV with the expected result. 

```
docker run --name swae -v $PWD/data:/usr/src/app/data --rm swae
```

## Test

```
pytest test.py
```

### Build docker for testing

```
docker build -t swae_test -f DockerfileTest .
```

### Run docker for testing

```
docker run --name swae_test --rm swae_test
```
