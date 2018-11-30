

def text_search(text,head,tail,increment):
    # SEARCHES TEXT FOR A STRING BETWEEN HEAD & TAIL

    while True:
        try:
            index = text.index(head)
        except ValueError: # QUERY NOT FOUND
            return None
        else:
            # FIND STRING
            text = text[index+increment:]
            try:
                name = text[:text.index(tail)].lower()
                if not name.isalpha():
                    raise ValueError
            except ValueError:
                pass
            else:
                return name
            


