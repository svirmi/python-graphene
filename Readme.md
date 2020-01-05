### [WIP]
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
#### CreateTrack mutation example (auth token required to successfully run this mutation):
```graphql endpoint
mutation{
  createTrack(
    title:"New linked track",
    description:"Description of the new track",
    url:"https://mytrack1243.de",
  ){
    track{
      id
      title
    }
  }
}
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

#### Get auth token mutation example:
```graphql endpoint
mutation{
tokenAuth(username:"Telman",password:"secret"){
  token
}
}
```

