# encoding: utf-8 
import logging 

class Bot(object):
	def __init__(self, send_callback, users_dao, tree):
		self.send_callback = send_callback
		self.users_dao = users_dao
		self.tree = tree 

	def handle(self, user_id, user_message):
		logging.info("Se invocó el método handle")
		# obtener el historial de eventos/mensajes 
		history = [
			(u"Hola! Por favor selecciona una opción para poder ayudarte.","bot"),
			(u"Cursos disponibles", "user"),
			(u"Tenemos varios cursos! Todos ellos son muy interesantes y totalmente prácticos. Por favor selecciona la opción que te resulte más interesante.","bot"),
			(user_message, "user")
		]
		# determine 1 rpta en func al mensaje escrito por el usuario (y tree)
		response_text = self.tree['say']
		possible_answers = self.tree['answers'].keys()

		tree = self.tree

		for text, author in history:
			logging.info("text: %s", text)
			logging.info("author: %s", author)

			if author == 'bot':
				if text == tree['say']:
					tree = tree['answers']

			elif author == 'user':
				key = get_key_if_valid(text, tree)
				if key is not None:
					tree = tree [key]
					if 'say' in tree:
						response_text = tree['say']
					if 'answers' in tree:
						possible_answers = tree['answers'].keys()
						possible_answers.sort()
					else: 
						possible_answers = None 


		
		self.send_callback(user_id, response_text, possible_answers)


def get_key_if_valid(text, dictionary):
	for key in dictionary:
		if key.lower() == text.lower():
			return key

	return None 
