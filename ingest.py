import requests
from bs4 import BeautifulSoup
import os
import time

os.makedirs("data", exist_ok=True)

urls = {
    "pakistan_penal_code": "https://en.wikipedia.org/wiki/Pakistan_Penal_Code",
    "constitution": "https://en.wikipedia.org/wiki/Constitution_of_Pakistan",
    "peca_2016": "https://en.wikipedia.org/wiki/Prevention_of_Electronic_Crimes_Act_2016",
    "harassment_act": "https://en.wikipedia.org/wiki/Protection_against_Harassment_of_Women_at_Workplace_Act_2010",
    "family_laws": "https://en.wikipedia.org/wiki/Muslim_Family_Laws_Ordinance_1961",
    "child_marriage": "https://en.wikipedia.org/wiki/Child_marriage_in_Pakistan",
    "honor_killing": "https://en.wikipedia.org/wiki/Honor_killing_in_Pakistan",
    "labour_laws": "https://en.wikipedia.org/wiki/Labour_laws_of_Pakistan",
    "women_rights": "https://en.wikipedia.org/wiki/Women_in_Pakistan",
    "human_rights": "https://en.wikipedia.org/wiki/Human_rights_in_Pakistan",
    "domestic_violence": "https://en.wikipedia.org/wiki/Domestic_violence_in_Pakistan",
    "divorce_pakistan": "https://en.wikipedia.org/wiki/Divorce_in_Pakistan",
}

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9",
}

all_text = ""
for name, url in urls.items():
    try:
        response = requests.get(url, headers=headers, timeout=15)
        soup = BeautifulSoup(response.content, "html.parser")
        
        # Sirf article content lo
        content_div = soup.find("div", {"class": "mw-parser-output"})
        if content_div:
            for tag in content_div(["script", "style", "table", "sup", "span", "nav"]):
                tag.decompose()
            text = content_div.get_text(separator="\n", strip=True)
        else:
            text = soup.get_text(separator="\n", strip=True)

        if len(text) > 1000:
            all_text += f"\n\n=== {name.upper()} ===\n\n{text}"
            # File mein bhi save karo
            with open(f"data/{name}.txt", "w", encoding="utf-8") as f:
                f.write(text)
            print(f"✅ {name} — {len(text)} chars")
        else:
            print(f"❌ {name} — Too short: {len(text)} chars")
        
        time.sleep(2)
        
    except Exception as e:
        print(f"❌ {name}: {e}")

print(f"\n✅ Total: {len(all_text)} chars")
print(f"Files: {os.listdir('data')}")