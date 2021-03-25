![Yalul logo](img/logo_final.png)

Yalul born with purpose of bring be simple and have a fun while studying programming languages.

This is not a language for production systems, but a language to help everyone that wants to learn how a programming language works behind scenes in a fun way.

## Table of Contents

- [Development Status](#development-status-v1)
- [Syntax](#syntax)
    * [print](#print)
    * [basic types](#basic-types)
    * [Arithmetic and Comparison](#arithmetic-and-comparison)
    * [Variables](#variables)
    * [Loop](#loop)
    * [Control Flow](#control-flow)
    * [Functions](#functions)
- [Installing](#installing)
    * [Linux/Mac](#linux-systems-and-mac-os)
      + [Install lib requirements](#install-lib-requirements)
      + [Running](#running)
    * [Docker](#docker)
    * [Windows](#windows)
- [Development Tools](#development-tools)
  * [REPL](#repl-everybody-loves-repl)
  * [Render AST](#render-ast)
  * [Render Lex Tokens](#render-lex-tokens)
- [Developing](#developing)
  * [Tests](#tests)
  * [Lint](#lint)

## Development Status V1

[x] Basic structure

[x] Lexer

[x] Parser

[x] Tokens/AST Printers

[x] Interpreter

[] Documentation (WIP)

## Syntax

### Print

Yalul has a built-in print statement to help you while developing:

```javascript
print("Hello Yalul")
```

### Basic types

Yalul has five basic value types, `boolean`, `float`, `integer`, `null`, and `string`:

#### Integers

The most basic data type, integer represent any integer number:

```javascript
Yalul v0.0.1 > 42
=> 42
```

#### Float

Floats are floating point numbers, using dots:

```javascript
Yalul v0.0.1 > 3.18
=> 3.18
```

#### String

Strings represents any text, and on Yalul strings are represented around ONLY double quotes:

```javascript
Yalul v0.0.1 > "Hello World" 
=> "Hello World"
```

#### Booleans

Booleans as you may imagine, represents `true` and `false`:

```javascript
Yalul v0.0.1 > true
=> true
Yalul v0.0.1 > false
=> false
```

#### Null

And unfortunately Yalul has its dark side (among many others), yes we have Null types to represent the absence of any information.

```javascript
Yalul v0.0.1 > null
=> null
```

### Arithmetic and Comparison

Yalul has basic math operations `+`, `-`, `*` and `/`. It has basic comparison operators too, `>`, `<`, `<=`, `>=`, `==`:

```javascript
Yalul v0.0.1 > 1 + 1
=> 2
Yalul v0.0.1 > 1 - 1
=> 0
Yalul v0.0.1 > 2 * 2
=> 4
Yalul v0.0.1 > 4 / 2
=> 2.0
Yalul v0.0.1 > 2 > 1
=> true
Yalul v0.0.1 > 2 < 1
=> false
Yalul v0.0.1 > 1 <= 1
=> true
Yalul v0.0.1 > 1 >= 1
=> true
Yalul v0.0.1 > 1 == 1
=> true
```

### Variables

To declare your variable its easy, just use `def` keyword, pass a name and any expression as value.

```
def name = "otavio"
```

And feel free to redefine your variable:

```
name = "Valadares"
```

### Loop

To loop yalul have a while statement, that will execute a given block till the given condition is true:

```javascript
def counter = 0

while(counter < 10) {
  print(counter)
  counter = counter + 1
}
```

### Control Flow

To control your flow, yalul provides a basic if/else structure:

```javascript
if (42 > 41) {
  print("If block")
} else {
  print("Else block")
}
```

### Functions

To create functions and call it its easy too, yalul provides a nice syntax for it:

```javascript

func sum(a b) {
  return a + b
}

def result = sum(41, 1)

print(result)
```

## Installing

### Linux Systems and Mac os

Clone yalul repository:

```
git clone https://github.com/OtavioHenrique/yalul.git
```

#### Install lib requirements

```
pip install -r requirements.txt
```

#### Running

Go to yalul root folder and run:

```bash
PYTHONPATH=$PATHONPATH:`pwd` bin/yalul
```

Example passing a file

```bash
PYTHONPATH=$PATHONPATH:`pwd` bin/yalul yalul_test.yalul
```

*You can add your folder path to your `PYTHONPATH` instead of set it everytime.*
### Docker

Clone yalul repository:

```
git clone https://github.com/OtavioHenrique/yalul.git
```

#### build image

Run

```
docker build . -t yalul
```

#### Running

```
docker run -v "$PWD":/usr/src/app -w /usr/src/app yalul bin/yalul
```

Example passing a file

```bash
docker run -v "$PWD":/usr/src/app -w /usr/src/app yalul bin/yalul yalul_test.yalul
```

### Windows

Clone yalul repository:

```
git clone https://github.com/OtavioHenrique/yalul.git
```

#### Install package requeriments(Go to your cmd):

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

Example passing a file

```bash
python bin\yalul yalul_test.yalul
```

## Development Tools

### REPL (Everybody loves REPL)

Yalul REPL is simple and intuitive, just start it without passing any file as argument, and REPL will start:

![image](https://user-images.githubusercontent.com/11178512/111860263-3a4f4180-8925-11eb-84ad-07ace41e7f32.png)


### Render Lex Tokens

Yalul has a buil-in tool to render its lex tokens generated by our code. Just use the flag `--render-lex-tokens`.

#### Example

Considering the file named `yalul_test.yalul` containing the fallowing code:

```javascript
1 + 1
```

Run `bin/yalul --render-lex-tokens yalul_test.yalul` (Unix example), and the fallowing image will be generated:

![image](https://user-images.githubusercontent.com/11178512/111235466-77d36800-85cf-11eb-969b-b2027c5bfc78.png)


All generated images will be placed inside `yalul-renders/` folder that it will create as `pdf` files.

**Pay attention, this tool need [graphviz](https://graphviz.org/) installed, you need to install it to use. You can find the install instructions [here](https://graphviz.org/download/). Graphviz are known to have PATH problems on windows, if you are using it, manually add it to yourrr PATH.**

### Render AST

Yalul has a built-in tool to render its AST, available out of box. To use just use the flag `--render-ast` while executing a file. 

#### Example

Considering the a file named `yalul_test.yalul` containing the fallowing code:


```javascript
func sum(a b) {
  return a + b
}
```

Run `bin/yalul --render-ast yalul_test.yalul` (Unix example), and the fallowing image will be generated:

![image](https://user-images.githubusercontent.com/11178512/111708367-7c448e80-8824-11eb-8c3d-68cb70a26f5a.png)


All generated images will be placed inside `yalul-renders/` folder that it will create as `pdf` files.

**Pay attention, this tool need [graphviz](https://graphviz.org/) installed, you need to install it to use. You can find the install instructions [here](https://graphviz.org/download/). Graphviz are known to have PATH problems on windows, if you are using it, manually add it to yourrr PATH.**

## Developing

### Tests

Yalul uses `pytest` as its test framework. To run it, just type:

```shell
PYTHONPATH=$PATHONPATH:`pwd` pytest
```

### Lint

Yalul uses `flake8` as python linter. By default we run the fallowing line while developing:

```shell
flake8 . --count --exit-zero --max-complexity=10 --max-line-length=127 --statistics
```
