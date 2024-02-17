import re

message_chunks = []

def chunk_message(message, length=1500):
    """Splits the message into chunks of a specified length."""
    return [message[i:i+length] for i in range(0, len(message), length)]

def stop_being_dolphin(message):
    """Replaces all case-insensitive occurrences of 'dolphin' with 'LUNA'."""
    return re.sub(r'\bdolphin\b', 'LUNA', message, flags=re.IGNORECASE)


def set_message(message):
    """Sets the message and chunks it if necessary."""
    global message_chunks
    message = stop_being_dolphin(message)
    if len(message) > 1500:
        # Chunk the message and add continuation prompts
        message_chunks = chunk_message(message)
        for i in range(len(message_chunks) - 1):
            message_chunks[i] += "\n\n**Reply with !cont for more**"
        message_chunks[-1] += "\n\n**Output Complete**"
    else:
        # If the message is short enough, keep it as a single chunk
        message_chunks = [message]

def get_next_chunk():
    """Returns the next chunk of the message."""
    if message_chunks:
        return message_chunks.pop(0)
    else:
        return "No more content to display."
