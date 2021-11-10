# # This files contains your custom actions which can be used to run
# # custom Python code.
# #
# # See this guide on how to implement these action:
# # https://rasa.com/docs/rasa/core/actions/#custom-actions/
# # This is a simple example for a custom action which utters "Hello World!"
# from typing import Any, Text, Dict, List

# from rasa_sdk import Action, Tracker
# from rasa_sdk.executor import CollectingDispatcher


# class ActionYesNo(Action):
#     def name(self):
#         return "action_greet"

#     def run(self, dispatcher, tracker, domain):
#         if tracker.get_latest_input_channel() == 'facebook':
#             message = {
#                 "text": "Hey there! How can we help you ☺️ ?",
#                   "quick_replies": 
#                   [
#                     {
#                       "content_type": "text",
#                       "payload": "/tax",
#                       "title": "Tax",
#                     },
#                     {
#                       "content_type": "text",
#                       "payload": "/licence",
#                       "title": "Licence",
#                     },
#                     {
#                       "content_type": "text",
#                       "payload": "/driving_test",
#                       "title": "Driving Test"
#                     },
#                     {
#                       "content_type": "text",
#                       "payload": "/different_other_categories",
#                       "title": "Others"
#                     },
#                     {
#                       "content_type": "text",
#                       "payload": "/faq",
#                       "title": "FAQ"
#                     }
#                 ]
#             }
#             dispatcher.utter_custom_json(message)
#         else:
#             dispatcher.utter_message(template="action_greet",name=tracker)
#         return []

# class ActionTaxPeriod(Action):
#     def name(self):
#         return "action_tax_periods"

#     def run(self, dispatcher, tracker, domain):
#         if tracker.get_latest_input_channel() == 'facebook':
#             message1 = {
#                 "text": "Category of Vehicle are : ",
#                   "quick_replies": 
#                   [
#                     {
#                       "content_type": "text",
#                       "payload": "/non_transport",
#                       "title": "Non Transport/Contract carriages ordinarily kept in the state",
#                     },
#                     {
#                       "content_type": "text",
#                       "payload": "/transport",
#                       "title": "Transport Vehicles other than contract carriages and the Stage Carriages ordinarily kept in the state",
#                     },
#                     {
#                       "content_type": "text",
#                       "payload": "/stage_carriages",
#                       "title": "Stage Carriages"
#                     },
#                     {
#                       "content_type": "text",
#                       "payload": "/newly_purchased",
#                       "title": "Vehicles newly purchased and registered in the state or brought from outside"
#                     },
#                     {
#                       "content_type": "text",
#                       "payload": "/transport_vehicle_other_states",
#                       "title": "Transport Vehicles of other states"
#                     }
#                 ]
#             }
#             dispatcher.utter_custom_json(message1)
#         else:
#             dispatcher.utter_message(template="action_tax_periods",name=tracker)
#         return []

# class AdditionalTaxOneYear(Action):
#     def name(self):
#         return "action_add_one_years"

#     def run(self, dispatcher, tracker, domain):
#         if tracker.get_latest_input_channel() == 'facebook':
#             message2 = {
#                 "text": "Choose any one of the above : ",
#                   "quick_replies": 
#                   [
#                     {
#                       "content_type": "text",
#                       "payload": "/tax_one_month",
#                       "title": "Within 1 month",
#                     },
#                     {
#                       "content_type": "text",
#                       "payload": "/tax_three_month",
#                       "title": "Within 3 months",
#                     },
#                     {
#                       "content_type": "text",
#                       "payload": "/tax_six_months",
#                       "title": "Within 6 months"
#                     },
#                     {
#                       "content_type": "text",
#                       "payload": "/additional_tax_others",
#                       "title": "Other cases"
#                     }
#                 ]
#             }
#             dispatcher.utter_custom_json(message2)
#         else:
#             dispatcher.utter_message(template="action_add_one_years",name=tracker)
#         return []

# class AdditionalTaxQuartely(Action):
#     def name(self):
#         return "action_add_quartelys"

#     def run(self, dispatcher, tracker, domain):
#         if tracker.get_latest_input_channel() == 'facebook':
#             message3 = {
#                 "text": "Choose any one of the above : ",
#                   "quick_replies": 
#                   [
#                     {
#                       "content_type": "text",
#                       "payload": "/quartertaxonemonth",
#                       "title": "Within 1 month",
#                     },
#                     {
#                       "content_type": "text",
#                       "payload": "/quartaxthreemonth",
#                       "title": "Within 3 months",
#                     },
#                     {
#                       "content_type": "text",
#                       "payload": "/quartaxsixmonth",
#                       "title": "Within 6 months"
#                     },
#                     {
#                       "content_type": "text",
#                       "payload": "/quartaxothers",
#                       "title": "Other cases"
#                     }
#                 ]
#             }
#             dispatcher.utter_custom_json(message3)
#         else:
#             dispatcher.utter_message(template="action_add_quartelys",name=tracker)
#         return []

