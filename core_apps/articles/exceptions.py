from rest_framework.exceptions import APIException


class UpdateArticle(APIException):
    status_code = 403
    default_detail = "You cannot update an article that does not belong to you."