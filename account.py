import uuid
from typing import Any

from key_pair import KeyPair
from signature import Signature
from blockchain import Blockchain


class Account:
    def __init__(self) -> None:
        self.account_id: str = str(uuid.uuid4())
        self.wallet: list = []
        self.balance: float = 0

    def add_key_pair_to_wallet(self) -> None:
        key_pair = KeyPair.generate_key_pair()
        self.wallet.append(key_pair)

    def update_balance(self, amount: int | float) -> None:
        self.balance += amount

    def create_payment_op(self, recipient_account, amount: int | float, key_index: int) -> dict[str, Any]:
        if key_index < 0 or key_index >= len(self.wallet):
            raise ValueError("Invalid key index")

        sender_key = self.wallet[key_index]
        recipient_key = recipient_account.wallet[0]

        payment_op = {
            'sender_public_key': sender_key.public_key,
            'recipient_public_key': recipient_key.public_key,
            'amount': amount
        }

        return payment_op

    def get_balance(self) -> float:
        return self.balance

    def print_balance(self) -> None:
        print(f"Balance for account {self.account_id}: {self.balance} coins")

    def sign_data(self, message: Any, key_index: int) -> bytes:
        if key_index < 0 or key_index >= len(self.wallet):
            raise ValueError("Invalid key index")

        key_pair = self.wallet[key_index]
        signature = Signature.sign_message(private_key=key_pair.private_key, message=message)

        return signature
