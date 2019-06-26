import os
from flask_restplus import Resource

from bdc_geoserver.status import ns
from bdc_geoserver.helpers import return_response

api = ns

@api.route('/')
class StatusController(Resource):
    
    def get(self):
        """
        Endpoint responsável por retornar o status da aplicação
        """
        return return_response({
            "status": "Running",
            "success": True
        }, 200)
