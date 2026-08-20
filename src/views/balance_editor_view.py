from src.controllers.interfaces.balance_editor import BalanceEditorInterface
from src.views.http_types.http_request import HttpRequest
from src.views.http_types.http_reponse import HttpResponse
from .interfaces.view_interfaces import ViewInterface

class BalanceEditorView(BalanceEditorInterface):
    def __init__(self, controller: BalanceEditorInterface) -> None:
        self.__controller = controller

    def handle(self, http_request: HttpRequest) -> HttpResponse:
        new_balance = http_request.body.get("new_balance")
        user_id = http_request.params.get("user_id")

        self.__validate_inputs(new_balance, user_id)

        response = self.__controller.edit(user_id, new_balance)
        return HttpResponse(body={"data": response}, status_code=200)

    def __validate_inputs(self, new_balance: any, user_id: any) -> None:
        print()
        print(new_balance)
        print(user_id)
        if (
            not new_balance
            or not user_id
            or not isinstance(new_balance, float)
        ): raise Exception("Invalid Input")