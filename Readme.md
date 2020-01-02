To spin up a container run command
```bash
docker-compose build
docker-compose up -d
```

http://0.0.0.0:5001/graphql/

To run command inside container
```bash
docker-compose run app /bin/sh
docker-compose run node /bin/sh
```

To avoid possible issues with access rights between host machine user and container user run 
```bash
docker-compose run -u $(id -u ${USER}):$(id -g ${USER}) graphql /bin/bash
```

#### Create user mutation example:
```graphql endpoint
mutation{
  createUser(email:"test@mail.de",username:"Telman", password:"secret"){    
    user{
      id
      email
      dateJoined
    }
  }
}
```

#### Get token mutation example:
```graphql endpoint
mutation{
tokenAuth(username:"Telman",password:"secret"){
  token
}
}
```

