from calendar import c


def names(city, country, population=''):
    """Generate a neatly formatted full string."""
    if population:
        full_name = f"{city} , {country} , Population = {population}"
    else:
        full_name = f"{city} , {country}"
    return full_name.title()

