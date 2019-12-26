To spin up a container run command
```bash
docker-compose up -d
```

```bash
docker-compose build
docker-compose run app /bin/sh
docker-compose run node /bin/sh
```

To fix issues with access rights between host machine user and container user run 
```bash
docker-compose run -u $(id -u ${USER}):$(id -g ${USER}) graphql /bin/bash
```