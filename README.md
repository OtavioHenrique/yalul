![Yalul logo](img/logo_final.png)

## How to run

### Linux Systems / Mac os

#### Install the lib requeriments

```
pip install -r requirements.txt
```

#### Run

Just go to yalul root folder and run:

```bash
PYTHONPATH=$PATHONPATH:`pwd` bin/yalul
```

Example passing a file

```bash
PYTHONPATH=$PATHONPATH:`pwd` bin/yalul yalul_test.yalul
```

### Docker

#### build image

```
docker build . -t yalul
```

#### Running

```
docker run -v "$PWD":/usr/src/app -w /usr/src/app yalul bin/yalul
```

### Windows

#### Install package requeriments(Go yo your cmd):

```
pip install -r requirements.txt
```

#### Add Yalul to your PYTHONPATH

Access:

```
My Computer > Properties > Advanced System Settings > Environment Variables
```

Create a new environment variable with name `PYTHONPATH` and select yalul directory.

#### Run

Open CMD, go yo your yalul folder and run:

```
python bin\yalul
```

## Render AST

Yalul has a built-it tool to render its AST, available out of box. To use just use the flag `--render-ast` while executing a file. 

### Example

Considering the a file named `yalul_test.yalul` containing the fallowing code:


```javascript
func sum(a b) {
  return a + b
}
```

Run `bin/yalul --render-ast yalul_test.yalul` (Unix example), and the fallowing image will be generated:

![image](https://user-images.githubusercontent.com/11178512/111231612-57ec7600-85c8-11eb-9528-4c6a0e47dcba.png)
