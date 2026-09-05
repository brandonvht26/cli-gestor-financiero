# OPERACIONES DEL GESTOR FINANCIERO

# Los ":" tras una variable o constante es Type-Hint e indica el tipo de dato o estructura asignada.
transaction_history: list = []

# La "->" es Type-Hint para una función.
def add_transaction(amount: float, description: str, transaction_type: str) -> dict:
    """
        La función add_transaction(...) está ligada a la creación de una nueva transacción,
        esta podría ser un ingreso o egreso, pero nunca un cero, obviamente.
    """
    
    if amount <= 0: return {}
    
    transaction: dict = {
        "amount": amount, 
        "description": description, 
        "transaction_type": transaction_type
    }

    transaction_history.append(transaction)
    
    return transaction

def get_balance() -> float:
    """
        La función get_balance(...) está enlazada a una consulta que calcula el balance del 
        usuario en base a sus trasancciones.
    """

    general_balance: float = 0

    for transaction in transaction_history:
        balance_transactional = transaction["amount"]
        type = transaction["transaction_type"]
        
        if type == "Ingreso":
            general_balance += balance_transactional
        elif type == "Egreso":
            general_balance -= balance_transactional

    return general_balance
