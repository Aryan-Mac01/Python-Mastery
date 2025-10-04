def brew_chai(flavor):
    if flavor not in ["masala", "ginger", "elaichi"]:
        raise ValueError("Un-supported chai...")
    print(f"brewing {flavor} chai...")

brew_chai("mint")