
import datetime
from django.shortcuts import render

# Create your views here.
def index(request):
     now = datetime.datetime.now()
     return render(request, "mothersDAY/index.html",{
         "mothersDAY": now.month == 5 and now.day == 12
     }

)