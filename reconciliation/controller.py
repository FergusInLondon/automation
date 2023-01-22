
class InvalidUpdateException(Exception):
    pass

class NoControllerAvailable(Exception):
    pass

Payload = Dict[str, Any]

@dataclass
class UpdateJob():
    thing: str
    payload: Payload

class Controller:
    def identifier() -> str:
        pass

    def update():
        raise NotImplementedError()

    def get(identifier=None):
        raise NotImplementedError()

class ControllerRegistry:
    def __init__(self, controllers=[]):
        self.controllers = {
            ctrl.ident(): ctrl
            for ctrl in controllers
        }

    def __getitem__(self, key) -> Controller:
        if self.controllers.hasattr(key):
            return self.controllers[key]

        raise NoControllerAvailable()

    def __setitem__(self, key: str, ctrl: Controller):
        self.controllers[key] = ctrl

    def __len__(self) -> int:
        return len(self.controllers)

    def __contains__(self, key: str) -> bool:
        return key in self.controllers.keys()

    def __call__(self, update: UpdateJob):
        self[update.thing.split("/")[0]].update(update.payload)
