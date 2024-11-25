import speech_recognition as sr
import pyttsx3
from datetime import datetime
import wikipedia

# Initialize the text-to-speech engine
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()
    engine.setProperty('rate',170)

def recognize_speech():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening.....")
        speak("Listning")
        audio = recognizer.listen(source)
        try:
            text = recognizer.recognize_google(audio) # type: ignore
            print(f"You said: {text}")
            return text.lower()
        except sr.UnknownValueError:
            print("Sorry, I did not understand that.")
            return None
        except sr.RequestError:
            print("Sorry, my speech service is down.")
            return None

def get_date():
    return datetime.now().strftime("%B %d, %Y")

def get_time():
    return datetime.now().strftime("%H :%M")

def get_greeting():
    current_hour = datetime.now().hour
    if current_hour < 12:
        return "Good morning!"
    elif 12 <= current_hour < 18:
        return "Good afternoon!"
    else:
        return "Good evening!"

# Dictionary with information about various places in India
india_info = {
        'hello':'hello user , how can I help you',
        'hey':'hello user, how can I help you',
        'yo' :'yo whatsup buddy , how can I help you',
        'who made you':"I was created by Manasva from class 11th A1*.",
        'what is your name' : 'hi my name is alex , am a python chatbot ',
        'what can you do':"I can solve any mathemetical problem or you can ask some questions to me according to my data.",
        'what are your capabilities':"I can solve any mathemetical problem or you can ask some questions to me according to my data.",
        'how are you': "I am fine , thank you user,  and how about you .",
        'recomend songs': "\n Here you can try some of this:\n \n despasito, \t\t by- louis fonsi \n levitating,\t\t by- dua lipa \n no lie, \t\t by- san paul & dua lipa \n dream on,\t\t by- aerosmiths \n way down we go,\t\t by- kaleo \n world smallest violin,\t\t by- AJR \n And many more!!  ",
        'tell me about you':"I am Alex, a python chatbot , am capable of solving mathametival problems and to answer some questions according to my data.",
        'who are you ':'hi I am alex a python chatbot .',
        "delhi": "Delhi is the capital city of India. It is known for its rich history and cultural heritage.",
        "mumbai": "Mumbai is the financial capital of India. It is famous for Bollywood and its bustling city life.",
        "kolkata": "Kolkata, also known as the City of Joy, is known for its cultural festivals and colonial architecture.",
        "chennai": "Chennai is the capital of Tamil Nadu. It is known for its temples, beaches, and classical music.",
        "bangalore": "Bangalore, also known as Bengaluru, is the tech hub of India. It is famous for its parks and nightlife.",
        "hyderabad": "Hyderabad is known for its historical sites, including the Charminar and Golconda Fort. It is also famous for its biryani.",
        "jaipur": "Jaipur, the Pink City, is known for its palaces, forts, and vibrant culture.",
        "agra": "Agra is home to the iconic Taj Mahal, one of the Seven Wonders of the World.",
        "varanasi": "Varanasi is one of the oldest cities in the world. It is a major religious hub for Hindus.",
        "goa": "Goa is known for its beautiful beaches, Portuguese heritage, and vibrant nightlife.",
        "pune": "Pune is known for its educational institutions and vibrant cultural scene.",
        "ahmedabad": "Ahmedabad is famous for its textile industry and the Sabarmati Ashram.",
        "lucknow": "Lucknow is known for its Mughlai cuisine and historical monuments.",
        "kanpur": "Kanpur is an industrial city known for its leather and textile industries.",
        "nagpur": "Nagpur is famous for its oranges and is known as the Orange City.",
        "bhopal": "Bhopal is known for its lakes and is called the City of Lakes.",
        "patna": "Patna is one of the oldest continuously inhabited places in the world.",
        "indore": "Indore is known for its food and is considered the cleanest city in India.",
        "vadodara": "Vadodara is known for the Lakshmi Vilas Palace and its cultural heritage.",
        "coimbatore": "Coimbatore is known for its textile industry and pleasant climate.",
        "kochi": "Kochi, also known as Cochin, is a major port city in Kerala.",
        "visakhapatnam": "Visakhapatnam is known for its beaches and shipbuilding industry.",
        "madurai": "Madurai is famous for the Meenakshi Amman Temple.",
        "meerut": "Meerut is known for its sports goods industry.",
        "nashik": "Nashik is known for its vineyards and the Kumbh Mela.",
        "jodhpur": "Jodhpur, the Blue City, is known for its forts and palaces.",
        "udaipur": "Udaipur, the City of Lakes, is known for its palaces and lakes.",
        "guwahati": "Guwahati is the largest city in Assam and is known for the Kamakhya Temple.",
        "dehradun": "Dehradun is known for its educational institutions and scenic beauty.",
        "shimla": "Shimla is a popular hill station and the capital of Himachal Pradesh.",
        "ranchi": "Ranchi is known for its waterfalls and scenic beauty.",
        "bhubaneswar": "Bhubaneswar is known for its temples and is called the Temple City of India.",
        "trivandrum": "Trivandrum, also known as Thiruvananthapuram, is the capital of Kerala.",
        "mysore": "Mysore is known for its palaces and the Mysore Dasara festival.",
        "amritsar": "Amritsar is home to the Golden Temple, the holiest site in Sikhism.",
        "jabalpur": "Jabalpur is known for the Marble Rocks and Dhuandhar Falls.",
        "gwalior": "Gwalior is known for its fort and classical music heritage.",
        "raipur": "Raipur is the capital of Chhattisgarh and is known for its steel industry.",
        "panaji": "Panaji is the capital of Goa and is known for its Portuguese architecture.",
        "aurangabad": "Aurangabad is known for the Ajanta and Ellora Caves.",
        "solapur": "Solapur is known for its textile industry and historical sites.",
        "hubli": "Hubli is a major commercial hub in Karnataka.",
        "dharwad": "Dharwad is known for its educational institutions and cultural heritage.",
        "tirupati": "Tirupati is famous for the Tirumala Venkateswara Temple.",
        "vellore": "Vellore is known for the Vellore Fort and Christian Medical College.",
        "warangal": "Warangal is known for its historical sites and temples.",
        "rajkot": "Rajkot is known for its jewelry and textile industries.",
        "jamshedpur": "Jamshedpur is known for its steel industry and is called the Steel City of India.",
        "cuttack": "Cuttack is known for its silver filigree work and historical significance.",
        "aligarh": "Aligarh is known for the Aligarh Muslim University and lock industry.",
        "bareilly": "Bareilly is known for its furniture and trade in sugar and grain.",
        "moradabad": "Moradabad is known for its brass handicrafts and is called the Brass City.",
        "guntur": "Guntur is known for its chili production and historical significance.",
        "noida": "Noida is a planned city and a major hub for IT and software companies.",
        "ghaziabad": "Ghaziabad is known for its industrial and commercial significance.",
        "faridabad": "Faridabad is an industrial city in Haryana, known for its manufacturing sector.",
        "meerut": "Meerut is known for its sports goods industry and historical significance.",
        "varanasi": "Varanasi is one of the oldest cities in the world and a major religious hub for Hindus.",
        "agra": "Agra is home to the iconic Taj Mahal, one of the Seven Wonders of the World.",
        "judicial review":"Judicial review is the power of the judiciary to examine the constitutionality of legislative acts and executive orders.",
        "fundamental rights": "Fundamental rights are the basic human rights enshrined in the Indian Constitution, including the right to equality, freedom, and protection against discrimination.",
        "directive principles": "Directive Principles of State Policy are guidelines for the framing of laws by the government, aimed at creating social and economic conditions under which citizens can lead a good life.",
        "right to information": "The Right to Information Act, 2005, empowers citizens to seek information from public authorities, promoting transparency and accountability.",
        "consumer protection": "The Consumer Protection Act, 2019, provides for the protection of consumer rights and the establishment of consumer councils and other authorities for the settlement of consumer disputes.",
        "environmental laws": "Environmental laws in India include the Environment Protection Act, 1986, and the Air (Prevention and Control of Pollution) Act, 1981, aimed at protecting and improving the environment.",
        "cyber laws": "Cyber laws in India include the Information Technology Act, 2000, which provides legal recognition for electronic transactions and aims to prevent cybercrimes.",
        "intellectual property": "Intellectual property laws in India include the Patents Act, 1970, and the Copyright Act, 1957, aimed at protecting the rights of creators and inventors.",
        "labor laws": "Labor laws in India include the Industrial Disputes Act, 1947, and the Minimum Wages Act, 1948, aimed at regulating labor relations and ensuring fair wages.",
        "criminal law": "Criminal law in India includes the Indian Penal Code, 1860, and the Code of Criminal Procedure, 1973, which define offenses and prescribe punishments.",
        "civil law": "Civil law in India includes the Code of Civil Procedure, 1908, which governs the procedure for civil litigation in India.",
        "population": "India's population is approximately 1.44 billion people, making it the most populous country in the world.",
        "area": "India is the seventh-largest country by area, covering 3.287 million square kilometers.",
        "gdp": "India's GDP is over $2.6 trillion, making it one of the largest economies in the world.",
        "literacy rate": "The literacy rate in India is around 77.7%, with significant improvements over the years.",
        "life expectancy": "The average life expectancy in India is approximately 70 years.",
        "urbanization": "About 34% , of India's population lives in urban areas.",
        "poverty rate": "The poverty rate in India has been declining, with significant efforts to reduce poverty levels.",
        "inflation rate": "India's inflation rate varies, with recent figures around 2.86% year-on-year.",
        "unemployment rate": "The unemployment rate in India is around 7.2%, with variations across different regions.",
        "foreign exchange reserves": "India's foreign exchange reserves are over $600 billion, providing economic stability.",
        "export partners": "India's main export partners include the United States, China, and the United Arab Emirates.",
        "prime minister": "Narendra Modi is the current Prime Minister of India, having held office since May 2014. He is a member of the Bharatiya Janata Party (BJP) and has been instrumental in implementing various economic and social reforms.",
    "capital of india": "New Delhi is the capital of India. It is a vibrant city known for its rich history, cultural heritage, and political significance. It houses important government buildings, including the Parliament House and the Rashtrapati Bhavan.",
    "ganga of the south": "The Godavari River is often referred to as the Ganga of the South. It is the second longest river in India and flows through the states of Maharashtra, Telangana, Andhra Pradesh, Chhattisgarh, and Odisha.",
    "first president": "Dr. Rajendra Prasad was the first President of India, serving from 1950 to 1962. He played a crucial role in the Indian independence movement and was a prominent leader in the Indian National Congress.",
    "national animal": "The Bengal Tiger is the national animal of India. It symbolizes strength, power, and grace. India is home to the largest population of Bengal tigers in the world, primarily found in national parks and wildlife sanctuaries.",
    "longest coastline": "Gujarat has the longest coastline among Indian states, stretching over 1,600 kilometers. The coastline is dotted with important ports, beaches, and coastal towns, contributing significantly to the state's economy.",
    "national anthem": "The national anthem of India, 'Jana Gana Mana,' was written by Rabindranath Tagore. It was adopted as the national anthem on January 24, 1950, and is sung at various national events and ceremonies.",
    "national flower": "The Lotus is the national flower of India. It is a symbol of purity, beauty, and spirituality. The lotus holds significant cultural and religious importance in Indian traditions and mythology.",
    "largest state": "Rajasthan is the largest state in India by area. It is known for its desert landscapes, historical forts, palaces, and vibrant culture. The state is a popular tourist destination.",
    "father of the nation": "Mahatma Gandhi is known as the Father of the Nation in India. He led the Indian independence movement through non-violent civil disobedience and played a pivotal role in achieving India's freedom from British rule.",
    "national sport": "Field Hockey is considered the national sport of India. The Indian men's hockey team has won numerous Olympic gold medals and has a rich history of success in international competitions.",
    "silicon valley": "Bangalore, also known as Bengaluru, is referred to as the Silicon Valley of India. It is a major hub for the information technology industry and is home to numerous tech companies and startups.",
    "first woman pm": "Indira Gandhi was the first woman Prime Minister of India. She served as Prime Minister from 1966 to 1977 and again from 1980 until her assassination in 1984. She was a prominent leader of the Indian National Congress.",
    "national bird": "The Indian Peafowl, also known as the peacock, is the national bird of India. It is known for its vibrant plumage and majestic appearance. The peacock holds cultural and religious significance in India.",
    "smallest state": "Goa is the smallest state in India by area. It is known for its beautiful beaches, Portuguese heritage, and vibrant nightlife. Goa is a popular tourist destination, attracting visitors from around the world.",
    "current president of India": "Droupadi Murmu is the current President of India. She is the first tribal woman to hold the office and has a background in social work and politics.",
    "land of five rivers": "Punjab is known as the Land of Five Rivers. The five rivers are Sutlej, Beas, Ravi, Chenab, and Jhelum. The state is known for its fertile land and agricultural productivity.",
    "India's currency": "The Indian Rupee is the national currency of India. It is abbreviated as INR and is issued and regulated by the Reserve Bank of India.",
    "highest civilian award": "The Bharat Ratna is the highest civilian award in India. It is awarded for exceptional service in various fields, including arts, literature, science, and public service.",
    "first nobel prize in india": "Rabindranath Tagore was the first Indian to win a Nobel Prize. He received the Nobel Prize in Literature in 1913 for his collection of poems, 'Gitanjali.'",
    "Which state in India has the highest literacy rate?": "Kerala",
        "What is India's largest state by area?": "Rajasthan",
        "Which Indian city is known as the 'Silicon Valley of India'?": "Bengaluru",
        "Which river is considered sacred in Hinduism?": "Ganges",
        "What is the national bird of India?": "Peacock",
        "Which Indian state is famous for its tea plantations?": "Assam",
        "What is the currency of India?": "Indian Rupee",
        "Which Indian festival is celebrated with colorful lights?": "Diwali",
        "What is the national animal of India?": "Tiger",
        "Which Indian state is known for its backwaters?": "Kerala",
        "Which Indian monument is a UNESCO World Heritage Site?": "Taj Mahal",
        "What is the largest Indian state by population?": "Uttar Pradesh",
        "Which Indian city is known as the 'City of Joy'?": "Kolkata",
        "Which Indian language is spoken by the most people?": "Hindi",
        "Which Indian state is famous for its beaches?": "Goa",
        "Which Indian festival is celebrated with colorful powders?": "Holi",
        "Which Indian state is known for its wildlife sanctuaries?": "Madhya Pradesh",
        "Which Indian city is known as the 'Financial Capital of India'?": "Mumbai",
        "Which Indian state is known for its beautiful valleys?": "Kashmir",
        "Which Indian state is known for its temples?": "Tamil Nadu",
        "Which Indian state is known for its spices?": "Kerala",
        "Which Indian state is known for its handicrafts?": "Uttar Pradesh",
        "Which Indian state is known for its silk sarees?": "West Bengal",
        "Which Indian state is known for its handicrafts?": "Rajasthan",
        "Which Indian state is known for its tea gardens?": "Assam",
        "Which Indian state is known for its coffee plantations?": "Karnataka",
        "Which Indian state is known for its rubber plantations?": "Kerala",
        "Which Indian state is known for its jute mills?": "West Bengal",
        "Which Indian state is known for its iron ore mines?": "Odisha",
        "Which Indian state is known for its coal mines?": "Jharkhand",
        "Which Indian state is known for its oil refineries?": "Gujarat",
        "Which Indian state is known for its automobile industry?": "Tamil Nadu",
        "Which Indian state is known for its IT industry?": "Karnataka",
        "Which Indian state is known for its textile industry?": "Maharashtra",
        "Which Indian state is known for its pharmaceutical industry?": "Andhra Pradesh",
        "Which Indian state is known for its tourism industry?": "Uttar Pradesh",
        "Which Indian state is known for its agriculture?": "Uttar Pradesh",
        "Which Indian state is known for its dairy industry?": "Gujarat",
        "Which Indian state is known for its fisheries?": "Andhra Pradesh",
        "Which Indian state is known for its forestry?": "Madhya Pradesh",
        "Which Indian state is known for its mineral resources?": "Chhattisgarh",
        "Which Indian state is known for its wind energy?": "Tamil Nadu",
        "Which Indian state is known for its solar energy?": "Rajasthan",
        "Which Indian state is known for its hydroelectric power?": "Himachal Pradesh",
        "Which Indian state is known for its nuclear power?": "Maharashtra",
        "Which Indian state is known for its thermal power?": "West Bengal",
        "Which Indian state is known for its education?": "Kerala",
        "Which Indian state is known for its healthcare?": "Tamil Nadu",
        "Which Indian state is known for its social welfare?": "Kerala",
        "Which Indian state is known for its women's empowerment?": "Kerala",
        "Which Indian state is known for its tribal population?": "Chhattisgarh",
        "Which Indian state is known for its religious diversity?": "Uttar Pradesh",
        "Which Indian state is known for its linguistic diversity?": "Karnataka",
        "Which Indian state is known for its cultural diversity?": "Maharashtra",
        "Which Indian state is known for its historical monuments?": "Uttar Pradesh",

            "capital of France": "Paris is the capital of France, known for its art, fashion, and culture. It is home to landmarks like the Eiffel Tower and the Louvre Museum.",
    "largest ocean": "The Pacific Ocean is the largest ocean on Earth, covering more than 63 million square miles and containing more than half of the world's free water.",
    "tallest mountain": "Mount Everest, located in the Himalayas, is the tallest mountain in the world, standing at 29,032 feet above sea level.",
    "author of Hamlet": "William Shakespeare, an English playwright and poet, wrote Hamlet. It is one of his most famous tragedies, exploring themes of revenge and madness.",
    "currency of Japan": "The Japanese Yen is the official currency of Japan. It is one of the most traded currencies in the foreign exchange market.",
    "largest desert": "The Sahara Desert is the largest hot desert in the world, covering most of North Africa. It spans approximately 9.2 million square kilometers.",
    "inventor of the telephone": "Alexander Graham Bell is credited with inventing the first practical telephone. He was awarded the first US patent for the invention in 1876.",
    "smallest country": "Vatican City is the smallest country in the world, both in terms of area and population. It is the spiritual and administrative center of the Roman Catholic Church.",
    "longest river": "The Nile River is traditionally considered the longest river in the world, flowing through northeastern Africa for about 6,650 kilometers.",
    "first man on the moon": "Neil Armstrong was the first person to walk on the moon during NASA's Apollo 11 mission in 1969. His famous words were 'That's one small step for man, one giant leap for mankind.'",
    "largest planet": "Jupiter is the largest planet in our solar system. It is a gas giant with a mass more than twice that of all the other planets combined.",
    "capital of Australia": "Canberra is the capital city of Australia. It is located in the Australian Capital Territory and is the political center of the country.",
    "painter of the Mona Lisa": "Leonardo da Vinci, an Italian Renaissance artist, painted the Mona Lisa. It is one of the most famous and valuable paintings in the world.",
    "fastest land animal": "The cheetah is the fastest land animal, capable of reaching speeds up to 70 miles per hour in short bursts covering distances up to 500 meters.",
    "largest continent": "Asia is the largest continent, both in terms of area and population. It covers about 30% of Earth's land area and is home to over 4.5 billion people.",
    "discovery of penicillin": "Alexander Fleming, a Scottish bacteriologist, discovered penicillin in 1928. It was the first antibiotic and revolutionized the treatment of bacterial infections.",
    "capital of Canada": "Ottawa is the capital city of Canada. It is located in the province of Ontario and is known for its historic landmarks and cultural institutions.",
    "largest mammal": "The blue whale is the largest mammal on Earth. It can grow up to 100 feet in length and weigh as much as 200 tons.",
    "first President of the USA": "George Washington was the first President of the United States, serving from 1789 to 1797. He is often referred to as the 'Father of His Country.'",
    "deepest ocean trench": "The Mariana Trench is the deepest oceanic trench in the world, located in the western Pacific Ocean. Its deepest point, Challenger Deep, reaches about 36,000 feet.",
    "capital of Italy": "Rome is the capital city of Italy. It is known for its nearly 3,000 years of globally influential art, architecture, and culture.",
    "largest island": "Greenland is the world's largest island that is not a continent. It is an autonomous territory within the Kingdom of Denmark.",
    "discovery of gravity": "Sir Isaac Newton, an English mathematician and physicist, formulated the laws of motion and universal gravitation in the late 17th century.",
    "capital of Russia": "Moscow is the capital city of Russia. It is the largest city in the country and is known for its historical and architectural landmarks.",
    "largest rainforest": "The Amazon Rainforest is the largest rainforest in the world, covering much of northwestern Brazil and extending into Colombia, Peru, and other South American countries.",
    "first woman to win a Nobel Prize": "Marie Curie was the first woman to win a Nobel Prize. She won the Nobel Prize in Physics in 1903 and later in Chemistry in 1911.",
    "capital of China": "Beijing is the capital city of China. It is one of the world's most populous cities and is known for its modern architecture and ancient sites.",
    "largest volcano": "Mauna Loa in Hawaii is the largest volcano on Earth in terms of volume and area covered. It is one of the most active volcanoes in the world.",
    "discovery of America": "Christopher Columbus, an Italian explorer, is credited with discovering America in 1492, although indigenous peoples had been living there for thousands of years.",
    "capital of Brazil": "Brasília is the capital city of Brazil. It was founded in 1960 and is known for its modernist architecture designed by Oscar Niemeyer.",
    "largest coral reef": "The Great Barrier Reef, located off the coast of Queensland, Australia, is the largest coral reef system in the world. It is composed of over 2,900 individual reefs.",
    "first artificial satellite": "Sputnik 1 was the first artificial satellite launched by the Soviet Union on October 4, 1957. It marked the beginning of the space age.",
    "capital of India": "New Delhi is the capital city of India. It serves as the seat of all three branches of the Government of India and is known for its historical landmarks.",
    "largest desert": "The Antarctic Desert is the largest desert in the world, covering the continent of Antarctica. It is classified as a cold desert due to its low precipitation.",
    "discovery of DNA structure": "James Watson and Francis Crick are credited with discovering the double helix structure of DNA in 1953, which revolutionized the field of genetics.",
    "capital of Egypt": "Cairo is the capital city of Egypt. It is the largest city in the Arab world and is known for its rich history and proximity to the ancient pyramids.",
    "largest lake in  world": "The Caspian Sea is the largest enclosed inland body of water on Earth by area. It is bordered by five countries: Kazakhstan, Russia, Turkmenistan, Iran, and Azerbaijan.",
    "first human in space": "Yuri Gagarin, a Soviet astronaut, was the first human to journey into outer space. He orbited Earth on April 12, 1961, aboard Vostok 1.",
    "capital of Germany": "Berlin is the capital city of Germany. It is known for its art scene, modern landmarks, and historical significance, including the Berlin Wall.",
    "largest waterfall": "Angel Falls in Venezuela is the world's highest uninterrupted waterfall, with a height of 3,212 feet. It is located in the Canaima National Park.",
    "discovery of electricity": "Benjamin Franklin is often credited with discovering electricity through his famous kite experiment in 1752, although electricity was known to ancient civilizations.",
    "capital of Mexico": "Mexico City is the capital of Mexico. It is one of the largest cities in the world and is known for its rich history, culture, and architecture.",
    "largest river by volume": "The Amazon River is the largest river by discharge volume of water in the world. It flows through South America and has the largest drainage basin.",
    "first computer": "The ENIAC (Electronic Numerical Integrator and Computer) was the first general-purpose electronic digital computer, completed in 1945 by John Presper Eckert and John Mauchly.",
    "capital of Japan": "Tokyo is the capital city of Japan. It is one of the most populous urban areas in the world and is known for its skyscrapers, shopping, and culture.",
    "largest desert": "The Antarctic Desert is the largest desert in the world, covering the continent of Antarctica. It is classified as a cold desert due to its low precipitation.",
    "discovery of radioactivity": "Henri Becquerel discovered radioactivity in 1896, and his work was further developed by Marie and Pierre Curie, leading to significant advancements in science.",
    "capital of South Korea": "Seoul is the capital city of South Korea. It is a major global city known for its technology, culture, and history."


}


