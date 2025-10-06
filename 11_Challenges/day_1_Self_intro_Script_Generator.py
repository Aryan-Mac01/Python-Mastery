import datetime

name = input("What is your name? ").strip()
age = input("How old are you? ").strip()
city = input("Which city are you from? ").strip()
profession = input("What is your profession? ").strip()
hobby = input("What is your favourite hobby? ").strip()

intro_message = (
    f"Hello! my name is  {name}, I'm {age} years old and live in {city}"
    f"I work as a {profession} and I absolutely enjoy {hobby} in my free time"
    f"Nice to meet you!\n"
)

current_date = datetime.date.today().isoformat()
intro_message += f"\n Logged on: {current_date}"

border = "*" * 80
final_output = f"{border}\n{intro_message}\n{border}"

print("\n" + final_output)