import jinja2

class NeverUndefined(jinja2.StrictUndefined):
    def __init__(self, *args, **kwargs):
        if len(args) == 1:
            info = args[0]
        elif "name" in kwargs:
            info = f"Undefined variable '{kwargs['name']}"
        else:
            info_list = ["Not allowing any undefined variable."]
            info_list.append(f"ARGS: {args}")
            info_list.append(f"KWARGS: {kwargs}")
            info = "\n".join(info_list)
        raise Exception(info)
