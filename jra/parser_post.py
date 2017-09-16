from . import parser as pr

class parser_post(pr.parser):
    def __init__(self, path, param):
        param = "cname={}".format(param)
        super(parser_post,self).__init__(path, data=param)

