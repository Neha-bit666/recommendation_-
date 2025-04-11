import pandas as pd

# Expanded dataset
data = {
    "Disease": [
        "Diabetes", "Common Cold", "Migraine", "Arthritis", "Indigestion", 
        "High Blood Pressure", "Insomnia", "Skin Burns", "Asthma", "Acne", 
        "Eczema", "High Cholesterol", "Constipation", "Depression", "Allergies", 
        "Sore Throat", "Gastritis", "Kidney Stones", "Psoriasis", "Menstrual Cramps"
    ],
    "Symptoms": [
        "frequent urination, increased thirst, fatigue",
        "cough, sore throat, runny nose",
        "headache, nausea, sensitivity to light",
        "joint pain, stiffness, swelling",
        "bloating, stomach pain, gas",
        "headache, dizziness, blurred vision",
        "difficulty sleeping, fatigue, irritability",
        "redness, pain, blistering",
        "wheezing, shortness of breath, chest tightness",
        "pimples, oily skin, blackheads",
        "dry skin, itching, redness",
        "chest pain, fatigue, yellow patches on skin",
        "infrequent bowel movements, bloating, discomfort",
        "sadness, loss of interest, fatigue",
        "sneezing, runny nose, itchy eyes",
        "pain or irritation in the throat, difficulty swallowing",
        "stomach pain, nausea, vomiting, bloating",
        "severe pain in the back or side, blood in urine",
        "red patches, itching, flaking skin",
        "cramping, lower back pain, fatigue"
    ],
    "Herbal Remedies": [
        "Bitter Melon, Fenugreek",
        "Ginger Tea, Turmeric Milk",
        "Peppermint Oil, Feverfew",
        "Turmeric, Ginger",
        "Peppermint Tea, Fennel Seeds",
        "Garlic, Hawthorn",
        "Chamomile Tea, Valerian Root",
        "Aloe Vera, Honey",
        "Licorice Root, Ginger",
        "Tea Tree Oil, Neem",
        "Coconut Oil, Oatmeal Bath",
        "Garlic, Flaxseeds",
        "Psyllium Husk, Senna",
        "St. John's Wort, Lavender",
        "Butterbur, Quercetin",
        "Slippery Elm, Marshmallow Root",
        "Chamomile, Licorice Root",
        "Dandelion Root, Nettle Leaf",
        "Aloe Vera, Tea Tree Oil",
        "Ginger, Cramp Bark"
    ],
    "Description": [
        "Bitter Melon helps regulate blood sugar levels. Fenugreek improves insulin sensitivity.",
        "Ginger Tea relieves sore throat and boosts immunity. Turmeric Milk reduces inflammation.",
        "Peppermint Oil soothes headaches. Feverfew reduces migraine frequency.",
        "Turmeric reduces inflammation. Ginger alleviates joint pain.",
        "Peppermint Tea relieves bloating. Fennel Seeds aid digestion.",
        "Garlic helps lower blood pressure. Hawthorn improves blood flow.",
        "Chamomile Tea promotes relaxation. Valerian Root improves sleep quality.",
        "Aloe Vera soothes burns and promotes healing. Honey has antibacterial properties.",
        "Licorice Root reduces inflammation in airways. Ginger helps with breathing.",
        "Tea Tree Oil has antibacterial properties. Neem purifies the skin.",
        "Coconut Oil moisturizes dry skin. Oatmeal Bath soothes itching and redness.",
        "Garlic reduces cholesterol levels. Flaxseeds are rich in omega-3 fatty acids.",
        "Psyllium Husk adds bulk to stool. Senna stimulates bowel movements.",
        "St. John's Wort improves mood. Lavender reduces anxiety and stress.",
        "Butterbur reduces allergy symptoms. Quercetin is a natural antihistamine.",
        "Slippery Elm coats the throat. Marshmallow Root soothes irritation.",
        "Chamomile reduces stomach inflammation. Licorice Root protects the stomach lining.",
        "Dandelion Root flushes out toxins. Nettle Leaf supports kidney health.",
        "Aloe Vera reduces redness. Tea Tree Oil soothes itching and flaking.",
        "Ginger reduces inflammation. Cramp Bark relaxes uterine muscles."
    ]
}

# Convert the dataset into a pandas DataFrame
df = pd.DataFrame(data)

# Save the DataFrame to a CSV file
df.to_csv("herbal_remedies_expanded.csv", index=False)

print("Expanded dataset saved successfully as 'herbal_remedies_expanded.csv'.")