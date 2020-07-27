import json
import logging

import azure.functions as func


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')



    ret = {}
    ret["message"] = "Response from api successful"
    return func.HttpResponse(json.dumps(ret), mimetype="application/json")
