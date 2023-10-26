from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views.generic.base import TemplateView
from django.utils.decorators import method_decorator
from . models import Order
from django.views.decorators.csrf import csrf_exempt
from . helpers import custom_id
from hashlib import sha256
import base64
import requests
from django.views.decorators.csrf import csrf_exempt
import json
from django.conf  import settings

# Create your views here.

@method_decorator(csrf_exempt , name= 'dispatch')
class LandingDashboard(TemplateView):
    template_name = 'landing/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs) 
        return context
    def post(self,request):
        print(request.POST)
        name = (request.POST['name'])
        number = (request.POST['number'])
        alternative_number = (request.POST['alternative'])
        address1 = (request.POST['address1'])
        address2 = (request.POST['address2'])
        city = (request.POST['city'])
        state = (request.POST['state'])
        zip = (request.POST['zip'])
        order_id = custom_id('ord_')
        payment_method = request.POST['payment_mode']
        product = request.POST['product']

        amount = ''           

        #for iniciating prepaid order
        if payment_method == 'PPD':
            if product == 'ap1':
                amount = '130000'
            elif product == 'ap7':
                amount = '90000'
        elif payment_method == 'COD':
            amount = '10000'

        print(amount)

        # url ="https://api.phonepe.com/apis/hermes/pg/v1/pay"
        url = "https://api-preprod.phonepe.com/apis/merchant-simulator/pg/v1/pay"

        data = {
        # "merchantId": "TREZUNTONLINE",
        "merchantId": "MERCHANTUAT",
        "merchantTransactionId": order_id,
        "merchantUserId": name,
        "amount": amount,
        "redirectUrl": f"http://127.0.0.1:8000/order-placed/",
        "redirectMode": "POST",
        "callbackUrl": "https://8e9b-103-41-27-54.ngrok-free.app/phone_pay_web/?od={order_id}",
        "mobileNumber": '8847509330',
        "paymentInstrument": {
            "type": "PAY_PAGE"
        }
        }

        # converting data to string
        convert_to_string = json.dumps(data)

        encoded_string = base64.b64encode(convert_to_string.encode('utf-8'))

        # decoded byte to string
        decoded_string = encoded_string.decode()

        payload = {
            "request":decoded_string
            }   
        
        x_verify = sha256(encoded_string+'/pg/v1/pay'.encode()+settings.SALT_KEY.encode()).hexdigest()+'###'+ settings.SALT_INDEX

        print(x_verify)

        headers = {
            "accept": "application/json",
            "Content-Type": "application/json",
            "X-VERIFY": x_verify
            }

        response = requests.post(url,headers=headers,json=payload)

        # converting response to json object
        object_data = json.loads(response.text)
        if object_data['code'] == 'PAYMENT_INITIATED':
            
            redirect_url  =object_data['data']['instrumentResponse']['redirectInfo']['url']

            if object_data['code'] == 'PAYMENT_INITIATED':
                data = Order(name = name , number = number,alternative_number = alternative_number, address1 = address1 , address2 = address2 , city = city,state = state , zip = zip , payment_mode = payment_method ,amount =int(amount)/100, order_id = order_id , product_code = product )
                data.save()


            return HttpResponseRedirect(redirect_url)    

        return HttpResponseRedirect("/")
        
class OrderPlaced(TemplateView):
    template_name = 'landing/order_placed.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs) 
        return context

@csrf_exempt
def webhook_handel(request):
    print(request.headers['X-Verify'])
    print('header====>',request.headers)
    print('body====>',request.body)
    decoded_data = request.body.decode()
    converted_json_data = json.loads(decoded_data)
    response = base64.b64decode(converted_json_data['response']).decode()
    json_response = json.loads(response)
    print('Json parse bosy====>',json_response)
    tran_id = json_response['data']['merchantTransactionId']

    return JsonResponse({'status':200})