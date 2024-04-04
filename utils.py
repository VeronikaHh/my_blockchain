# from account import Account
# from block import Block
# from blockchain import Blockchain
# from operation import Operation
# from transaction import Transaction

# def create_user(amount: float) -> Account:
#     user = Account()
#     user.add_key_pair_to_wallet()
#     user.update_balance(amount=amount)

# def create_operation(massege: str, key_index: int, amount: float) -> Operation:
#     ...

# def process_operation(operation: Operation):
#     if operation.verify_operation(message=op3_message, key_index=op3_key_index):
#         operation.sender.update_balance(-operation.amount)
#         operation.receiver.update_balance(+operation.amount)
#         print(f"Added valid operation [{operation.id}] to operations list.")
#         return operation
#     else:
#         print(f"Operation [{operation.id}] is not valid!")
        
