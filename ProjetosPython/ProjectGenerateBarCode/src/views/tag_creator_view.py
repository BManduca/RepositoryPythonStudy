#view para criação de tags

from src.views.http_types.http_request import HttpRequest
from src.views.http_types.http_response import HttpResponse
from src.controllers.tag_creator_controller import TagCreatorController

class TagCreatorView:
    '''
        responsability for interacting with HTTP
    '''
        
    # return from validate_and_create method will be an http response
    def validate_and_create(self, http_request: HttpRequest) -> HttpResponse:
        tag_creator_controller = TagCreatorController()
        
        body = http_request.body
        product_code = body["product_code"]
        
        # business rule logic -> creating tags -> return formatted response
        formatted_response = tag_creator_controller.create(product_code)
        
        # return response with formatted response for user
        return HttpResponse(status_code=200, body=formatted_response)
    