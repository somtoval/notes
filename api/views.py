# from django.http import JsonResponse


# # This view just returns a json data of routes, the safe=False we can return any kind of data to json response as this is just a python list here
# def getRoutes(request):
#     routes = [
#         {
#             'Endpoint':'/notes/',
#             'method':'GET',
#             'body':None,
#             'description':'Returns an array of notes'
#         },
#         {
#             'Endpoint':'/notes/id',
#             'method':'GET',
#             'body':None,
#             'description':'Returns a single note object'
#         },
#         {
#             'Endpoint':'/notes/create/',
#             'method':'POST',
#             'body':{'body':""},
#             'description':'Creates new note with data sent in post request'
#         },
#         {
#             'Endpoint':'/notes/id/update/',
#             'method':'PUT',
#             'body':{'body':""},
#             'description':'Creates an existing note with data sent in'
#         },
#         {
#             'Endpoint':'/notes/id/delete/',
#             'method':'DELETE',
#             'body':None,
#             'description':'Deletes an existing note'
#         },
#     ]
#     return JsonResponse(routes, safe=False)

# # At this point we have just built a simplified api that returns a json response, but if we continue like this it would be a pain in the ass as we would have to manually do stuffs like serialization of our python object so we would use django rest framework

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import NoteSerializer
from .models import Note

@api_view(['GET'])
def getRoutes(request):
    routes = [
        {
            'Endpoint':'/notes/',
            'method':'GET',
            'body':None,
            'description':'Returns an array of notes'
        },
        {
            'Endpoint':'/notes/id',
            'method':'GET',
            'body':None,
            'description':'Returns a single note object'
        },
        {
            'Endpoint':'/notes/create/',
            'method':'POST',
            'body':{'body':""},
            'description':'Creates new note with data sent in post request'
        },
        {
            'Endpoint':'/notes/id/update/',
            'method':'PUT',
            'body':{'body':""},
            'description':'Creates an existing note with data sent in'
        },
        {
            'Endpoint':'/notes/id/delete/',
            'method':'DELETE',
            'body':None,
            'description':'Deletes an existing note'
        },
    ]
    return Response(routes)

# In other to render routes out we need to do data serialization that would convert our python object to a json data and then we render it out

@api_view(['GET'])
def getNotes(request):
    notes = Note.objects.all()
    serializer = NoteSerializer(notes, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getNote(request, pk):
    note = Note.objects.get(id=pk)
    serializer = NoteSerializer(note, many=False)
    return Response(serializer.data)

@api_view(['POST'])
def createNote(request):
    data = request.data
    note = Note.objects.create(
        body = data['body']
    )
    serializer = NoteSerializer(note, many=False)
    return Response(serializer.data)

@api_view(['PUT'])
def updateNote(request, pk):
    data = request.data
    note = Note.objects.get(id=pk)
    serializer = NoteSerializer(note, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['DELETE'])
def deleteNote(request, pk):
    note = Note.objects.get(id=pk)
    note.delete()
    return Response('Note was deleted')