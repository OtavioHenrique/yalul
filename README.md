![Yalul logo](img/logo_final.png)

## How to run

### Linux Systems

Just go to yalul root folder and run:

```bash
PYTHONPATH=$PATHONPATH:`pwd` bin/yalul
```

Example passing a file

```bash
PYTHONPATH=$PATHONPATH:`pwd` bin/yalul yalul_test.yalul
```

### Docker

Just build image

```
docker build . -t yalul
```

Running:

```
docker run -v "$PWD":/usr/src/app -w /usr/src/app yalul bin/yalul yalul_test.yalul
```