

from django.views.decorators.csrf import csrf_exempt
from django.views import View
from django.http import JsonResponse
from django.conf import settings
import requests
from django.utils.decorators import method_decorator
import json


@method_decorator(csrf_exempt, name='dispatch')
class QuoteView(View):
    def post(self, request):
        try:
            
            
            
            data = json.loads(request.body)
            phone = data.get('phone')
            rooms = data.get('rooms')
            from_address = data.get('fromAddress')
            to_address = data.get('toAddress')
            
            
            # Проверка данных
            if not phone or not rooms or not from_address or not to_address:
                return JsonResponse({'status': 'error', 'error': 'Missing required fields'}, status=400)

            

            # Формируем сообщение
            message = f"""
            New Quote Request:
            Phone: {phone}
            Rooms: {rooms}
            From: {from_address}
            To: {to_address}
            """
            
         
            
            

            # Отправляем сообщение в Telegram
            telegram_api_url = f"https://api.telegram.org/bot{settings.TELEGRAM_BOT_TOKEN}/sendMessage"
            payload = {
                'chat_id': settings.TELEGRAM_CHAT_ID,
                'text': message,
                'parse_mode': 'HTML',
            }
            response = requests.post(telegram_api_url, data=payload)
            
            
            
            

            if response.status_code == 200:
                return JsonResponse({'status': 'success'}, status=200)
            else:
                return JsonResponse({'status': 'failed', 'error': response.text}, status=500)

        except Exception as e:
            
        
            
            return JsonResponse({'status': 'error', 'error': str(e)}, status=400)
