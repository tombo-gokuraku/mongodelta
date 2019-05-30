import datetime
import copy

    
def timedelta_to_mongodelta(timedelta):
    return {'mongodelta':timedelta.total_seconds()}
    
def mongodelta_to_timedelta(document):
    assert 'mongodelta' in document
    return datetime.timedelta(seconds=document['mongodelta'])

def timedelta_encoder(collection):
    tmp = copy.deepcopy(collection)
    return inner_encoder(tmp)

def inner_encoder(collection):
    if isinstance(collection,dict):
        for key, value in collection.items():
            if(isinstance(value,dict) or
               isinstance(value,list) or
               isinstance(value,tuple)):
                collection[key] = inner_encoder(value)
            elif isinstance(value,type(datetime.timedelta())):
                collection[key] = timedelta_to_mongodelta(value)
    elif isinstance(collection,list) or isinstance(collection,tuple):
        for item in collection:
            inner_encoder(item)
    return collection 

def timedelta_decoder(collection):
    tmp = copy.deepcopy(collection)
    return inner_decoder(tmp)

def inner_decoder(collection):
    if isinstance(collection,dict):
        for key, value in collection.items():
            if isinstance(value,dict):
                if 'mongodelta' in value:
                    collection[key] = mongodelta_to_timedelta(value)
                else:
                    collection[key] = inner_decoder(value)
    elif isinstance(collection,list) or isinstance(collection,tuple):
        for item in collection:
            inner_decoder(item)
    return collection
