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

*You can add your folder path to your `PYTHONPATH` instead of set it everytime.*
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

## Render Lex Tokens

Yalul has a buil-in tool to render its lex tokens generated by our code. Just use the flag `--render-lex-tokens`.

### Example

Considering the file named `yalul_test.yalul` containing the fallowing code:

```javascript
1 + 1
```

Run `bin/yalul --render-lex-tokens yalul_test.yalul` (Unix example), and the fallowing image will be generated:

![image](https://user-images.githubusercontent.com/11178512/111235466-77d36800-85cf-11eb-969b-b2027c5bfc78.png)


All generated images will be placed inside `yalul-renders/` folder that it will create as `pdf` files.

**Pay attention, this tool need [graphviz](https://graphviz.org/) installed, you need to install it to use. You can find the install instructions [here](https://graphviz.org/download/). Graphviz are known to have PATH problems on windows, if you are using it, manually add it to yourrr PATH.**

## Render AST

Yalul has a built-in tool to render its AST, available out of box. To use just use the flag `--render-ast` while executing a file. 

### Example

Considering the a file named `yalul_test.yalul` containing the fallowing code:


```javascript
func sum(a b) {
  return a + b
}
```

Run `bin/yalul --render-ast yalul_test.yalul` (Unix example), and the fallowing image will be generated:

![image](https://user-images.githubusercontent.com/11178512/111231612-57ec7600-85c8-11eb-9528-4c6a0e47dcba.png)

All generated images will be placed inside `yalul-renders/` folder that it will create as `pdf` files.

**Pay attention, this tool need [graphviz](https://graphviz.org/) installed, you need to install it to use. You can find the install instructions [here](https://graphviz.org/download/). Graphviz are known to have PATH problems on windows, if you are using it, manually add it to yourrr PATH.**

## Tests

Yalul uses `pytest` as its test framework. To run it, just type:

```
PYTHONPATH=$PATHONPATH:`pwd` pytest
```
