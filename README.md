mongodelta
====
The mongodelta is encoder and decoder for handling datetime.timedelta object with MongoDB.

## Description
The mongodelta is an encoder and decoder for processing datetime.timedelta objects in MongoDB.
As you know MongoDB cannot handle datetime.timedelta objects. It was better to use the SON Manipulator as a way to format arbitrary data and store it in MongoDB, but this method is now deprecated and the Son Manipulators will be removed in PyMongo 4.0([son_manipulator](https://api.mongodb.com/python/current/api/pymongo/son_manipulator.html)). Therefore, it is currently necessary to encode the data before storing it in MongoDB and to decode it when reading the data.
The mongodelta processes lists, tuples and dictionaries recursively and replaces the dictionary containing datetime.timedelta objects as values with {'mongodelta': datetime.timedelta.total_seconds ()}.
Please let me know if there is a smarter way.

## Install
`$ pip install git+https://github.com/tombo-gokuraku/mongodelta`

## Usage
```python
import mongodelta
from pymongo import MongoClient
from pprint import pprint

client = MongoClient('mongodb://localhost:27017/')
db = client['test']

item = {'hoge_timedelta': datetime.timedelta(days=1)}
encorded_item = mongodelta.timedelta_encoder(item)
pprint(encorded_item)
#{'hoge_timedelta': {'mongodelta': 86400.0}}
db.items.insert_one(encorded_item)

decorded_item = mongodelta.timedelta_decoder(db.items.find_one())
pprint(decorded_item)
#{'_id': ObjectId('5cef49e68586b0517885415f'),'hoge_timedelta': datetime.timedelta(1)}
```

## Licence

[MIT](https://github.com/tombo-gokuraku/mongodelta/blob/master/LICENSE)

## Author

[tombo-gokuraku](https://github.com/tombo-gokuraku)
