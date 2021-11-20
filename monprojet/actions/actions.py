# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"




from builtins import str 

from typing import Any, Text, Dict, List
from rasa_sdk.forms import FormAction
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet





##########################################################################################################################################
####                                                                                                                               #######
#### form :  consiste à collecter quelques informations auprès d'un utilisateur                                                    #######
#### afin de faire quelque chose (réserver un restaurant, appeler une API, rechercher une base de données, etc.).                  #######
### Ceci est également appelé **remplissage de fentes**.                                                                           #######
##########################################################################################################################################
class ValideInformationForm(FormAction):

     

   def name(self) -> Text :

      return "form_commande_pizza" #formulaire de commande de pizza 
   
   @staticmethod
   def recupere_slot( traker : Tracker  ) -> List[Text] :

     """ liste entites pour remplir le formulaire """

     return["type" , "taille" ,"nombre"]

   
   def slot_mappings(self) -> Dict[Text, Any]:
   
       return {
         "type" : self.from_entity(entity= "type" , intent= ["dire_type"] ) ,
         "taille " : self.from_entity(entity= "taille"  , intent=["commander"]),
         "nombre" : self.from_entity(entity="nombre"  , intent = ["dire_nombre"])
         
       }


   def submit(self ,        
      dispatcher : CollectingDispatcher ,  # utilisée pour générer des réponses à renvoyer à l'utilisateur.
      tracker: Tracker, #  tracker permet d'acceder a la memoira de notre bot dans les action personnalise 
      domain: Dict[Text ,Any] , # domain est une representation json du ficier domain.yml
   )   -> List[Dict] :
      type = tracker.get_slot("type") ,
      taille = tracker.get_slot("taille") ,
      nombre = tracker.get_slot("nombre"),
      dispatcher.utter_message (text = "super  !vous avez commander {}  de taille {} d'une valeur {} veillez confirmer SVP" .format( type , taille ,nombre))
    
      return []



class ActionChangementCommande(Action):
   def name(Self):
      return "action_changement_commande"


   def run(self, dispatcher, tracker, domain):
      taille = tracker.get_slot("taille")
      type= tracker.get_slot("type")
      nombre = tracker.get_slot("nombre")
      SlotSet("type", type)
      SlotSet("taille", taille)
      SlotSet("nombre", nombre )
      return[]



class ActionAjouterCommande(Action):
	def name(self):
		return 'action_ajouter_commande'


      
	def run(self, dispatcher, tracker, domain):
		taille = tracker.get_slot("taille")
		type = tracker.get_slot("type")
		nombre = tracker.get_slot("nombre")
		detail_commande =  str(nombre + " " + type + "  "+ taille )
		ancien_commande = tracker.get_slot("total_order")

   
		return[SlotSet("total_order", [detail_commande]) if ancien_commande is None else SlotSet("total_order", ancien_commande[[0]+' and '+ detail_commande])]




class Commandeupdate(Action) :

   def name(self):
		
      return 'action_commande_update'

   
   def run(self, dispatcher, tracker, domain):


	   return[SlotSet("type", None),SlotSet("taille", None),SlotSet("nombre", None)]

class numero_commande(Action):
   def name(self):
	   return 'action_numero_commande'

   def run(self, dispatcher, tracker, domain):
	   nom_client = tracker.get_slot("nom_client")
	   numero_client = tracker.get_slot("numero_client")
      
	   numero_commande =  str(nom_client + "_"+numero_client)
	   print(numero_commande)
	   return[SlotSet("numero_commande", numero_commande)]



class ActionautresQuestion(Action):
	def name(self):
		return 'action_question_pizza'

	def run(self, dispatcher, tracker, domain):
		return[]

