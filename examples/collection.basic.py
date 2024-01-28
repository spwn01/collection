import examples.register_paths as register_paths
from main import Collection

# You can create an empty collection, and insert data later.
empty_collection = Collection()
# Or you can insert data just from initializing.
test_collection = Collection(
    {'user1': {'id': 1, 'language': 'en'}},
    {'user2': {'id': 2, 'language': 'uk'}})

# You can insert data into collection using set() function.
empty_collection.set('user3', {'id': 1, 'language': 'en'})
empty_collection.set('user4', 'uk')
#! The data you pass can be anything

# You can get the value from collection using unique key.
def get_existing():
    result = empty_collection.get('user4')
    print(result)
# If the key doesn't exist in collection, it will return None.
def get_not_existing():
    result = empty_collection.get('user1')
    print(result)

# You can check, whether collection has the key or not.
# If it has, it will return True, otherwise False
def has_existing():
    result = test_collection.has('user1')
    print(result)
def has_not_existing():
    result = test_collection.has('user5')
    print(result)

# If you want to measure the entire collection, you can use len() method.
def measure():
    result = len(test_collection)
    print(result)

# You can pring all the data inside the collection
def show():
    print(test_collection)