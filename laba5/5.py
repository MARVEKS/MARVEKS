class Strategy:
    def execute(self, a, b):
        pass

class AddStrategy(Strategy):
    def execute(self, a, b):
        return a + b

class MultiplyStrategy(Strategy):
    def execute(self, a, b):
        return a * b

class Context:
    def __init__(self, strategy):
        self.strategy = strategy

    def set_strategy(self, strategy):
        self.strategy = strategy

    def execute(self, a, b):
        return self.strategy.execute(a, b)

class State:
    def handle(self, context, strategy_context):
        pass

class IdleState(State):
    def handle(self, context, strategy_context):
        print("[IdleState] Система в очікуванні...")
        context.set_state(ActiveState())
        strategy_context.set_strategy(AddStrategy())

class ActiveState(State):
    def handle(self, context, strategy_context):
        print("[ActiveState] Система активна. Виконуємо множення...")
        context.set_state(IdleState())
        strategy_context.set_strategy(MultiplyStrategy())

class SystemContext:
    def __init__(self):
        self.state = IdleState()

    def set_state(self, state):
        self.state = state

    def request(self, strategy_context):
        self.state.handle(self, strategy_context)

if __name__ == "__main__":
    print("=== Strategy + State ===")
    system = SystemContext()
    strategy = Context(AddStrategy())

    system.request(strategy)
    print("Результат:", strategy.execute(5, 3))

    system.request(strategy)
    print("Результат:", strategy.execute(5, 3))
