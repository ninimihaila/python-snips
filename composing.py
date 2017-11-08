def composable(func):
    """
    @composable
    def double(x):
        return 2*x

    def cube(x):
        return x*x
        
    (double + cube)(3)  # == double(cube(3)) == 18
    """
    class Composable:
        def __init__(self, fn):
            self._func = fn
            
        def _add(self, other):
            return Composable(lambda *args, **kwargs: self(other(*args, **kwargs)))
            
        def __call__(self, *args, **kwargs):
            return self._func(*args, **kwargs)
            
        __add__ = _add
        __iadd__ = _add    
            
    return Composable(func)



