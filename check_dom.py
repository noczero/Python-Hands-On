def check_dom(str_param):
    tag_pairs = {
        'b': '/b',
        'i': '/i',
        'em': '/em',
        'div': '/div',
        'p': '/p'
    }

    i = 0
    wrong_tags = []
    while i < len(str_param):
        if str_param[i] == '<':
            # Step 1: Find the closing '>'
            close_pos = str_param.find('>', i)
            if close_pos == -1:
                return False

            # Step 2: Extract the tag
            tag_str = str_param[i:close_pos + 1]
            # print(tag_str)
            i = close_pos + 1

            tag_name = tag_str.strip("<>/").split()[0]
            # print(tag_name)

            # Step 3: Check opening or closing tag
            if tag_str[1] == '/':
                if not wrong_tags or wrong_tags[-1] != tag_name:
                    if not wrong_tags:
                        return False

                    return wrong_tags[-1]

                wrong_tags.pop()
            else:
                if tag_name in tag_pairs:
                    wrong_tags.append(tag_name)

        else:
            i += 1

    # Step 4 : Check wrong tags if empty then tags are correct
    if not wrong_tags:
        return True
    else:
        return False


# Example test cases
print(check_dom("<div><b><p>hello world</p></b></div>"))  # Should return True
print(check_dom("<div><i>hello</i>world</b>"))  # Should return 'div'
print(check_dom("</div><p></p><div>"))  # Should return False