"""Inference engine for the Anime Recommendation Expert System (Sistem Pakar)."""

from knowledge_base import ANIME_DB, RULES


def max_possible_score() -> float:
    """Return the theoretical maximum match score any anime can receive."""
    # Base scoring: genre(2.0) + mood(1.5) + type(1.5) + episodes(1.0) + year(1.0)
    base = 2.0 + 1.5 + 1.5 + 1.0 + 1.0
    # Top rule boost (take the 3 highest boosts as a ceiling estimate)
    top_boosts = sorted((r["boost"] for r in RULES), reverse=True)[:3]
    return base + sum(top_boosts)


def run_inference(user_preferences: dict) -> list:
    """
    Apply forward-chaining rules to score and rank anime based on user preferences.

    Args:
        user_preferences: dict with keys matching QUESTIONS ids and user-chosen values.

    Returns:
        List of dicts with keys 'anime', 'score', and 'reasons', sorted by descending score.
    """
    results = []

    for anime in ANIME_DB:
        score = 0.0
        reasons = []

        # --- Base scoring: direct attribute matches ---
        # Genre match
        pref_genre = user_preferences.get("preferred_genre")
        if pref_genre and pref_genre in anime["genre"]:
            score += 2.0
            reasons.append(f"Matches your preferred genre: {pref_genre}")

        # Mood match
        pref_mood = user_preferences.get("preferred_mood")
        if pref_mood and pref_mood != "any":
            if anime["mood"] == pref_mood:
                score += 1.5
                reasons.append(f"Matches your preferred mood: {pref_mood}")
            elif pref_mood == "mixed":
                # mixed mood users are okay with all moods
                score += 0.5

        # Type match
        pref_type = user_preferences.get("preferred_type")
        if pref_type and pref_type != "any":
            if anime["type"] == pref_type:
                score += 1.5
                reasons.append(f"Matches your preferred type: {pref_type}")
        else:
            score += 0.5  # slight neutral bonus

        # Episodes match
        pref_episodes = user_preferences.get("preferred_episodes")
        if pref_episodes and pref_episodes != "any":
            if anime["episodes"] == pref_episodes:
                score += 1.0
                reasons.append(f"Matches your preferred length: {pref_episodes}")
        else:
            score += 0.3

        # Year match
        pref_year = user_preferences.get("preferred_year")
        if pref_year and pref_year != "any":
            if anime["year"] == pref_year:
                score += 1.0
                reasons.append(f"Matches your preferred era: {pref_year}")
        else:
            score += 0.3

        # --- Rule-based scoring ---
        for rule in RULES:
            if _rule_matches(rule["conditions"], user_preferences, anime):
                score += rule["boost"]
                reasons.append(rule["reason"])

        if score > 0:
            results.append(
                {
                    "anime": anime,
                    "score": round(score, 2),
                    "reasons": list(dict.fromkeys(reasons)),  # deduplicate, keep order
                }
            )

    results.sort(key=lambda x: x["score"], reverse=True)
    return results


def _rule_matches(conditions: dict, user_prefs: dict, anime: dict) -> bool:
    """
    Check whether a rule's conditions are satisfied by both the user preferences
    and the anime's attributes.
    """
    for attr, expected_value in conditions.items():
        if attr.startswith("preferred_"):
            # Check user preference
            user_val = user_prefs.get(attr)
            if user_val in (None, "any"):
                return False
            if user_val != expected_value:
                return False
        else:
            # Check anime attribute
            anime_val = anime.get(attr)
            if anime_val is None:
                return False
            if isinstance(anime_val, list):
                if expected_value not in anime_val:
                    return False
            elif anime_val != expected_value:
                return False
    return True
