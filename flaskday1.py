from flask import Flask,render_template

from functools import reduce 
app=Flask(__name__)

@app.route('/')     #url修饰器
def hello() -> str:
    return 'hello world from Flask'



@app.route('/hi')
def readfile(filename):
    with open(filename,'r',encoding='utf-8')as files:
        content = reduce(lambda x,y:x+y,files.readlines())
        return content
    return 'content'   

app.run()    