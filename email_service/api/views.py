from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.core.mail import send_mail

class EmailAPIView(APIView):
    def post(self,request):
        try:
            to_email="lenisgm0@gmail.com"
            subject="Mensaje de prueba"
            message="Este es un mensaje de Prueba desde DRF para la hermana mas tierna y que tanto quiero"
            send_mail(subject,message, None, [to_email])
            return Response({'message':'Correo enviado con exito'},status=status.HTTP_200_OK)
        except Exception as e:
            error_message = str(e)
            return Response({'message': error_message}, status=status.HTTP_400_BAD_REQUEST)    

