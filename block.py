import json

from datetime import datetime
from hash import Hash


class Block:
    def __init__(self, block_id, prev_hash, set_of_transactions, timestamp) -> None:
        self.block_id = block_id
        self.prev_hash = prev_hash
        self.set_of_transactions = set_of_transactions
        self.timestamp = timestamp # changed time lib ti date lib
        # self.hash = Hash.calculate(self.to_string())

    def __str__(self) -> str:
        return f"\n Block id: {self.block_id},\n previous hash: {self.prev_hash},\n set of transaction:\n {self.get_serializable_transactions(self.set_of_transactions)}\n timestamp: {self.timestamp}\n" 

    @staticmethod
    def get_serializable_transactions(transactions: list) -> list:
        return [
            transaction.__dict__() for transaction in transactions
        ]
        
    @classmethod
    def create_block(cls, transactions: list, prev_block_hash: str):
        transactions_serializable = cls.get_serializable_transactions(transactions)
        creation_timestamp = datetime.now()
        block_id = cls.__calculate_block_id(transaction_data=transactions_serializable, timestamp = creation_timestamp, prev_hash=prev_block_hash)
        new_block = Block(
            block_id=block_id,
            prev_hash=prev_block_hash,
            set_of_transactions=transactions,
            timestamp = creation_timestamp
        )
        return new_block

    def __calculate_block_id(transaction_data: list, timestamp: datetime, prev_hash: str) -> str:
        transaction_string = json.dumps(transaction_data, sort_keys=True) + str(timestamp) + str(prev_hash)
        return Hash.calculate(message=transaction_string)
