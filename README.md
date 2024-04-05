# FastAPI Beanie Base Project

# Development Environment Set Up

## Start project local
### Clone Project to your local environment
```bash
  git clone git@github.com:NikaMdinaradze/fastapi-beanie-base.git
```

## Run project using docker-compose
#### Build and start containers
Build images and start containers. Migration command will be run during startup.
```bash
  make build
  make run
```

#### Working with running container
* When container is running
```bash
  docker-compose exec api <your_command>
```
* Without running container
```bash
  docker-compose run --rm api <your_command>
```

### Installation pre-commit

```bash
  make install_pre_commit
```

### Unit tests
Run tests
```bash
  make run_tests
```