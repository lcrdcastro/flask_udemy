from flask import Flask, request

app = Flask(__name__)

stores = [
    {
        'name':'dreambmx',
        'items':[
                    {   'name': 'handlebar',
                        'price': 200
                    }
                ]
    }
]


@app.get("/stores")
def get_data():
    return {'stores': stores}


@app.get("/store/<string:name>")
def get_data_store(name):
    for store in stores:
        if store['name']==name:
            return {'store': store}
    return {'message': 'Store not found'}, 404


@app.get("/store/<string:name>/items")
def get_data_items(name):
    for store in stores:
        if store['name']==name:
            return {'items': store['items']}
    return {'message': 'Store not found'}, 404


@app.post('/store/<string:name>/item')
def create_item(name):
    data = request.get_json()
    for store in stores:
        if name == store['name']:
            new_item = {'name': data['name'], 'price': data['price']}
            store['items'].append(new_item)
            return new_item,201
    return {'message': 'Store not found'}, 404


@app.post("/store")
def create_store():
    data = request.get_json()
    new_store = {'name':data['name'], 'items':[]}
    stores.append(new_store)
    return new_store, 201


#if __name__=='__main__':
#    app.run()
