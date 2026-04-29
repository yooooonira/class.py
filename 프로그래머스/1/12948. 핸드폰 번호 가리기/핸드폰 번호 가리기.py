def solution(phone_number):
    keep=phone_number[-4:]
    secret=(len(phone_number)-4)*"*"
    return secret+keep