# class LicenceDetails(Action):
#     def name(self):
#         return "action_licences"

#     def run(self, dispatcher, tracker, domain):
#         if tracker.get_latest_input_channel() == 'facebook':
#             message4 = {
#                 "text": "Choose any one of the above : ",
#                   "quick_replies": 
#                   [
#                     {
#                       "content_type": "text",
#                       "payload": "/driving_licence",
#                       "title": "Driving Licence",
#                     },
#                     {
#                       "content_type": "text",
#                       "payload": "/check_criterian",
#                       "title": "Licence Criterian",
#                     },
#                     {
#                       "content_type": "text",
#                       "payload": "/learners_validity",
#                       "title": "Learner's Valididty"
#                     },
#                     {
#                       "content_type": "text",
#                       "payload": "/licence_card",
#                       "title": "Licence card issued"
#                     },
#                     {
#                       "content_type": "text",
#                       "payload": "/renewal_driving_licence",
#                       "title": "Licence Renewal"
#                     },
#                     {
#                       "content_type": "text",
#                       "payload": "/eligibility_condition",
#                       "title": "Eligibility Age"
#                     }
#                 ]
#             }
#             dispatcher.utter_custom_json(message4)
#         else:
#             dispatcher.utter_message(template="action_licences",name=tracker)
#         return []

# class OthersDetails(Action):
#     def name(self):
#         return "action_different_other_categoriess"

#     def run(self, dispatcher, tracker, domain):
#         if tracker.get_latest_input_channel() == 'facebook':
#             message5 = {
#                 "text": "Select any one of the category : ",
#                   "quick_replies": 
#                   [
#                     {
#                       "content_type": "text",
#                       "payload": "/application",
#                       "title": "Application Forms",
#                     },
#                     {
#                       "content_type": "text",
#                       "payload": "/driving_school",
#                       "title": "Driving School",
#                     },
#                     {
#                       "content_type": "text",
#                       "payload": "/forms",
#                       "title": "Licence Forms"
#                     },
#                     {
#                       "content_type": "text",
#                       "payload": "/medical_certificates",
#                       "title": "Medical Certificates"
#                     },
#                     {
#                       "content_type": "text",
#                       "payload": "/renewal_duplicate_forms",
#                       "title": "Renewal/Duplicate forms"
#                     }
#                 ]
#             }
#             dispatcher.utter_custom_json(message5)
#         else:
#             dispatcher.utter_message(template="action_different_other_categoriess",name=tracker)
#         return []

# class ApplicationDetails(Action):
#     def name(self):
#         return "action_applications"

#     def run(self, dispatcher, tracker, domain):
#         if tracker.get_latest_input_channel() == 'facebook':
#             message6 = {
#                 "text": "Select any one of the category : ",
#                   "quick_replies": 
#                   [
#                     {
#                       "content_type": "text",
#                       "payload": "/application_driving_licence_form",
#                       "title": "Driving Learner form",
#                     },
#                     {
#                       "content_type": "text",
#                       "payload": "/application_physical_fitness",
#                       "title": "Physical Fitness form",
#                     },
#                     {
#                       "content_type": "text",
#                       "payload": "/application_new_class",
#                       "title": "Addition New Class"
#                     },
#                     {
#                       "content_type": "text",
#                       "payload": "/application_motor_registration",
#                       "title": "Motor Vehicle Registration"
#                     },
#                     {
#                       "content_type": "text",
#                       "payload": "/grant_learners",
#                       "title": "Grant Learners Licence"
#                     }
#                 ]
#             }
#             dispatcher.utter_custom_json(message6)
#         else:
#             dispatcher.utter_message(template="action_applications",name=tracker)
#         return []

# class FormsDetails(Action):
#     def name(self):
#         return "action_formss"

#     def run(self, dispatcher, tracker, domain):
#         if tracker.get_latest_input_channel() == 'facebook':
#             message7 = {
#                 "text": "Select any one of the category : ",
#                   "quick_replies": 
#                   [
#                     {
#                       "content_type": "text",
#                       "payload": "/applicant_licence_drive_motor_vehicle",
#                       "title": "Drive Motor Vehicle",
#                     },
#                     {
#                       "content_type": "text",
#                       "payload": "/authorisation_drive_transport_vehicle",
#                       "title": "Authorisation to Drive Transport Vehicle",
#                     },
#                     {
#                       "content_type": "text",
#                       "payload": "/intimation_of_loss",
#                       "title": "Loss/Duplicate"
#                     },
#                     {
#                       "content_type": "text",
#                       "payload": "/international_driving_permit",
#                       "title": "International Driving Permit"
#                     },
#                     {
#                       "content_type": "text",
#                       "payload": "/fresh_conductor_licence",
#                       "title": "Conductor's Licence(Fresh)"
#                     },
#                     {
#                       "content_type": "text",
#                       "payload": "/measurement_certificate",
#                       "title": "Measurement Certificate"
#                     }
#                 ]
#             }
#             dispatcher.utter_custom_json(message7)
#         else:
#             dispatcher.utter_message(template="action_formss",name=tracker)
#         return []

