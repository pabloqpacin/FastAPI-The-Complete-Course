# FastAPI 101

> [!NOTE]
> https://www.udemy.com/course/fastapi-the-complete-course


~~Course and code created by: Eric Roby~~

> [!IMPORTANT]  
> Desarrollo en [./CURSO.md](/CURSO.md)


---

> [!CAUTION]
> Estas instrucciones va a haber que adaptarlas para Docker y tal

1. [...] Navigate to the file that have `requirements.txt` in it.
2. In terminal type `pip install -r requirements.txt`
3. This will download all dependencies to your machine!

---

ojo, parece que lo de *Note* *Important* *Caution* etc. no funciona dentro de `<details></details>`

<details>


> [!CAUTION]
> Prueba


</details>


---


## CUSTOM ([./03-foo/](#))

> [!IMPORTANT]
> La idea es que sea válido para los [proyectos de Setenova](https://github.com/orgs/setenova/repositories)

### Dockerizar app (Dockerfile + docker-compose.yaml)

#### Tema BD

> db mysql - https://github.com/pabloqpacin/proyecto_lemp_compose/blob/main/compose.yaml


### Kubernetizar app (Helm Chart)
### CICD (~~test,~~ build & push)


----

<!-- 
### STYLE for IMPORTS
1. Stanadard Library: built-in modules (eg. os,sys, typing)
2. Third-party imports: libraries installed with pip etc. (eg. fastapi, pydantic, sqlalchemy, passlib)
3. Local applications: our own modules and files (eg. database, models)
 -->

<!-- 
---

OJO [JWT Lab](https://jwt.io/) and [jwt-cli](https://github.com/mike-engel/jwt-cli) ~~and [jwt-ui](https://github.com/jwt-rs/jwt-ui)~~

#### jwt-cli

```bash
cargo info jwt-cli
  #     Updating crates.io index
  #   Downloaded jwt-cli v6.1.1
  #   Downloaded 1 crate (40.9 KB) in 0.73s
  # jwt-cli
  # A super fast CLI tool to decode and encode JWTs built in Rust
  # version: 6.1.1
  # license: MIT
  # rust-version: unknown
  # documentation: https://docs.rs/jwt-cli/6.1.1
  # repository: https://github.com/mike-engel/jwt-cli
  # crates.io: https://crates.io/crates/jwt-cli/6.1.1

rustup update
cargo install jwt-cli
```
```bash
jwt encode foo
jwt decode bar
```
 -->


