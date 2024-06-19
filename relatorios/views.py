from django.http import HttpResponse
from django.views import View
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from combustiveis.models import Abastecimento
from django.db.models import Sum
from io import BytesIO
import PyPDF2
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import DateRangeSerializer

class AbastecimentoRelatorioPDFView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = DateRangeSerializer(data=request.data)
        if serializer.is_valid():
            data_inicio = serializer.validated_data['data_inicio']
            data_fim = serializer.validated_data['data_fim']

            buffer = BytesIO()
            p = canvas.Canvas(buffer, pagesize=letter)
            width, height = letter

            abastecimentos = Abastecimento.objects.filter(data_hora__date__range=[data_inicio, data_fim]).values(
                'data_hora__date', 'bomba__tanque__tipo_combustivel', 'bomba__numero'
            ).annotate(
                total_litros=Sum('litros'),
                total_valor=Sum('valor'),
                total_imposto=Sum('valor') * 0.13
            ).order_by('data_hora__date', 'bomba__tanque__tipo_combustivel')

            p.setFont("Helvetica-Bold", 16)
            p.drawString(200, height - 50, "Relatório de Abastecimentos")

            p.setFont("Helvetica", 10)
            y = height - 100
            for abastecimento in abastecimentos:
                data = abastecimento['data_hora__date']
                tipo_combustivel = abastecimento['bomba__tanque__tipo_combustivel']
                bomba_numero = abastecimento['bomba__numero']
                total_litros = abastecimento['total_litros']
                total_valor = abastecimento['total_valor']
                total_imposto = abastecimento['total_imposto']

                p.drawString(50, y, f"Data: {data}")
                p.drawString(140, y, f"Combustível: {tipo_combustivel}")
                p.drawString(260, y, f"Bomba: {bomba_numero}")
                p.drawString(320, y, f"Litros: {total_litros}")
                p.drawString(380, y, f"Valor: R${total_valor:.2f}")
                p.drawString(460, y, f"Imposto: R${total_imposto:.2f}")

                y -= 20
                if y < 50:
                    p.showPage()
                    p.setFont("Helvetica", 10)
                    y = height - 50

            p.showPage()
            p.save()

            buffer.seek(0)

            reader = PyPDF2.PdfReader(buffer)

            response = HttpResponse(content_type='application/pdf')
            response['Content-Disposition'] = f'attachment; filename="relatorio_abastecimentos_{data_inicio}_a_{data_fim}.pdf"'

            writer = PyPDF2.PdfWriter()

            for page in range(len(reader.pages)):
                writer.add_page(reader.pages[page])

            writer.write(response)

            return response
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
