from flask import Flask

app = Flask(__name__)

print("pr3")

@app.route('/')

def print_item(box, itemname):
    print(f'There is a price of {itemname}: ')
    return(f"{box[itemname]}")

def add_bread(box):
    itemname = 'bread'
    itemvalue = 10
    box[itemname] = itemvalue
    return(f'{box}')

def print_basket_len(box):
    return(f'{len(box)}')

def print_basket(box):
    return(f"{box}")


box = {'potato': 20, 'meat':70, 'cheese':35, 'tea':16}

print_basket(box)
print_basket_len(box)
add_bread(box)
print_item(box, 'meat')

if __name__ == '__main__':
    app.run(debug=True)