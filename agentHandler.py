def welcome_handler(agent):
    agent.add('Hi!')
    agent.add('How can I help you?')

def fallback_handler(agent):
    agent.add('Sorry, I missed what you said.')

handler = {
    'Default Welcome Intent': welcome_handler,
    'Default Fallback Intent': fallback_handler,
}