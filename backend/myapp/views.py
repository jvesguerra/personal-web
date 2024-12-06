from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Person
from .serializers import PersonSerializer

class PersonListView(APIView):
    def get(self, request):
        # Fetch all people from the database
        people = Person.objects.all()  
        
        # Print the generated SQL query (useful for debugging)
        print(people.query)  # This prints the raw SQL query Django is executing
        print(people)
        
        # Serialize the data (convert the objects into JSON-friendly format)
        serializer = PersonSerializer(people, many=True)
        
        # Print the serialized data to the console for debugging
        print(serializer.data)
        
        # Return the serialized data in the HTTP response
        return Response(serializer.data)
