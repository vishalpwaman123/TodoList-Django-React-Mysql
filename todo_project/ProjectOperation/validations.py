

def Parameter_Validation_Checker(attribute, attribute_value, request):
    if attribute is None or attribute == "":
        Message = attribute_value + " Is Required"
        data = {
            "Message": Message,
            "data": request.data
        }
        return data

    return False


def CreateProductView_Validation(request):

    name = request.data.get("name")
    Response = Parameter_Validation_Checker(name, "name", request)
    if Response:
        return Response

    category = request.data.get("category")
    Response = Parameter_Validation_Checker(category, "category", request)
    if Response:
        return Response

    price = request.data.get("price")
    Response = Parameter_Validation_Checker(price, "price", request)
    if Response:
        return Response

    description = request.data.get("description")
    Response = Parameter_Validation_Checker(
        description, "description", request)
    if Response:
        return Response

    stars = request.data.get("stars")
    Response = Parameter_Validation_Checker(
        stars, "stars", request)
    if Response:
        return Response

    return False
