def convert_to_int(value) : 
    
    try:
        return int(value)
    except ValueError:
        raise ValueError(f"Invalid value")