import time
import hashlib
import json


class Block:
    """
        Class to represent a block.

        ...

        Attributes
        ----------
        index : int
            ...
        proof : int
            ...
        prev : int
            ...
        data: dict
            ...
        nonce: int
            ...
        timestamp: str
            ...


        Methods
        -------
        hash():
            ...
        """

    def __init__(self, index, proof, prev, data, nonce, timestamp=time.time()):
        """
       Constructs attributes for pre-hashed block.

       Parameters
       ----------
        index : int
        ...
        proof : int
            ...
        prev : int
            ...
        data: dict
            ...
        nonce: int
            ...
        timestamp: str
            ...
       """
        self.__block = {'index': index, 'proof': proof, 'prev': prev,
                        'data': data, 'nonce': nonce, 'timestamp': timestamp}

    @property
    def hash(self):
        """Get or set, or delete the hash. Setting Block.hash = True will hash the value"""
        return self.__block

    @hash.setter
    def hash(self, state):
        if state:
            self.__block = hashlib.blake2b(str(json.dumps(self.__block, sort_keys=True)).encode('utf-8')).hexdigest()

    @hash.deleter
    def hash(self):
        del self.__block

    def __repr__(self):
        return f"{self.__dict__}"
