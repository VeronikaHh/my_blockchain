from account import Account
from block import Block
from blockchain import Blockchain
from operation import Operation
from transaction import Transaction

import time

# import utils

if __name__ == "__main__":

    # 3) Create Blockchain
    blockchain = Blockchain()
    # 1) Create Account for user1 and user2
    # TODO: You can create a separate function for account creation,
    #  which will receive as parameter just initial amount of money
    user1 = Account()
    user1.add_key_pair_to_wallet()
    user1.update_balance(amount=1000)
    # user1 = utils.create_user(1000)

    # TODO: This also to account create function
    user2 = Account()
    user2.add_key_pair_to_wallet()
    user2.update_balance(amount=400)

    # user2 = utils.create_user(400)

    # 2) Create Operations op1, op2, op3
    # TODO: Create function which is called "create_operation()" and fill with below steps
    #  will receive operation message, op_key_index and amount as parameters
    operations_list = []

    op1_message = "Operation user1 to user2, for 100"
    op1_key_index = 0
    op1_amount = 100

    op1 = Operation.create_operation(
        sender=user1,
        receiver=user2,
        amount=op1_amount,
        signature=user1.sign_data(message=op1_message, key_index=op1_key_index)
    )

    # TODO: Also here we need separate function for verify operation
    if op1.verify_operation(message=op1_message, key_index=op1_key_index):
        user1.update_balance(-op1_amount)
        user2.update_balance(+op1_amount)
        operations_list.append(op1)
        print(f"Added valid operation [{op1.id}] to operations list.")
    else:
        print(f"Operation [{op1.id}] is not valid!")

    user1.print_balance()
    user2.print_balance()

    # TODO: This all again should be in create operation function
    op2_message = "Operation user2 to user1, for 700"
    op2_key_index = 0
    op2_amount = 700

    op2 = Operation.create_operation(
        sender=user2,
        receiver=user1,
        amount=op2_amount,
        signature=user2.sign_data(message=op2_message, key_index=op2_key_index)
    )

    # TODO: This in verify operation
    if op2.verify_operation(message=op2_message, key_index=op2_key_index):
        user2.update_balance(-op2_amount)
        user1.update_balance(+op2_amount)
        operations_list.append(op2)
        print(f"Added valid operation [{op2.id}] to operations list.")
    else:
        print(f"Operation [{op2.id}] is not valid!")

    user1.print_balance()
    user2.print_balance()

    # TODO: This as well in create operation
    op3_message = "Operation user2 to user1, for 450"
    op3_key_index = 0
    op3_amount = 450

    op3 = Operation.create_operation(
        sender=user2,
        receiver=user1,
        amount=op3_amount,
        signature=user2.sign_data(message=op3_message, key_index=op3_key_index)
    )

    # TODO: This in verify operation
    if op3.verify_operation(message=op3_message, key_index=op3_key_index):
        user2.update_balance(-op3_amount)
        user1.update_balance(+op3_amount)
        operations_list.append(op3)
        print(f"Added valid operation [{op3.id}] to operations list.")
    else:
        print(f"Operation [{op3.id}] is not valid!")

    user1.print_balance()
    user2.print_balance()

    # 4) Create Transaction
    transactions_list = []
    transaction = Transaction.create_transaction(operations=operations_list, nonce=100)
    transactions_list.append(transaction)

    # 5) Create Block
    block1 = Block.create_block(transactions=transactions_list, prev_block_hash="0")
    blockchain.validate_block(block1)

    block2 = Block.create_block(transactions=[],prev_block_hash=block1.block_id)
    blockchain.validate_block(block2)

    block3 = Block.create_block(transactions=[],prev_block_hash=block2.block_id)
    blockchain.validate_block(block3)

    block4 = Block.create_block(transactions=[],prev_block_hash=block3.block_id)
    blockchain.validate_block(block4)

    print(str(block1))
    print(str(block2))
    print(str(block3))
    print(str(block4))
    print(str(blockchain))


