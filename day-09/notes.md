from fastapi import FastAPI
#from library import class

app= FastAPI()
#object=Class


#CREATING FIRST END-POINT:
@app.get('/')
def index():
    return {'message':'Hello, FastAPI!'}



#@name of app.method(endpoint)
#followed by function
#return in the form of dictionary(json)