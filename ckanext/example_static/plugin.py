from flask import Blueprint

import ckan.plugins as plugins
import ckan.plugins.toolkit as tk

example = Blueprint("example", __name__)

@example.route("/hello-page")
def hello():
    return tk.render("custom/index.html")


class ExampleStaticPlugin(plugins.SingletonPlugin):
    plugins.implements(plugins.IConfigurer)
    plugins.implements(plugins.IBlueprint)

    # IConfigurer
    def update_config(self, config_):
        tk.add_template_directory(config_, "templates")
        tk.add_public_directory(config_, "public")

    # IBlueprint
    def get_blueprint(self):
        return example
