# Copyright 2017 Mycroft AI Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from mycroft.skills import MycroftSkill, intent_handler
from mycroft.skills.audioservice import AudioService
from mycroft.util import play_mp3
    AudioService = None


class BdiasTardesNoitesSkill(MycroftSkill):
    @intent_handler("BosDias.intent")
    def handle_bos_dias_intent(self, message):
        self.speak_dialog("BosDias")

    @intent_handler("BoasTardes.intent")
    def handle_boas_tardes_intent(self, message):
        self.speak_dialog("BoasTardes")

    @intent_handler("BoasNoites.intent")
    def handle_boas_noites_intent(self, message):
        self.speak_dialog("BoasNoites")
        
    @intent_handler("PonCCRadio.intent")
    def handle_pon_ccradio_intent(self, message):   
        self.audioservice.play(self.settings['https://radioserver02.ccradio.es/radio/8000/radio.mp3'])

   # @intent_handler("WhoAreYou.intent")
   # def handle_who_are_you_intent(self, message):
   #     name = self.config_core.get("listener", {}).get("wake_word",
   #                                                     "mycroft")
   #     name = name.lower().replace("hey ", "")
   #     self.speak_dialog("who.am.i", {"name": name})
   #  
   # @intent_handler("WhatAreYou.intent")
   # def handle_what_are_you_intent(self, message):
   #     self.speak_dialog("what.am.i")
   #
   # @intent_handler("DoYouRhyme.intent")
   # def handle_do_you_rhyme(self, message):
   #     self.speak_dialog("tell.a.rhyme")
   #
   # @intent_handler("DoYouDream.intent")
   # def handle_do_you_dream(self, message):
   #     self.speak_dialog("dream")
   #

def create_skill():
    return BdiasTardesNoitesSkill()
