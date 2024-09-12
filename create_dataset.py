from langsmith import Client
from dotenv import load_dotenv

load_dotenv()

client = Client()
dataset_name = "week1_project_evaluation"

inputs = [
    "Can you summarize 'The Little Prince'?",
    "Summarize The Godfather",
    "Can you summarize 'Moby Dick'?",
    "Summarize Dune",
    "Please do an analysis for Harry Potter I",
    "Perform your magic for 'Lord of The Rings: Two Towers'",
    "List all of the books that you have summarized for me in this session",
    "Please help me to buy a book. Let me know what is your favorite one.",
    "Summarize IT by Stephen King",
    "Can you summarize 'Sapiens' by Yuval Noah Harari?",
]

outputs = [
"""
Sure! Here’s a summary of "The Little Prince" by Antoine de Saint-Exupéry.

I. Plot Summary
The story begins with a pilot stranded in the Sahara Desert who meets a young boy, the Little Prince. The Prince shares tales of his home asteroid, B-612, where he lives alone with a rose. He recounts his travels to various planets, each inhabited by unique characters, such as a king, a vain man, a drunkard, and a businessman. Through these encounters, the Prince learns about love, loneliness, and the nature of adulthood. Ultimately, he seeks to return to his rose, realizing that true love means taking responsibility for those we care about.

II. Character Analysis
The Little Prince is a curious and innocent character who embodies the wisdom of childhood. His longing for connection and understanding drives his journey. The pilot, who represents the adult world, undergoes a transformation as he learns from the Prince's perspective. Other characters, like the fox, teach valuable lessons about relationships and the importance of seeing with the heart rather than the eyes.

III. Themes
The novel explores themes of love, friendship, and the critique of adult behavior. It emphasizes the value of imagination and the importance of nurturing relationships. The story suggests that adults often lose sight of what truly matters in life, focusing instead on materialism and superficiality.

IV. Symbolism
The rose symbolizes love and beauty, representing the Prince's feelings for his home. The various planets he visits symbolize different aspects of human nature and the complexities of adult life. The fox represents wisdom and the idea that true connections require effort and understanding.

If you have any other documents or topics you'd like summarized, feel free to ask!""",
"""
Title: "The Godfather" by Mario Puzo

I. Plot Summary
"The Godfather" follows the powerful and influential Corleone crime family in post-World War II America. The story centers around patriarch Vito Corleone, who is known for his wisdom and ruthlessness in the world of organized crime. As Vito's youngest son, Michael, initially tries to distance himself from the family's illegal activities, he is eventually drawn into the family business after an assassination attempt on his father. The plot unfolds with themes of loyalty, betrayal, and the struggle for power, culminating in Michael's transformation into a ruthless leader who takes over the family business.

II. Character Analysis
Vito Corleone is a complex character, embodying both a loving father and a cunning mob boss. His ability to navigate the criminal underworld while maintaining a sense of honor and loyalty makes him a formidable figure. Michael Corleone starts as an outsider, a war hero who wants nothing to do with the family's criminal activities. However, as the story progresses, he becomes increasingly involved and ultimately embraces his role as the new Godfather. Other key characters include Sonny, Vito's impulsive eldest son, and Tom Hagen, the family's consigliere, who provide insight into the dynamics of the Corleone family and the challenges they face.

III. Themes
The novel explores themes of power, loyalty, and the American Dream. It delves into the moral complexities of crime and the sacrifices made for family and loyalty. The story also critiques the notion of the American Dream, showing how the pursuit of power and success can lead to corruption and moral decay. The struggle between personal ethics and familial loyalty is a central conflict for Michael as he navigates his dual identity.

IV. Symbolism
The Godfather himself symbolizes the intersection of power and family loyalty, representing the duality of love and violence in the pursuit of control. The recurring motif of the olive branch signifies peace and reconciliation, contrasting with the violent methods employed by the Corleones. Additionally, the use of the wedding scene at the beginning symbolizes the intertwining of personal and criminal lives, setting the stage for the conflicts that follow.

ELI5 Summary: "The Godfather" is about a powerful crime family led by Vito Corleone. His son Michael tries to stay away from crime but gets pulled in when his dad is attacked. The story shows how family loyalty can lead to tough""",
"""
Sure! Here’s a summary of "Moby Dick" by Herman Melville:

I. Plot Summary
"Moby Dick" follows the journey of Ishmael, a sailor who joins the whaling ship Pequod, captained by the obsessive Captain Ahab. Ahab is on a relentless quest for revenge against Moby Dick, a giant white whale that had previously destroyed his ship and bitten off his leg. As the crew sails across the oceans, they encounter various challenges and other ships, all while Ahab's obsession with the whale grows. The story culminates in a dramatic confrontation between Ahab and Moby Dick, leading to catastrophic consequences for the crew.

II. Character Analysis
Ishmael serves as the narrator and represents a curious and philosophical perspective on life at sea. Captain Ahab is a complex character driven by vengeance and obsession, showcasing the darker aspects of human nature. The crew members, including Queequeg, Starbuck, and others, each bring their own backgrounds and motivations, highlighting themes of camaraderie and conflict. Their interactions with Ahab reveal the tension between loyalty and moral dilemmas.

III. Themes
The novel explores themes of obsession, revenge, and the struggle between man and nature. Ahab's fixation on Moby Dick symbolizes humanity's struggle against the uncontrollable forces of nature. The story also delves into existential questions about fate, free will, and the search for meaning in life. Melville critiques the whaling industry and the human tendency to pursue destructive goals.

IV. Symbolism
Moby Dick, the whale, serves as a powerful symbol of nature's majesty and unpredictability, as well as the embodiment of Ahab's obsession. The Pequod represents the human endeavor and the quest for knowledge, while the ocean itself symbolizes the vast, unknown challenges of life. The color white of the whale can be interpreted as a symbol of both purity and terror, reflecting the duality of nature.

I hope this summary helps you understand "Moby Dick" better! If you have any specific questions or need further details, feel free to ask!
""",
"""Sure! Here’s a summary of "Dune" by Frank Herbert:

I. Plot Summary
"Dune" is set in a distant future where interstellar travel and feudal societies exist. The story follows young Paul Atreides, heir to House Atreides, as his family is given control of the desert planet Arrakis, also known as Dune. Arrakis is the only source of the valuable spice melange, which grants extended life and enhances mental abilities. After a betrayal leads to the downfall of House Atreides, Paul escapes into the desert, where he discovers his destiny intertwined with the planet and its native people, the Fremen. As he embraces his role as a leader and potential messiah, Paul must navigate political intrigue, ecological challenges, and his own burgeoning powers to reclaim his family's legacy.

II. Character Analysis
Paul Atreides is a complex protagonist who evolves from a noble heir into a powerful leader. His journey is marked by personal growth, as he grapples with the responsibilities of leadership and the weight of prophecy. Lady Jessica, Paul's mother, is a member of the Bene Gesserit sisterhood and plays a crucial role in shaping Paul's abilities and destiny. Duke Leto, Paul's father, embodies honor and integrity but faces the harsh realities of political machinations. The Fremen, led by figures like Stilgar and Chani, represent resilience and adaptability, forming a deep bond with Paul as he becomes a part of their culture.

III. Themes
"Dune" explores themes of power, ecology, and the interplay between religion and politics. The struggle for control over Arrakis and its spice reflects broader issues of resource exploitation and environmental stewardship. The novel also delves into the concept of destiny and the burdens of leadership, questioning the morality of messianic figures. Herbert critiques the cyclical nature of power and the consequences of fanaticism, urging readers to consider the complexities of human ambition and survival.

IV. Symbolism
The spice melange symbolizes wealth, power, and the addictive nature of resources, serving as a catalyst for conflict throughout the story. The desert landscape of Arrakis represents both harshness and beauty, reflecting the duality of life and survival. The sandworms, colossal creatures of the desert, symbolize the untamed forces of nature and the interconnectedness of life on the planet. Paul's transformation into the Kwisatz Haderach embodies the struggle between human potential and the dangers of absolute power.

I hope""",
"""
Sure! Here’s a summary of "Harry Potter and the Sorcerer's Stone" (or "Philosopher's Stone" in some regions) by J.K. Rowling:

I. Plot Summary
The story begins with an orphaned boy named Harry Potter, who lives with his neglectful relatives, the Dursleys. On his eleventh birthday, Harry receives a letter revealing that he is a wizard and has been accepted to Hogwarts School of Witchcraft and Wizardry. As he enters the magical world, Harry makes friends with Ron Weasley and Hermione Granger, discovers his fame as "The Boy Who Lived," and learns about his parents' tragic past. Throughout the school year, Harry uncovers a plot involving the Sorcerer's Stone, a magical object that grants immortality. With the help of his friends, Harry confronts the dark wizard Voldemort, who seeks the stone to regain his power.

II. Character Analysis
Harry Potter is a brave and kind-hearted protagonist who embodies the themes of friendship and courage. His journey from an unloved child to a hero showcases his resilience and determination. Ron Weasley, Harry's loyal friend, provides comic relief and represents the importance of family and loyalty. Hermione Granger, the intelligent and resourceful witch, highlights the value of knowledge and hard work. Together, they form a strong trio that faces challenges and grows throughout the story. The antagonist, Voldemort, serves as a representation of evil and the dangers of power and ambition.

III. Themes
The novel explores themes of friendship, bravery, and the battle between good and evil. The importance of loyalty and support among friends is emphasized through Harry, Ron, and Hermione's bond. The story also delves into the idea of identity and belonging, as Harry discovers his true self in the wizarding world. Additionally, the narrative critiques prejudice and the consequences of hatred, as seen in the treatment of characters like Voldemort and the Death Eaters.

IV. Symbolism
The Sorcerer's Stone symbolizes the quest for immortality and the moral implications of seeking power at any cost. Hogwarts itself represents a place of learning, acceptance, and the discovery of one's true potential. The sorting hat symbolizes the choices individuals make and how those choices shape their identities. The scar on Harry's forehead serves as a reminder of his past and the connection to Voldemort, representing the ongoing struggle between light and darkness.

I hope this analysis helps you understand
""",
"""
Absolutely! Here’s a summary of "The Lord of the Rings: The Two Towers" by J.R.R. Tolkien:

I. Plot Summary
"The Two Towers" continues the epic journey of the Fellowship of the Ring as they face the growing threat of Sauron. After the Fellowship is broken, the story splits into multiple narratives. Aragorn, Legolas, and Gimli pursue the kidnapped Merry and Pippin, leading them to the ancient forest of Fangorn, where they encounter the Ents, tree-like beings who are stirred to action against Saruman, the corrupted wizard. Meanwhile, Frodo and Sam continue their perilous journey to Mount Doom to destroy the One Ring, guided by the treacherous Gollum, who seeks to reclaim the Ring for himself. The narrative culminates in the Battle of Helm's Deep, where the forces of Rohan unite against Saruman's army, showcasing themes of hope, courage, and the struggle against darkness.

II. Character Analysis
Frodo Baggins is a reluctant hero burdened by the weight of the One Ring, showcasing themes of sacrifice and resilience. Samwise Gamgee, Frodo's loyal companion, embodies friendship and loyalty, often providing the strength Frodo needs to continue. Aragorn, the rightful heir to the throne of Gondor, grapples with his identity and destiny as he steps into a leadership role. Gollum serves as a tragic figure, representing the corrupting influence of the Ring and the duality of human nature. The characters' interactions and growth highlight the importance of unity and friendship in the face of overwhelming odds.

III. Themes
The novel explores themes of friendship, loyalty, and the struggle between good and evil. The bonds formed between characters, especially among the members of the Fellowship, emphasize the power of camaraderie in overcoming adversity. The corrupting influence of power is illustrated through Gollum's obsession with the Ring and Saruman's fall from grace. Additionally, the theme of hope is prevalent, as characters face despair yet continue to fight for a better future.

IV. Symbolism
The One Ring symbolizes the seductive nature of power and its ability to corrupt even the purest of hearts. The Ents and their march against Saruman represent nature's resistance against industrialization and destruction. Helm's Deep serves as a symbol of hope and resilience, illustrating the importance of unity in the face of overwhelming darkness. The contrasting landscapes of Middle-earth, from
""",
"""
Sure! Here are the books I've summarized for you in this session:

"Moby Dick" by Herman Melville
"Dune" by Frank Herbert
"Harry Potter and the Sorcerer's Stone" by J.K. Rowling
"The Lord of the Rings: The Two Towers" by J.R.R. Tolkien
If you need summaries for more books or any other assistance, feel free to ask!
""",
"""
As an AI, I don't have personal preferences or feelings, but I can suggest a popular and highly regarded book that many readers love: "The Alchemist" by Paulo Coelho. It's a beautiful story about following your dreams and discovering your personal legend, filled with wisdom and inspiration.

If you're looking for something specific, like a particular genre or topic, let me know, and I can recommend other great books!
""",
"""
Sure! Here’s a summary of "It" by Stephen King:

I. Plot Summary
"It" is set in the fictional town of Derry, Maine, where a malevolent entity known as "It" awakens every 27 years to prey on the town's children. The story alternates between two timelines: the childhood of a group of friends in the late 1950s and their return as adults in the 1980s to confront the evil they thought they had defeated. The group, known as the Losers' Club, faces their deepest fears and traumas as they battle It, which often takes the form of Pennywise the Clown. As they uncover the dark history of Derry and the nature of the entity, they must rely on their bond and courage to confront the horror that has haunted them since childhood.

II. Character Analysis
The members of the Losers' Club each have distinct personalities and struggles. Bill Denbrough, the group's leader, is driven by guilt over his brother's death. Beverly Marsh faces abuse and seeks acceptance, while Eddie Kaspbrak struggles with his overprotective mother. Richie Tozier provides comic relief but hides his insecurities, and Mike Hanlon serves as the group's historian, connecting their past with the present. Pennywise, the primary antagonist, embodies fear itself, showcasing the power of trauma and the darkness that lurks within individuals and society.

III. Themes
"It" explores themes of childhood innocence, the power of friendship, and the nature of fear. The novel emphasizes the importance of confronting one's fears and the strength that comes from unity and support. It also delves into the cyclical nature of evil and how trauma can shape individuals and communities. The contrast between childhood and adulthood highlights the loss of innocence and the lingering effects of unresolved trauma.

IV. Symbolism
Pennywise the Clown symbolizes the manifestation of fear and the darker aspects of human nature. The sewers of Derry represent the hidden horrors lurking beneath the surface of society, while the Losers' Club symbolizes the power of friendship and resilience in the face of adversity. The recurring motif of the red balloon serves as a harbinger of It’s presence, representing the allure and danger of fear.

I hope this summary helps you understand "It" better! If you have any specific questions or need further details, feel free to ask!
""",
"""
Sure! Here’s a summary of "Sapiens: A Brief History of Humankind" by Yuval Noah Harari:

I. Plot Summary
"Sapiens" traces the history of humankind from the emergence of Homo sapiens in the Stone Age to the present day. Harari explores key developments that have shaped human societies, including the Cognitive Revolution, which allowed early humans to develop complex language and shared myths; the Agricultural Revolution, which led to the establishment of settled communities and the rise of civilizations; and the Scientific Revolution, which transformed our understanding of the world and fueled technological advancements. Throughout the book, Harari examines how these revolutions have influenced social structures, economies, and cultures, ultimately leading to the modern world we inhabit today.

II. Character Analysis
While "Sapiens" does not focus on individual characters, it presents Homo sapiens as a collective character, highlighting the species' adaptability, creativity, and capacity for cooperation. Harari emphasizes the role of shared beliefs and social constructs in shaping human behavior and societal organization. He also discusses various influential figures throughout history, such as agriculturalists, scientists, and political leaders, who have contributed to the evolution of human societies.

III. Themes
The book explores themes of evolution, culture, and the impact of human choices on the planet. Harari examines how the ability to create and believe in shared myths has allowed Homo sapiens to cooperate in large groups, leading to the formation of complex societies. He also critiques the consequences of agricultural practices, capitalism, and technological advancements, questioning whether progress has truly led to a better quality of life for individuals and societies. The relationship between humans and the environment is another central theme, as Harari discusses the ecological impact of human activities.

IV. Symbolism
The idea of "shared myths" symbolizes the power of collective beliefs in shaping human societies and enabling cooperation. The Agricultural Revolution represents a turning point in human history, symbolizing both progress and the beginning of societal inequalities. The Scientific Revolution serves as a symbol of human curiosity and the quest for knowledge, illustrating the dual nature of scientific advancements as both beneficial and potentially harmful.

I hope this summary helps you understand "Sapiens" better! If you have any specific questions or need further details, feel free to ask!
"""
]

# Store
dataset = client.read_dataset(dataset_name=dataset_name)
client.create_examples(
    inputs=[{"question": q} for q in inputs],
    outputs=[{"answer": a} for a in outputs],
    dataset_id=dataset.id,
)