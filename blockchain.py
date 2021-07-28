from block import Block
from random import random
import hashlib


class BlockChain:
    def __init__(self):
        self.chain = []
        self.current_data = []
        self.nodes = set()
        self.genesis()
        self.nonce = ...

    def genesis(self):
        self.block(proof=0, prev=0)

    def block(self, proof, prev):
        block = Block(
            index=len(self.chain),
            proof=proof,
            prev=prev,
            data=self.current_data,
            nonce=...
        )
        self.current_data = []
        self.chain.append(block)
        return block

   