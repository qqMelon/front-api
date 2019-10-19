# Doc api

## Les urls

### can_connect/

Point d'api servant à tester la connection entre le front et le back

* url : http://127.0.0.1:8000/api/can_connect/
* method : get

Retour possible :

    * Connection établie :
        * code 200

    * Connection non établie :
        * failed to connect url...

ex :
```bash
$ curl http://127.0.0.1:8000/api/can_connect/
```

___

### login/

Point d'api servant à la connection d'un user

* url : http://127.0.0.1:8000/login/
* method : post
* formdata : { "username": "...", "password": "..." }

Retour possible :

    * username et password valides :
        * code 200
        * tokens jwt d'authentifications dans les cookies
        * response: {'login': 'true' }

    * username ou password invalides ou manquant :
        * code 404

ex :
```bash
$ curl -X POST --data "username=admin&password=adminadmin" http://127.0.0.1:8000/login/

{"login":true}
```

___

### api/token/

Point d'api servant à récupérer les token jwt d'authentification

* url: http://127.0.0.1:8000/api/token/
* method : get
* formdata : { "username": "...", "password": "..." }

Retour possible :

    * username et password valides :
        * code 200
        * response: {'refresh': '...', 'access': '...' }

    * username ou password invalides ou manquant :
        * code 401
        * response: {"detail":"No active account found with the given credentials"}%

ex :
```bash
$ curl -X POST -d "username=admin&password=adminadmin" http://localhost:8000/api/token/

{
    "refresh": "<refresh_token>",
    "access": "<valid_token>"
}
```

___

### api/token/refresh/

Point d'api servant a renouveller le token d'authentification grace au refresh token

* url: http://127.0.0.1:8000/api/token/refresh/
* method: get
* formdata: {"token": "<valid_token>"}

Retour possible :

    * token valide :
        * code 200
        * response: {'access': '<valid_token>' }

    * token invalide :
        * code 401
        * response: {"detail":"Token is invalid or expired","code":"token_not_valid"}%

ex :
```bash
$ curl -X POST -H "Content-Type: application/json" -d '{"refresh":"<valid_token>"}' http://localhost:8000/api/token/refresh/

{"access": "..."}
```

___

### api/unicorns/

Point d'api servant à récupérer la liste de toutes les licornes en base

* url: http://127.0.0.1:8000/api/unicorns/
* method: get

Retour possible :

    * code 200
    * response: {
        'id': '1', 'name': '...', 'model': '...' ...,
        'id': '2', 'name': '...', 'model': '...' ...,
    }

ex :
```bash
$ curl http://127.0.0.1:8000/api/unicorns/

{
    'id': '1', 'name': '...', 'model': '...' ...,
    'id': '2', 'name': '...', 'model': '...' ...,
}
```

___

### api/unicorns/<id>/

/!\ Nécessite d'être logué
Point d'api servant à récupérer le détail d'une licorne en base selon son id

* url: http://127.0.0.1:8000/api/unicorns/<id>/
* method: get
* header: "Authorization: Bearer <valid_token>"

Retour possible :

    * username et password valides :
        * code 200
        * response: {
            'id': '1', 'name': '...', 'model': '...' ...,
            'id': '2', 'name': '...', 'model': '...' ...,
        }
    * token invalide :
        * code 401
        * response: { "detail":"Given token not valid for any token type", ... }

ex :
```bash
curl -H "Authorization: Bearer <valid_token>" http://localhost:8000/api/unicorns/1/

{ 'id': '1', 'name': '...', 'model': '...' ..., }
```
