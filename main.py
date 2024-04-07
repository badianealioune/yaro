import random
import os
import importlib.util
from highrise import*
from highrise import BaseBot,Position
from highrise.models import SessionMetadata

folie = ["🤪Votre niveau de folie est de : 100%","🤪Votre niveau de folie est de : 99%","🤪Votre niveau de folie est de : 50%","🤪Votre niveau de folie est de : 0%","🤪Votre niveau de folie est de : 1%","🤪Votre niveau de folie est de : 2%","🤪Votre niveau de folie est de : 64%","🤪Votre niveau de folie est de : 22%","🤪Votre niveau de folie est de : 19%","🤪Votre niveau de folie est de : 88%","🤪Votre niveau de folie est de : 39%","🤪Votre niveau de folie est de : 40%","🤪Votre niveau de folie est de : 92%","🤪Votre niveau de folie est de : 74%","🤪Votre niveau de folie est de : 10%","🤪Votre niveau de folie est de : 9%","🤪Votre niveau de folie est de : 77%","🤪Votre niveau de folie est de : 82%","🤪Votre niveau de folie est de : 66%","🤪Votre niveau de folie est de : 11%","🤪Votre niveau de folie est de : 15%"]
        
mariage = ["Je me marie avec toi 💍","Bien sûr que oui 💍❤️","Je ne veux pas 💍💔","Évidemment que non 💍💔","Je t'aime bien sûr que je me marie avec toi 💍"]


curatif = ["🔴Vous avez utilisé le pansement, votre vie est à : 100%🔴","🔴Vous avez utilisé le pansement, votre vie est à : 50%🔴","🔴Vous avez utilisé le pansement, votre vie est à : 60%🔴","🔴Vous avez utilisé le pansement, votre vie est à : 75%🔴","🔴Vous avez utilisé le pansement, votre vie est à : 85%🔴","🔴Vous avez utilisé le pansement, votre vie est à : 80%🔴","🔴Vous avez utilisé le pansement, votre vie est à : 90%🔴","🔴Vous avez utilisé le pansement, votre vie est à : 95%🔴","🔴Vous avez utilisé le pansement, votre vie est à : 99%🔴","🔴Vous avez utilisé le pansement, votre vie est à : 91%🔴"]
         
bombe = ["💣🧟‍♂️ Vous avez lancé une bombe sur 1x Boss Zombie 🧟‍♀️💣","💣🧟 Vous avez lancé une bombe sur 3x Boss Zombie 🧟💣","💣🧟‍♂️ Vous avez lancé une bombe sur 2x Boss Zombie 💣🧟‍♀️","💣🧟‍♂️ Vous avez lancé une bombe sur 7x Boss Zombie 💣🧟‍♂️","💣🧟 Vous avez lancé une bombe sur 4x Boss Zombie 🧟💣"]

couteau = ["🧟🔪 Vous avez poignardé 1x Zombie 🔪🧟","🧟🔪 Vous avez poignardé 6x Zombie 🔪🧟","🧟🔪 Vous avez poignardé 7x Zombie 🔪🧟","🧟‍♂️🔪🧟‍♂️ Vous avez poignardé 8x Zombie 🔪🧟‍♂️","🧟🔪 Vous avez poignardé 10x Zombie 🔪🧟","🧟🔪 Vous avez poignardé 9x Zombie 🔪🧟","🧟‍♀️🔪🧟‍♂️ Vous avez poignardé 3x Zombie 🧟‍♂️🔪🧟‍♀️"]

tirer = ["🧟Vous avez tiré sur 5x Zombies🧟","🧟Vous avez tiré sur 1x Zombie🧟","🧟Vous avez tiré sur 8x Zombies🧟","🧟Vous avez tiré sur 3x Zombies🧟","🧟‍♂️Vous avez tiré sur 5x Zombies🧟‍♂️","🧟‍♀️Vous avez tiré sur 10x Zombies🧟‍♀️","🧟🧟‍♀️Vous avez tiré sur 9x Zombies🧟🧟‍♀️"]

play = ["🔴Votre vie est à 50%, utilisez : /curatif","🔴Votre vie est à 20%, utilisez : /curatif","🔴Votre vie est à 40%, utilisez : /curatif","🧟Les zombies arrivent, utilisez : /coup de couteau ou /tirer","🧟🧟‍♂️ Il y a beaucoup de zombies 🧟‍♀️🧟 🛡 Utilisez : /bouclier 🛡","🧟Le boss zombie arrive, utilisez : /bombe","🧟Les zombies arrivent, utilisez : /coup de couteau ou /tirer","🧟🧟‍♂️ Il y a beaucoup de zombies 🧟‍♀️🧟 🛡 Utilisez : /bouclier 🛡","🔴Votre vie est à 60%, utilisez : /curatif","🔴Votre vie est à 10%, utilisez : /curatif","🧟Les zombies arrivent, utilisez : /coup de couteau ou /tirer","🧟Les zombies arrivent, utilisez : /coup de couteau ou /tirer","🧟Les zombies arrivent, utilisez : /coup de couteau ou /tirer","🧟Les zombies arrivent, utilisez : /coup de couteau ou /tirer","🧟Les zombies arrivent, utilisez : /coup de couteau ou /tirer"]

pecher = ["🥈VOUS AVEZ REMPORTÉ LA MÉDAILLE : PÊCHEUR ARGENT🥈","🥉VOUS AVEZ REMPORTÉ LA MÉDAILLE : PÊCHEUR BRONZE🥉","🥉VOUS AVEZ REMPORTÉ LA MÉDAILLE : PÊCHEUR BRONZE🥉","🥉VOUS AVEZ REMPORTÉ LA MÉDAILLE : PÊCHEUR BRONZE🥉","🥉VOUS AVEZ REMPORTÉ LA MÉDAILLE : PÊCHEUR BRONZE🥉","🟡Événement : /carpe 🟡","⚫️Vous avez pêché 3x Lune de la nuit⚫️(+150 POINTS)","⚫️Vous avez pêché 2x Lune de la nuit⚫️(+100 POINTS)","⚫️Vous avez pêché 1x Lune de la nuit⚫️(+50 POINTS)","🟡Vous avez pêché 1x Crevette Dorée 🟡 (MULTIPOINTS)","🟡Vous avez pêché 1x Plie Dorée🟡 (MULTIPOINTS)","🪼🌈Vous avez pêché 1x Poulpe Arc-en-ciel🪼🌈 (POINTS SUPPLÉMENTAIRES)","🐢Vous avez pêché 3x Tortue 🐢 (PERTES DE POINTS)","🦑Vous avez pêché 1x Calmar Géant 🦑 (LÉGENDAIRE)","🦀Vous avez pêché 6x Crabe 🦀 (COMMUN)","🦀Vous avez pêché 2x Crabe 🦀 (COMMUN)","🦀Vous avez pêché 8x Crabe 🦀 (COMMUN)","🪼Vous avez pêché 1x Poulpe de mer🪼(ÉPIQUE)","🦈Vous avez pêché 2x Requin🦈 (ÉPIQUE)","🦈Vous avez pêché 5x Requin🦈 (ÉPIQUE)","🦈Vous avez pêché 8x Requin🦈 (ÉPIQUE)","🦈Vous avez pêché 1x Requin🦈 (ÉPIQUE)","🐠Vous avez pêché 1x Thon🐠 (LÉGENDAIRE)","🐠Vous avez pêché 3x Poisson-clown🐠 (LÉGENDAIRE)","🐠Vous avez pêché 3x Thon🐠 (LÉGENDAIRE)","🐠Vous avez pêché 1x Poisson-clown🐠 (LÉGENDAIRE)","🐠Vous avez pêché 8x Poisson-clown🐠 (LÉGENDAIRE)","🐠Vous avez pêché 10x Poisson-clown🐠 (LÉGENDAIRE)","🐟Vous avez pêché 1x Saumon🐟 (RARE)","🧜🏼‍♀️Vous avez pêché 5x Sirène🧜🏼‍♀️(ÉPIQUE)","🧜🏼‍♀️Vous avez pêché 2x Sirène🧜🏼‍♀️(ÉPIQUE)","🧜🏼‍♀️Vous avez pêché 1x Sirène🧜🏼‍♀️(ÉPIQUE)","🐟Vous avez pêché 3x Saumon🐟 (RARE)","🟡Vous avez pêché 1x Tilapia Dorée🟡 (MULTIPOINTS)","☠️🐋Vous avez pêché 3x Baleine Morte☠️🐋 (PERTES DE POINTS)","🐋Vous avez pêché 11x Baleine de mer🐋(COMMUN)","🐋🌈Vous avez pêché 1x Baleine Arc-en-ciel🌈🐋 (POINTS SUPPLÉMENTAIRES)","🥈VOUS AVEZ REMPORTÉ LA MÉDAILLE : PÊCHEUR ARGENT🥈","🥇VOUS AVEZ REMPORTÉ LA MÉDAILLE : PÊCHEUR OR🥇","🏅VOUS AVEZ REMPORTÉ LA MÉDAILLE : ÉTOILE DU PÊCHEUR🏅","💎Événement : /camarão💎"]

