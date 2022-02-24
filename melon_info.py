"""Print out all the melons in our inventory."""


from melons import melons_attributes


def print_melons_attributes(melons):
    """Print the atributes information of all melons types"""
    for name_key, attributes in melons.items():
        print(name_key,":")
        for attributes, value in attributes.items():
            print(attributes,":", value)
        print()

      
      


print_melons_attributes(melons_attributes)





      