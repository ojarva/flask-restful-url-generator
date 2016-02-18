"""
Flask-restful URLs view generator
"""

from flask_restful import Resource


class UrlList(Resource):
    """ Lists all registered URLs along with docstrings for classes
        and methods """

    def __init__(self, **kwargs):
        self.api = kwargs["api"]

    def get(self):
        """ Returns simple JSON for all registered endpoints """
        urls = self.api.app.url_map
        data = []
        view_funcs = self.api.app.view_functions
        for url in urls.iter_rules():
            methods = set(url.methods)
            methods.discard("HEAD")
            methods.discard("OPTIONS")
            item = {
                "methods": list(methods),
                "url": url.rule,
            }
            endpoint = url.endpoint
            if endpoint in self.api.app.view_functions:
                try:
                    endpoint_class = view_funcs.get(endpoint).view_class
                    doc = endpoint_class.__doc__
                    if doc:
                        item["doc"] = doc.strip()
                    for method in item["methods"]:
                        method_func = getattr(endpoint_class, method.lower())
                        doc = method_func.__doc__
                        if doc:
                            item["doc_for_%s" % method] = doc.strip()
                except AttributeError:
                    pass

            data.append(item)
        return data
