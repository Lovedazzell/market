


def custom_id(stri):
    import random
    import string
    lower =  string.ascii_lowercase
    upper = string.ascii_uppercase
    num = string.digits
    combine = list(lower+upper+num)
    random.shuffle(combine)
    final_id = ''.join(combine)[:8]
    data =  stri + final_id

    from .models import Order
    if Order.objects.filter(order_id = data).exists():
        data = order_id(stri)
        
    return data