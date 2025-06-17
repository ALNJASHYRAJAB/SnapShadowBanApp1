
import random

def check_shadowban(username):
    drop_percentage = random.randint(30, 90)
    shadow_ban = drop_percentage > 50

    return {
        "username": username,
        "views_drop_percent": drop_percentage,
        "shadow_ban_detected": shadow_ban,
        "reason": "Low story engagement and visibility" if shadow_ban else "No shadowban detected"
    }
