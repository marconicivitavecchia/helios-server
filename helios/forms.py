# This Python file uses the following encoding: utf-8
"""
Forms for Helios
"""

from django import forms
from models import Election
from widgets import SplitSelectDateTimeWidget
from fields import SplitDateTimeField
from django.conf import settings


class ElectionForm(forms.Form):
  short_name = forms.SlugField(max_length=40, help_text="senza spazi, farà parte dell'URL dell'elezione, e.g. my-club-2020")
  name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'size':60}), help_text='il nome della tua elezione, e.g. Elezioni per il mio club 2020')
  description = forms.CharField(max_length=4000, widget=forms.Textarea(attrs={'cols': 70, 'wrap': 'soft'}), required=False)
  election_type = forms.ChoiceField(label="tipo", choices = Election.ELECTION_TYPES)
  use_voter_aliases = forms.BooleanField(required=False, initial=False, help_text='Se selezionato, gli identificativi dei votanti saranno sostituiti da un alias, e.g. "V12", nel centro tracciamento voti')
  #use_advanced_audit_features = forms.BooleanField(required=False, initial=True, help_text='disable this only if you want a simple election with reduced security but a simpler user interface')
  randomize_answer_order = forms.BooleanField(required=False, initial=False, help_text='abilita questa spunta se vuoi che le risposte siano presentate in ordine casuale per ogni votante')
  private_p = forms.BooleanField(required=False, initial=False, label="Privata?", help_text='Un elezione privata è visibile solo agli elettori registrati.')
  help_email = forms.CharField(required=False, initial="", label="Indirizzo Email di supporto", help_text='Un indirizzo email che gli elettori possono contattare per chiedere supporto.')
  
  if settings.ALLOW_ELECTION_INFO_URL:
    election_info_url = forms.CharField(required=False, initial="", label="URL per scaricare le informazioni dell'elezione", help_text="un URL che punta ad un documento PDF che contiene informazioni extra sull'elezione, e.g. biografia e dichiarazioni dei candidati")
  
  # times
  voting_starts_at = SplitDateTimeField(help_text = 'UTC date and time when voting begins',
                                   widget=SplitSelectDateTimeWidget, required=False)
  voting_ends_at = SplitDateTimeField(help_text = 'UTC date and time when voting ends',
                                   widget=SplitSelectDateTimeWidget, required=False)

class ElectionTimeExtensionForm(forms.Form):
  voting_extended_until = SplitDateTimeField(help_text = 'UTC date and time voting extended to',
                                   widget=SplitSelectDateTimeWidget, required=False)
  
class EmailVotersForm(forms.Form):
  subject = forms.CharField(max_length=80)
  body = forms.CharField(max_length=4000, widget=forms.Textarea)
  send_to = forms.ChoiceField(label="Invia a", initial="tutti", choices= [('tutti', 'tutti gli elettori'), ('votato', 'tutti gli elettori che hanno votato'), ('non-votato', 'tutti gli elettori che non hanno ancora votato')])

class TallyNotificationEmailForm(forms.Form):
  subject = forms.CharField(max_length=80)
  body = forms.CharField(max_length=2000, widget=forms.Textarea, required=False)
  send_to = forms.ChoiceField(label="Invia a", choices= [('tutti', 'tutti i votanti'), ('votato', 'solo gli elettori che hanno votato'), ('nessuno', 'nessuno -- sei sicuro di questo?')])

class VoterPasswordForm(forms.Form):
  voter_id = forms.CharField(max_length=50, label="ID elettore")
  password = forms.CharField(widget=forms.PasswordInput(), max_length=100)

