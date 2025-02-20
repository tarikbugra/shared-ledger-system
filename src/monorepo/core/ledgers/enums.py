import enum


def create_extended_enum(enum_name, *enums):
    combined_values = {}
    for e in enums:
        combined_values.update({item.name: item.value for item in e})

    return enum.Enum(enum_name, combined_values)
