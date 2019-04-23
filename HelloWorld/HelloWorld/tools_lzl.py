def make_p_list(list_1):
    response1 = ""
    for var in list_1:
        response1 += "<p>" + var.name + "</p>"
    return response1


class ObjVar:
    def __init__(self, name):
        self.name = name


if __name__ == "__main__":
    result_str = make_p_list([ObjVar('a'), ObjVar('b'), ObjVar('c')])
    assert result_str == '<p>a</p><p>b</p><p>c</p>'
