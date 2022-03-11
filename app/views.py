from .serialiser import wallpepsSerialiser
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import wallpeps, catego


## get all category
@api_view(["GET"])
def getCatego(request):
  cate=[]
  for i in catego:
    cate.append(i[0])
  return Response(cate)


## get all wallpapers
@api_view(["GET"])
def getAll(request):
  allWalls=wallpeps.objects.all()
  serialized=wallpepsSerialiser(allWalls, many=True)
  return Response(serialized.data)



## get wallpapers by id
@api_view(["GET"])
def get_by_id(request, id):
  try:
    wall=wallpeps.objects.get(id=id)
    serialized=wallpepsSerialiser(wall)
    return Response(serialized.data)
  except:
    return Response({"info":"image does not exists"}, status=status.HTTP_404_NOT_FOUND)
  
  

## get wallpapers by category
@api_view(["GET"])
def get_by_cate(request, cate):
  wall=wallpeps.objects.filter(category=cate)
  serialized=wallpepsSerialiser(wall, many= True)
  if serialized.data==[]:
    return Response({"info":"image does not exists"}, status=status.HTTP_404_NOT_FOUND)
  return Response(serialized.data)
    
  