drague = ["Puis-je prendre une photo de vous ? C'est pour montrer au Père Noël ce que je veux comme cadeau.","Si le noir était la passion et le blanc était la tendresse, ce que je ressens pour toi serait un petit échiquier.","Quel est le numéro de la police ? Malheureusement, je vais devoir vous signaler pour avoir volé mon cœur.","Mes amis ont parié que je ne pourrais pas entamer une conversation avec la personne la plus belle ici. Comment devrions-nous dépenser leur argent ?","Enchanté(e), je suis un(e) voleur/voleuse. Je suis ici pour te voler ton cœur..","Les recherches indiquent que 'agente' ensemble est une faute de grammaire, mais 'a gente' séparé est une erreur du destin..","Si rien ne dure éternellement, veux-tu être mon rien ?","Ton nom est Wi-Fi ? Parce que je sens une connexion ici.","Tu vois cette étoile là-bas ? Je l'ai fait accrocher pour toi.","Alors, en plus de me couper le souffle, que fais-tu d'autre ?", "Wow j'ai mal à la poitrine ! J'espère que c'est de l'amour, car si c'est une crise cardiaque, je ne te reverrai jamais !","Les roses sont rouges, les violettes sont bleues, je ne sais pas rimer, mais puis-je sortir avec toi ?","Tu as été faite/fait avec des bougies, du miel, des rubans rouges et des roses ? Parce que je te trouve adorable."]

joke = ["Quel est le plat préféré de Thor? Thorresmo","Que fait le cheval dans la cabine téléphonique? Passer un coup de fil","Quel est le fleuve le plus acide du monde? Le Rio Solimões","Pourquoi les plongeurs plongent-ils toujours en arrière et jamais en avant ? Parce que sinon ils tombent toujours dans le bateau !.","Quel est le vin qui n'a pas d'alcool? Le vin d'œuf de caille"]

hate = ["Les gens te détestent à 0%","Les gens te détestent à 20%","Les gens te détestent à 100%","Les gens te détestent à 50%","Les gens te détestent à 45%","Les gens te détestent à 99%","Les gens te détestent à 95%","Les gens te détestent à 34%","Les gens te détestent à 77%","Les gens te détestent à 80%","Les gens te détestent à 66%","Les gens te détestent à 39%","Les gens te détestent à 20%","Les gens te détestent à 22%","Les gens te détestent à 49%"]

amour = ["Les gens t'aiment à 0%❤️","Les gens t'aiment à 20%❤️","Les gens t'aiment à 100%❤️","Les gens t'aiment à 50%❤️","Les gens t'aiment à 45%❤️","Les gens t'aiment à 99%❤️","Les gens t'aiment à 95%❤️","Les gens t'aiment à 34%❤️","Les gens t'aiment à 77%❤️","Les gens t'aiment à 80%❤️","Les gens t'aiment à 66%❤️","Les gens t'aiment à 39%❤️","Les gens t'aiment à 20%❤️","Les gens t'aiment à 22%❤️","Les gens t'aiment à 49%❤️"]


