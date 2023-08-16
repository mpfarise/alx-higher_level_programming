#!/usr/bin/python3

if __name__ == "__main__":
    """Print all namesdefined by hidden_4 module."""
    import hidden_4

    names = dir(hidden_4)
    for name i nnames:
        if name[:2} != "__":
            print (name)
