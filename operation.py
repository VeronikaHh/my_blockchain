import uuid

from signature import Signature


class Operation:
    def __init__(self, sender, receiver, amount: int | float, signature: bytes) -> None:
        self.id = str(uuid.uuid4())
        self.sender = sender
        self.receiver = receiver
        self.amount = amount
        self.signature = signature

    def __dict__(self) -> dict:
        return {
            "id": self.id,
            "sender": self.sender.account_id,
            "receiver": self.receiver.account_id,
            "amount": self.amount
        }

    @staticmethod
    def create_operation(sender, receiver, amount, signature):
        return Operation(sender, receiver, amount, signature)

    def verify_operation(self, message: str, key_index: int) -> bool:
        if self.amount <= 0:
            print("[Error] Invalid amount for the operation.")
            return False

        if not self.__check_balance():
            print("[Error] Insufficient balance for the sender.")
            return False

        if not self.__verify_signature(message=message, key_index=key_index):
            print("[Error] Invalid signature.")
            return False

        print("[Info] Operation verified successfully.")
        return True

    def __check_balance(self) -> bool:
        return self.sender.balance >= self.amount

    def __verify_signature(self, message: str, key_index: int) -> bool:
        return Signature.verify_signature(
            public_key=self.sender.wallet[key_index].public_key,
            message=message,
            signature=self.signature
        )
