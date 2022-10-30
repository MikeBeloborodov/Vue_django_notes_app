from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.response import Response
from rest_framework import status
from .models import User, Note
from .serializers import UserSerializer, NoteSerializer

@api_view(['GET'])
@permission_classes([])
@authentication_classes([])
def home(request):
    context = {
        'message': 'Welcome to the Notes api.'
    }
    return Response(context, status=status.HTTP_200_OK)

@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def notes(request, pk=0):
    if request.method == 'GET':
        user = request.user
        notes = Note.objects.filter(user=user).order_by('-created')
        serializer = NoteSerializer(notes, many=True)
        context = {
            'notes': serializer.data
        }
        return Response(context, status=status.HTTP_200_OK)

    if request.method == 'POST':
        body = request.data.get('body')
        if not body:
            context = {
                "error_message": "Text field is empty."
            }
            return Reponse(context, status=status.HTTP_400_BAD_REQUEST)
        title = request.data.get('title')
        user = request.user
        note = Note.objects.create(
            title=title,
            body=body,
            user=user
        )
        serializer = NoteSerializer(note)
        context = {
            "new_note": serializer.data
        }
        return Response(context, status=status.HTTP_200_OK)

    if request.method == 'PUT':
        if pk == 0:
            context = {
                "error_message": "This note does not exist."
            }
            return Response(context, status=status.HTTP_400_BAD_REQUEST)
        body = request.data.get('body')
        if not body:
            context = {
                "error_message": "Text field is empty."
            }
            return Reponse(context, status=status.HTTP_400_BAD_REQUEST)
        title = request.data.get('title')
        user = request.user
        try:
            note = Note.objects.get(id=pk)
            if note.user != user:
                context = {
                    "error_message": "You are not allowed to update this note."
                }
                return Response(context, status=status.HTTP_400_BAD_REQUEST)
            note.title = title
            note.body = body
            note.save()
            serializer = NoteSerializer(note)
            context = {
                "updated_note": serializer.data
            }
            return Response(context, status=status.HTTP_200_OK)
        except Note.DoesNoteExist:
            context = {
                "error_message": "This note does not exist."
            }
            return Response(context, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'DELETE':
        if pk == 0:
            context = {
                "error_message": "This note does not exist."
            }
            return Response(context, status=status.HTTP_400_BAD_REQUEST)
        try:
            note = Note.objects.get(id=pk)
            user = request.user
            if note.user != user:
                context = {
                    "error_message": "You are not allowed to update this note."
                }
                return Response(context, status=status.HTTP_400_BAD_REQUEST)
            serializer = NoteSerializer(note)
            note.delete()
            context = {
                'deleted_note': serializer.data
            }
            return Response(context, status=status.HTTP_200_OK)
        except Note.DoesNoteExist:
            context = {
                "error_message": "This note does not exist."
            }
            return Response(context, status=status.HTTP_400_BAD_REQUEST)
