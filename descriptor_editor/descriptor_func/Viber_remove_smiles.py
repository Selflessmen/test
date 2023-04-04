viber = {"(smiley)": "", "(sad)": "", "(angry)": "", "(inlove)": "", "(yummi)": "", "(laugh)": "",
         "(surprised)": "", "(moa)": "", "(happy)": "", "(cry)": "", "(sick)": "", "(shy)": "",
         "(teeth)": "", "(tongue)": "", "(money)": "", "(mad)": "", "(flirt)": "", "(crazy)": "",
         "(confused)": "", "(depressed)": "", "(scream)": "", "(nerd)": "", "(not_sure)": "",
         "(cool)": "", "(huh)": "", "(happycry)": "", "(mwah)": "", "(exhausted)": "", "(eek)": "",
         "(dizzy)": "", "(dead)": "", "(straight)": "", "(yo)": "", "(wtf)": "", "(ohno)": "",
         "(oh)": "", "(wink2)": "", "(what)": "", "(weak)": "", "(upset)": "", "(ugh)": "", "(teary)": "",
         "(singing)": "", "(silly)": "", "(meh)": "", "(mischievous)": "", "(hmm)": "", "(crying)": "",
         "(eyeroll)": "", "(ninja)": "", "(spiderman)": "", "(batman)": "", "(devil)": "", "(angel)": "",
         "(heart)": "", "(heart_break)": "", "(purple_heart)": "", "(yellow_heart)": "", "(blue_heart)": "",
         "(orange_heart)": "", "(black_heart)": "", "(2_hearts)": "", "(arrow_heart)": "", "(heart_lock)": "",
         "(unlike)": "", "(like)": "", "(V)": "", "(fu)": "", "(clap)": "", "(rockon)": "", "(pointer)": "",
         "(waving)": "", "(fist)": "", "(prayer_hands)": "", "(footsteps)": "", "(muscle)": "",
         "(thinking)": "", "(zzz)": "", "(!)": "", "(Q)": "", "(diamond)": "", "(trophy)": "", "(crown)": "",
         "(ring)": "", "($)": "", "(hammer)": "", "(wrench)": "", "(key)": "", "(lock)": "", "(video)": "",
         "(TV)": "", "(tape)": "", "(trumpet)": "", "(guitar)": "", "(drum)": "", "(speaker)": "", "(music)": "",
         "(microphone)": "", "(bell)": "", "(koala)": "", "(sheep)": "", "(ladybug)": "", "(kangaroo)": "",
         "(chick)": "", "(monkey)": "", "(panda)": "", "(turtle)": "", "(bunny)": "", "(dragonfly)": "",
         "(fly)": "", "(bee)": "", "(bat)": "", "(cat)": "", "(dog)": "", "(squirrel)": "", "(snake)": "",
         "(snail)": "", "(goldfish)": "", "(shark)": "", "(pig)": "", "(owl)": "", "(penguin)": "",
         "(porcupine)": "", "(fox)": "", "(octopus)": "", "(dinosaur)": "", "(paw)": "", "(poo)": "",
         "(cap)": "", "(fidora)": "", "(partyhat)": "", "(santa_hat)": "", "(tiara)": "", "(bowtie)": "",
         "(cactus)": "", "(clover)": "", "(sprout)": "", "(palmtree)": "", "(christmas_tree)": "",
         "(mapleleaf)": "", "(flower)": "", "(sunflower)": "", "(blue_flower)": "", "(bouquet)": "",
         "(sun)": "", "(moon)": "", "(cloud)": "", "(rain)": "", "(droplet)": "", "(tornado)": "",
         "(lightening)": "", "(rainbow)": "", "(earth)": "", "(full_moon)": "", "(shooting_star)": "",
         "(star)": "", "(umbrella)": "", "(snowman)": "", "(snowflake)": "", "(relax)": "", "(flipflop)": "",
         "(bikini)": "", "(sunglasses)": "", "(fan)": "", "(phone)": "", "(nobattery)": "", "(battery)": "",
         "(time)": "", "(camera)": "", "(telephone)": "", "(knife)": "", "(syringe)": "", "(termometer)": "",
         "(meds)": "", "(ruler)": "", "(scissor)": "", "(paperclip)": "", "(pencil)": "", "(magnify)": "",
         "(glasses)": "", "(book)": "", "(letter)": "", "(weight)": "", "(angrymark)": "", "(boxing)": "",
         "(light_bulb)": "", "(lantern)": "", "(fire)": "", "(torch)": "", "(bomb)": "", "(cigarette)": "",
         "(kiss)": "", "(gift)": "", "(skull)": "", "(ghost)": "", "(robot)": "", "(alien)": "",
         "(golf)": "", "(golfball)": "", "(football)": "", "(tennis)": "", "(soccer)": "", "(basketball)": "",
         "(baseball)": "", "(8ball)": "", "(beachball)": "", "(iceskate)": "", "(target)": "",
         "(racing_flag)": "", "(balloon2)": "", "(balloon1)": "", "(cards)": "", "(dice)": "", "(chicken)": "",
         "(dice)": "", "(burger)": "", "(pizza)": "", "(noodles)": "", "(sushi1)": "", "(sushi2)": "",
         "(donut)": "", "(egg)": "", "(hotdog)": "", "(bacon)": "", "(hotsauce)": "", "(ice_cream)": "",
         "(popsicle)": "", "(cupcake)": "", "(croissant)": "", "(chocolate)": "", "(lollipop)": "",
         "(cookie)": "", "(cake_slice)": "", "(popcorn)": "", "(cake)": "", "(cherry)": "", "(banana)": "",
         "(watermelon)": "", "(strawberry)": "", "(grapes)": "", "(lemon)": "", "(peach)": "", "(apple)": "",
         "(pineapple)": "", "(pea)": "", "(eggplant)": "", "(corn)": "", "(mushroom)": "", "(coffee)": "",
         "(soda)": "", "(beer)": "", "(wine)": "", "(martini)": "", "(champagne)": "", "(cocktail)": "",
         "(cutlery)": "", "(party_popper)": "", "(confetti_ball)": "", "(car)": "", "(taxi)": "",
         "(ambulance)": "", "(policecar)": "", "(bicycle)": "", "(airplane)": "", "(trafficlight)": "",
         "(stop_sign)": "", "(ufo)": "", "(rocket)": "", "(run)": "", "(shrug)": "", "(up_graph)": "",
         "(down_graph)": "", "(color_palette)": "", "(paintbrush)": "", "(crystal_ball)": "",
         "(checkmark)": "", "(tablet)": "", "(baby_bottle)": "", "(anchor)": "", "(first_aid)": "",
         "(handicap)": "", "(do_not_enter)": "", "(over18)": "", "(spiral)": "", "(moneybag)": "",
         "(eyes)": ""
         }


def remove_viber_smiles(name):
    for i in viber:
        if i in name:
            name = name.replace(i, viber[i])


    return name


if "__main__" == "__name__":
    remove_viber_smiles(name)