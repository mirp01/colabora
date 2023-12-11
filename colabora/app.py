from flask import Flask


app = Flask(__name__, instance_relative_config=True)
app.config.from_object("defaults")
app.config.from_envvar("COLABORA_CONFIG", silent=True)
