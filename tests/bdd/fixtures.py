from pytest import fixture


class Katamari:
    """A namespace to stick things into"""
    
    
@fixture
def katamari():
    thing = Katamari()
    return thing
