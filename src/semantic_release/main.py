import dagger
from dagger import dag, field, function, object_type


def init() -> str:
    return (
        "hello dagger world"
    )

@object_type
class SemanticRelease:
    
    # ctr: dagger.Container = field(default=init)

    @function
    def version(self) -> str:
        """Returns the string argument provided"""
        return "v.0.0.0"
    

