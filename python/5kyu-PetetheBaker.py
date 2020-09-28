def cakes(recipe, available):
    # Cake
    cake = []

    for ingridient, quantity in recipe.items():
        # Available or not
        if ingridient in available:
            cake.append(int(available[ingridient] / quantity))
        else:
            return 0

    # Minimum value
    return min(cake)