# class RenewalDetails(Action):
#     def name(self):
#         return "action_renewal_duplicate_formss"

#     def run(self, dispatcher, tracker, domain):
#         if tracker.get_latest_input_channel() == 'facebook':
#             message8 = {
#                 "text": "Select any one of the category : ",
#                   "quick_replies": 
#                   [
#                     {
#                       "content_type": "text",
#                       "payload": "/renewal_conductor_licence",
#                       "title": "Rene Conductor Licence",
#                     },
#                     {
#                       "content_type": "text",
#                       "payload": "/renewal_registration_number",
#                       "title": "Registration Certificate Vehicles",
#                     },
#                     {
#                       "content_type": "text",
#                       "payload": "/duplication_registration_certificate",
#                       "title": "Registration Certificate for Vehicles"
#                     },
#                     {
#                       "content_type": "text",
#                       "payload": "/reassigning_registration_number",
#                       "title": "Re-assignment number for vehicle"
#                     },
#                     {
#                       "content_type": "text",
#                       "payload": "/renewal_driving_licence",
#                       "title": "Licence Renewal"
#                     },
#                     {
#                       "content_type": "text",
#                       "payload": "/duplicate_conductor_licence",
#                       "title": "Dup Conductor Licence"
#                     }
#                 ]
#             }
#             dispatcher.utter_custom_json(message8)
#         else:
#             dispatcher.utter_message(template="action_renewal_duplicate_formss",name=tracker)
#         return []

# class DrivingDetails(Action):
#     def name(self):
#         return "action_driving_tests"

#     def run(self, dispatcher, tracker, domain):
#         if tracker.get_latest_input_channel() == 'facebook':
#             message9 = {
#                 "text": "Select any one of the category : ",
#                   "quick_replies": 
#                   [
#                     {
#                       "content_type": "text",
#                       "payload": "/driving_test_conducted",
#                       "title": "Driving Test Conducted",
#                     },
#                     {
#                       "content_type": "text",
#                       "payload": "/subject_driving_test",
#                       "title": "Subjects for test",
#                     },
#                     {
#                       "content_type": "text",
#                       "payload": "/criterian_driving_test",
#                       "title": "who apply Test"
#                     },
#                     {
#                       "content_type": "text",
#                       "payload": "/test_failed",
#                       "title": "Failed Test"
#                     }
#                 ]
#             }
#             dispatcher.utter_custom_json(message9)
#         else:
#             dispatcher.utter_message(template="action_driving_tests",name=tracker)
#         return []

# class HelpDetails(Action):
#     def name(self):
#         return "action_helps"

#     def run(self, dispatcher, tracker, domain):
#         if tracker.get_latest_input_channel() == 'facebook':
#             message10 = {
#                 "text": "Was this Helpful ?",
#                   "quick_replies": 
#                   [
#                     {
#                       "content_type": "text",
#                       "payload": "/yess",
#                       "title": " 👍 ",
#                     },
#                     {
#                       "content_type": "text",
#                       "payload": "/noo",
#                       "title": " 👎 "
#                     }
#                 ]
#             }
#             dispatcher.utter_custom_json(message10)
#         else:
#             dispatcher.utter_message(template="action_helps",name=tracker)
#         return []

# class HelpD(Action):
#     def name(self):
#         return "action_nopes"

#     def run(self, dispatcher, tracker, domain):
#         if tracker.get_latest_input_channel() == 'facebook':
#             message12 = {
#                 "text": " Select the Category you want to know about ? :",
#                   "quick_replies": 
#                   [
#                     {
#                       "content_type": "text",
#                       "payload": "/tax",
#                       "title": "Tax",
#                     },
#                     {
#                       "content_type": "text",
#                       "payload": "/licence",
#                       "title": "Licence",
#                     },
#                     {
#                       "content_type": "text",
#                       "payload": "/driving_test",
#                       "title": "Driving Test"
#                     },
#                     {
#                       "content_type": "text",
#                       "payload": "/different_other_categories",
#                       "title": "Others"
#                     },
#                     {
#                       "content_type": "text",
#                       "payload": "/faq",
#                       "title": "FAQ"
#                     }
#                 ]
#             }
#             dispatcher.utter_custom_json(message12)
#         else:
#             dispatcher.utter_message(template="action_nopes",name=tracker)
#         return []