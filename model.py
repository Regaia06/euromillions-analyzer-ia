from collections import Counter
from datetime import datetime

def analyser_tirages(tirages, exclude_last_n=0, jour=None, start_date=None, end_date=None):
    tirages = sorted(tirages, key=lambda x: x.get("date"), reverse=True)

    if exclude_last_n > 0:
        tirages = tirages[exclude_last_n:]

    if jour:
        jour = jour.lower()
        tirages = [
            t for t in tirages
            if datetime.strptime(t["date"], "%Y-%m-%dT%H:%M:%S").strftime('%A').lower() == jour
        ]

    if start_date:
        start = datetime.strptime(start_date, "%Y-%m-%d")
        tirages = [t for t in tirages if datetime.strptime(t["date"], "%Y-%m-%dT%H:%M:%S") >= start]
    if end_date:
        end = datetime.strptime(end_date, "%Y-%m-%d")
        tirages = [t for t in tirages if datetime.strptime(t["date"], "%Y-%m-%dT%H:%M:%S") <= end]

    numeros = []
    etoiles = []
    for tirage in tirages:
        numeros.extend(tirage["numbers"])
        etoiles.extend(tirage["stars"])

    freq_nums = Counter(numeros)
    freq_etoiles = Counter(etoiles)

    top_nums = [num for num, _ in freq_nums.most_common(5)]
    top_etoiles = [star for star, _ in freq_etoiles.most_common(2)]

    total_tirages = len(tirages)
    score_nums = {k: round(v / total_tirages, 3) for k, v in freq_nums.items()}
    score_etoiles = {k: round(v / total_tirages, 3) for k, v in freq_etoiles.items()}

    return {
        "filtrés": total_tirages,
        "top_nums": top_nums,
        "top_etoiles": top_etoiles,
        "freq_nums": dict(freq_nums),
        "freq_etoiles": dict(freq_etoiles),
        "score_nums": score_nums,
        "score_etoiles": score_etoiles
    }