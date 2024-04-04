from block import Block
from datetime import datetime

class Blockchain:
    def __init__(self):
        self.coin_database = {}  # Обліковий запис -> Баланс
        self.block_history = []  # Масив блоків
        self.tx_database = []  # Масив транзакцій
        self.faucet_coins = 1000  # Початкова кількість тестових монет

        self.init_blockchain()

    def init_blockchain(self):
        genesis_block = self.__create_genesis_block()
        self.block_history.append(genesis_block)

    def __str__(self) -> str:
        return f"\n IDs of blocks:\n{self.get_blocks_id()},\n Transaction history: {self.tx_database}"
    
    def get_blocks_id(self):
        return [block.block_id for block in self.block_history]
    
    # need implementation
    def update_coin_database(self, account_id: str, amount: float) -> None:
        self.coin_database[account_id] = amount

    @staticmethod
    def __create_genesis_block():
        genesis_block = Block(block_id="0", prev_hash="0", set_of_transactions=[], timestamp=datetime.now())  # Попередній геш буде "0" для генезис-блоку
        return genesis_block

    def get_token_from_faucet(self, account_id, amount):
        if amount > self.faucet_coins:
            print("Недостатньо монет в faucet.")
            return False

        if account_id not in self.coin_database:
            self.coin_database[account_id] = 0

        self.coin_database[account_id] += amount
        self.faucet_coins -= amount
        return True

    def validate_block(self, block):
        # Перевірка посилання на останній актуальний блок
        if block.prev_hash != self.block_history[-1].block_id:
            print("Неправильний попередній геш для блоку.")
            return False

        # Перевірка, що транзакції у блоці не було додано в історію
        for tx in block.set_of_transactions:
            if tx in self.tx_database:
                print("Транзакція вже існує в історії.")
                return False
            self.tx_database.append(tx)

        # Перевірка на конфлікти в транзакціях
        # ... (додаткова логіка)

        # Перевірка підпису та балансів в кожній транзакції
        for tx in block.set_of_transactions:
            if not self.verify_transaction(tx):
                print("Помилка перевірки транзакції.")
                return False

        # Додавання блоку до історії
        self.block_history.append(block)
        return True

    def verify_transaction(self, tx):
        """
        Перевірка транзакції (підпис, баланс).
        """
        # ... (додаткова логіка яка написала в main.py)
        return True

    def get_account_balances(self):
        """
        Отримати поточний стан облікових записів та балансів.
        """
        return self.coin_database
