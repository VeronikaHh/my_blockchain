import json
from typing import Any

from hash import Hash


class Transaction:
    def __init__(self, transaction_id, set_of_operations, nonce):
        self.transaction_id = transaction_id
        self.set_of_operations = set_of_operations
        self.nonce = nonce

    def __dict__(self):
        return {
            "transaction_id": self.transaction_id,
            "set_of_operations": [
                operation.__dict__() for operation in self.set_of_operations
            ],
            "nonce": self.nonce
        }

    @classmethod
    def create_transaction(cls, operations: list, nonce):
        operations_serializable = [
            operation.__dict__() for operation in operations
        ]
        transaction_data = {
            "set_of_operations": operations_serializable,
            "nonce": nonce
        }
        transaction_id = cls.__calculate_transaction_id(transaction_data)
        return cls(transaction_id, operations, nonce)

    @staticmethod
    def __calculate_transaction_id(transaction_data: dict[str, Any]) -> str:
        transaction_string = json.dumps(transaction_data, sort_keys=True)
        return Hash.calculate(message=transaction_string)
    
    