class Bot(BaseBot):
    async def on_start(self, session_metadata: SessionMetadata) -> None:
        print("funcionando")
        await self.highrise.walk_to(Position(17.5 , 0.0 , 12.5 , "FrontRight"))
    async def on_user_join(self, user: User, position: Position | AnchorPosition) -> None:
        print(f"{user.username} entrou na sala")
        wm = [f"Bienvenue 💎💎{user.username}💎💎 !",f"{user.username} Alors pret pour les cours ?🍀",f"Salut {user.username} bienvenue au Lycée📚😈🔞",f"Bienvenue {user.username} les danses sont de 1 à 95❤️!",f"Bienvenue {user.username} 💎utilise !up1 pour monter au 1er étage\n!up2 pour monter au 2eme étage\n!vip si t'es modo💎"]
        await self.highrise.chat(random.choice(wm))
        
        await self.highrise.send_emote("idle_singing")
      
        await self.highrise.send_emote("idle_singing",user.id)
      
    async def on_chat(self, user: User, message: str) -> None:
        print(f"{user.username}: {message}")  

        if message.startswith("/pescar"):
            await self.highrise.send_whisper(user.id,"Você Está Pescando 🎣...")
          
        if message.lower() == "/pecher":
           frase = random.choice(pecher)
           await self.highrise.send_whisper(user.id,frase)
        
        if message.lower() == "/bombe":
           frase = random.choice(bombe)
           await self.highrise.send_whisper(user.id,frase)
        if message.lower() == "/couteau":
           frase = random.choice(couteau)
           await self.highrise.send_whisper(user.id,frase)
        if message.lower() == "/curatif":
           frase = random.choice(curatif)
           await self.highrise.send_whisper(user.id,frase)
        if message.lower() == "/play":
           frase = random.choice(play)
           await self.highrise.send_whisper(user.id,frase)
        if message.lower() == "/tirer":
           frase = random.choice(tirer)
           await self.highrise.send_whisper(user.id,frase)

        if message.lower() == "/folie":
           frase = random.choice(folie)
           await self.highrise.send_whisper(user.id,frase)

        if message.lower() == "/mariage":
           frase = random.choice(mariage)
           await self.highrise.chat(frase)
             
        if message.startswith("/pescar"):
           await self.highrise.react("clap",user.id)

        if message.startswith("/carpa"):
           await self.highrise.react("clap",user.id)
           await self.highrise.send_whisper(user.id,"🟡Você Pescou 1x Carpa Dourada🟡 VOCÊ GANHOU A MEDALHA : (MEGA PESCADOR)")
          
        if message.startswith("/camarão"):
           await self.highrise.react("clap",user.id)
           await self.highrise.send_whisper(user.id,"💎Você Pescou 1x Camarão De Diamante💎VOCÊ GANHOU A MEDALHA : (PESCADOR MASTER DIAMANTE )")                                
        if message.startswith("/curativo"):
           await self.highrise.react("heart",user.id)

        if message.startswith("/escudo"):
           await self.highrise.react("heart",user.id)
           await self.highrise.send_whisper(user.id,f"@{user.username} 🛡 Você Usou O Escudo🛡")

        if message.lower() == "/% amour":
           frase = random.choice(amour)
           await self.highrise.send_whisper(user.id,frase)
        if message.lower() == "/% hate":
           frase = random.choice(hate)
           await self.highrise.send_whisper(user.id,frase)
      
        if message.lower() == "/joke":
           frase = random.choice(joke)
           await self.highrise.chat(frase)

        if message.lower() == "/drague":
           frase = random.choice(drague)
           await self.highrise.chat(frase)
          
        if message.startswith("/fly"):
          if user.username == "ALIOUNE_":
            await self.teleporter(message)

        if        message.startswith("/") or message.startswith("!"):
            await self.command_handler(user, message)
          
        if message.startswith("!emoteall"):
          await self.highrise.send_whisper(user.id,"Fashion All , Wrong All , Cutey All , Superpose All , Punk All , Tiktok2 All, Tiktok8 All , Tiktok9 All , Tiktok10 All , Gagging All , Blackpink All , Creepy All , Revelation All , Bashful All , Arabesque All , Party All")

        if message.startswith("!emoteall"):
          await self.highrise.send_whisper(user.id,"Pose3 All , Pose7 All , Pose5 All , Pose1 All , Enthused All , Pose8 All , Sing All , Teleport All , Telekinesis All , Casual All , Icecream All , Watch All")

        if message.startswith("!emoteall"):
          await self.highrise.send_whisper(user.id,"Zombie All , Celebrate All , Kiss All , Bow All , Snowangel All , Confused All , Charging All , Wei All , Cursing All , Greedy All , Russian All , Shop All , Model All , Ren All , Tiktok4 All , Snake All , Uwu All")

        if message.startswith("!emoteall"):
          await self.highrise.send_whisper(user.id,"Skating All , Time All , Gottago All  , Scritchy All , Bitnervous All , Jingle All , Curtsy All , Hot All , Hyped All ,Sleigh All , Surprise All, Repose All , Kawaii All , Touch All , Gift All , Pushit All , Tiktok All , Smooch All , Launch All")
          
        if message.startswith("/emote-id"):
          await self.highrise.send_whisper(user.id,"emote-gravity , idle-uwu , idle-enthusiastic , emote-kiss , emote-float , idle_singing , emote-cute , emote-pose7 , emote-pose8 , emote-fashionista , emote-creepycute , emote-headblowup , emote-shy2 , emote-celebrate , idle-nervous , idle-wild")

        if message.startswith("/emote-id"):
          await self.highrise.send_whisper(user.id,"emote-gift , dance-touch , dance-employee , dance-tiktok11 , emote-salute")
          
        if message.startswith("!list"):
            await self.highrise.send_whisper(user.id,"!angry ,!thumbsup , !cursing , !flex , !gagging , !celebrate , !blackpink , !tiktok2 , !tiktok9 , !pennywise , !russian , !shop , !enthused , !singing ,!wrong , !guitar , !pinguin , !astronaut , !saunter , !flirt , !creepy , !watch , !revelation")
          
        if message.startswith("!list"):
            await self.highrise.send_whisper(user.id,"!tiktok10 ,!tiktok8 , !cutey , !pose3 , !pose5 , !pose1 , !pose8 , !pose7  !pose9 , !cute , !superpose , !frog , !snake , !energyball , !maniac , !teleport , !float , !telekinesi , !fight , !wei , !fashion , !boxer , !bashful , !arabesque , !party")
          
        if message.startswith("!list"):
            await self.highrise.send_whisper(user.id,"!confused , !charging , !snowangel , !hot , !snowball , !curtsy , !bow ,!model , !greedy , !tired , !shy , !wave , !hello , !lau ,!yes , !sad , !no , !kiss , !casual , !ren , !sit , !punk , !zombie , !gravity , !icecream ,!uwu , !sayso , !star")

        if message.startswith("!list"):
          await self.highrise.send_whisper(user.id,"!skating , !bitnervous , !scritchy , !timejump , !gottago , !jingle , !hyped , !sleigh , !surprise , !repose , !kawaii , !touch , !gift , !pushit , !tiktok , !salute , !attention , !smooch , !launch")
          
        if message.startswith("/list"):
            await self.highrise.send_whisper(user.id,"/angry ,/thumbsup , /cursing , /flex , /gagging , /celebrate , /blackpink , /tiktok2 , /tiktok9 , /pennywise , /russian , /shop , /enthused , /singing , /wrong , /guitar , /pinguin , /astronaut , /saunter , /flirt , /creepy , /watch , /revelation")
          
        if message.startswith("/list"):
            await self.highrise.send_whisper(user.id,"/tiktok10 , /tiktok8 , /cutey , /pose3 , /pose5 , /pose1 , /pose8 , /pose7  /pose9 , /cute , /superpose , /frog , /snake , /energyball , /maniac , /teleport , /float , /telekinesi , /fight , /wei , /fashion , /boxer , /bashful , /arabesque , /party")
          
        if message.startswith("/list"):
            await self.highrise.send_whisper(user.id,"/confused , /charging , /snowangel , /hot , /snowball , /curtsy , /bow ,/model , /greedy , /lust , /tired , /shy , /wave , /hello , /lau , /yes , /sad , /no , /kiss , /casual , /ren ,   /sit , /punk , /zombie , /gravity , /icecream ,/uwu , /sayso , /star")

        if message.startswith("/list"):
          await self.highrise.send_whisper(user.id,"/skating , /bitnervous , /scritchy , /timejump , /gottago , /jingle , /hyped , /sleigh , /surprise , /repose , /kawaii /touch , /pushit , /gift , /tiktok , /salute , /attention , /smooch , /launch")
        
        if        message.startswith("/list") or         message.startswith("!emoteall") or message.startswith("!lista"):
            await self.highrise.send_emote("dance-floss")

        if        message.startswith("Feio") or      message.startswith("feio") or      message.startswith("veado") or message.startswith("Veado"):
            await self.highrise.chat(f"REPETE!!! {user.username} 🤬🤬")
            await self.highrise.send_emote("emote-swordfight")

        if        message.startswith("corno") or      message.startswith("Corno") or      message.startswith("Vagabundo") or message.startswith("vagabundo"):
            await self.highrise.chat(f"SEU PAI!!! {user.username} 🤬🤬")
            await self.highrise.send_emote("emote-swordfight")

        if        message.startswith("/pessoas") or      message.startswith("!pessoas"):
            room_users = (await self.highrise.get_room_users()).content
            await self.highrise.chat(f"Há  {len(room_users)} pessoas na sala ")
            await self.highrise.send_emote("dance-floss")
                      
        if        message.startswith("gostoso") or      message.startswith("Gostoso") or      message.startswith("GOSTOSO"):
            await self.highrise.send_emote("idle-uwu")
            await self.highrise.send_emote("idle-uwu", user.id)
            await self.highrise.chat(f"Voce tambem e gostoso(a) {user.username} 😳👉👈")

        if             message.startswith("!emotes") or message.startswith("/emotes"):
            await self.highrise.send_emote("emote-robot")
            await self.highrise.send_whisper(user.id,f"emotes disponiveis do numero 1 ao 95")

        if        message.startswith("Help") or      message.startswith("/help") or      message.startswith("!help") or message.startswith("help"):
            await self.highrise.chat(f"/list  , /drague,  /emotes, /joke  , /emote-id  , /folie , /mariage  , /% amour  , /% hate , /love , /mort , !punk" )
            await self.highrise.chat(f"{user.username} toutes les commandes peuvent etre activer par ( ! ou / )")
            await self.highrise.send_emote("dance-floss")
          
        if        message.startswith("Lindo") or      message.startswith("LINDO") or      message.startswith("lindo"):
            await self.highrise.react("heart",user.id,)
            await self.highrise.chat(f"você tambem e muito lind(a) {user.username} 🥰🥰")
            await self.highrise.send_emote("emote-shy")

        if message.startswith("!palma"):
            await self.highrise.react("clap",user.id)
          
        if        message.startswith("Bom dia") or      message.startswith("Bom Dia") or      message.startswith("bom dia") or message.startswith("BOM DIA"):
            await self.highrise.send_emote("emote-tapdance")
            await self.highrise.send_whisper(user.id,f"Bom Dia {user.username} 😊🌅")

        if        message.startswith("Boa noite") or      message.startswith("boa noite") or      message.startswith("Boa Noite") or message.startswith("BOA NOITE"):
            await self.highrise.send_emote("dance-singleladies")
            await self.highrise.send_whisper(user.id,f"Boa Noite {user.username} 😊🌃🌉")

        if message.lstrip().startswith(("/love", "/mort", "!punk")):
          response = await self.highrise.get_room_users()
          users = [content[0] for content in response.content]
          usernames = [user.username.lower() for user in users]
          parts = message[1:].split()
          args = parts[1:]

          if len(args) < 1:
              await self.highrise.send_whisper(user.id, f"Kullanım: !{parçalar[0]} <@kullanıcı adı>")
              return
          elif args[0][0] != "@":
              await self.highrise.send_whisper(user.id, f"Format invalide. Utilise '@username'.")
              return
          elif args[0][1:].lower() not in usernames:
              await self.highrise.chat(user.id, f"{args[0][1:]} n'est pas dans la salle.")
              return

          user_id = next((u.id for u in users if u.username.lower() == args[0][1:].lower()), None)
          if not user_id:
              await self.highrise.chat(user.id, f"Utilisateur {args[0][1:]} non trouvé")
              return

          try:
              if message.startswith("/love"):
                  await self.highrise.chat(f"\n @{user.username} et @{args[0][1:]} votre pourcentage d'amour est de {random.randint(0, 100)}%")
                  await self.highrise.send_emote("emote-lust", user.id)
                  await self.highrise.send_emote("emote-lust", user_id)
              elif message.startswith("/mort"):
                  await self.highrise.chat(f"\n @{user.username} et @{args[0][1:]} votre année de mort est {random.randint(2024, 2105)}")
                  await self.highrise.send_emote("idle-uwu", user.id)
                  await self.highrise.send_emote("idle-uwu", user_id)
              elif message.startswith("!punk"):
                  await self.highrise.chat(f"\n Hey @{user.username} ve @{args[0][1:]} ooo çok havalilar")
                  await self.highrise.send_emote("emote-punkguitar", user.id)
                  await self.highrise.send_emote("emote-punkguitar", user_id)
          except Exception as e:
              print(f"An exception occurred[Due To {parts[0][1:]}]: {e}")

        if        message.startswith("Boa tarde") or      message.startswith("boa tarde") or      message.startswith("Boa Tarde") or message.startswith("BOA TARDE"):
            await self.highrise.send_emote("emote-monster_fail")
            await self.highrise.send_whisper(user.id,f"Boa Tarde {user.username} ☀️")

        if        message.startswith("😡") or      message.startswith("🤬") or      message.startswith("😤") or             message.startswith("🤨") or             message.startswith("😒") or message.startswith("🙄"):
            await self.highrise.send_emote("emote-boxer",user.id)
   
        if        message.startswith("🤔") or      message.startswith("🧐") or      message.startswith("🥸") or             message.startswith("🫤") or message.startswith("😕"):
            await self.highrise.send_emote("emote-confused",user.id)

        if        message.startswith("🤣") or      message.startswith("😂") or      message.startswith("😁") or message.startswith("😀"):
            await self.highrise.send_emote("emote-laughing",user.id)

        if        message.startswith("😗") or      message.startswith("😘") or      message.startswith("😙") or             message.startswith("💋") or             message.startswith("😚"):
            await self.highrise.send_emote("emote-kiss",user.id)

        if        message.startswith("😊") or      message.startswith("🥰") or      message.startswith("😳") or message.startswith("🤗"):
            await self.highrise.send_emote("idle-uwu",user.id)

        if        message.startswith("🤢") or      message.startswith("🤮") or      message.startswith("🤧") or             message.startswith("😵‍💫") or message.startswith("🤒"):
            await self.highrise.send_emote("emoji-gagging",user.id)

        if        message.startswith("😱") or      message.startswith("😬") or      message.startswith("😰") or             message.startswith("😫") or message.startswith("😨"):
            await self.highrise.send_emote("idle-nervous",user.id)

        if message.startswith("🤯"):
            await self.highrise.send_emote("emote-headblowup",user.id)

        if        message.startswith("☺️") or      message.startswith("🫣") or       message.startswith("😍") or      message.startswith("🥺") or message.startswith("🥹"):
            await self.highrise.send_emote("emote-shy2",user.id)

        if        message.startswith("😏") or message.startswith("😈"):
            await self.highrise.send_emote("emote-lust",user.id)           

        if        message.startswith("🥵") or message.startswith("🫠"):
            await self.highrise.send_emote("emote-hot",user.id)
          
        if        message.startswith("/thumbs") or      message.startswith("!thumbs") or      message.startswith("Thumbs") or message.startswith("Like"):
            await self.highrise.react("thumbs",user.id,)                    
        if        message.startswith("/clap") or      message.startswith("!clap") or      message.startswith("Clap") or message.startswith("Palma"):
            await self.highrise.react("clap",user.id,)
          
        if        message.startswith("/wave") or      message.startswith("!wave") or      message.startswith("wave") or message.startswith("Tchau"):
            await self.highrise.react("wave",user.id,)
        
        if        message.startswith("/heart") or      message.startswith("!heart") or      message.startswith("Heart") or message.startswith("Amor"):
            await self.highrise.react("heart",user.id,)
             
        if        message.startswith("/wink") or      message.startswith("!wink") or      message.startswith("wink") or message.startswith("Piscar"):
            await self.highrise.react("wink",user.id,)
          
        if        message.startswith("!wrong") or      message.startswith("/wrong") or      message.startswith("Wrong") or message.startswith("1"):
            await self.highrise.send_emote("dance-wrong",user.id)
            

        if        message.startswith("/fashion") or      message.startswith("!fashion") or      message.startswith("Fashion") or message.startswith("2"):
            await self.highrise.send_emote("emote-fashionista",user.id)
            

        if        message.startswith("/gravity") or      message.startswith("!gravity") or      message.startswith("Gravity") or message.startswith("3"):
            await self.highrise.send_emote("emote-gravity",user.id)
            

        if        message.startswith("/icecream") or      message.startswith("!icecream") or      message.startswith("Icecream") or message.startswith("4"):
            await self.highrise.send_emote("dance-icecream",user.id)
            

        if        message.startswith("/casual") or      message.startswith("!casual") or      message.startswith("Casual") or message.startswith("5"):
            await self.highrise.send_emote("idle-dance-casual",user.id)
            

        if        message.startswith("/kiss") or      message.startswith("!kiss") or      message.startswith("Kiss") or message.startswith("6"):
            await self.highrise.send_emote("emote-kiss",user.id)
            

        if        message.startswith("/no") or      message.startswith("!no") or      message.startswith("No") or message.startswith("7"):
            await self.highrise.send_emote("emote-no",user.id)
            

        if        message.startswith("/sad") or      message.startswith("!sad") or      message.startswith("Sad") or message.startswith("8"):
            await self.highrise.send_emote("emote-sad",user.id)
          

        if        message.startswith("/yes") or      message.startswith("!yes") or      message.startswith("Yes") or message.startswith("9"):
            await self.highrise.send_emote("emote-yes",user.id)
          

        if        message.startswith("/lau") or      message.startswith("!lau") or      message.startswith("Lau") or message.startswith("10"):
            await self.highrise.send_emote("emote-laughing",user.id)
          

        if        message.startswith("/hello") or      message.startswith("!hello") or      message.startswith("Hello") or message.startswith("11"):
            await self.highrise.send_emote("emote-hello",user.id)
          

        if        message.startswith("/wave") or      message.startswith("!wave") or      message.startswith("Wave") or message.startswith("12"):
            await self.highrise.send_emote("emote-wave",user.id)
            

        if        message.startswith("/shy") or      message.startswith("!shy") or      message.startswith("Shy") or message.startswith("13"):
            await self.highrise.send_emote("emote-shy",user.id)
          

        if        message.startswith("/Tired") or      message.startswith("!Tired") or      message.startswith("Tired") or message.startswith("14"):
            await self.highrise.send_emote("emote-tired",user.id)
          

        if        message.startswith("/flirt") or      message.startswith("!flirt") or      message.startswith("Flirt") or          message.startswith("/Flirty") or           message.startswith("!Flirty") or           message.startswith("Flirty") or       message.startswith("!flirtywave") or    message.startswith("/flirtywave") or    message.startswith("Flirtywave") or message.startswith("15"):
            await self.highrise.send_emote("emote-lust",user.id)
          

        if        message.startswith("/greedy") or      message.startswith("!greedy") or      message.startswith("Greedy") or message.startswith("16"):
            await self.highrise.send_emote("emote-greedy",user.id)
          

        if        message.startswith("/model") or      message.startswith("!model") or      message.startswith("Model") or message.startswith("17"):
            await self.highrise.send_emote("emote-model",user.id)
          

        if        message.startswith("/bow") or      message.startswith("!bow") or      message.startswith("Bow") or message.startswith("18"):
            await self.highrise.send_emote("emote-bow",user.id)
          

        if        message.startswith("/curtsy") or      message.startswith("!curtsy") or      message.startswith("Curtsy") or message.startswith("19"):
            await self.highrise.send_emote("emote-curtsy",user.id)
          

        if        message.startswith("/snowball") or      message.startswith("!snowball") or      message.startswith("Snowball") or message.startswith("20"):
            await self.highrise.send_emote("emote-snowball",user.id)
          

        if        message.startswith("/hot") or      message.startswith("!hot") or      message.startswith("Hot") or message.startswith("21"):
            await self.highrise.send_emote("emote-hot",user.id)
          

        if        message.startswith("/snowangel") or      message.startswith("!snowangel") or      message.startswith("Snowangel") or message.startswith("22"):
            await self.highrise.send_emote("emote-snowangel",user.id)
          

        if        message.startswith("/charging") or      message.startswith("!charging") or      message.startswith("Charging") or message.startswith("23"):
            await self.highrise.send_emote("emote-charging",user.id)
          

        if        message.startswith("/confused") or      message.startswith("!confused") or      message.startswith("Confused") or message.startswith("24"):
            await self.highrise.send_emote("emote-confused",user.id)
          

        if        message.startswith("/telekinesis") or      message.startswith("!telekinesis") or      message.startswith("Telekinesis") or message.startswith("25"):
            await self.highrise.send_emote("emote-telekinesis",user.id)
            

        if        message.startswith("/float") or      message.startswith("!float") or      message.startswith("Float") or message.startswith("26"):
            await self.highrise.send_emote("emote-float",user.id)
            

        if        message.startswith("/teleport") or      message.startswith("!teleport") or      message.startswith("Teleport") or message.startswith("27"):
            await self.highrise.send_emote("emote-teleporting",user.id)
            

        if        message.startswith("/maniac") or      message.startswith("!maniac") or      message.startswith("Maniac") or message.startswith("28"):
            await self.highrise.send_emote("emote-maniac",user.id)
            

        if        message.startswith("/energyball") or      message.startswith("!energyball") or      message.startswith("Energyball") or message.startswith("29"):
            await self.highrise.send_emote("emote-energyball",user.id)
            

        if        message.startswith("/snake") or      message.startswith("!snake") or      message.startswith("Snake") or message.startswith("30"):
            await self.highrise.send_emote("emote-snake",user.id)
            

        if        message.startswith("/frog") or      message.startswith("!frog") or      message.startswith("Frog") or message.startswith("31"):
            await self.highrise.send_emote("emote-frog",user.id)
            

        if        message.startswith("/superpose") or      message.startswith("!superpose") or      message.startswith("Superpose") or message.startswith("32"):
            await self.highrise.send_emote("emote-superpose",user.id)
        

        if        message.startswith("/cute") or      message.startswith("!cute") or      message.startswith("Cute") or message.startswith("33"):
            await self.highrise.send_emote("emote-cute",user.id)
            

        if        message.startswith("/pose7") or      message.startswith("!pose7") or      message.startswith("Pose7") or message.startswith("34"):
            await self.highrise.send_emote("emote-pose7",user.id)
            

        if        message.startswith("/pose8") or      message.startswith("!pose8") or      message.startswith("Pose8") or message.startswith("35"):
            await self.highrise.send_emote("emote-pose8",user.id)
            

        if        message.startswith("/pose1") or      message.startswith("!pose1") or      message.startswith("Pose1") or message.startswith("36"):
            await self.highrise.send_emote("emote-pose1",user.id)
            

        if        message.startswith("/pose5") or      message.startswith("!pose5") or      message.startswith("Pose5") or message.startswith("37"):
            await self.highrise.send_emote("emote-pose5",user.id)
            

        if        message.startswith("/pose3") or      message.startswith("!pose3") or      message.startswith("Pose3") or message.startswith("38"):
            await self.highrise.send_emote("emote-pose3",user.id)
            

        if        message.startswith("/cutey") or      message.startswith("!cutey") or      message.startswith("Cutey") or message.startswith("39"):
            await self.highrise.send_emote("emote-cutey",user.id)
            

        if        message.startswith("/tik10") or      message.startswith("!tik10") or      message.startswith("Tik10") or message.startswith("40"):
            await self.highrise.send_emote("dance-tiktok10",user.id)
            

        if        message.startswith("/sing") or      message.startswith("!sing") or          message.startswith("Sing") or           message.startswith("Singing") or       message.startswith("/singing") or   message.startswith("!singing") or message.startswith("41"):
            await self.highrise.send_emote("idle_singing",user.id)
            

        if        message.startswith("/enthused") or      message.startswith("!enthused") or      message.startswith("Enthused") or message.startswith("42"):
            await self.highrise.send_emote("idle-enthusiastic",user.id)
            

        if        message.startswith("/shop") or      message.startswith("!shop") or      message.startswith("Shop") or message.startswith("43"):
            await self.highrise.send_emote("dance-shoppingcart",user.id)
            

        if        message.startswith("/russian") or      message.startswith("!russian") or      message.startswith("Russian") or message.startswith("44"):
            await self.highrise.send_emote("dance-russian",user.id)
            

        if        message.startswith("/pennywise") or      message.startswith("!pennywise") or      message.startswith("Pennywise") or message.startswith("45"):
            await self.highrise.send_emote("dance-pennywise",user.id)
            

        if        message.startswith("/tik2") or      message.startswith("!tik2") or      message.startswith("Tik2") or message.startswith("46"):
            await self.highrise.send_emote("dance-tiktok2",user.id)
          

        if        message.startswith("/blackpink") or      message.startswith("!blackpink") or      message.startswith("Blackpink") or message.startswith("47"):
            await self.highrise.send_emote("dance-blackpink",user.id)
            

        if        message.startswith("/celebrate") or      message.startswith("!celebrate") or      message.startswith("Celebrate") or message.startswith("48"):
            await self.highrise.send_emote("emoji-celebrate",user.id)
            

        if        message.startswith("/gagging") or      message.startswith("!gagging") or      message.startswith("Gagging") or message.startswith("49"):
            await self.highrise.send_emote("emoji-gagging",user.id)
            

        if        message.startswith("/flex") or      message.startswith("!flex") or      message.startswith("Flex") or message.startswith("50"):
            await self.highrise.send_emote("emoji-flex",user.id)
            

        if        message.startswith("/cursing") or      message.startswith("!cursing") or      message.startswith("Cursing") or message.startswith("51"):
            await self.highrise.send_emote("emoji-cursing",user.id)
            

        if        message.startswith("/thumbsup") or      message.startswith("!thumbsup") or      message.startswith("Thumbsup") or message.startswith("52"):
            await self.highrise.send_emote("emoji-thumbsup",user.id)
            

        if        message.startswith("/angry") or      message.startswith("!angry") or      message.startswith("Angry") or message.startswith("53"):
            await self.highrise.send_emote("emoji-angry",user.id)
            

        if        message.startswith("/punk") or      message.startswith("!punk") or      message.startswith("Punk") or message.startswith("54"):
            await self.highrise.send_emote("emote-punkguitar",user.id)
            

        if        message.startswith("/zombie") or      message.startswith("!zombie") or      message.startswith("Zombie") or message.startswith("55"):
            await self.highrise.send_emote("emote-zombierun",user.id)
            

        if        message.startswith("/sit") or      message.startswith("!sit") or      message.startswith("Sit") or message.startswith("56"):
            await self.highrise.send_emote("idle-loop-sitfloor",user.id)
            

        if        message.startswith("/fight") or      message.startswith("!fight") or      message.startswith("Fight") or message.startswith("57"):
            await self.highrise.send_emote("emote-swordfight",user.id)
            

        if        message.startswith("/ren") or      message.startswith("!ren") or      message.startswith("Ren") or message.startswith("58"):
            await self.highrise.send_emote("dance-macarena",user.id)
            

        if        message.startswith("/wei") or      message.startswith("!wei") or      message.startswith("Wei") or message.startswith("59"):
            await self.highrise.send_emote("dance-weird",user.id)
            

        if        message.startswith("/tik8") or      message.startswith("!tik8") or      message.startswith("Tik8") or           message.startswith("/savage") or           message.startswith("!savage") or           message.startswith("Savage") or message.startswith("60"):
            await self.highrise.send_emote("dance-tiktok8",user.id)
            

        if        message.startswith("/tik9") or      message.startswith("!tik9") or      message.startswith("Tik9") or           message.startswith("/viral") or           message.startswith("!viral") or           message.startswith("Viral") or  message.startswith("61"):
            await self.highrise.send_emote("dance-tiktok9",user.id)
          

        if        message.startswith("/uwu") or      message.startswith("!uwu") or      message.startswith("Uwu") or message.startswith("62"):
            await self.highrise.send_emote("idle-uwu",user.id)
            

        if        message.startswith("/tik4") or      message.startswith("!tik4") or      message.startswith("Tik4") or               message.startswith("/sayso") or               message.startswith("!sayso") or               message.startswith("Sayso") or message.startswith("63"):
            await self.highrise.send_emote("idle-dance-tiktok4",user.id)
            

        if        message.startswith("/star") or      message.startswith("!star") or      message.startswith("Star") or message.startswith("64"):
            await self.highrise.send_emote("emote-stargazer",user.id)
            

        if        message.startswith("/pose9") or      message.startswith("!pose9") or      message.startswith("Pose9") or message.startswith("65"):
            await self.highrise.send_emote("emote-pose9",user.id)
            

        if        message.startswith("/boxer") or      message.startswith("!boxer") or      message.startswith("Boxer") or message.startswith("66"):
            await self.highrise.send_emote("emote-boxer",user.id)
            

        if        message.startswith("/guitar") or      message.startswith("!guitar") or      message.startswith("Guitar") or message.startswith("67"):
            await self.highrise.send_emote("idle-guitar",user.id)
            

        if        message.startswith("/penguin") or      message.startswith("!penguin") or      message.startswith("Penguin") or message.startswith("68"):
            await self.highrise.send_emote("dance-pinguin",user.id)
            

        if        message.startswith("/astronaut") or      message.startswith("!astronaut") or      message.startswith("Astronaut") or message.startswith("69"):
            await self.highrise.send_emote("emote-astronaut",user.id)
            

        if        message.startswith("/saunter") or      message.startswith("!saunter") or      message.startswith("Saunter") or               message.startswith("/anime") or               message.startswith("!anime") or               message.startswith("Anime") or   message.startswith("70"):
            await self.highrise.send_emote("dance-anime",user.id)
            

        if        message.startswith("/creepy") or      message.startswith("!creepy") or      message.startswith("Creepy") or message.startswith("71"):
            await self.highrise.send_emote("dance-creepypuppet",user.id)
          

        if        message.startswith("/watch") or      message.startswith("!watch") or      message.startswith("Watch") or message.startswith("72"):
            await self.highrise.send_emote("emote-creepycute",user.id)
            

        if        message.startswith("/revelations") or      message.startswith("!revelations") or      message.startswith("Revelations") or message.startswith("73"):
            await self.highrise.send_emote("emote-headblowup",user.id)
            

        if        message.startswith("/bashful") or      message.startswith("!bashful") or      message.startswith("Bashful") or message.startswith("74"):
            await self.highrise.send_emote("emote-shy2",user.id)
            

        if        message.startswith("/arabesque") or      message.startswith("!arabesque") or      message.startswith("Arabesque") or message.startswith("75"):
            await self.highrise.send_emote("emote-pose10",user.id)
            

        if        message.startswith("/party") or      message.startswith("!party") or      message.startswith("Party") or message.startswith("76"):
            await self.highrise.send_emote("emote-celebrate",user.id)
            

        if        message.startswith("/skating") or      message.startswith("!skating") or      message.startswith("Skating") or message.startswith("77"):
            await self.highrise.send_emote("emote-iceskating",user.id)
            

        if        message.startswith("/scritchy") or      message.startswith("!scritchy") or      message.startswith("Scritchy") or message.startswith("78"):
            await self.highrise.send_emote("idle-wild",user.id)
            

        if        message.startswith("/bitnervous") or      message.startswith("!bitnervous") or      message.startswith("Bitnervous") or               message.startswith("!nervous") or               message.startswith("/nervous") or               message.startswith("Nervous") or message.startswith("79"):
            await self.highrise.send_emote("idle-nervous",user.id)
            

        if        message.startswith("/timejump") or      message.startswith("!timejump") or      message.startswith("Timejump") or message.startswith("80"):
            await self.highrise.send_emote("emote-timejump",user.id)
            

        if        message.startswith("/gottago") or      message.startswith("!gottago") or      message.startswith("Gottago") or message.startswith("81"):
            await self.highrise.send_emote("idle-toilet",user.id)
            

        if        message.startswith("/jingle") or      message.startswith("!jingle") or      message.startswith("Jingle") or message.startswith("82"):
            await self.highrise.send_emote("dance-jinglebell",user.id)
            

        if        message.startswith("/hyped") or      message.startswith("!hyped") or      message.startswith("Hyped") or message.startswith("83"):
            await self.highrise.send_emote("emote-hyped",user.id)
            

        if        message.startswith("/sleigh") or      message.startswith("!sleigh") or      message.startswith("Sleigh") or message.startswith("84"):
            await self.highrise.send_emote("emote-sleigh",user.id)
            

        if        message.startswith("/surprise") or      message.startswith("!surprise") or      message.startswith("Surprise") or message.startswith("85"):
            await self.highrise.send_emote("emote-pose6",user.id)
            
          
        if        message.startswith("/repose") or      message.startswith("!repose") or      message.startswith("Repose") or message.startswith("86"):
            await self.highrise.send_emote("sit-relaxed",user.id)

        if        message.startswith("/kawaii") or      message.startswith("!kawaii") or      message.startswith("Kawaii") or message.startswith("87"):
            await self.highrise.send_emote("dance-kawai",user.id)

        if        message.startswith("/touch") or      message.startswith("!touch") or      message.startswith("Touch") or message.startswith("88"):
            await self.highrise.send_emote("dance-touch",user.id)

        if        message.startswith("/gift") or      message.startswith("!gift") or      message.startswith("Gift") or message.startswith("89"):
            await self.highrise.send_emote("emote-gift",user.id)

        if        message.startswith("/pushit") or      message.startswith("!pushit") or      message.startswith("Pushit") or message.startswith("90"):
            await self.highrise.send_emote("dance-employee",user.id)

        if        message.startswith("salute") or      message.startswith("!salute") or      message.startswith("Salute") or message.startswith("91"):
            await self.highrise.send_emote("emote-cutesalute",user.id)

        if        message.startswith("/attention") or      message.startswith("!attention") or      message.startswith("Attention") or message.startswith("92"):
            await self.highrise.send_emote("emote-salute",user.id)

        if        message.startswith("/tiktok") or      message.startswith("!tiktok") or      message.startswith("Tiktok") or message.startswith("93"):
            await self.highrise.send_emote("dance-tiktok11",user.id)

        if        message.startswith("/smooch") or      message.startswith("!smooch") or      message.startswith("Smooch") or message.startswith("94"):
            await self.highrise.send_emote("emote-kissing-bound",user.id)

        if        message.startswith("/launch") or      message.startswith("!launch") or      message.startswith("Launch") or message.startswith("95"):
            await self.highrise.send_emote("emote-launch",user.id)

        if message.startswith("Launch All"):
          if user.username == "R0__Sa":
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("emote-launch", roomUser.id)

        if message.startswith("Smooch All"):
          if user.username == "R0__Sa":
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("emote-kissing-bound", roomUser.id)

        if message.startswith("Pushit All"):
          if user.username == "R0__Sa":
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("dance-employee", roomUser.id)

        if message.startswith("Gift All"):
          if user.username == "R0__Sa":
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("emote-gift", roomUser.id)

        if message.startswith("Attention All"):
          if user.username == "R0__Sa":
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("emote-salute", roomUser.id)

        if message.startswith("Salute All"):
          if user.username == "R0__Sa":
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("emote-cutesalute", roomUser.id)

        if message.startswith("Tiktok All"):
          if user.username == "R0__Sa":
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("dance-tiktok11", roomUser.id)
          
        if message.startswith("Touch All"):
          if user.username == "R0__Sa":
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("dance-touch", roomUser.id)
              
        if message.startswith("Kawaii All"):
          if user.username == "R0__Sa":
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("dance-kawai", roomUser.id)
          
        if message.startswith("Hot All"):
          if user.username == "R0__Sa":
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("emote-hot", roomUser.id)
      
      
        if message.startswith("Curtsy All"):
          if user.username == "R0__Sa":
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("emote-curtsy", roomUser.id)

        if message.startswith("Surprise All"):
          if user.username == "R0__Sa":
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("emote-pose6", roomUser.id)

        if message.startswith("Jingle All"):
          if user.username == "R0__Sa":
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("dance-jinglebell", roomUser.id)

        if message.startswith("Creepy All"):
          if user.username == "ALIOUNE_":
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("dance-creepypuppet", roomUser.id)

        if message.startswith("Bitnervous All"):
          if user.username == "ALIOUNE_":
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("idle-nervous", roomUser.id)

        if message.startswith("Scritchy All"):
          if user.username == "ALIOUNE_":
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("idle-wild", roomUser.id)
              
        if message.startswith("Fashion All"):
          if user.username == "ALIOUNE_":
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("emote-fashionista", roomUser.id)
                
        if message.startswith("Wrong All"):
          if user.username == "ALIOUNE_":
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("dance-wrong", roomUser.id)

        if message.startswith("Cutey All"):
          if user.username == "ALIOUNE_":
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("emote-cutey", roomUser.id)

        if message.startswith("Hyped All"):
          if user.username == "ALIOUNE_":
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("emote-hyped", roomUser.id)
                
        if message.startswith("Superpose All"):
          if user.username == "ALIOUNE_":
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("emote-superpose", roomUser.id)

        if message.startswith("Punk All"):
          if user.username == "ALIOUNE_":
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("emote-punkguitar", roomUser.id) 
                
        if message.startswith("Tiktok2 All"):
          if user.username == "ALIOUNE_":
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("dance-tiktok2", roomUser.id)
                
        if                            message.startswith("Savage All") or   message.startswith("Tiktok8 All"):
          if user.username == "ALIOUNE_":
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("dance-tiktok8", roomUser.id)
                
        if message.startswith("Tiktok10 All"):
          if user.username == "ALIOUNE_":
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("dance-tiktok10", roomUser.id)
                
        if                            message.startswith("Viral All") or          message.startswith("Viralgroove All") or  message.startswith("Tiktok9 All"):
          if user.username == "ALIOUNE_":
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("dance-tiktok9", roomUser.id)
                
        if message.startswith("Blackpink All"):
          if user.username == "ALIOUNE_":
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("dance-blackpink", roomUser.id)             
        if message.startswith("Gagging All"):
          if user.username == "ALIOUNE_":
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("emoji-gagging", roomUser.id)

        if message.startswith("Pose3 All"):
          if user.username == "ALIOUNE_":
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("emote-pose3", roomUser.id)

        if message.startswith("Pose7 All"):
          if user.username == "ALIOUNE_":
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("emote-pose7", roomUser.id)

        if message.startswith("Pose5 All"):
          if user.username == "ALIOUNE_":
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("emote-pose5", roomUser.id)

        if message.startswith("Pose1 All"):
          if user.username == "ALIOUNE_":
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("emote-pose1", roomUser.id)

        if message.startswith("Pose8 All"):
          if user.username == "ALIOUNE_":
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("emote-pose8", roomUser.id)
     
        if message.startswith("Enthused All"):
          if user.username == "ALIOUNE_":
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("idle-enthusiastic", roomUser.id)
                
        if message.startswith("Sing All"):
          if user.username == "ALIOUNE_":
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("idle_singing", roomUser.id)

        if message.startswith("Teleport All"):
          if user.username == "ALIOUNE_":
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("emote-teleporting", roomUser.id)
                
        if message.startswith("Telekinesis All"):
          if user.username == "ALIOUNE_":
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("emote-telekinesis", roomUser.id)

        if message.startswith("Casual All"):
          if user.username == "ALIOUNE_":
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("idle-dance-casual", roomUser.id)
                
        if message.startswith("Icecream All"):
          if user.username == "ALIOUNE_":
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("dance-icecream", roomUser.id)
                   
        if message.startswith("Zombie All"):
          if user.username == "ALIOUNE_":
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("emote-zombierun", roomUser.id)

        if message.startswith("Celebrate All"):
          if user.username == "ALIOUNE_":
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("emoji-celebrate", roomUser.id)

        if message.startswith("Kiss All"):
          if user.username == "ALIOUNE_":
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("emote-kiss", roomUser.id)

        if message.startswith("Snowangel All"):
          if user.username == "ALIOUNE_":
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("emote-snowangel", roomUser.id)

        if message.startswith("Bow All"):
          if user.username == "ALIOUNE_":
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("emote-bow", roomUser.id)

        if message.startswith("Skating All"):
          if user.username == "ALIOUNE_":
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("emote-iceskating", roomUser.id)

        if message.startswith("Confused All"):
          if user.username == "ALIOUNE_":
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("emote-confused", roomUser.id)

        if message.startswith("Charging All"):
          if user.username == "ALIOUNE_":
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("emote-charging", roomUser.id)

        if message.startswith("Wei All"):
          if user.username == "ALIOUNE_":
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("dance-weird", roomUser.id)

        if message.startswith("Greedy All"):
          if user.username == "ALIOUNE_":
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("emote-greedy", roomUser.id)

        if message.startswith("Cursing All"):
          if user.username == "ALIOUNE_":
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("emoji-cursing", roomUser.id)

        if message.startswith("Russian All"):
          if user.username == "ALIOUNE_":
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("dance-russian", roomUser.id)

        if message.startswith("Repose All"):
          if user.username == "ALIOUNE_":
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("sit-relaxed", roomUser.id)
                
        if message.startswith("Shop All"):
          if user.username == "ALIOUNE_":
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("dance-shoppingcart", roomUser.id)

        if message.startswith("Ren All"):
          if user.username == "ALIOUNE_":
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("dance-macarena", roomUser.id)

        if message.startswith("Snake All"):
          if user.username == "ALIOUNE_":
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("emote-snake", roomUser.id)

        if message.startswith("Model All"):
          if user.username == "ALIOUNE_":
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("emote-model", roomUser.id)

        if message.startswith("Sleigh All"):
          if user.username == "R0__Sa":
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("emote-sleigh", roomUser.id)

        if message.startswith("Tiktok4 All"):
          if user.username == "R0__Sa":
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("idle-dance-tiktok4", roomUser.id)

        if message.startswith("Uwu All"):
          if user.username == "R0__Sa":
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("idle-uwu", roomUser.id)

        if message.startswith("Star All"):
          if user.username == "R0__Sa":
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("emote-stargazer", roomUser.id)

        if message.startswith("Pose9 All"):
          if user.username == "R0__Sa":
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("emote-pose9", roomUser.id)

        if message.startswith("Boxer All"):
          if user.username == "R0__Sa":
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("emote-boxer", roomUser.id)

        if message.startswith("Guitar All"):
          if user.username == "R0__Sa":
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("idle-guitar", roomUser.id)

        if message.startswith("Penguin All"):
          if user.username == "R0__Sa":
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("dance-pinguin", roomUser.id)

        if message.startswith("Zero All"):
          if user.username == "R0__Sa":
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("emote-astronaut", roomUser.id)

        if message.startswith("Saunter All"):
          if user.username == "R0__Sa":
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("dance-anime", roomUser.id)

        if message.startswith("Flirt All"):
          if user.username == "R0__Sa":
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("emote-lust", roomUser.id)

        if message.startswith("Watch All"):
          if user.username == "R0__Sa":
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("emote-creepycute", roomUser.id)

        if message.startswith("Revelation All"):
          if user.username == "R0__Sa":
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("emote-headblowup", roomUser.id)

        if message.startswith("Bashful All"):
          if user.username == "R0__Sa":
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("emote-shy2", roomUser.id)

        if message.startswith("Arabesque All"):
          if user.username == "R0__Sa":
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("emote-pose10", roomUser.id)

        if message.startswith("Party All"):
          if user.username == "R0__Sa":
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("emote-celebrate", roomUser.id)

        if message.startswith("Time All"):
          if user.username == "R0__Sa":
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("emote-timejump", roomUser.id)

        if message.startswith("Gottago All"):
          if user.username == "R0__YA":
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("idle-toilet", roomUser.id)
                  
        if message.startswith("/cardapio1"):
            await self.highrise.send_whisper(user.id,"esse é o nosso cardapio de bebidas espero que goste 😄")
                                     
        if message.startswith("/cardapio1"):
            await self.highrise.send_whisper(user.id,"/tequila , /gim , /vinho , /vinho-branco , /vodka , /whisky , /rum , /champanhe , /cachaça /conhaque , /cerveja , /coca-cola , /suco , /agua , /agua-de-coco , /toddy , /nescau")

        if message.startswith("/coca-cola"):  
            await self.highrise.send_whisper(user.id,f"{user.username} aqui está sua deliciosa coca cola gelada 🧊🥤 ")
            await self.highrise.react("thumbs", user.id)

        if message.startswith("/toddy"):  
            await self.highrise.send_whisper(user.id,f"{user.username} aki está seu delicioso toddy 🥛")
            await self.highrise.react("thumbs", user.id)
          
        if message.startswith("/suco"):  
            await self.highrise.send_whisper(user.id,f"{user.username} aqui está seu delicioso suco natural 🧃")
            await self.highrise.react("thumbs", user.id)
        if message.startswith("/agua"):  
            await self.highrise.send_whisper(user.id,f"🌊aqui está sua deliciosa agua {user.username} diretamente da toneira 🌊")
            await self.highrise.react("thumbs", user.id)

        if message.startswith("/agua-de-coco"):  
            await self.highrise.send_whisper(user.id,f"🥥aki está sua aguá de coco {user.username} aproveite que está deliciosa 🥥")
            await self.highrise.react("thumbs", user.id)
          
        if message.startswith("/nescau"):  
            await self.highrise.send_whisper(user.id,f"aqui está {user.username} seu delicioso nescau 🥛")
            await self.highrise.react("thumbs", user.id)
          
        if message.startswith("/tequila"):  
            await self.highrise.send_whisper(user.id,f"{user.username} se deliciando na Tequila 😄🥃")
            await self.highrise.react("thumbs", user.id)
          
        if message.startswith("/gim"):
            await self.highrise.send_whisper(user.id,f"vira vira todo o gim {user.username} 🥃")
            await self.highrise.react("thumbs", user.id)

        if message.startswith("/conhaque"):  
            await self.highrise.send_whisper(user.id,f"Aqui Está Seu conhaque {user.username} 🥃🥃")
            await self.highrise.react("thumbs", user.id)

        if message.startswith("/whisky"):  
            await self.highrise.send_whisper(user.id,f"Aqui Está seu Whisky  {user.username} 🥃")
            await self.highrise.react("thumbs", user.id)

        if message.startswith("/rum"):  
            await self.highrise.send_whisper(user.id,f"Aqui Está seu Rum 🥃 {user.username}")
            await self.highrise.react("thumbs", user.id)
          
        if message.startswith("/cachaça"):  
            await self.highrise.send_whisper(user.id,f"Aqui Está a Sua Cachaça {user.username} não beba muito 🥃")
            await self.highrise.react("thumbs", user.id)

        if message.startswith("/vodka"):  
            await self.highrise.send_whisper(user.id,f"Aqui Está Sua  Vodka {user.username} ")
            await self.highrise.react("thumbs", user.id)
           
        if message.startswith("/champanhe"):  
            await self.highrise.send_whisper(user.id,f"Aqui Está Sua Champanhe {user.username} 🍾🥂")
            await self.highrise.react("thumbs", user.id)

        if message.startswith("/cerveja"):  
            await self.highrise.send_whisper(user.id,f"Aqui Está Sua Cerveja {user.username} 🍺")
            await self.highrise.react("thumbs", user.id)

        if message.startswith("/vinho-branco"):  
            await self.highrise.send_whisper(user.id,f"Aqui Está Seu Vinho-Branco {user.username}")
            await self.highrise.react("thumbs", user.id)

        if message.startswith("/vinho"):  
            await self.highrise.send_whisper(user.id,f"Aqui Está Seu Vinho {user.username}")
            await self.highrise.react("thumbs", user.id)

        if message.startswith("/cardapio2"):
            await self.highrise.send_whisper(user.id,"esse é o nosso cardapio de comidas e petiscos espero que goste 😄")
                                     
        if message.startswith("/cardapio2"):
            await self.highrise.send_whisper(user.id,"/camarão , /salada-de-alface , /salada-de-repolho , /macarrão , /pizza , /bolo-de-cenoura")

        if message.startswith("/cardapio2"):
            await self.highrise.send_whisper(user.id,"/bolo-de-morango , /açai , /sorvete , /cupcake , /sorvete , /batata-frita , /espetinho , /pão-de-alho")

        if message.startswith("/pizza"):  
            await self.highrise.send_whisper(user.id,f"{user.username} aqui está sua deliciosa pizza 🍕")
            await self.highrise.react("thumbs", user.id)
          
        if message.startswith("/bolo-de-morango"):
            await self.highrise.send_whisper(user.id,f"Aqui Está seu Delicioso Bolo de Morango {user.username} 🍰")
            await self.highrise.react("thumbs", user.id)

        if message.startswith("/salada-de-repolho"):  
            await self.highrise.send_whisper(user.id,f"Aqui Está Sua Deliciosa salada de repolho {user.username} 🥬🥬")
            await self.highrise.react("thumbs", user.id)

        if message.startswith("/camarão"):  
            await self.highrise.send_whisper(user.id,f"🍤Aqui Está seu Delicoso Camarão 🍤 {user.username} 🍤")
            await self.highrise.react("thumbs", user.id)

        if message.startswith("/macarrão"):  
            await self.highrise.send_whisper(user.id,f"Aqui Está seu macarrão {user.username} aproveite 🍜🍝")
            await self.highrise.react("thumbs", user.id)
          
        if message.startswith("/salada-de-alface"):  
            await self.highrise.send_whisper(user.id,f"Aqui Está a Sua salada de alface {user.username} com um pouco de tomates por cima 🥬🥗")
            await self.highrise.react("thumbs", user.id)

        if message.startswith("/bolo-de-cenoura"):  
            await self.highrise.send_whisper(user.id,f"aqui está seu bolo de cenoura  {user.username} 🥕🥮")
            await self.highrise.react("thumbs", user.id)
           
        if message.startswith("/açai"):  
            await self.highrise.send_whisper(user.id,f"Aqui Está Seu Açai {user.username} 🍨 Aproveite")
            await self.highrise.react("thumbs", user.id)
          
        if message.startswith("/sorvete"):  
            await self.highrise.send_whisper(user.id,f"Aqui Está Seu sorvete {user.username} 🍦🍨")
            await self.highrise.react("thumbs", user.id)

        if message.startswith("/pão-de-alho"):  
            await self.highrise.send_whisper(user.id,f"Aqui Está Sua pão de alho {user.username} 🥖🧄")
            await self.highrise.react("thumbs", user.id)

        if message.startswith("/batata-frita"):  
            await self.highrise.send_whisper(user.id,f"Aqui Está Sua Batata Frita {user.username} aproveite 🍟")
            await self.highrise.react("thumbs", user.id)

        if message.startswith("/espetinho"):  
            await self.highrise.send_whisper(user.id,f"Aqui Está Seu Espetinho {user.username} 🍢🍢")
            await self.highrise.react("thumbs", user.id)

        if message.startswith("/cupcake"):  
            await self.highrise.send_whisper(user.id,f"Aqui Está Seu cupcake {user.username} 🧁")
            await self.highrise.react("thumbs", user.id)
              
        if        message.startswith("/tp") or      message.startswith("!tp") or      message.startswith("/tele") or          message.startswith("Tp") or          message.startswith("Tele") or  message.startswith("!tele"):
          target_username =         message.split("@")[-1].strip()
          await                     self.teleport_to_user(user, target_username)

        if message.startswith("!up1"):
          await self.highrise.teleport(user.id,Position(13.5,8.0,10.5))

        if message.startswith("!up2"):
          await self.highrise.teleport(user.id,Position(16.5,14.75,17.5))

        if message.startswith("!vip"):
          if user.username == "R0__YA" or user.username == "didyousaydonut" or user.username == "Demic._" or user.username == "Mini_sad" or user.username == "f__7oo" or user.username == "H.kakashi" or user.username == "Just_xx" or user.username == "mielX_baby" or user.username == "Ria__Jeyn":
            await self.highrise.teleport(user.id,Position(4.0,15.75,4.5))

        if message.startswith("!down"):
          await self.highrise.teleport(user.id,Position(15.5,0.0,11.5))

        if                            message.startswith("Summon") or          message.startswith("/summon") or  message.startswith("!summon"):
          if user.username == "R0__YA" or user.username == "didyousaydonut" or user.username == "Demic._" or user.username == "Mini_sad" or user.username == "f__7oo" or user.username == "H.kakashi" or user.username == "Just_xx" or user.username == "mielX_baby" or user.username == "Ria__Jeyn":
           target_username = message.split("@")[-1].strip()
           await self.teleport_user_next_to(target_username, user)
    
        if message.startswith("kick"):
          if user.username == "R0__YA" or user.username == "didyousaydonut" or user.username == "Demic._" or user.username == "Mini_sad" or user.username == "f__7oo" or user.username == "H.kakashi" or user.username == "Just_xx":
              pass
          else:
              await self.highrise.chat("Pas la permission.")
              return
          #separete message into parts
          parts = message.split()
          #check if message is valid "kick @username"
          if len(parts) != 2:
              await self.highrise.chat("pas le bon format.")
              return
          #checks if there's a @ in the message
          if "@" not in parts[1]:
              username = parts[1]
          else:
              username = parts[1][1:]
          #check if user is in room
          room_users = (await self.highrise.get_room_users()).content
          for room_user, pos in room_users:
              if room_user.username.lower() == username.lower():
                  user_id = room_user.id
                  break
          if "user_id" not in locals():
              await self.highrise.chat("L'utilisateur n'est pas dans la salle.")
              return
          #kick user
          try:
              await self.highrise.moderate_room(user_id, "kick")
          except Exception as e:
              await self.highrise.chat(f"{e}")
              return
          #send message to chat
          await self.highrise.chat(f"{username} est banni de la salle!!")

    async def teleport(self, user: User, position: Position):
        try:
            await self.highrise.teleport(user.id, position)
        except Exception as e:
            print(f"Caught Teleport Error: {e}")

    async def teleport_to_user(self, user: User, target_username: str) -> None:
        try:
            room_users = await self.highrise.get_room_users()
            for target, position in room_users.content:
                if target.username.lower() == target_username.lower():
                    z = position.z
                    new_z = z - 1
                    await self.teleport(user, Position(position.x, position.y, new_z, position.facing))
                    break
        except Exception as e:
            print(f"An error occurred while teleporting to {target_username}: {e}")

    async def teleport_user_next_to(self, target_username: str, requester_user: User) -> None:
        try:
            # Get the position of the requester_user
            room_users = await self.highrise.get_room_users()
            requester_position = None
            for user, position in room_users.content:
                if user.id == requester_user.id:
                    requester_position = position
                    break

            # Find the target user and their position
            for user, position in room_users.content:
                if user.username.lower() == target_username.lower():
                    z = requester_position.z
                    new_z = z + 1  # Example: Move +1 on the z-axis (upwards)
                    await self.teleport(user, Position(requester_position.x, requester_position.y, new_z, requester_position.facing))
                    break
        except Exception as e:
            print(f"An error occurred while teleporting {target_username} next to {requester_user.username}: {e}")
          
    async def teleporter(self, message: str)-> None:
        """
            Teleports the user to the specified user or coordinate
            Usage: /teleport <username> <x,y,z>
                                                                """
        #separates the message into parts
        #part 1 is the command "/teleport"
        #part 2 is the name of the user to teleport to (if it exists)
        #part 3 is the coordinates to teleport to (if it exists)
        try:
            command, username, coordinate = message.split(" ")
        except:
            
            return
        
        #checks if the user is in the room
        room_users = (await self.highrise.get_room_users()).content
        for user in room_users:
            if user[0].username.lower() == username.lower():
                user_id = user[0].id
                break
        #if the user_id isn't defined, the user isn't in the room
        if "user_id" not in locals():
            
            return
            
        #checks if the coordinate is in the correct format (x,y,z)
        try:
            x, y, z = coordinate.split(",")
        except:
          
            return
        
        #teleports the user to the specified coordinate
        await self.highrise.teleport(user_id = user_id, dest = Position(float(x), float(y), float(z)))

    async def command_handler(self, user: User, message: str):
        parts = message.split(" ")
        command = parts[0][1:]
        functions_folder = "functions"
        # Check if the function exists in the module
        for file_name in os.listdir(functions_folder):
            if file_name.endswith(".py"):
                module_name = file_name[:-3]  # Remove the '.py' extension
                module_path = os.path.join(functions_folder, file_name)
                
                # Load the module
                spec = importlib.util.spec_from_file_location(module_name, module_path)
                module = importlib.util.module_from_spec(spec)
                spec.loader.exec_module(module)
                
                # Check if the function exists in the module
                if hasattr(module, command) and callable(getattr(module, command)):
                    function = getattr(module, command)
                    await function(self, user, message)
        
        # If no matching function is found
        return              
               
    async def on_reaction(self, user: User, reaction: Reaction, receiver: User) -> None:
        print(f"{user.username} enviou a reação  {reaction} para {receiver.username}")

        if reaction.startswith("wink"):
              await self.highrise.send_emote("idle-uwu",receiver.id)
              await self.highrise.send_emote("emote-lust",user.id)            
              await self.highrise.send_emote("emote-ghost-idle")
                       
        if reaction.startswith("heart"):
              await self.highrise.send_emote("emote-kissing-bound",receiver.id)            
              await self.highrise.send_emote("emote-kissing-bound",user.id)
              await self.highrise.send_emote("emote-gordonshuffle")
              
        if reaction.startswith("wave"):
              await self.highrise.send_emote("emote-confused",receiver.id)             
              await self.highrise.send_emote("emote-hello",user.id)          
              await self.highrise.send_emote("dance-smoothwalk")

        if reaction.startswith("thumbs"):
              await self.highrise.send_emote("emote-pose1",receiver.id)            
              await self.highrise.send_emote("dance-spiritual")

        if reaction.startswith("clap"):
              await self.highrise.send_emote("idle-enthusiastic",receiver.id)          
              await self.highrise.send_emote("emoji-celebrate",user.id)
              await self.highrise.send_emote("dance-breakdance")             

    async def on_whisper(self, user: User, message: str) -> None:
        print(f"{user.username} whispered: {message}")

        if message.startswith("/fly"):
          if user.username == "R0__Sa":
            await self.teleporter(message)

        if        message.startswith("/") or message.startswith("!"):
            await self.command_handler(user, message)

        if              message.startswith("gold") or       message.startswith("carteira"):
          if user.username == "R0__Sa":
            wallet = (await self.highrise.get_wallet()).content
            await self.highrise.send_whisper(user.id,f"VALEUR TOTAL : {wallet[0].amount} {wallet[0].type}")
            await self.highrise.send_emote("emote-bunnyhop")
            
    async def on_user_move(self, user: User, pos: Position) -> None:
        print (f"{user.username} moved to {pos}")

    async def on_emote(self, user: User, emote_id: str, receiver: User | None) -> None:
        print(f"{user.username} emoted: {emote_id}")

    async def on_user_leave(self, user: User) -> None:
        print(f"{user.username} saiu da sala")
        await self.highrise.chat(f"Au revoir @{user.username} j'espére que t'as bien profité❤️")
        await self.highrise.send_emote("dance-kawai")