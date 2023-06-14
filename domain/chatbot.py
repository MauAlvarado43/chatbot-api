from django.shortcuts import get_object_or_404
from app.models import Chat, User
import openai
import json
import os

openai.api_key = os.getenv('OPENAI_API_KEY')
ft_model = os.getenv('OPENAI_FT_MODEL')

def generate_chatbot_response(message, user_id):

    user = get_object_or_404(User, pk=user_id)

    Chat.objects.create(
        message = message,
        type = 'USER',
        user = user
    )
    
    answer = openai.Completion.create(
        model = ft_model,
        prompt = message
    )

    try: 
        answer_message = answer['choices'][0]['text']
    except:
        answer_message = "I don't understand what you mean."

    Chat.objects.create(
        message = answer_message,
        type = 'BOT',
        user = user
    )