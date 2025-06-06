from datetime import datetime
from collections import Counter

def filtrer_tirages(tirages, params):
    exclude_count = int(params.get("exclude_last", 0))
    start_date = datetime.strptime(params["start_date"], "%Y-%m-%d")
    end_date = datetime.strptime(params["end_date"], "%Y-%m-%d")
    jour = params.get("jour", "Tous")

    tirages = tirages[exclude_count:]
    filtered = []
    for tirage in tirages:
        d = datetime.strptime(tirage["date"], "%Y-%m-%d")
        if start_date <= d <= end_date:
            if jour == "Tous" or d.strftime("%A") == jour:
                filtered.append(tirage)
    return filtered

def analyser_tirages(tirages):
    nums = Counter()
    etoiles = Counter()
    for tirage in tirages:
        for n in tirage["numbers"]:
            nums[n] += 1
        for e in tirage["stars"]:
            etoiles[e] += 1
    return {
        "nombres_frequents": nums.most_common(5),
        "etoiles_frequentes": etoiles.most_common(2)
    }