# def get_data(place):
#     return data.get(place.lower())


# def get_info(place):
#     return india_info.get(place.lower())

def get_gk_answer(question):
    for key in india_info:
        if key in question:
            return india_info[key]
    # return "Sorry, I don't have information about that."

def main():
    wake_word = "hello assistant"
    sleep_word = "stop listening"
    active = False

    while True:
        if not active:
            print("Say the wake word to activate...")
            speak("On")
            user_input = recognize_speech()
            if user_input and wake_word in user_input:
                active = True
                speak(get_greeting())
                speak("How can I help you")
        else:
            user_input = recognize_speech()
            if user_input:
                if sleep_word in user_input:
                    active = False
                    speak("Going to sleep. Goodbyeee")
                elif user_input == True:
                    # speak(f"You said: {user_input}")
                    def search_wiki(user_input):
                        try:
                            result = wikipedia.summary(user_input, sentences=1)
                            print(result) 
                            speak(result)
                        except wikipedia.exceptions.DisambiguationError:
                            print("Multiple matches found .Please be more specific.")
                            speak("Multiple matches found .Please be more specific.")
                        except wikipedia.exceptions.PageError:
                            print("No Wikipedia page found for that query.") 
                            speak("No Wikipedia page found for that query.") 
                    if __name__ == "__main__" :
                        search_term = user_input
                        search_wiki(search_term)
                    
                elif "date" in user_input:
                    speak(f"Today's date is {get_date()}.")
                elif "time" in user_input:
                    speak(f"The current time is {get_time()}.")
                    
                else:
                    answer = get_gk_answer(user_input)
                    speak(answer)
                # elif "tell me about" in user_input:
                #     place = user_input.replace("tell me about", "").strip()
                #     info = get_info(place)
                #     speak(info)
                    
                # elif "tell me" in data:
                #     place2 = user_input.replace("tell me", "").strip()
                #     infor = get_data(place2)
                #     speak(infor)
                    

if __name__ == "__main__":
    main()




    
        