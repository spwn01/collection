import register_paths
from main import Collection

test_collection = Collection()
test_collection.set('user1', {'id': 1, 'language': 'en'})
test_collection.set('user2', {'id': 2, 'language': 'uk'})

# Gets the value of the key 'user1', since it exists in test_collection.
def ensure_existing():
    return test_collection.ensure('user1')

# Creates the value for the key 'user3', since it doesn't exist in test_collection.
def ensure_not_existing():
    # Generates value based on the key if it doesn't exist in test_collection
    def value_generator(key: str):
        user_id = key.split('user')[1]
        return { 'id': user_id, 'language': 'en' }
    return test_collection.ensure('user3', value_generator)
