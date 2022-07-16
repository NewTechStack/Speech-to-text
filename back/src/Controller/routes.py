from Model.recognition import *

def setuproute(app, call):
    @app.route('/recognition',              ['OPTIONS', 'POST'],           lambda x = None: call([recognition])                                           )
    def base():
        return
