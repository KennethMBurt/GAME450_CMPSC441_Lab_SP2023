import sentence_transformers as st


# Method takes 2 prompts and measures their similarity
# Uses sentence transformer to return a second list opf strings
def transform(prompt1, prompt2):
    min_len = min(len(prompt1), len(prompt2))
    tensor = []
    for i in range(0, min_len):
        model = st.SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')
        embed1 = model.encode(prompt1[i], convert_to_tensor=True)
        embed2 = model.encode(prompt2[i], convert_to_tensor=True)
        tensor.append(st.util.pytorch_cos_sim(embed1, embed2))
    return tensor


# breaking the response into a list of sentences
def resp_to_list(resp):
    # replace ! and ? with .
    resp.replace("!", ".")
    resp.replace("?", ".")

    prompt_list = resp.split(". ")
    return prompt_list


if __name__ == '__main__':
    q_string = "Write an article in paragraph form describing how to cook a steak with grape jelly."

    chat_resp_1 = "Cooking a steak with grape jelly might sound unusual, but it can actually be a delicious way to add a unique flavor to your meal. The jelly melts into a glaze that creates a sweet and tangy coating on the steak, making it a tasty and memorable dish. To start, gather your ingredients. You'll need a steak of your choice, grape jelly, soy sauce, Worcestershire sauce, garlic powder, and black pepper. Begin by seasoning both sides of the steak with garlic powder and black pepper to taste. Next, in a small bowl, mix together 1/4 cup of grape jelly, 1 tablespoon of soy sauce, and 1 tablespoon of Worcestershire sauce until well combined. Set aside. Preheat your grill or grill pan to medium-high heat. Once heated, place the seasoned steak onto the grill and cook for 4-5 minutes per side for medium-rare, or longer if you prefer it more well-done. After the steak has been cooking for a few minutes, use a pastry brush or spoon to brush the grape jelly glaze onto both sides of the steak. Be sure to coat it evenly so that the flavor is distributed throughout the meat. Continue cooking the steak until it reaches your desired level of doneness. When finished, remove the steak from the grill and let it rest for a few minutes before slicing and serving. The grape jelly glaze will have created a sweet and tangy coating on the steak, making it a delicious and memorable dish. In conclusion, using grape jelly to glaze a steak might seem unconventional, but it's a unique and tasty way to add flavor to your meal. Give it a try the next time you're looking to switch up your usual steak recipe!"
    chat_resp_2 = "Cooking steak with grape jelly might sound odd, but it's a fantastic way to add a sweet and tangy flavor to your dish. The jelly melts into a glaze that coats the steak, giving it a unique taste. To start, season the steak with salt, pepper, and garlic powder. In a bowl, mix together grape jelly, soy sauce, and Worcestershire sauce. Preheat your grill or pan, and cook the steak for 4-5 minutes per side for medium-rare or longer if you prefer. Once the steak is cooking, brush the grape jelly mixture on both sides. Coat the steak evenly to ensure an even flavor. Continue cooking until it reaches your desired doneness. Once the steak is cooked, let it rest for a few minutes before slicing and serving. The grape jelly glaze will create a sticky, delicious coating on the steak that will delight your taste buds. In summary, cooking steak with grape jelly is an excellent way to create a unique, tasty dish that you will love."

    prompt1 = resp_to_list(chat_resp_1)
    prompt2 = resp_to_list(chat_resp_2)

    print(transform(prompt1, prompt2))
