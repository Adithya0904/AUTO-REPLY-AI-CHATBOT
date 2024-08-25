import pyautogui
import time
import pyperclip
from openai import OpenAI


client = OpenAI(
  api_key="<Your Key Here>",
)

def is_last_message_from_sender(chat_log, sender_name="replier_name"):
    # Split the chat log into individual messages
    messages = chat_log.split("\n")[-1]
    print(messages)
    if sender_name in messages:
        return True 
    return False
    
    
# Step 1: Click on the browser icon at coordinates (x,y)
pyautogui.click(1128, 1043)

time.sleep(1)  # Wait for 1 second to ensure the click is registered

#click on the whatsapp/instagram website
pyautogui.click(1220, 920)

time.sleep(1)  # Wait for 1 second to ensure the click is registered

#automate the reply when ever the last message is not user message
while True:
    
    # Step 2: Drag the mouse from (616,228) to (1268, 919) to select the text
    pyautogui.moveTo(616,228)
    pyautogui.dragTo(1268, 919, duration=2.0)  # Drag for 1 second

    # Step 3: Copy the selected text to the clipboard
    pyautogui.hotkey('ctrl', 'c')
    time.sleep(2)  # Wait for 1 second to ensure the copy command is completed
    #click on the screen to de-select the text
    pyautogui.click(1207, 886)

    # Step 4: Retrieve the text from the clipboard and store it in a variable
    chat_history = pyperclip.paste()

    # Print the copied text to verify
    print(chat_history)

    #checking if the last message is not the user message
    # print(is_last_message_from_sender(chat_history))
    if is_last_message_from_sender(chat_history):

        completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a person named <Your name> who speaks hindi as well as english.\
             You are from India and you are a coder.\
             You analyze chat history and roast people in a funny way.\
             Output should be the next chat response (text message only)"},
            {"role": "user", "content": chat_history}
        ]
        )

        response = completion.choices[0].message.content
        pyperclip.copy(response)

        # Step 5: Click at coordinates (1466, 988)
        pyautogui.click(1466, 988)
        time.sleep(1)  # Wait for 1 second to ensure the click is registered

        # Step 6: Paste the text
        pyautogui.hotkey('ctrl', 'v')
        time.sleep(1)  # Wait for 1 second to ensure the paste command is completed

        # Step 7: Press Enter
        pyautogui.press('enter')